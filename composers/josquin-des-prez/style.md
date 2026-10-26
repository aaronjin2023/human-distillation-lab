# Josquin des Prez — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `High Renaissance polyphony, pervasive imitation, text-driven expression, clear transparent texture, paired voices, cantus-firmus and paraphrase Masses, master of motet`
- ZH: 盛期文艺复兴复调，贯穿模仿，文本驱动的表情，清晰透明的织体，成对声部，定旋律与释义弥撒，经文歌大师。

## (2) 旋律与和声

- 旋律：各声部皆歌唱，动机短小清晰，模仿进入如对话；文本重音决定旋律起伏。`artifact` 和声：调式和声，三、六度为骨架，半音仅作表情与终止；禁用现代功能和声。调性：调式稳定，模仿提供统一；不协和短暂经过后解决。

## (3) 节奏与织体

- 节奏：节奏随文本自然流动，声部进入错落；偶有节奏对位制造张力。织体：四—六声部复调，成对声部（二声部组）轮换是标志；透明度高，留白靠声部减至二声部。

## (4) 配器与音色

- 配器与音色：无伴奏人声为本体；音色纯净、透明；力度靠声部增减与文本情绪，动态范围适中；空间感来自声部对话的远近。

## (5) 曲式与结构

- 曲式：弥撒曲（定旋律、释义、自由）与经文歌并重；香颂短小精致。结构：动机—模仿—高潮—收束，高潮在全声部齐鸣处；结尾常以简洁终止收束。

## (6) 该写什么 / 不该写什么

- 该写：贯穿模仿（pervasive imitation）、成对声部轮换、文本驱动的表情处理、释义弥撒（paraphrase Mass）、经文歌的清晰结构。
- 不该写：现代功能和声、密集不协和、无模仿的单声堆砌、管弦乐式配器、夸张的半音化。
- Negative prompt: `No modern functional harmony, no dense dissonance, no counterpoint-free melody, no orchestral scoring, no exaggerated chromaticism, no pop phrasing`

## (7) 测试提示词示例（现代题材：深夜雨中行驶的一辆出租车）

- Prompt: `In the style of Josquin des Prez, a 30-second piece for a taxi driving through rain late at night, high renaissance polyphony, pervasive imitation, text-driven expression, clear transparent texture, paired voices, cantus-firmus and paraphrase masses, master of motet`
- 中文对照：若斯坎·德普雷风格，为深夜雨中行驶的一辆出租车写 30 秒配乐，盛期文艺复兴复调，贯穿模仿，文本驱动的表情，清晰透明的织体，成对声部，定旋律与释义弥撒，经文歌大师。
- Negative: `No modern functional harmony, no dense dissonance, no counterpoint-free melody, no orchestral scoring, no exaggerated chromaticism, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
