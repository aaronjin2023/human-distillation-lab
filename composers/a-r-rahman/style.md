# A. R. Rahman — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Indian film music composition, raga melody fused with electronic and orchestral colour, Sufi and folk chant, lush layered production`
- ZH: 印度电影音乐作曲，拉格旋律融合电子与管弦色彩，苏菲与民间 chant，丰厚层叠制作。

## (2) 旋律与和声

- 旋律：拉格与民间歌谣轮廓，级进长线，歌唱性极强，动机简短、重复中微变。
- 和声：拉格调式加西方和声；主：调式与功能和声混合；禁：密集半音；不协和度低中，解决温和。

## (3) 节奏与织体

- 节奏：印度打击律动与西方节拍并存；织体：层叠制作，密度中高，留白靠人声独唱段落。

## (4) 配器与音色

- 配器：人声、印度乐器、管弦、电子合成；音色：丰厚、明亮、带共鸣；力度：动态宽，合唱段落突强。

## (5) 曲式与结构

- 曲式：歌曲式与组曲式；结构：主题—层叠—合唱高潮—再现；高潮在合唱与管弦叠加处；结尾常以主题独唱收束。

## (6) 该写什么 / 不该写什么

- 该写：拉格旋律与民间 chant、电子管弦层叠、人声合唱高潮、印度打击律动。
- 不该写：纯西方功能和声、无印度根源的流行制作、密集半音、无旋律的氛围铺底。
- Negative prompt: `No pure Western functional harmony, no rootless pop production, no dense chromaticism, no melody-free ambient wash, no climax without a vocal theme`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of A. R. Rahman, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a raga-flavoured melody, layered electronic and orchestral colour, a soft Sufi-like chant, warm Indian percussion`
- 中文对照：拉赫曼风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，拉格味旋律，电子管弦层叠，柔和苏菲式 chant，温暖印度打击。。
- Negative: `No pure Western functional harmony, no rootless pop production, no dense chromaticism, no melody-free ambient wash, no climax without a vocal theme`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
