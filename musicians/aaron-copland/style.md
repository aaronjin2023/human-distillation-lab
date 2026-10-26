# Aaron Copland — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Copland style, open intervals, Americana, folk melody, clear diatonic harmony, spacious orchestration, ballet with American landscape`
- ZH: 科普兰风格，开放音程，美国风，民间旋律，清晰的调性和声，辽阔配器，带美国风景的芭蕾。

## (2) 音高与和声方向

- 主：调性和声 + 开放音程（四五度叠置）、民间调式；和声清晰、解决明确；禁：半音化拥挤与无调性的失控。`artifact`

## (3) 旋律与节奏

- 旋律：民间歌谣式长线条、级进为主、呼吸感强；节奏：切分与牛仔舞曲律动、开阔的长音；织体：稀疏、留白大。`artifact`

## (4) 配器与音色

- 管弦乐辽阔：铜管号角、木管清澈、弦乐长音、打击乐克制；《阿巴拉契亚之春》原为十三件乐器，后扩为管弦乐版。`artifact`

## (5) 曲式与结构

- 曲式：芭蕾组曲、变奏曲（《阿巴拉契亚之春》以“简朴的礼物”变奏）；结构：主题—变奏—再现，高潮靠铜管号角，结尾开阔宁静。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：开放音程、民间旋律、号角、辽阔配器、变奏曲、美国风景。
- 不该写：见 Negative prompt。
- Negative prompt: `chromatic density, atonal wandering, dense Romantic swell, sentimental cliché, formless improvisation`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Aaron Copland, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Copland style, open intervals, Americana, folk melody, clear diatonic harmony, spacious orchestration, ballet with American landscape`
- 中文对照：科普兰风格，为一只坐在地铁座位上的小约克夏犬写一段 30 秒配乐，科普兰风格，开放音程，美国风，民间旋律，清晰的调性和声，辽阔配器，带美国风景的芭蕾。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
