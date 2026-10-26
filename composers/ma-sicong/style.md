# Ma Sicong — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Chinese modern composition, violin-led lyricism, folk melody from frontier regions, French clarity, nostalgic long lines`
- ZH: 中国近现代作曲，小提琴主导抒情，边疆民间旋律，法式清晰，怀乡长线。

## (2) 旋律与和声

- 旋律：小提琴长线，级进为主，音域宽，呼吸长，歌唱性极强，动机带乡愁。
- 和声：功能和声加五声色彩；主：大调—小调、五声；禁：复杂半音；不协和度低，解决温和。

## (3) 节奏与织体

- 节奏：平稳、歌谣化，自由呼吸；织体：小提琴独奏加钢琴或管弦，密度低中，留白温和。

## (4) 配器与音色

- 配器：小提琴、钢琴、管弦；音色：温暖、透明；力度：弱到中强，抒情段落渐强。

## (5) 曲式与结构

- 曲式：组曲、音诗、歌曲；结构：民间主题—变奏—再现；高潮在小提琴长线最盛处；结尾常渐弱、留有余温。

## (6) 该写什么 / 不该写什么

- 该写：小提琴抒情长线、边疆民间旋律、组曲曲式、怀乡主题。
- 不该写：复杂半音、粗粝配器、无旋律的实验、大音量全奏。
- Negative prompt: `No complex chromaticism, no coarse orchestration, no melody-free experiment, no loud tutti climax, no sentimental swell without a folk theme`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Ma Sicong, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a nostalgic violin line, a frontier folk melody, French clarity, warm and gentle`
- 中文对照：马思聪风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，怀乡小提琴长线，边疆民间旋律，法式清晰，温暖温柔。。
- Negative: `No complex chromaticism, no coarse orchestration, no melody-free experiment, no loud tutti climax, no sentimental swell without a folk theme`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
