# Hector Berlioz — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `French Romantic programme music, idée fixe, colossal orchestration, dramatic contrast, literary imagination turned into sound, from tenderness to witches' sabbath`
- ZH: 法国浪漫主义标题音乐，固定乐思，宏大配器，戏剧对比，文学想象化为声音，从温柔到女巫安息日。

## (2) 音高与和声方向

- 主：功能和声 + 大胆半音与远关系转调；固定乐思的和声变形。禁：无调性、半音滥用。调性：调性为剧情服务，转调即场景切换。

## (3) 旋律与节奏

- 旋律：固定乐思（idée fixe）贯穿全曲、变形；旋律长句、不均衡乐句。节奏：驱动性强，突然对比；圆舞曲与进行曲节奏。织体：管弦织体丰富，独奏与全奏对比。

## (4) 配器与音色

- 乐器：大管弦乐队（《幻想》用 4 支定音鼓、钟、竖琴、英国管等）；配器为色彩与剧情服务。音色：从极弱到极强，幅度大。力度：靠配器对比。

## (5) 曲式与结构

- 曲式：标题交响曲（五乐章 + 文字说明）、歌剧、安魂曲。结构：以剧情结构定音乐结构；固定乐思统一全曲。高潮在女巫安息日。结尾：按剧情收束，或辉煌或恐怖。

## (6) 该写什么 / 不该写什么

- 该写：标题音乐、固定乐思、宏大配器、戏剧对比、文学想象。
- 不该写：无标题的抽象形式、半音滥用、炫技泛滥、情感浮夸。
- Negative prompt: `abstract form without programme, aimless chromaticism, empty virtuosity, sentimental bombast`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Hector Berlioz, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, French Romantic programme music, idée fixe, colossal orchestration, dramatic contrast, from tenderness to witches' sabbath, large orchestra`
- 中文对照：柏辽兹风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，法国浪漫主义标题音乐，固定乐思，宏大配器，戏剧对比，从温柔到女巫安息日，大管弦乐队。
- Negative: `abstract form without programme, aimless chromaticism, empty virtuosity, sentimental bombast`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
