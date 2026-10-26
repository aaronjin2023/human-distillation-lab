# Nie Er — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Chinese modern composition, short march songs, folk melody with Western march form, direct slogan-like themes, brief life with lasting anthems`
- ZH: 中国近现代作曲，短小进行曲歌曲，民间旋律加西方进行曲曲式，直接的口号式主题，短暂一生留下传世颂歌。

## (2) 旋律与和声

- 旋律：民间歌谣轮廓，级进为主，跳进作号角，歌唱性极强，动机短小、口号化。
- 和声：功能和声加五声色彩；主：大调、五声；禁：复杂半音；不协和度低，解决明确。

## (3) 节奏与织体

- 节奏：进行曲律动，强拍明确；织体：人声主调加简单伴奏，密度低，留白靠齐唱。

## (4) 配器与音色

- 配器：人声、简单管弦或民乐；音色：明亮、直接；力度：中强，号角段落突强。

## (5) 曲式与结构

- 曲式：短歌曲式；结构：主题—重复—高潮—再现；高潮在主题最后一次齐唱；结尾常以重音收束。

## (6) 该写什么 / 不该写什么

- 该写：短小进行曲歌曲、民间歌谣旋律、口号式主题、直接的齐唱高潮。
- 不该写：复杂和声、长篇交响曲式、室内乐式克制、无旋律的实验。
- Negative prompt: `No complex harmony, no long symphonic form, no chamber-music restraint, no melody-free experiment, no vague wandering without a march pulse`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Nie Er, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a short march melody, a folk-like slogan theme, direct and stirring, a unison chorus lift`
- 中文对照：聂耳风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，短小进行曲旋律，民间口号主题，直接激昂，齐唱上扬。。
- Negative: `No complex harmony, no long symphonic form, no chamber-music restraint, no melody-free experiment, no vague wandering without a march pulse`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
