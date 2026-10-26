# Tōru Takemitsu — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Japanese contemporary composition, sparse notes and long silences, pentatonic fragments, shakuhachi-like breath, delicate orchestral colour, dreamlike East-West fusion`
- ZH: 日本当代作曲，稀疏音符与长寂静，五声碎片，尺八式呼吸，精致管弦色彩，梦幻的东西融合。

## (2) 旋律与和声

- 旋律：五声碎片，短小、断续，音域窄，呼吸长，歌唱性让位于呼吸感。
- 和声：五声与半音化并置，功能和声淡化；主：五声、调式；禁：属—主强解决；不协和度中低，解决靠寂静。

## (3) 节奏与织体

- 节奏：自由、缓慢，长停顿；织体：稀疏，单音加极简伴奏，留白是主角。

## (4) 配器与音色

- 配器：尺八、琵琶、管弦乐；音色：透明、带水汽与木质感；力度：弱到中弱，极少强音。

## (5) 曲式与结构

- 曲式：自由曲式，碎片拼贴；结构：碎片—寂静—碎片；高潮在音色最精处而非音量最大处；结尾常渐弱、悬置。

## (6) 该写什么 / 不该写什么

- 该写：五声碎片与长寂静、尺八式呼吸、精致管弦色彩、东西乐器对照。
- 不该写：密集管弦堆砌、属—主强解决、连续高潮、规整曲式。
- Negative prompt: `No dense orchestral padding, no strong dominant-tonic resolution, no continuous climax, no rigid formal scheme, no sentimental melody`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Toru Takemitsu, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, sparse pentatonic fragments, long silences, shakuhachi-like breath, delicate orchestral colour, dreamlike`
- 中文对照：武满彻风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，稀疏五声碎片，长寂静，尺八式呼吸，精致管弦色彩，梦幻。。
- Negative: `No dense orchestral padding, no strong dominant-tonic resolution, no continuous climax, no rigid formal scheme, no sentimental melody`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
