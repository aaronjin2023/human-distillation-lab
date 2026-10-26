# György Ligeti — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Ligeti style, micropolyphony, sound mass, cluster, slow transformation, mechanical rhythm, no melody, texture as form`
- ZH: 利盖蒂风格，微复调，音块，音簇，缓慢变形，机械节奏，无旋律，织体即曲式。

## (2) 音高与和声方向

- 主：音簇、微复调织体、半音拥挤；无调性中心、无功能进行；禁：调性和声的回归与传统旋律主题的套用。`artifact`

## (3) 旋律与节奏

- 旋律：无歌唱旋律，单声部线条淹没在织体中；节奏：机械重复、复节奏、速度错位；织体：多声部卡农以微小音程差叠置成音块。`artifact`

## (4) 配器与音色

- 大型管弦乐与合唱：弦乐群、木管群以微复调织体发声；钢琴练习曲以机械节奏与复节奏为材料；音色：云雾状、缓慢流动。`artifact`

## (5) 曲式与结构

- 曲式：音块的缓慢变形即曲式；结构：织体密度与音区的渐变，高潮靠密度而非音量突变，结尾常渐隐。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：微复调、音块、音簇、缓慢变形、机械节奏、织体曲式。
- 不该写：见 Negative prompt。
- Negative prompt: `singable melody, tonal cadence, Romantic swell, clear theme, regular beat, dramatic climax`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of György Ligeti, a 30-second piece for a rainy bus stop at dusk in a modern city, Ligeti style, micropolyphony, sound mass, cluster, slow transformation, mechanical rhythm, no melody, texture as form`
- 中文对照：利盖蒂风格，为现代城市黄昏雨中的公交站写一段 30 秒配乐，利盖蒂风格，微复调，音块，音簇，缓慢变形，机械节奏，无旋律，织体即曲式。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
