# Philip Glass — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Philip Glass style, additive process, repetitive arpeggio, cyclic harmony, modular structure, steady pulse, hypnotic, opera and film`
- ZH: 格拉斯风格，加法过程，重复琶音，循环和声，模块结构，稳定脉冲，催眠感，歌剧与电影。

## (2) 音高与和声方向

- 主：循环和声进行、琶音和弦、调性清晰；和声节奏缓慢、解决温和；禁：半音化拥挤与戏剧性和声解决。`artifact`

## (3) 旋律与节奏

- 旋律：琶音型重复细胞、加法过程（音符逐个增加）；节奏：稳定脉冲、切分少；织体：多层琶音叠置，密度渐增。`artifact`

## (4) 配器与音色

- 键盘与木管主导：合成器、钢琴、萨克斯、木管、弦乐、人声；音色明亮、颗粒清晰；电影配乐中配器更丰满。`artifact`

## (5) 曲式与结构

- 曲式：模块循环、歌剧多场、电影配乐段落；结构：细胞重复—加法扩展—新模块进入，高潮靠密度，结尾渐隐。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：加法过程、重复琶音、循环和声、模块结构、稳定脉冲、歌剧与电影。
- 不该写：见 Negative prompt。
- Negative prompt: `dramatic climax, chromatic density, Romantic swell, irregular free rhythm, sentimental melody, formless wandering`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Philip Glass, a 30-second piece for a quiet night scene at a convenience store in a modern city, Philip Glass style, additive process, repetitive arpeggio, cyclic harmony, modular structure, steady pulse, hypnotic, opera and film`
- 中文对照：菲利普·格拉斯风格，为现代城市街角便利店的深夜写一段 30 秒配乐，格拉斯风格，加法过程，重复琶音，循环和声，模块结构，稳定脉冲，催眠感，歌剧与电影。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
