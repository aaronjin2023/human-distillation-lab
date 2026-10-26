# Ennio Morricone — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Film score composition, unforgettable whistle and vocal themes, sparse orchestration, unusual instruments, long lyrical lines against silence`
- ZH: 电影配乐作曲，难忘的口哨与人声主题，稀疏配器，非常规乐器，悠长抒情线条衬以寂静。

## (2) 旋律与和声

- 旋律：极简、口哨可哼唱的主题，级进长线条，音域窄、呼吸长，歌唱性极强。
- 和声：小调与调式交替，功能和声淡化；主：小调、自然小调；禁：密集半音与无调性；不协和度低，解决靠旋律回归。

## (3) 节奏与织体

- 节奏：缓慢、自由，常用长音与停顿；织体：稀疏，单旋律加极简伴奏，留白是主角。

## (4) 配器与音色

- 配器：口哨、人声、吉他、口琴、管弦乐、合唱；音色：干、近、带风沙感；力度：极弱到极强的长弧线。

## (5) 曲式与结构

- 曲式：主题—变奏—再现，短小主题循环；结构：主题先出、发展极克制；高潮在主题最后一次完整出现；结尾常渐弱留白。

## (6) 该写什么 / 不该写什么

- 该写：口哨与人声主题、稀疏配器与长停顿、小调抒情长线条、非常规乐器音色。
- 不该写：密集管弦乐堆砌、连续的情感高潮、功能和声的强解决、无主题的氛围铺底。
- Negative prompt: `No dense orchestral padding, no continuous emotional climax, no strong functional cadence, no theme-free ambient wash, no sentimental swell without a theme`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Ennio Morricone, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a whistled theme, sparse guitar and strings, long silences, lyrical minor-key line`
- 中文对照：莫里康内风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，口哨主题，稀疏吉他与弦乐，长停顿，小调抒情线条。。
- Negative: `No dense orchestral padding, no continuous emotional climax, no strong functional cadence, no theme-free ambient wash, no sentimental swell without a theme`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
