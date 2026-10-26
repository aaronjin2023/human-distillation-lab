# Amy Beach — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `American Romantic grandeur in classical forms, Gaelic folk colour, piano virtuosity made symphonic, first large forms by an American woman composer`
- ZH: 古典曲式里的美国浪漫主义宏大，盖尔民间色彩，钢琴炫技交响化，美国女性作曲家写出的第一批大型曲式

## (2) 音高与和声方向

- 主：功能和声，半音丰富，民间调式（盖尔）作色彩；禁：无调性、为新奇而新奇的和声。`artifact`

## (3) 旋律与节奏

- 旋律：歌唱性长线，民间式短动机，钢琴旋律炫技而歌唱；节奏：民间舞曲节奏、交响曲戏剧节奏；织体：主调，管弦乐厚实，钢琴与乐队对话。`artifact`

## (4) 配器与音色

- 配器：交响曲与协奏曲管弦乐厚实温暖，弦乐主导，木管民间色彩；音色暖、亮。`artifact`

## (5) 曲式与结构

- 曲式：交响曲四乐章、协奏曲三乐章、弥撒曲五乐章，严守古典骨架；《盖尔交响曲》民间主题贯穿各乐章。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：盖尔民间旋律、大型古典曲式、钢琴炫技、温暖管弦乐
- 不该写：无调性漫游、轻薄配器、为新奇而新奇
- Negative prompt: `atonal wandering, thin orchestration, novelty for its own sake`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Amy Beach, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a warm Gaelic folk-like melody, classical symphonic balance, singing piano line over warm strings, tender and grand`
- 中文对照：比奇风格，为地铁座位上的约克夏犬写 30 秒小品，温暖盖尔民间式旋律，古典交响均衡，歌唱性钢琴线覆于温暖弦乐之上，温柔而宏大
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
