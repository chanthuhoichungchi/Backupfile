# -*- coding: utf-8 -*-
from __future__ import annotations
from colorama import Fore
import re
from typing import Optional, TYPE_CHECKING

import asyncspotify
from asyncspotify import Client, ClientCredentialsFlow

from utils.music.converters import fix_characters
from utils.music.errors import MissingSpotifyClient, GenericError
from utils.music.models import PartialPlaylist, PartialTrack

if TYPE_CHECKING:
    from utils.client import BotCore

spotify_regex = re.compile("https://open.spotify.com?.+(album|playlist|artist|track)/([a-zA-Z0-9]+)")
spotify_regex_w_user = re.compile("https://open.spotify.com?.+(album|playlist|artist|track|user)/([a-zA-Z0-9]+)")


def query_spotify_track(func, url_id: str):
    return func(url_id)


async def process_spotify(bot: BotCore, requester: int, query: str):

    if not (matches := spotify_regex.match(query)):
        return

    if not bot.spotify:
        raise MissingSpotifyClient()

    url_type, url_id = matches.groups()

    if url_type == "track":
        result = await bot.spotify.get_track(url_id)

        t = PartialTrack(
            uri=result.link,
            author=result.artists[0].name,
            title=result.name,
            thumb=result.album.images[1].url,
            duration=result.duration.total_seconds() * 1000,
            source_name="spotify",
            requester=requester
        )

        t.info["extra"]["authors"] = [fix_characters(i.name) for i in result.artists if f"feat. {i.name.lower()}"
                                      not in result.name.lower()]

        t.info["extra"]["authors_md"] = ", ".join(f"[`{a.name}`]({a.link})" for a in result.artists)

        try:
            if result.album.name != result.name:
                t.info["extra"]["album"] = {
                    "name": result.album.name,
                    "url": result.album.external_urls["spotify"]
                }
        except (AttributeError, KeyError):
            pass

        return [t]

    data = {
        'loadType': 'PLAYLIST_LOADED',
        'playlistInfo': {'name': ''},
        'sourceName': "spotify",
        'tracks_data': []
    }

    if url_type == "album":

        result = await bot.spotify.get_album(url_id)

        if len(result.tracks) < 2:

            track = result.tracks[0]

            try:
                thumb = result.images[1].url
            except IndexError:
                thumb = ""

            return [PartialTrack(
                uri=track.link,
                author=track.artists[0].name or "Unknown Artist",
                title=track.name,
                thumb=thumb,
                duration=track.duration.total_seconds() * 1000,
                requester=requester
            )]

        data["playlistInfo"]["name"] = result.name

        for t in result.tracks:
            t.album = result

        tracks_data = result.tracks

    elif url_type == "artist":

        result = await bot.spotify.get_artist_top_tracks(url_id)

        data["playlistInfo"]["name"] = "Được chơi nhiều nhất của: " + \
                                       [a.name for a in result[0].artists if a.id == url_id][0]
        tracks_data = result

    elif url_type == "playlist":
        try:
            result = await bot.spotify.get_playlist(url_id)
        except asyncspotify.NotFound:
            raise GenericError("**Danh sách phát không tìm thấy (hoặc chỉ có sẵn trên các tài khoản đã đăng nhập trên nền tảng).**")
        data["playlistInfo"]["name"] = result.name
        tracks_data = result.tracks

    else:
        raise GenericError(f"**Liên kết Spotify không được công nhận/hỗ trợ:**\n{query}")

    if not tracks_data:
        raise GenericError(f"**Không có kết quả trong liên kết Spotify được thông báo ...**")

    data["playlistInfo"]["selectedTrack"] = -1

    playlist = PartialPlaylist(data, url=query)

    for t in tracks_data:

        try:
            thumb = t.album.images[1].url
        except IndexError:
            thumb = ""

        track = PartialTrack(
            uri=t.link,
            author=t.artists[0].name or "Unknown Artist",
            title=t.name,
            thumb=thumb,
            duration=t.duration.total_seconds() * 1000,
            source_name="spotify",
            requester=requester,
            playlist=playlist
        )

        try:
            track.info["extra"]["album"] = {
                "name": t.album.name,
                "url": t.album.external_urls["spotify"]
            }
        except (AttributeError, KeyError):
            pass

        if t.artists[0].name:
            track.info["extra"]["authors"] = [fix_characters(i.name) for i in t.artists if f"feat. {i.name.lower()}" not in t.name.lower()]
            track.info["extra"]["authors_md"] = ", ".join(f"[`{a.name}`]({a.link})" for a in t.artists)
        else:
            track.info["extra"]["authors"] = ["Unknown Artist"]
            track.info["extra"]["authors_md"] = "`Unknown Artist`"

        playlist.tracks.append(track)

    return playlist


def spotify_client(config: dict) -> Optional[Client]:
    if not config['SPOTIFY_CLIENT_ID']:
        print(Fore.YELLOW + 
            f"[Bỏ qua] - Hỗ trợ Spotify: SPOTIFY_CLIENT_ID Nó không được cấu hình trong env (hoặc tệp .env)."
            f"\n{'-' * 30}")
        return

    if not config['SPOTIFY_CLIENT_SECRET']:
        print(Fore.YELLOW + 
            F"[Bỏ qua] - Hỗ trợ Spotify: SPOTIFY_CLIENT_SECRET Nó không được cấu hình trong máy chủ env "
            F"(hoặc trong tệp .env).\n{'-' * 30}")
        return

    try:
        return Client(
            ClientCredentialsFlow(
                client_id=config['SPOTIFY_CLIENT_ID'],
                client_secret=config["SPOTIFY_CLIENT_SECRET"]
            )
        )

    except Exception as e:
        print(Fore.RED + 
            f"Apikey của Spotify không được cấu hình đúng trong env của máy chủ (hoặc tệp .env), "
            f"Kiểm tra và thử lại nếu bạn muốn hỗ trợ các bài hát Spotify (lỗi: {repr(e)}).\n{'-' * 30}")
        return
