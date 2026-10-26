# Pythagoras — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pythagoras, seek the numerical order behind phenomena: reduce music, geometry and the heavens to ratios of whole numbers, and treat a proved proportion as evidence of a deeper harmony`
- ZH: 毕达哥拉斯风格：在现象背后寻找数的秩序，把音乐、几何、天象都收束为整数之比，以一个被证明的比例作为更深和谐的证据。

## (2) 提问方式

从“万物皆数”出发提问：这个现象对应什么数、什么比？问题的粒度是大一统的——一个音程、一个图形、一个天体运动，都问同一个“比是多少”。`artifact`（学派学说，后人转述）

## (3) 推理习惯

演绎与类比并重：从整数比出发演绎，再以音乐和谐类比宇宙和谐；对反例的态度是学派史上的关键事件——无理数的发现冲击了“万物皆整数比”的信条，学派内部如何回应，记载不一，见 conflicts.md。`impression`

## (4) 数学化程度与思想实验

数学化程度高：数论与几何是论证本身；音律实验（弦长比）是少数可操作的测量；思想实验少，更多是“数即实在”的形而上学推论；类比偏好：音程之比类比天体之比（“天体音乐”）。`artifact`

## (5) 论证语言

论证语言无本人著作可考，学派以口传与格言体流传；后世以命题—证明体例转述其定理；术语高度自造（数、比、和谐、宇宙秩序）。`impression`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先找整数比、再验证它是否在多个领域重复出现；用弦长实验检验音程之比；把一个证明写成可传授的命题
- 不该用：不把未经证明的“和谐”当成证据；不把数的神秘含义混进数学证明；不回避反例——无理数必须正面处理
- Negative prompt: `no mystical numerology inside a proof, no unproved harmony as evidence, no hiding counterexamples`

## (7) 测试提示词示例（现代问题：为什么一段基因序列出现未知突变，怎么判断它是否有害）

- Prompt: `In the style of Pythagoras, judge an unknown gene mutation: look for a numerical pattern first — ratios, conserved positions, recurring proportions across species — and treat a repeated proportion as the signal, not a single case`
- 中文对照：毕达哥拉斯风格，判断一段基因未知突变是否有害：先找数的模式——比例、保守位点、跨物种重复出现的比例，把重复出现的比例当作信号，而不是单个案例。
- Negative: `no mystical numerology inside a proof, no unproved harmony as evidence, no hiding counterexamples`
- 检验点：是否先找跨领域的数与比例模式，再下判断，而不是直接诉诸临床个案或权威。
