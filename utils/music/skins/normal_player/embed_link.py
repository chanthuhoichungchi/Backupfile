# -*- coding: utf-8 -*-
import datetime
import itertools
from os.path import basename
import disnake

from utils.music.converters import fix_characters, time_format, get_button_style, music_source_image
from utils.music.models import LavalinkPlayer
from utils.others import ProgressBar, PlayerControls


class DefaultProgressbarSkin:

    __slots__ = ("name", "preview")

    def __init__(self):
        self.name = basename(__file__)[:-3]
        self.preview = "https://cdn.discordapp.com/attachments/554468640942981147/1119822945745915914/default_progressbar.png"

    def setup_features(self, player: LavalinkPlayer):
        player.mini_queue_feature = True
        player.controller_mode = True
        player.auto_update = 15
        player.hint_rate = player.bot.config["HINT_RATE"]
        player.static = False

    def load(self, player: LavalinkPlayer) -> dict:

        data = {
            "content": None,
            "embeds": []
        }

        embed = disnake.Embed(color=player.bot.get_color(player.guild.me))
        embed_queue = None

        if not player.paused:
            embed.set_author(
                name="Đang phát:",
                icon_url=music_source_image(player.current.info["sourceName"])
            )
        else:
            embed.set_author(
                name="Đã tạm dừng:",
                icon_url="https://cdn.discordapp.com/attachments/480195401543188483/896013933197013002/pause.png"
            )

        if player.current_hint:
            embed.set_footer(text=f"💡 Mẹo: {player.current_hint}")
        elif player.node.identifier != "LOCAL":
            embed.set_footer(
                text=str(player),
                icon_url="https://cdn.discordapp.com/attachments/480195401543188483/907119505971486810/speaker-loud-speaker.gif"
            )

        if player.current.is_stream:
            duration = "```ansi\n🔴 [31;1m Livestream[0m```"
        else:

            progress = ProgressBar(
                player.position,
                player.current.duration,
                bar_count=8
            )

            duration = f"```ansi\n[34;1m[{time_format(player.position)}] {('='*progress.start)}[0m🔴️[36;1m{'-'*progress.end} " \
                       f"[{time_format(player.current.duration)}][0m```\n"

        vc_txt = ""

        txt = f"[`{player.current.single_title}`]({player.current.uri or player.current.search_uri})\n\n" \
              f"> 💠 **⠂Yêu cầu bởi:** {player.current.authors_md}\n"

        if player.current.autoplay:
            txt += f"> 🎵 **⠂Tự động phát:** `Bật`"

            try:
                txt += f" [`(Ref.)`]({player.current.info['extra']['related']['uri']})\n"
            except:
                txt += "\n"
        else:
            txt += f"> ✋ **⠂Yêu cầu bởi:** <@{player.current.requester}>\n"

        txt += f"> 🔊 **⠂Âm lượng:** `{player.volume}%`"

        if player.current.track_loops:
            txt += f"\n> 🔂 **⠂Lặp lại:** `{player.current.track_loops}`"

        if player.loop:
            if player.loop == 'current':
                e = '🔂'
                m = 'Bài hát'
            else:
                e = '🔁'
                m = 'Danh sách phát'
            txt += f"\n> {e} **⠂Chế độ lặp lại:** `{m}`"

        if player.nightcore:
            txt += f"\n> 💫 **⠂Nightcore:** `Bật`"

        if player.current.album_name:
            txt += f"\n> 💽 **⠂Album:** [`{fix_characters(player.current.album_name, limit=16)}`]({player.current.album_url})"

        if player.current.playlist_name:
            txt += f"\n> 📑 **⠂Danh sách phát:** [`{fix_characters(player.current.playlist_name, limit=16)}`]({player.current.playlist_url})"

        if (qlenght:=len(player.queue)) and not player.mini_queue_enabled:
            txt += f"\n> 🎶 **⠂Bài hát đang chờ:** `{qlenght}`"

        if player.keep_connected:
            txt += "\n> ♾️ **⠂24/7:** `Bật`"

        elif player.restrict_mode:
            txt += f"\n> 🔒 **⠂Bảo vệ:** `Bật`"

        if player.ping:
            txt += f"\n> 📶 **⠂Độ trễ:** `{player.ping}ms`"

        txt += f"{vc_txt}\n"

        if player.command_log:
            txt += f"> {player.command_log_emoji} **⠂Tương tác gần đây:** {player.command_log}\n"

        txt += duration

        if qlenght and player.mini_queue_enabled:

            queue_txt = "\n".join(
                f"`{(n + 1):02}) [{time_format(t.duration) if not t.is_stream else '🔴 Livestream'}]` [`{fix_characters(t.title, 38)}`]({t.uri})"
                for n, t in (enumerate(itertools.islice(player.queue, 3)))
            )

            embed_queue = disnake.Embed(title=f"Bài hát đang chờ: {qlenght}", color=player.bot.get_color(player.guild.me),
                                        description=f"\n{queue_txt}")

            if not player.loop and not player.keep_connected and not player.paused and not player.current.is_stream:

                queue_duration = 0

                for t in player.queue:
                    if not t.is_stream:
                        queue_duration += t.duration

                if queue_duration:
                    embed_queue.description += f"\n`[⌛ Bài hát kết thúc vào` <t:{int((disnake.utils.utcnow() + datetime.timedelta(milliseconds=(queue_duration + (player.current.duration if not player.current.is_stream else 0)) - player.position)).timestamp())}:R> `⌛]`"

        embed.description = txt
        embed.set_thumbnail(url=player.current.thumb)

        data["embeds"] = [embed_queue, embed] if embed_queue else [embed]

        data["components"] = [
            disnake.ui.Button(emoji="<:previous:1119423676727701534>", custom_id=PlayerControls.back, style=disnake.ButtonStyle.primary),
            disnake.ui.Button(emoji="<:play_pause:1119425718997225592>", custom_id=PlayerControls.pause_resume, style=disnake.ButtonStyle.success),
            disnake.ui.Button(emoji="<:next:1119423672386588703>", custom_id=PlayerControls.skip, style=disnake.ButtonStyle.primary),
            disnake.ui.Button(emoji="<:stop:1119423681983168583>", custom_id=PlayerControls.stop, style=disnake.ButtonStyle.danger),
            disnake.ui.Button(emoji="<:music_queue:703761160679194734>", custom_id=PlayerControls.queue, label="Hàng chờ"),
            disnake.ui.Select(
                placeholder="Tùy chọn khác:",
                custom_id="musicplayer_dropdown_inter",
                min_values=0, max_values=1,
                options=[
                    disnake.SelectOption(
                        label="Thêm bài hát", emoji="<:add_music:588172015760965654>",
                        value=PlayerControls.add_song,
                        description="Thêm bài hát/danh sách phát vào hàng chờ."
                    ),
                    disnake.SelectOption(
                        label="Thêm bài hát yêu thích", emoji="⭐",
                        value=PlayerControls.enqueue_fav,
                        description="Thêm bài hát trong danh sách yêu thích của bạn vào hàng chờ."
                    ),
                    disnake.SelectOption(
                        label="Phát lại", emoji="⏪",
                        value=PlayerControls.seek_to_start,
                        description="Phát lại từ đầu bài hát hiện tại."
                    ),
                    disnake.SelectOption(
                        label="Âm lượng", emoji="🔊",
                        value=PlayerControls.volume,
                        description="Điều chỉnh âm lượng."
                    ),
                    disnake.SelectOption(
                        label="Trộn bài", emoji="🔀",
                        value=PlayerControls.shuffle,
                        description="Trộn ngẫu nhiên thứ tự phát trong danh sách phát."
                    ),
                    disnake.SelectOption(
                        label="Thêm lại", emoji="🎶",
                        value=PlayerControls.readd,
                        description="Thêm lại các bài hát đã phát vào hàng chờ."
                    ),
                    disnake.SelectOption(
                        label="Lặp lại", emoji="🔁",
                        value=PlayerControls.loop_mode,
                        description="Bật/Tắt chế độ lặp lại."
                    ),
                    disnake.SelectOption(
                        label="Nightcore", emoji="💫",
                        value=PlayerControls.nightcore,
                        description="Bật/Tắt chế độ Nightcore."
                    ),
                    disnake.SelectOption(
                        label="Tự động phát", emoji="🔄",
                        value=PlayerControls.autoplay,
                        description="Tự động phát các bài hát được gợi ý khi hàng chờ trống."
                    ),
                    disnake.SelectOption(
                        label="Bảo vệ", emoji="🔐",
                        value=PlayerControls.restrict_mode,
                        description="Chỉ các thành viên DJ mới có thể điều khiển trình phát."
                    ),
                ]
            ),
        ]

        if player.mini_queue_feature:
            data["components"][5].options.append(
                disnake.SelectOption(
                    label="Hàng chờ mini", emoji="<:music_queue:703761160679194734>",
                    value=PlayerControls.miniqueue,
                    description="Bật/Tắt chế độ hàng chờ mini."
                )
            )

        if not player.static and not player.has_thread:
            data["components"][5].options.append(
                disnake.SelectOption(
                    label="Chủ đề riêng", emoji="💬",
                    value=PlayerControls.song_request_thread,
                    description="Tạo chủ đề riêng để yêu cầu bài hát."
                )
            )

        return data

def load():
    return DefaultProgressbarSkin()
