# Alban Berg — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Berg style, twelve-tone row with tonal allusion, lyrical atonality, expressive dissonance, large-scale opera form, leitmotif, tragic climax`
- ZH: 贝尔格风格，带调性暗示的十二音音列，抒情无调性，表现性不协和，大型歌剧曲式，主导动机，悲剧高潮。

## (2) 音高与和声方向

- 主：十二音音列但常含三和弦与调性暗示（如小提琴协奏曲音列含三和弦）；不协和带抒情性；禁：纯粹的调性解决与无表情的序列机械。`artifact`

## (3) 旋律与节奏

- 旋律：歌唱性强、长线条、半音化抒情；人声旋律可唱，与勋伯格的念唱不同；节奏：自由中带舞曲与进行曲细胞。`artifact`

## (4) 配器与音色

- 大型管弦乐与歌剧编制；音色：浓郁、浪漫配器底色上的现代和声；力度范围宽，悲剧高潮音量大。`artifact`

## (5) 曲式与结构

- 曲式：歌剧用严格古典曲式（《沃采克》每场一种曲式：组曲、帕萨卡利亚、赋格等）；小提琴协奏曲为两乐章；结构：主导动机 + 音列变形双线并行。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：抒情十二音、歌剧主导动机、古典曲式套用、悲剧高潮、半音化长旋律。
- 不该写：见 Negative prompt。
- Negative prompt: `dry serial exercise, atonal noise without lyricism, tonal cadence, light entertainment, formless wandering`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Alban Berg, a 30-second piece for a rainy bus stop at dusk in a modern city, Berg style, twelve-tone row with tonal allusion, lyrical atonality, expressive dissonance, large-scale opera form, leitmotif, tragic climax`
- 中文对照：贝尔格风格，为现代城市黄昏雨中的公交站写一段 30 秒配乐，贝尔格风格，带调性暗示的十二音音列，抒情无调性，表现性不协和，大型歌剧曲式，主导动机，悲剧高潮。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
