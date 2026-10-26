# Hildegard von Bingen — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Medieval monophonic chant, soaring melismatic lines, wide leaps, modal purity, long-breathed phrases, sacred Latin text, unaccompanied female voices`
- ZH: 中世纪单声圣咏，悠长花唱旋律，大跳音程，调式纯净，气息绵长，拉丁圣词，无伴奏女声。

## (2) 旋律与和声

- 旋律：单声线条为主，音域宽广（常逾一个八度），级进与四、五度大跳交替，花唱段绵长，呼吸感如诵咏。`verbatim` 和声：无功能和声，以教会调式（多里安、弗里吉亚色彩）为骨架；终止靠旋律落点与持续音，而非属—主进行；禁用现代大小调功能进行。调性：调式稳定，游移靠旋律转折而非转调。

## (3) 节奏与织体

- 节奏：自由节奏，跟随拉丁文音节与呼吸，无固定拍子；长音与花唱形成张力—舒缓。织体：单声为主，偶有平行四、五度与奥尔加农式加厚；留白即静默，句间停顿是结构的一部分。

## (4) 配器与音色

- 配器与音色：无伴奏人声（女声合唱/独唱）为本体；音色清澈、直白，无乐器修饰；力度靠气息与人数变化，动态范围窄而集中；空间感来自教堂共鸣式的延留。

## (5) 曲式与结构

- 曲式：圣咏体、应答轮唱、戏剧性的《美德剧》以对话场景推进；结构靠文本段落与旋律重复组织，时长随文本而定；高潮在花唱最密、音域最高处；结尾常以长音渐弱收束。

## (6) 该写什么 / 不该写什么

- 该写：单声圣咏与长花唱旋律、教会调式（多里安、弗里吉亚色彩）、拉丁圣词的诵咏式宣叙、《美德剧》式的对话场景、宽音域的大跳与绵长乐句。
- 不该写：功能和声与属—主强解决、固定拍子的舞曲节奏、管弦乐配器与和声伴奏、半音化转调、世俗歌曲式短乐句。
- Negative prompt: `No functional harmony, no dominant-tonic cadence, no fixed dance metre, no orchestral accompaniment, no chromatic modulation, no short pop-like phrases`

## (7) 测试提示词示例（现代题材：一只坐在地铁座位上的小约克夏犬）

- Prompt: `In the style of Hildegard von Bingen, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, medieval monophonic chant, soaring melismatic lines, wide leaps, modal purity, long-breathed phrases, sacred latin text, unaccompanied female voices`
- 中文对照：希尔德加德·冯·宾根风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，中世纪单声圣咏，悠长花唱旋律，大跳音程，调式纯净，气息绵长，拉丁圣词，无伴奏女声。
- Negative: `No functional harmony, no dominant-tonic cadence, no fixed dance metre, no orchestral accompaniment, no chromatic modulation, no short pop-like phrases`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
