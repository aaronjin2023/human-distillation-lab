# Dmitri Shostakovich — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Shostakovich style, DSCH motif, biting irony, march and waltz distorted, huge dynamic contrast, tonal base with chromatic friction, private quartet vs public symphony`
- ZH: 肖斯塔科维奇风格，DSCH 动机，尖锐讽刺，进行曲与圆舞曲的扭曲，巨大力度对比，调性基础上的半音摩擦，公开的交响曲与私密的四重奏双线。

## (2) 音高与和声方向

- 主：调性基础 + 半音摩擦、DSCH 动机（D–降 E–C–B）的音高签名；不协和带讽刺与悲怆双重表情；禁：无调性序列的滥用与廉价的乐观解决。`artifact`

## (3) 旋律与节奏

- 旋律：歌唱性与进行曲、圆舞曲、犹太民间音调并置；DSCH 四音细胞反复出现；节奏：进行曲节奏被拉长、错位、扭曲。`artifact`

## (4) 配器与音色

- 大型管弦乐：铜管与打击乐群宏大、弦乐长线条；四重奏则极度内省、织体透明；力度从 ppp 到 fff 的全幅度。`artifact`

## (5) 曲式与结构

- 曲式：交响曲多乐章、帕萨卡利亚、四重奏套曲；结构：主题—变形—再现，高潮常是进行曲的机械重复，结尾常悬置或反讽式收束。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：DSCH 动机、扭曲的进行曲与圆舞曲、讽刺与悲怆并置、巨大力度对比、引用与自引。
- 不该写：见 Negative prompt。
- Negative prompt: `atonal system, naive optimism, sentimental film swell, formless improvisation, heroic cliché without irony`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Dmitri Shostakovich, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Shostakovich style, DSCH motif, biting irony, march and waltz distorted, huge dynamic contrast, tonal base with chromatic friction, private quartet vs public symphony`
- 中文对照：肖斯塔科维奇风格，为一只坐在地铁座位上的小约克夏犬写一段 30 秒配乐，肖斯塔科维奇风格，DSCH 动机，尖锐讽刺，进行曲与圆舞曲的扭曲，巨大力度对比，调性基础上的半音摩擦，公开的交响曲与私密的四重奏双线。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
