# disnake-LL-music-bot
## Bot âm nhạc được lập trình Python với trình phát tương tác, lệnh thanh/chém, v.v.Sử dụng LIBS DISNAKE và WAVELINK/LAVALINK.

## Ví dụ bot sử dụng nguồn này: [Bấm vào đây](https://gist.github.com/zRitsu/4875008554a00c3c372b2df6dcdf437f#file-muse_heart_invites-md).

### Một số xem trước:

-Bộ điều khiển người chơi: Modo Bình thường/Người chơi mini (skin: default)và hỗ trợ cho[RPC (Rich Presence)](https://github.com/zRitsu/Discord-MusicBot-RPC)

![](https://media.discordapp.net/attachments/554468640942981147/1089678647230726185/rpc_support.png)

<details>
<summary>
Xem trước nhiều hơn:
</summary>
<br>

- Các lệnh thanh 

![](https://cdn.discordapp.com/attachments/554468640942981147/1125158772608876565/slash_commands.png)

- Bộ điều khiển lớp: Chế độ cố định /mở rộng với các yêu cầu kênh và bài hát (da: default_prigressba), có thể định cấu hình với lệnh: /setup

![](https://cdn.discordapp.com/attachments/554468640942981147/1125154702569504768/player_controller_textchannel.png)

-Trình điều khiển người chơi: Chế độ cố định/mở rộng với kênh yêu cầu bài hát diễn đàn

![](https://cdn.discordapp.com/attachments/554468640942981147/1125160296785383468/forum_song_request_channel.png)


* Có một số giao diện khác, xem tất cả bằng cách sử dụng lệnh/thay đổi_skin (bạn cũng có thể tạo các giao dịch khác, sử dụng các mô hình tiêu chuẩn có trong thư mục [skin] và sửa đổi sở thích của bạn).

</details>

## Teste agora mesmo criando/reusando um bot próprio com essa source fazendo deploy em um dos serviços abaixo:

---

<details>
<summary>
Repl.it
</summary>

Hướng dẫn liên kết với hình ảnh: https://gist.github.com/zRitsu/70737984cbe163f890dae05a80a3ddbe
</details>

---

<details>
<summary>
Render.com
</summary>
<br>

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/zRitsu/disnake-LL-music-bot/tree/main)

* **[ 1 ]** - No campo **TOKEN** coloque o token do bot **( [tutorial de como obter](https://www.youtube.com/watch?v=lfdmZQySTXE) )**. `Nota: Caso queira, no campo TOKEN você pode incluir token de mais bots para ter bots extras pra ativar o suporte a multi-voice incluindo mais tokens no value (separando com espaços).`


* **[ 2 ]** - No campo **DEFAULT_PREFIX** coloque um prefixo para o bot.


* **[ 3 ]** - Nos campos **SPOTIFY_CLIENT_ID** e **SPOTIFY_CLIENT_SECRET** coloque as suas keys do spotify **( [tutorial de como obter](https://www.youtube.com/watch?v=ceKQjWiCyWE) )**.


* **[ 4 ]** - No campo **MONGO** coloque o link da sua database do MongoDB **( [tutorial de como obter](https://www.youtube.com/watch?v=x1Gq5beRx9k) )**.


* **[ 5 ]** - Nhấp vào Áp dụng và chờ quá trình xây dựng cho đến khi bot bắt đầu (điều này có thể mất nhiều thời gian, ít nhất 13 phút trở lên để triển khai hoàn thành + Bot Start + Lavalink Server Start).
</details>

---

<details>
<summary>
Gitpod
</summary>
<br>

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/zRitsu/disnake-LL-music-bot)

* **[ 1 ]** - Mở tệp .ENV và đặt Token bot vào trường thích hợp (nếu không, xem làm thế nào để có được hướng dẫn này [tutorial](https://www.youtube.com/watch?v=lfdmZQySTXE) de como obter). Cũng rất khuyến khích sử dụng MongoDB, hãy tìm nơi bạn có Mongo = trong tệp .ENV và đặt liên kết DB của MongoDB của bạn (nếu không, xem cách nhận nó cho nó cho điều này[tutorial](https://www.youtube.com/watch?v=x1Gq5beRx9k)).


* **[ 2 ]** - Bên phải -Click trên tệp main.py và sau đó nhấp vào: Chạy tệp Python trong thiết bị đầu cuối.


* **Nota 1:** Yêu cầu xác minh tài khoản theo số điện thoại di động/di động.
* **Nota 2:** Đừng quên đi vào danh sách [workspaces](https://gitpod.io/workspaces) và nhấp vào 3 chấm của dự án và sau đó nhấp vào **pin**. `(isso evitará o worskpace ser deletado após 14 dias inativo)`
* **Nota 3:** NKhông sử dụng GitPod để lưu trữ / giữ bot trực tuyến, vì nó có nhiều hạn chế trong kế hoạch miễn phí (thêm thông tin [tại liên kết này](https://www.gitpod.io/pricing)).
</details>

---

<details>
<summary>
Heroku
</summary>
<br>

[![Heroku_Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/zRitsu/disnake-LL-music-bot/tree/main)

**Nota: A partir do dia 28/11/2022 a heroku não vai mais fornecer planos gratuitos ([clique aqui](https://blog.heroku.com/next-chapter) para saber mais).**


* **[ 1 ]** - Điền vào dữ liệu sẽ được yêu cầu trên trang tiếp theo.`Lưu ý: Nếu bạn muốn, trong trường Token, bạn có thể bao gồm nhiều Token bot hơn để có thêm bot để kích hoạt hỗ trợ đa năng bao gồm nhiều Token hơn trong giá trị (tách biệt với khoảng trắng) .`.


* **[ 2 ]** - Nhấp vào triển khai ứng dụng và chờ (quy trình có thể mất từ ​​2-5 phút).


* **[ 3 ]** - Nhấp vào Quản lý và sau đó đi đến tài nguyên.

* **[ 4 ]** - Vô hiệu hóa Dyno Web và Bật AutopDate (hoặc QuickFix, không kích hoạt 2 cùng một lúc!) Và đợi cho bot đăng nhập.`(Ở góc trên, nhấp vào thêm và xem nhật ký để theo dõi nhật ký)`

* **Nota:** Nếu bạn muốn thay đổi các cấu hình được sử dụng trong Bước 1, hãy chuyển sang Cài đặt và nhấp vào Hiển thị Cấu hình Vars, Tạo/Thay đổi phím và giá trị mong muốn của cấu hình, hãy xem tệp .example.env để xem tất cả các cấu hình có sẵn.
</details>

---

<details>
<summary>
Chạy trên PC/VPS của riêng bạn (Windows/Linux)
</summary>
<br>

### Yêu cầu:

* Python 3.8:<br/>
[Tải xuống thông qua Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5?hl=vi-vn) (Được đề xuất cho người dùng Windows 10/11).<br/>
[Tải xuống trực tiếp từ trang web chính thức](https://www.python.org/downloads/) (Đánh dấu tùy chọn này khi cài đặt: ** Thêm Python vào đường dẫn **)
* [Git](https://git-scm.com/downloads) (Không chọn phiên bản portable)</br>

* [JDK 11](https://www.azul.com/downloads) (Windows và Linux không cần thiết để cài đặt, nó được tải xuống tự động)</br>
 
`Lưu ý: Source này yêu cầu ít nhất 512MB RAM và 1GHz CPU để chạy bình thường (nếu bạn chạy Lavalink ở cùng trường hợp với bot xem xét rằng bot là riêng tư).`

### Bắt đầu bot (hướng dẫn nhanh):

* Tải xuống nguồn này dưới dạng [zip](https://github.com/NamfromVN/disnake-LL-music-bot-but-it-vietnammese/archive/refs/tags/test.zip) 
Hoặc bạn cũng có thể tải bản gốc [Tại_đây](https://github.com/zRitsu/disnake-LL-music-bot/archive/refs/tags/0.1.zip) và sau đó Giải nén 
(hoặc sử dụng lệnh bên dưới tại Terminal/CMD và mở thư mục sau đó):
```shell
git clone https://github.com/NamfromVN/disnake-LL-music-bot-but-it-vietnammese.git
```
* Nhấp vào tệp setup.sh (hoặc setup nếu Windows của bạn không hiển thị đuôi tệp) và chờ.</br>
`Nếu bạn đang sử dụng Linux, hãy sử dụng lệnh tại thiết bị đầu cuối:` 
```shell
bash setup.sh
```
* Sẽ xuất hiện một tệp có tên **.env **, chỉnh sửa nó và đặt Token của bot trong trường thích hợp (bạn cũng có thể chỉnh sửa những thứ khác từ cùng một tệp này nếu bạn muốn thực hiện các điều chỉnh cụ thể trong bot).</br>
`Lưu ý: Nếu bạn chưa tạo bot, `[Xem hướng dẫn này](https://www.youtube.com/watch?v=lfdmZQySTXE) `để tạo bot của bạn và nhận Token cần thiết.`</br>`Tôi cũng khuyên bạn nên sử dụng mongodb, tìm vị trí của MONGO= trong tệp .env và đặt liên kết tới db mongodb của bạn trong đó (nếu bạn không có nó, hãy xem cách lấy nó bằng cách này` [hướng dẫn](https://www.youtube.com/watch?v=x1Gq5beRx9k)`). ` 
* Bây giờ hãy chạy start.sh để khởi động bot (nếu bạn đang sử dụng Linux, hãy sử dụng lệnh bên dưới):
```shell
bash start.sh
```

### Notas:

*Để cập nhật bot của bạn, hãy nhấp đúp vào Update.sh (Windows), để sử dụng lệnh trên shell/terminal:
```shell
bash update.sh
```
`Khi cập nhật, có cơ hội thay đổi thủ công được thực hiện để bị mất (nếu không phải là một cái nĩa của nguồn này)...`<br/>

`Lưu ý: Nếu bạn đang chạy nguồn trực tiếp từ máy Windows (và đã cài đặt Git) chỉ cần nhấp đúp vào tệp Update.sh`
</details>

---

Lưu ý: Có một số hướng dẫn khác tại [Wiki]((https://github.com/zRitsu/disnake-LL-music-bot/wiki)).

### Quan sát quan trọng:

* Nguồn này được tạo ra để được sử dụng trong các bot riêng (không được tối ưu hóa đủ để đối phó với nhu cầu máy chủ cao).

* Tôi khuyên bạn nên sử dụng nguồn hiện tại mà không thay đổi mã. Nếu bạn muốn thực hiện các sửa đổi (và đặc biệt là thêm các tính năng mới), rất khuyến khích bạn có kiến ​​thức về Python và Dysnake.Và nếu bạn muốn giữ nguồn của mình được sửa đổi với các bản cập nhật vào ngày sử dụng nguồn cơ sở, tôi cũng khuyên bạn nên có kiến ​​thức trong GIT (ít nhất là những gì bạn cần làm hợp nhất mà không có lỗi).

* Hỗ trợ sẽ không được cung cấp nếu nó sửa đổi nguồn hiện tại (ngoại trừ các giao diện tùy chỉnh), vì tôi cập nhật các phiên bản thường xuyên và sửa đổi có xu hướng lỗi thời khiến việc hỗ trợ lý do này (và tùy thuộc vào sửa đổi hoặc thực hiện có thể tạo ra lỗi không xác định Điều đó gây khó khăn khi cố gắng giải quyết vấn đề và tôi cần sử dụng các phương thức để cập nhật mã thường hoàn tác các thay đổi này).

* Nếu bạn muốn tạo video/hướng dẫn bằng nguồn này, bạn hoàn toàn tự do sử dụng nó cho mục đích này miễn là bạn phù hợp với [giấy phép](/LICENSE).

---

### Nếu bạn gặp sự cố, hãy đăng [tại đây](https://github.com/zRitsu/disnake-LL-music-bot/issues)