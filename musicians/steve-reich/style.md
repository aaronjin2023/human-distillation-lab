# Steve Reich — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Steve Reich style, phasing, repetitive pattern, gradual process, audible process, pulsing rhythm, speech melody, mallet percussion`
- ZH: 赖希风格，相位移动，重复音型，渐进过程，可听的过程，脉冲节奏，言语旋律，打击乐（马林巴、颤音琴）。

## (2) 音高与和声方向

- 主：调性和声循环（11 个和弦的循环，见《十八位音乐家的音乐》）、缓慢和声节奏；和声清晰、解决温和；禁：半音化拥挤与功能和声的戏剧解决。`artifact`

## (3) 旋律与节奏

- 旋律：短小重复细胞、言语旋律（《不同的火车》用人声录音的语调作旋律）；节奏：相位移动、脉冲稳定、加法过程；织体：多层重复音型叠置。`artifact`

## (4) 配器与音色

- 打击乐与键盘主导：马林巴、颤音琴、钢琴、木管、弦乐、人声；音色明亮、颗粒清晰；力度平稳、少突强。`artifact`

## (5) 曲式与结构

- 曲式：过程即曲式、循环段落；结构：细胞重复—相位移动—新细胞进入，高潮靠密度叠加，结尾渐隐或戛然。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：相位移动、重复细胞、可听过程、言语旋律、打击乐脉冲、和声循环。
- 不该写：见 Negative prompt。
- Negative prompt: `dramatic climax, chromatic density, Romantic swell, irregular free rhythm, tonal cadence as drama, sentimental melody`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Steve Reich, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Steve Reich style, phasing, repetitive pattern, gradual process, audible process, pulsing rhythm, speech melody, mallet percussion`
- 中文对照：史蒂夫·赖希风格，为一只坐在地铁座位上的小约克夏犬写一段 30 秒配乐，赖希风格，相位移动，重复音型，渐进过程，可听的过程，脉冲节奏，言语旋律，打击乐（马林巴、颤音琴）。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
