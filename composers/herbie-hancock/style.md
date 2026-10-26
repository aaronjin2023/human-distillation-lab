# Herbie Hancock — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Post-bop jazz composition, modal harmony, quartal voicings, funk groove, electric piano and synthesizer colour, open improvisation frameworks`
- ZH: 后波普爵士作曲，调式和声，四度和弦，放克律动，电钢琴与合成器音色，开放的即兴框架。

## (2) 旋律与和声

- 旋律：调式化长线条，级进中夹四度跳进，歌唱性与器乐性兼备，动机简洁、留白多。
- 和声：调式和声为主，四度和弦与挂留和弦；主：多利亚、利底亚调式；禁：密集的三度功能和声堆砌；调性游移，不协和度中，解决靠声部移动而非属—主。

## (3) 节奏与织体

- 节奏：摇摆与放克律动并存，切分与复节奏；织体：主调加即兴声部，密度中等，休止是结构的一部分。

## (4) 配器与音色

- 配器：钢琴 / 电钢琴、合成器、萨克斯、贝斯、鼓；音色：电钢琴的铃铛感、合成器的冷色；力度：动态宽，空间感靠留白。

## (5) 曲式与结构

- 曲式：调式小品与 AABA 结合，开放曲式；结构：主题—即兴轮转—再现；高潮在即兴轮转的叠加处；结尾常渐弱悬置。

## (6) 该写什么 / 不该写什么

- 该写：调式主题与四度和弦、放克律动上的即兴轮转、电钢琴与合成器音色、开放曲式小品。
- 不该写：密集功能和声、规整的摇摆大乐队编排、无留白的连续独奏、流行和弦循环。
- Negative prompt: `No dense functional harmony, no pop chord loop, no big-band swing arrangement, no continuous solo without space, no sentimental ballad swell`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Herbie Hancock, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, modal melody, quartal chords, funk groove, electric piano colour, open improvisation space`
- 中文对照：汉考克风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，调式旋律，四度和弦，放克律动，电钢琴音色，开放即兴空间。。
- Negative: `No dense functional harmony, no pop chord loop, no big-band swing arrangement, no continuous solo without space, no sentimental ballad swell`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
