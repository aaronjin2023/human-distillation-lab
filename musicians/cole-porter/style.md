# Cole Porter — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Cole Porter style, sophisticated song, witty lyric-melody fit, chromatic harmony, elegant swing, Broadway song form, urbane`
- ZH: 科尔·波特风格，精致歌曲，机智的词曲咬合，半音化和声，优雅摇摆，百老汇歌曲曲式，都会气质。

## (2) 音高与和声方向

- 主：半音化精致和声、扩展和弦、突然转调；调性清晰；禁：无调性与蓝调的粗粝。`artifact`

## (3) 旋律与节奏

- 旋律：歌唱性强、线条优雅、半音装饰；词曲咬合：旋律重音与歌词重音一致；节奏：摇摆、切分克制。`artifact`

## (4) 配器与音色

- 音乐剧乐队：钢琴、弦乐、木管、铜管克制；音色：都会、优雅、明亮。`artifact`

## (5) 曲式与结构

- 曲式：32 小节歌曲曲式、音乐剧多场；结构：主歌—副歌，副歌是记忆点，高潮在副歌重复，结尾干脆。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：精致歌曲、词曲咬合、半音化和声、优雅摇摆、32 小节曲式。
- 不该写：见 Negative prompt。
- Negative prompt: `atonal wandering, blues roughness, sentimental cliché, formless improvisation, heavy orchestration`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Cole Porter, a 30-second piece for a quiet night scene at a convenience store in a modern city, Cole Porter style, sophisticated song, witty lyric-melody fit, chromatic harmony, elegant swing, Broadway song form, urbane`
- 中文对照：科尔·波特风格，为现代城市街角便利店的深夜写一段 30 秒配乐，科尔·波特风格，精致歌曲，机智的词曲咬合，半音化和声，优雅摇摆，百老汇歌曲曲式，都会气质。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
