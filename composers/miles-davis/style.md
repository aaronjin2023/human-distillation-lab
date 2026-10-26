# Miles Davis — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Modal jazz, cool muted trumpet, space and silence, minimal notes, Gil Evans orchestration, fusion groove, understatement as power`
- ZH: 调式爵士，冷峻弱音小号，空间与沉默，极简音符，吉尔·埃文斯配器，融合律动，克制即力量。

## (2) 旋律与和声

- 旋律：调式级进，音符极少；小号线条克制、歌唱。`artifact`
- 和声：调式和声，少用功能进行；《那又怎样》以 D 多利亚调式为底。`verbatim`

## (3) 节奏与织体

- 节奏：摇摆与融合律动并存；织体：小乐队透明，大乐队（埃文斯）层次丰富。

## (4) 配器与音色

- 配器：弱音小号、萨克斯、钢琴、贝斯、鼓；《西班牙素描》大乐队配器。

## (5) 曲式与结构

- 曲式：调式即兴框架、专辑曲式；结构靠调式与律动，高潮克制，结尾渐弱收束。

## (6) 该写什么 / 不该写什么

- 该写：调式和声、弱音小号、空间与沉默、极简音符、吉尔·埃文斯配器、融合律动。
- 不该写：dense bebop runs as the main line、no functional harmony as structure、no loud climax、no sentimental swell、no free improvisation without a modal framework。
- Negative prompt: `No dense bebop runs as the main line, no functional harmony as structure, no loud climax, no sentimental swell, no free improvisation without a modal framework`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Miles Davis, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, modal harmony, muted trumpet line, space and silence, minimal notes, cool groove`
- 中文对照：戴维斯风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，调式和声，弱音小号线条，空间与沉默，极简音符，冷峻律动。
- Negative: `No dense bebop runs as the main line, no functional harmony as structure, no loud climax, no sentimental swell, no free improvisation without a modal framework`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
