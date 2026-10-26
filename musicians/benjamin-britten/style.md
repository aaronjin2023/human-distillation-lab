# Benjamin Britten — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Britten style, clear vocal line, English lyricism, transparent orchestration, passacaglia, sea imagery, dramatic opera with chamber clarity`
- ZH: 布里顿风格，清晰的人声线条，英国抒情，透明配器，帕萨卡利亚，海的意象，室内乐清晰度的戏剧歌剧。

## (2) 音高与和声方向

- 主：调性基础 + 半音摩擦、调式色彩；和声清晰、解决明确；禁：无调性序列的滥用与印象主义的调性悬浮。`artifact`

## (3) 旋律与节奏

- 旋律：人声旋律歌唱性极强、线条清晰、英语语音重音即音乐重音；器乐旋律带民间歌谣味；节奏：海浪般的律动与帕萨卡利亚的重复。`artifact`

## (4) 配器与音色

- 管弦乐透明：弦乐、木管、竖琴清晰分层；歌剧编制按戏剧情境收放；《青少年管弦乐队指南》以变奏展示各乐器音色。`artifact`

## (5) 曲式与结构

- 曲式：歌剧多幕、帕萨卡利亚间奏曲、变奏曲；结构：主题—变奏—再现清晰，高潮靠织体叠加，结尾常归于宁静或悬置。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：清晰人声线条、帕萨卡利亚、英国抒情、透明配器、海的意象、变奏展示。
- 不该写：见 Negative prompt。
- Negative prompt: `atonal wandering, dense Romantic swell, muddy orchestration, sentimental cliché, formless improvisation`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Benjamin Britten, a 30-second piece for a late-night ramen shop with steam rising, Britten style, clear vocal line, English lyricism, transparent orchestration, passacaglia, sea imagery, dramatic opera with chamber clarity`
- 中文对照：布里顿风格，为深夜拉面店升起的热气写一段 30 秒配乐，布里顿风格，清晰的人声线条，英国抒情，透明配器，帕萨卡利亚，海的意象，室内乐清晰度的戏剧歌剧。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
