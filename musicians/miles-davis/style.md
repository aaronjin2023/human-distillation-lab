# Miles Davis — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Miles Davis style, modal jazz, cool muted trumpet, space and silence, minimal notes, modal scale, electric fusion, less is more`
- ZH: 戴维斯风格，调式爵士，冷峻弱音小号，留白与静默，少即是多，调式音阶，电声融合。

## (2) 音高与和声方向

- 主：调式和声（多利亚等调式）、静态和声、少和弦变化；调性悬置、调式即和声；禁：比波普的密集和弦变化与功能解决。`artifact`

## (3) 旋律与节奏

- 旋律：小号旋律极简、长音、留白大、弱音器音色；节奏：摇摆中带自由、留白；织体：独奏与乐队对话、空间感大。`artifact`

## (4) 配器与音色

- 小乐队到电声乐队：小号、萨克斯、钢琴、贝斯、鼓，后期加电钢琴、电吉他、打击乐；音色：弱音小号冷峻、电声迷幻。`artifact`

## (5) 曲式与结构

- 曲式：调式曲式、专辑曲式；结构：主题—即兴—主题，即兴在调式内自由，高潮靠密度，结尾渐隐或戛然。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：调式爵士、弱音小号、留白、少即是多、电声融合、空间感。
- 不该写：见 Negative prompt。
- Negative prompt: `bebop chord chasing, dense harmony, sentimental swell, loud climax, formless noise, pretty melody`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Miles Davis, a 30-second piece for a late-night ramen shop with steam rising, Miles Davis style, modal jazz, cool muted trumpet, space and silence, minimal notes, modal scale, electric fusion, less is more`
- 中文对照：迈尔斯·戴维斯风格，为深夜拉面店升起的热气写一段 30 秒配乐，戴维斯风格，调式爵士，冷峻弱音小号，留白与静默，少即是多，调式音阶，电声融合。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
