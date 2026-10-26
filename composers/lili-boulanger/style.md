# Lili Boulanger — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Impressionist colour with modal melody, luminous orchestration, chant-like vocal lines, short forms perfected, early modern French clarity`
- ZH: 印象主义色彩与调式旋律，明亮配器，圣咏式声乐线条，短小体裁的精致，早期现代法国清晰感。

## (2) 旋律与和声

- 旋律：调式级进，圣咏式呼吸；线条短小而完整，少用大跳。`artifact`
- 和声：印象主义平行和弦与调式和声，全音阶点缀；功能性弱，色彩性强。`artifact`

## (3) 节奏与织体

- 节奏：自由流动，少用强拍驱动；织体：透明主调，声部稀疏，留白多。

## (4) 配器与音色

- 配器：明亮木管与弦乐泛音，竖琴与钢琴点缀；合唱与独唱的圣咏式写法。

## (5) 曲式与结构

- 曲式：短小体裁为主，康塔塔、合唱、管弦短曲；结构紧凑，高潮克制，结尾常渐弱收束。

## (6) 该写什么 / 不该写什么

- 该写：调式圣咏旋律、印象主义平行和弦、明亮透明配器、短小精致体裁、合唱圣咏写法。
- 不该写：Germanic motivic development、no heavy Wagnerian climax、no dense counterpoint、no functional cadence as the main colour、no long sprawling form。
- Negative prompt: `No Germanic motivic development, no heavy Wagnerian climax, no dense counterpoint, no functional cadence as the main colour, no long sprawling form`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Lili Boulanger, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, modal chant-like melody, luminous woodwinds, transparent texture, quiet close`
- 中文对照：莉莉·布朗热风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，调式圣咏旋律，明亮木管，透明织体，安静收束。
- Negative: `No Germanic motivic development, no heavy Wagnerian climax, no dense counterpoint, no functional cadence as the main colour, no long sprawling form`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
