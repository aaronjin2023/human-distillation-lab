# Florence Price — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Florence Price style, Romantic symphonic form, spiritual melody, Juba dance rhythm, lyrical strings, American folk idiom inside European form`
- ZH: 普赖斯风格，浪漫主义交响曲式，灵歌旋律，朱巴舞节奏，抒情弦乐，欧洲曲式内的美国民间语汇。

## (2) 音高与和声方向

- 主：调性功能和声 + 灵歌式半音与蓝调色彩；和声温暖、解决明确；禁：无调性与印象主义的调性悬浮。`artifact`

## (3) 旋律与节奏

- 旋律：灵歌式长线条、歌唱性强、装饰音带民间风味；节奏：朱巴舞的切分与拍手节奏、灵歌的自由呼吸。`artifact`

## (4) 配器与音色

- 管弦乐：弦乐抒情主导、木管歌唱、铜管克制、打击乐带民间节奏；钢琴协奏曲中钢琴与乐队对话清晰。`artifact`

## (5) 曲式与结构

- 曲式：四乐章交响曲、组曲；结构：主题—发展—再现清晰，第三乐章常用朱巴舞，高潮靠弦乐歌唱，结尾明确。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：灵歌旋律、朱巴舞节奏、浪漫交响曲式、抒情弦乐、民间舞曲乐章。
- 不该写：见 Negative prompt。
- Negative prompt: `atonal wandering, vague impressionism, formless improvisation, sentimental cliché without folk root, muddy orchestration`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Florence Price, a 30-second piece for a quiet night scene at a convenience store in a modern city, Florence Price style, Romantic symphonic form, spiritual melody, Juba dance rhythm, lyrical strings, American folk idiom inside European form`
- 中文对照：弗洛伦斯·普赖斯风格，为现代城市街角便利店的深夜写一段 30 秒配乐，普赖斯风格，浪漫主义交响曲式，灵歌旋律，朱巴舞节奏，抒情弦乐，欧洲曲式内的美国民间语汇。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
