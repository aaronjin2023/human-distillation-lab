# Thelonious Monk — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Thelonious Monk style, angular melody, dissonant piano, whole-tone and chromatic, stride root, space and silence, bebop with idiosyncrasy`
- ZH: 孟克风格，棱角旋律，不协和钢琴，全音与半音，跨步钢琴根源，留白与静默，带个性的比波普。

## (2) 音高与和声方向

- 主：不协和和声、全音阶、半音摩擦、属和弦的变形；调性可辨但常被扭曲；禁：功能和声的顺滑解决与流行和声。`artifact`

## (3) 旋律与节奏

- 旋律：棱角分明、大跳进、重复单音、突然静默；钢琴：跨步根源上的不协和和弦；节奏：比波普律动、错位重音、留白。`artifact`

## (4) 配器与音色

- 小乐队：钢琴、三重奏、四重奏；音色：钢琴干脆、棱角、打击性；独奏与合奏交替。`artifact`

## (5) 曲式与结构

- 曲式：32 小节歌曲曲式、布鲁斯；结构：主题—即兴—主题，即兴框架严格，结尾干脆。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：棱角旋律、不协和钢琴、留白、比波普律动、主题—即兴框架。
- 不该写：见 Negative prompt。
- Negative prompt: `smooth bebop cliché, sentimental swell, tonal cadence, dense harmony, formless jam, pretty melody`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Thelonious Monk, a 30-second piece for a rainy bus stop at dusk in a modern city, Thelonious Monk style, angular melody, dissonant piano, whole-tone and chromatic, stride root, space and silence, bebop with idiosyncrasy`
- 中文对照：塞隆尼斯·孟克风格，为现代城市黄昏雨中的公交站写一段 30 秒配乐，孟克风格，棱角旋律，不协和钢琴，全音与半音，跨步钢琴根源，留白与静默，带个性的比波普。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
