# Antonín Dvořák — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Bohemian folk melody in classical forms, pentatonic warmth, Slavonic dance rhythms, cello singing over warm orchestration`
- ZH: 波希米亚民间旋律装进古典曲式，五声暖意，斯拉夫舞曲节奏，大提琴歌唱覆于温暖配器之上

## (2) 音高与和声方向

- 主：功能和声，五声音阶与民间调式作色彩，调性清晰；禁：无调性、为新奇而新奇的和声。`artifact`

## (3) 旋律与节奏

- 旋律：民间歌唱线，级进 + 五声跳进，乐句均衡；节奏：斯拉夫舞曲（波尔卡、弗里安特）切分与附点；织体：主调，弦乐歌唱、木管民间色彩。`artifact`

## (4) 配器与音色

- 配器：管弦乐温暖，弦乐主导，木管（尤其中音区）民间音色，铜管克制；大提琴协奏曲独奏歌唱性强。`artifact`

## (5) 曲式与结构

- 曲式：交响曲四乐章、协奏曲三乐章、舞曲组曲；《自新大陆》各乐章动机互引；结尾常辉煌收束。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：民间歌唱旋律、斯拉夫舞曲节奏、五声音阶、古典交响曲式
- 不该写：无调性漫游、为新奇而新奇、轻薄配器
- Negative prompt: `atonal wandering, novelty harmony, thin orchestration`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Antonin Dvorak, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a warm Bohemian folk-like melody, Slavonic dance lilt, pentatonic warmth, singing cello line over warm strings`
- 中文对照：德沃夏克风格，为地铁座位上的约克夏犬写 30 秒小品，温暖波希米亚民间式旋律，斯拉夫舞曲摇曳，五声暖意，歌唱性大提琴线覆于温暖弦乐之上
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
