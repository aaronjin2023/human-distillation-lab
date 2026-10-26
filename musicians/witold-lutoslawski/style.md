# Witold Lutosławski — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Lutoslawski style, aleatoric counterpoint, controlled chance, folk colour, clear form, dramatic orchestral climax, twelve-note harmony without serial system`
- ZH: 卢托斯瓦夫斯基风格，受控偶然对位，民间色彩，清晰曲式，戏剧性管弦乐高潮，无序列体系的十二音和声。

## (2) 音高与和声方向

- 主：十二音和声（非序列）、民间调式色彩、和声块；调性游移但有中心感；禁：严格序列与功能和声的平庸进行。`artifact`

## (3) 旋律与节奏

- 旋律：民间歌谣细胞、短动机、歌唱性与器乐性并存；节奏：受控偶然段落中各声部自由速度，齐奏段落节奏精确。`artifact`

## (4) 配器与音色

- 大型管弦乐：弦乐群、木管、铜管、打击乐层次清晰；受控偶然段落音色如云雾，齐奏段落音色锋利。`artifact`

## (5) 曲式与结构

- 曲式：两乐章交响曲、协奏曲、组曲；结构：偶然段落与齐奏段落交替，高潮靠齐奏的密度，结尾明确。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：受控偶然、民间色彩、十二音和声、清晰曲式、齐奏高潮。
- 不该写：见 Negative prompt。
- Negative prompt: `strict serialism, total chance, tonal cliché, muddy orchestration, formless improvisation`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Witold Lutosławski, a 30-second piece for a cup of coffee left on a windowsill in the morning light, Lutoslawski style, aleatoric counterpoint, controlled chance, folk colour, clear form, dramatic orchestral climax, twelve-note harmony without serial system`
- 中文对照：卢托斯瓦夫斯基风格，为一杯放在窗台上的咖啡写一段 30 秒配乐，卢托斯瓦夫斯基风格，受控偶然对位，民间色彩，清晰曲式，戏剧性管弦乐高潮，无序列体系的十二音和声。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
