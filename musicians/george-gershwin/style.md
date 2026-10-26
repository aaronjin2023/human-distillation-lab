# George Gershwin — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `George Gershwin style, jazz-classical crossover, blues melody, syncopation, Rhapsody form, brilliant piano, American song, orchestral jazz`
- ZH: 格什温风格，爵士—古典跨界，蓝调旋律，切分，狂想曲式，辉煌钢琴，美国歌曲，管弦乐化爵士。

## (2) 音高与和声方向

- 主：蓝调和声 + 欧洲功能和声、扩展和弦；调性清晰；禁：无调性与印象主义的调性悬浮。`artifact`

## (3) 旋律与节奏

- 旋律：蓝调式歌唱旋律、美国歌曲式长线条；节奏：切分、摇摆、拉格泰姆律动；钢琴：辉煌的琶音与八度。`artifact`

## (4) 配器与音色

- 管弦乐与钢琴：钢琴主奏、管弦乐丰满、爵士乐队色彩；《一个美国人在巴黎》用汽车喇叭等音色点缀。`artifact`

## (5) 曲式与结构

- 曲式：狂想曲、歌剧、交响诗；结构：主题—变奏—再现，高潮靠钢琴与乐队齐奏，结尾辉煌。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：蓝调旋律、切分、狂想曲式、辉煌钢琴、美国歌曲、跨界配器。
- 不该写：见 Negative prompt。
- Negative prompt: `atonal wandering, vague impressionism, sentimental cliché, formless improvisation, dry academic counterpoint`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of George Gershwin, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, George Gershwin style, jazz-classical crossover, blues melody, syncopation, Rhapsody form, brilliant piano, American song, orchestral jazz`
- 中文对照：格什温风格，为一只坐在地铁座位上的小约克夏犬写一段 30 秒配乐，格什温风格，爵士—古典跨界，蓝调旋律，切分，狂想曲式，辉煌钢琴，美国歌曲，管弦乐化爵士。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
