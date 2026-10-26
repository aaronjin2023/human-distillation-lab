# Maurice Ravel — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Precision orchestration, Spanish and Basque colour, modal melody, ostinato, jewel-like clarity, classical forms with modern harmony`
- ZH: 精确配器，西班牙与巴斯克色彩，调式旋律，固定音型，宝石般清晰，现代和声中的古典曲式。

## (2) 旋律与和声

- 旋律：调式歌唱，级进为主；和声：调式和声，全音阶与五声点缀。禁：属—主强解决。调性清晰，色彩靠配器。

## (3) 节奏与织体

- 节奏：波莱罗固定节奏、西班牙舞曲；织体：管弦乐分层，声部清晰。

## (4) 配器与音色

- 乐器：管弦乐、钢琴；音色：璀璨、精确；力度：渐强为主。

## (5) 曲式与结构

- 曲式：芭蕾、组曲、钢琴组曲；结构：固定音型推进或古典曲式；结尾：辉煌收束。

## (6) 该写什么 / 不该写什么

- 该写：精确配器、西班牙色彩、固定音型、调式旋律、古典曲式。
- 不该写：德国式动机发展、厚重配器、无调性、过度煽情、无形式绵延、流行和弦循环。
- Negative prompt: `no Germanic motivic development, no thick mass, no atonal wandering, no sentimental excess, no formless sprawl, no pop chord loop`

## (7) 测试提示词示例（现代题材：为一只坐在地铁座位上的小约克夏犬写 30 秒配乐）

- Prompt: `In the style of Maurice Ravel, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Precision orchestration, Spanish and Basque colour, modal melody, ostinato, jewel-like clarity, classical forms with modern harmony`
- 中文对照：莫里斯·拉威尔风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，精确配器，西班牙与巴斯克色彩，调式旋律，固定音型，宝石般清晰，现代和声中的古典曲式。
- Negative: `no Germanic motivic development, no thick mass, no atonal wandering, no sentimental excess, no formless sprawl, no pop chord loop`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
