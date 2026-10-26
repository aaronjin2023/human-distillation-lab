# Thelonious Monk — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Angular melody, dissonant harmony, stride piano, unexpected silences, bebop with space, whole-tone and chromatic colour`
- ZH: 棱角旋律，不协和和声，跨步钢琴，意外沉默，比波普而留白，全音与半音色彩。

## (2) 旋律与和声

- 旋律：棱角分明，大跳与半音交替；主题短小、富于辨识。`artifact`
- 和声：不协和和弦，全音阶点缀；调性游移，解决出人意料。`artifact`

## (3) 节奏与织体

- 节奏：比波普快速度与突然沉默并存；跨步钢琴左手；织体：钢琴主导，小乐队透明。

## (4) 配器与音色

- 配器：钢琴、萨克斯、贝斯、鼓；音色干、棱角分明。

## (5) 曲式与结构

- 曲式：爵士标准曲（AABA）、布鲁斯；结构简洁，即兴框架内展开，高潮克制。

## (6) 该写什么 / 不该写什么

- 该写：棱角旋律、不协和和声、跨步钢琴、意外沉默、比波普节奏、全音色彩。
- 不该写：smooth lyrical melody as the main line、no functional harmony resolving on schedule、no dense big-band sound、no sentimental swell、no free improvisation without a written theme。
- Negative prompt: `No smooth lyrical melody as the main line, no functional harmony resolving on schedule, no dense big-band sound, no sentimental swell, no free improvisation without a written theme`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Thelonious Monk, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, angular melody, dissonant stride piano, unexpected silences, bebop pulse with space`
- 中文对照：孟克风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，棱角旋律，不协和跨步钢琴，意外沉默，比波普脉冲而留白。
- Negative: `No smooth lyrical melody as the main line, no functional harmony resolving on schedule, no dense big-band sound, no sentimental swell, no free improvisation without a written theme`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
