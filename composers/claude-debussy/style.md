# Claude Debussy — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Whole-tone and pentatonic colour, parallel chords, timbre as structure, fluid rhythm, suggestion over statement, orchestral shimmer`
- ZH: 全音阶与五声音阶色彩，平行和弦，音色即结构，流动节奏，暗示重于陈述，管弦乐的闪烁。

## (2) 旋律与和声

- 旋律：短小动机，级进为主；和声：全音阶、五声音阶、平行和弦。禁：属—主强解决、德国式动机发展。调性游移，色彩即结构。

## (3) 节奏与织体

- 节奏：自由律动，无重音；织体：管弦乐分层，音色主导。

## (4) 配器与音色

- 乐器：管弦乐，木管与竖琴突出；音色：朦胧、闪烁；力度：中弱为主。

## (5) 曲式与结构

- 曲式：前奏曲、交响素描、歌剧；结构：自由、并置；结尾：渐弱或悬置。

## (6) 该写什么 / 不该写什么

- 该写：全音阶、五声音阶、平行和弦、音色分层、自由律动、暗示而非陈述。
- 不该写：属—主强解决、德国式动机发展、厚重铜管高潮、方正乐句、煽情电影配乐式 swell、响亮高潮。
- Negative prompt: `no dominant-tonic resolution, no Germanic motivic development, no thick brass climax, no square phrasing, no sentimental film-score swell, no loud climax`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡，晨光中）

- Prompt: `In the style of Claude Debussy, a cup of coffee sitting on a windowsill in the morning light, Whole-tone and pentatonic colour, parallel chords, timbre as structure, fluid rhythm, suggestion over statement, orchestral shimmer`
- 中文对照：克洛德·德彪西风格，一杯放在窗台上的咖啡，晨光中，全音阶与五声音阶色彩，平行和弦，音色即结构，流动节奏，暗示重于陈述，管弦乐的闪烁。
- Negative: `no dominant-tonic resolution, no Germanic motivic development, no thick brass climax, no square phrasing, no sentimental film-score swell, no loud climax`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
