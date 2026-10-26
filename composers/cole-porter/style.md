# Cole Porter — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Witty sophisticated song, chromatic harmony, elegant melody, Latin rhythm, urbane lyricism in music alone, show-tune craft`
- ZH: 机智精致歌曲，半音和声，优雅旋律，拉丁节奏，音乐本身的都市抒情，音乐剧歌曲工艺。

## (2) 旋律与和声

- 旋律：优雅长线，半音点缀；主题鲜明、易记。`artifact`
- 和声：半音化丰富，扩展和弦；调性清晰，解决温和。`artifact`

## (3) 节奏与织体

- 节奏：拉丁节奏与摇摆并存；织体：主调为主，钢琴与乐队轻盈。

## (4) 配器与音色

- 配器：音乐剧乐队，木管与弦乐轻盈；钢琴突出。

## (5) 曲式与结构

- 曲式：歌曲（AABA）、音乐剧；结构简洁，高潮克制，结尾明亮收束。

## (6) 该写什么 / 不该写什么

- 该写：优雅抒情旋律、半音和声、拉丁节奏、AABA 歌曲曲式、轻盈音乐剧配器。
- 不该写：atonal wandering、no dense counterpoint、no sentimental swell without wit、no heavy orchestration、no free improvisation without a written song。
- Negative prompt: `No atonal wandering, no dense counterpoint, no sentimental swell without wit, no heavy orchestration, no free improvisation without a written song`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Cole Porter, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, elegant witty melody, chromatic harmony, Latin rhythm, light show-tune orchestration`
- 中文对照：科尔·波特风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，优雅机智旋律，半音和声，拉丁节奏，轻盈音乐剧配器。
- Negative: `No atonal wandering, no dense counterpoint, no sentimental swell without wit, no heavy orchestration, no free improvisation without a written song`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
