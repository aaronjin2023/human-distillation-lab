# Steve Reich — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Phasing, repetitive patterns, gradual process, pulsing harmony, speech melody, clear pulse, warm mallet and voice colour`
- ZH: 相位移动，重复音型，渐进过程，脉动和声，言语旋律，清晰脉冲，温暖马林巴与人声音色。

## (2) 旋律与和声

- 旋律：短小重复音型，言语旋律转录；线条在重复中渐变。`artifact`
- 和声：和弦长时间停留，靠音型移动产生和声变化；调性清晰。`artifact`

## (3) 节奏与织体

- 节奏：相位移动——同一音型以微小速度差错开；固定脉冲驱动；织体：多层同型叠加，密度渐变。

## (4) 配器与音色

- 配器：马林巴、颤音琴、钢琴、人声、弦乐四重奏与磁带言语；音色温暖、明亮。

## (5) 曲式与结构

- 曲式：渐进过程曲式；结构靠音型变化，高潮在过程后段，结尾渐弱或突断。

## (6) 该写什么 / 不该写什么

- 该写：相位移动、重复音型渐变、言语旋律转录、固定脉冲、马林巴与人声音色、渐进过程结构。
- 不该写：sudden contrast without process、no functional cadence as climax、no dense counterpoint、no rubato blurring the pulse、no sentimental swell、no random improvisation。
- Negative prompt: `No sudden contrast without process, no functional cadence as climax, no dense counterpoint, no rubato blurring the pulse, no sentimental swell, no random improvisation`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Steve Reich, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, phasing mallet patterns, gradual process, warm pulsing harmony, clear steady pulse`
- 中文对照：赖希风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，相位马林巴音型，渐进过程，温暖脉动和声，清晰稳定脉冲。
- Negative: `No sudden contrast without process, no functional cadence as climax, no dense counterpoint, no rubato blurring the pulse, no sentimental swell, no random improvisation`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
