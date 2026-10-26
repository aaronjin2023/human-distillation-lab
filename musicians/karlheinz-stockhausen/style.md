# Karlheinz Stockhausen — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Stockhausen style, serialism extended to all parameters, electronic music, spatial music, moment form, formula composition, sound as cosmos`
- ZH: 施托克豪森风格，序列主义扩展到全部参数，电子音乐，空间音乐，瞬间曲式，程式作曲，声音即宇宙。

## (2) 音高与和声方向

- 主：全参数序列（音高、时值、力度、音色皆序列化）、电子音色、泛音列；无调性中心；禁：调性和声的回归与传统曲式的套用。`artifact`

## (3) 旋律与节奏

- 旋律：无歌唱旋律，音高序列点状分布；节奏：序列化的时值、空间化的声部移动；织体：多声道空间布局，声音在空间中移动。`artifact`

## (4) 配器与音色

- 电子音乐与大型管弦乐：磁带、合成器、多声道扬声器；《群》为三个管弦乐队，分置空间；《光》为七日歌剧周期。`artifact`

## (5) 曲式与结构

- 曲式：瞬间曲式（Moment form）、程式曲式；结构：瞬间并置而非发展，高潮靠空间与密度的变化，结尾开放。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：全参数序列、电子音色、空间布局、瞬间曲式、程式作曲。
- 不该写：见 Negative prompt。
- Negative prompt: `tonal cadence, singable melody, traditional sonata form, Romantic swell, regular beat`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Karlheinz Stockhausen, a 30-second piece for a late-night ramen shop with steam rising, Stockhausen style, serialism extended to all parameters, electronic music, spatial music, moment form, formula composition, sound as cosmos`
- 中文对照：施托克豪森风格，为深夜拉面店升起的热气写一段 30 秒配乐，施托克豪森风格，序列主义扩展到全部参数，电子音乐，空间音乐，瞬间曲式，程式作曲，声音即宇宙。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
