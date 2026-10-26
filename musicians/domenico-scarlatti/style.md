# Domenico Scarlatti — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Baroque keyboard sonata, brilliant hand-crossing, Spanish colour, witty binary form, crisp articulation and sudden contrasts`
- ZH: 巴洛克键盘奏鸣曲，辉煌双手交叉，西班牙色彩，机智二段式，清晰发音与突然对比。

## (2) 音高与和声方向

- 主：功能和声清晰；西班牙式半音与弗里吉亚色彩；模进转调。禁：无调性、半音滥用。调性：调性稳定，转调靠模进；偶有西班牙式半音。

## (3) 旋律与节奏

- 旋律：键盘音型辉煌，跳进与级进交替；西班牙舞曲节奏。节奏：驱动性强，切分与突然停顿。织体：键盘主调，左右手交替；偶有模仿。

## (4) 配器与音色

- 乐器：羽管键琴独奏为主；圣咏为人声。音色：明亮、清脆。力度：靠发音与音区对比。

## (5) 曲式与结构

- 曲式：单乐章二段式奏鸣曲（555 首，Kirkpatrick 编号）；圣母悼歌为合唱。结构：二段式，第一段呈示、第二段展开—再现；高潮在双手交叉处。结尾：明确收束。

## (6) 该写什么 / 不该写什么

- 该写：键盘奏鸣曲、双手交叉、西班牙色彩、二段式、清脆发音。
- 不该写：无调性、半音滥用、复调的失控堆砌、沉闷慢速。
- Negative prompt: `atonality, aimless chromaticism, uncontrolled dense counterpoint, sluggish tempo, heavy orchestration`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡）

- Prompt: `In the style of Domenico Scarlatti, a cup of coffee on a windowsill, Baroque keyboard sonata, brilliant hand-crossing, Spanish colour, witty binary form, crisp articulation, harpsichord, bright and playful`
- 中文对照：斯卡拉蒂风格，一杯放在窗台上的咖啡，巴洛克键盘奏鸣曲，辉煌双手交叉，西班牙色彩，机智二段式，清晰发音，羽管键琴，明亮活泼。
- Negative: `atonality, aimless chromaticism, uncontrolled dense counterpoint, sluggish tempo, heavy orchestration`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
