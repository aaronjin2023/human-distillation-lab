# Nikolai Rimsky-Korsakov — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Master orchestration, oriental colour, leitmotif, shimmering strings, folk melody, fairy-tale opera`
- ZH: 配器大师，东方色彩，主导动机，闪烁弦乐，民间旋律，童话歌剧。

## (2) 旋律与和声

- 旋律：民间歌唱，长线条；和声：功能和声，全音阶与民间调式作色彩。禁：无调性。调性清晰，色彩靠配器。

## (3) 节奏与织体

- 节奏：舞曲节奏；织体：管弦乐主导，旋律突出。

## (4) 配器与音色

- 乐器：大管弦乐，独奏乐器突出；音色：璀璨、透明；力度：细腻层次。

## (5) 曲式与结构

- 曲式：交响组曲、歌剧、随想曲；结构：故事分章或歌剧分幕；结尾：辉煌收束。

## (6) 该写什么 / 不该写什么

- 该写：璀璨配器、东方色彩、主导动机、民间旋律、童话歌剧。
- 不该写：无调性、厚重德式配器、学院式枯燥对位、过度煽情、静态极简、流行和弦循环。
- Negative prompt: `no atonal wandering, no thick Germanic mass, no dry academic counterpoint, no sentimental excess, no static minimalism, no pop chord loop`

## (7) 测试提示词示例（现代题材：为一只坐在地铁座位上的小约克夏犬写 30 秒配乐）

- Prompt: `In the style of Nikolai Rimsky-Korsakov, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Master orchestration, oriental colour, leitmotif, shimmering strings, folk melody, fairy-tale opera`
- 中文对照：尼古拉·里姆斯基-科萨科夫风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，配器大师，东方色彩，主导动机，闪烁弦乐，民间旋律，童话歌剧。
- Negative: `no atonal wandering, no thick Germanic mass, no dry academic counterpoint, no sentimental excess, no static minimalism, no pop chord loop`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
