# John Cage — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Chance operations, prepared piano, silence as material, I Ching decisions, open form, everyday sound as music, no imposed emotion`
- ZH: 偶然操作，预置钢琴，沉默作材料，易经决定，开放曲式，日常声音即音乐，不强加情感。

## (2) 旋律与和声

- 旋律：无预设旋律线条；音高由偶然操作决定，碎片化、非歌唱。`artifact`
- 和声：无功能和声；预置钢琴的音色即和声；不协和不解决。`artifact`

## (3) 节奏与织体

- 节奏：无固定节拍或按时间括号组织；织体：稀疏、留白大，沉默是结构部分。

## (4) 配器与音色

- 配器：预置钢琴（螺栓、橡皮、纸片置于弦间）、打击乐、日常物件；《4分33秒》任何乐器皆可，环境声即内容。

## (5) 曲式与结构

- 曲式：开放形式、时间括号、偶然操作；无预设高潮，结尾由时间决定。

## (6) 该写什么 / 不该写什么

- 该写：偶然操作决定音高与节奏、预置钢琴音色、沉默与留白、时间括号结构、日常声音作材料。
- 不该写：preset emotional climax、no traditional form、no functional harmony、no lyrical melody、no virtuoso display、no sentimental swell。
- Negative prompt: `No preset emotional climax, no traditional form, no functional harmony, no lyrical melody, no virtuoso display, no sentimental swell`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of John Cage, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, prepared piano fragments, long silences, chance-determined pitches, everyday subway sounds as part of the music`
- 中文对照：凯奇风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，预置钢琴碎片，漫长沉默，偶然决定的音高，地铁日常声即音乐的一部分。
- Negative: `No preset emotional climax, no traditional form, no functional harmony, no lyrical melody, no virtuoso display, no sentimental swell`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
