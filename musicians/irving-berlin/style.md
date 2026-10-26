# Irving Berlin — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Irving Berlin style, simple memorable song, diatonic melody, ragtime rhythm, direct emotion, American songbook, singable`
- ZH: 欧文·柏林风格，简单易记的歌曲，调式旋律，拉格泰姆节奏，直接情感，美国歌曲集，可唱。

## (2) 音高与和声方向

- 主：调性和声、简单功能进行、偶有半音装饰；和声清晰、解决直接；禁：半音化拥挤与无调性。`artifact`

## (3) 旋律与节奏

- 旋律：级进为主、音域窄、极易唱、易记；节奏：拉格泰姆切分、进行曲律动；织体：主调、伴奏简单。`artifact`

## (4) 配器与音色

- 流行歌曲乐队：钢琴、弦乐、木管克制；音色：直接、明亮、不装饰过度。`artifact`

## (5) 曲式与结构

- 曲式：32 小节歌曲曲式、音乐剧歌曲；结构：主歌—副歌，副歌极简，高潮在副歌重复，结尾干脆。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：简单易记旋律、调性和声、拉格泰姆节奏、直接情感、32 小节曲式。
- 不该写：见 Negative prompt。
- Negative prompt: `chromatic density, atonal wandering, sophisticated jazz harmony, sentimental over-decoration, formless improvisation`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Irving Berlin, a 30-second piece for a cup of coffee left on a windowsill in the morning light, Irving Berlin style, simple memorable song, diatonic melody, ragtime rhythm, direct emotion, American songbook, singable`
- 中文对照：欧文·柏林风格，为一杯放在窗台上的咖啡写一段 30 秒配乐，欧文·柏林风格，简单易记的歌曲，调式旋律，拉格泰姆节奏，直接情感，美国歌曲集，可唱。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
