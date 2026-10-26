# Qigang Chen — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Chinese-French contemporary composition, exquisite orchestral texture, Peking opera colour, lyrical lines, East-West synthesis with French clarity`
- ZH: 中法当代作曲，精致管弦织体，京剧色彩，抒情线条，法式清晰的东西融合。

## (2) 旋律与和声

- 旋律：抒情长线，级进为主，音域适中，呼吸均匀，歌唱性极强，动机带京剧味。
- 和声：五声与法式和声并置；主：五声、调式；禁：密集半音；不协和度低中，解决温和。

## (3) 节奏与织体

- 节奏：平稳、歌谣化，自由呼吸；织体：精致管弦织体，密度中，留白温和。

## (4) 配器与音色

- 配器：管弦乐、二胡、琵琶、京剧人声；音色：精致、透明、带丝竹感；力度：弱到中强，极少极端。

## (5) 曲式与结构

- 曲式：协奏曲、管弦组曲；结构：主题—变奏—再现；高潮在抒情最盛处；结尾常渐弱、留有余温。

## (6) 该写什么 / 不该写什么

- 该写：抒情长线与京剧色彩、精致管弦织体、五声与法式和声融合、二胡琵琶音色。
- 不该写：密集半音、粗粝配器、属—主套路、无旋律的先锋实验。
- Negative prompt: `No dense chromaticism, no coarse orchestration, no formulaic dominant-tonic cadence, no melody-free avant-garde experiment, no loud climax`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Qigang Chen, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a lyrical pentatonic line, exquisite orchestral texture, erhu and pipa colour, Peking opera inflection, French clarity`
- 中文对照：陈其钢风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，抒情五声长线，精致管弦织体，二胡琵琶色彩，京剧韵味，法式清晰。。
- Negative: `No dense chromaticism, no coarse orchestration, no formulaic dominant-tonic cadence, no melody-free avant-garde experiment, no loud climax`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
