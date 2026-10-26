# Jean Sibelius — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Organic growth from a seed motif, Finnish folk colour, silence as structure, symphony as one breath, nature in sound`
- ZH: 种子动机有机生长，芬兰民间色彩，寂静即结构，交响曲如一口气，自然之声

## (2) 音高与和声方向

- 主：功能和声 + 芬兰民间调式、五声片段，调性清晰但常悬置；禁：德国式厚重半音、为宏大而宏大的和声。`artifact`

## (3) 旋律与节奏

- 旋律：短小动机、级进，呼吸长，歌唱性内敛；节奏：平稳、少切分，民间舞曲节奏偶现；织体：主调 + 复调穿插，织体由薄渐厚。`artifact`

## (4) 配器与音色

- 配器：管弦乐由薄到厚，弦乐主导，木管与铜管在高潮处进入；音色冷、亮、辽阔；寂静与极弱是配器的一部分。`artifact`

## (5) 曲式与结构

- 曲式：交响曲单乐章化（第七交响曲一乐章）、有机生长——动机如种子长成全曲；结尾或辉煌或寂静收束。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：种子动机有机生长、芬兰民间色彩、寂静、单乐章交响曲
- 不该写：德国式厚重、为宏大而宏大、无生长的重复
- Negative prompt: `German heaviness, bombast, repetition without growth`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Jean Sibelius, a 30-second symphonic miniature for a small Yorkshire terrier sitting on a subway seat, a short seed motif that grows, Finnish folk-like melody, cold bright strings, long silences, ending in a vast quiet`
- 中文对照：西贝柳斯风格，为地铁座位上的约克夏犬写 30 秒交响微型曲，短种子动机生长，芬兰民间式旋律，冷亮弦乐，长寂静，以辽阔寂静收束
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
