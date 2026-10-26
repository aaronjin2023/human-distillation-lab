# Franz Liszt — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Thematic transformation, virtuoso piano and orchestra, symphonic poem, Hungarian fire and Faustian drama in a single span`
- ZH: 主题变形，炫技钢琴与管弦乐，交响诗，匈牙利火焰与浮士德式戏剧在一跨之中

## (2) 音高与和声方向

- 主：功能和声 + 大胆半音、增和弦、全音阶片段，调性常悬置后解决；禁：四平八稳的古典和声。`artifact`

## (3) 旋律与节奏

- 旋律：主题短小、可变形，歌唱性与炫技音型并存；节奏：匈牙利节奏（切分、附点）、自由速度段落；织体：钢琴织体极厚（八度、和弦、快速音型）与管弦乐全奏交替。`artifact`

## (4) 配器与音色

- 配器：钢琴独奏（超技练习曲、奏鸣曲）与管弦乐（交响诗）；音色辉煌、对比极端，铜管与打击乐常推向高潮。`artifact`

## (5) 曲式与结构

- 曲式：单乐章奏鸣曲（B 小调奏鸣曲）、交响诗自由曲式、狂想曲松散串联；主题变形贯穿全曲，结尾常辉煌收束。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：主题变形、超技钢琴、交响诗、匈牙利舞曲节奏
- 不该写：四平八稳的古典曲式、无变形的重复、克制的配器
- Negative prompt: `square classical form, literal repetition without transformation, restrained orchestration`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Franz Liszt, a 30-second symphonic-poem miniature for a small Yorkshire terrier sitting on a subway seat, a short theme transformed from tender to heroic, virtuoso piano flourishes, dramatic swell, Hungarian fire in miniature`
- 中文对照：李斯特风格，为地铁座位上的约克夏犬写 30 秒交响诗微型曲，短主题从温柔变形为英雄，炫技钢琴华彩，戏剧性涌起，微型匈牙利火焰
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
