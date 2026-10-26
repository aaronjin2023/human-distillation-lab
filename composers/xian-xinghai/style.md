# Xian Xinghai — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Chinese modern composition, mass choral writing, folk melody with Western cantata form, march rhythm, direct and powerful lyricism`
- ZH: 中国近现代作曲，群众合唱写作，民间旋律加西方大合唱曲式，进行曲律动，直接有力的抒情。

## (2) 旋律与和声

- 旋律：民间歌谣与号子轮廓，级进与跳进并存，歌唱性极强，动机口号化、易记。
- 和声：功能和声加五声色彩；主：大调—小调、五声；禁：复杂半音；不协和度低，解决明确。

## (3) 节奏与织体

- 节奏：进行曲与号子律动，强拍明确；织体：合唱主调加管弦，密度中高，留白靠齐唱收束。

## (4) 配器与音色

- 配器：合唱、管弦乐；音色：明亮、有力；力度：动态宽，合唱段落突强。

## (5) 曲式与结构

- 曲式：大合唱、组曲；结构：民间主题—合唱发展—再现；高潮在合唱全奏处；结尾常以齐唱重音收束。

## (6) 该写什么 / 不该写什么

- 该写：民间歌谣旋律、群众合唱、进行曲律动、大合唱曲式。
- 不该写：复杂半音和声、室内乐式克制、无合唱的纯器乐抒情、西方浪漫铺陈。
- Negative prompt: `No complex chromatic harmony, no chamber-music restraint, no purely instrumental lyricism without chorus, no Western Romantic padding, no vague wandering without a march pulse`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Xian Xinghai, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a folk-like march melody, a mass chorus, direct and powerful lyricism, Yellow River drive`
- 中文对照：冼星海风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，民间进行曲旋律，群众合唱，直接有力的抒情，黄河般的驱动。。
- Negative: `No complex chromatic harmony, no chamber-music restraint, no purely instrumental lyricism without chorus, no Western Romantic padding, no vague wandering without a march pulse`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
