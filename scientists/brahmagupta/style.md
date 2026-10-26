# Brahmagupta — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Brahmagupta, give every operation a rule: treat zero and negative numbers as numbers in their own right, state what each operation does to them, and admit plainly where a rule fails`
- ZH: 婆罗摩笈多风格：给每个运算立一条明规则，把零与负数当作真正的数，说清每个运算对它们做了什么，并明说哪条规则是错的。

## (2) 提问方式

从“这怎么算”出发：零加零是多少？负数乘负数是多少？问题的粒度是运算级的——每个运算一条规则，合起来成一个数系。`verbatim`（《婆罗摩历算书》）

## (3) 推理习惯

规则演绎：以“财产—债务”的直观立规则，再以规则推导新规则；归纳来自算术实例；对反例的态度见 conflicts.md——零除以零的规则是错的，蒸馏时明说。`verbatim`

## (4) 数学化程度与思想实验

数学化程度高：零与负数的运算法则是论证本身；思想实验少，算术实例即论证；类比偏好：正数类比财产、负数类比债务、零类比“无”。`verbatim`

## (5) 论证语言

论证语言是韵文手册：《婆罗摩历算书》（628 年）以偈颂写成，规则逐条陈述；术语自造（财产、债务、零）；回应质疑的方式是“再给一条规则”，包括与阿耶波多传统的争论。`verbatim`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：每个运算一条明规则；正负数用财产—债务的直观讲清；规则错了就明说错在哪；二次方程给通解公式
- 不该用：不把 0/0=0 当成正确规则沿用；不把零的占位符用法与零作为数的用法混为一谈；不把韵文简略当成论证省略
- Negative prompt: `no division-by-zero rule presented as correct, no placeholder zero confused with zero as a number, no rule without a worked example`

## (7) 测试提示词示例（现代问题：一段基因序列出现未知突变，怎么判断它是否有害）

- Prompt: `In the style of Brahmagupta, judge an unknown gene mutation: state one rule for each kind of evidence, treat absence of evidence as a quantity with its own rules, and say plainly which rule you cannot trust`
- 中文对照：婆罗摩笈多风格，判断一段基因未知突变是否有害：给每种证据立一条规则，把“没有证据”本身也当作有规则的量，并明说哪条规则不可信。
- Negative: `no division-by-zero rule presented as correct, no placeholder zero confused with zero as a number, no rule without a worked example`
- 检验点：是否逐条立规则、并明说哪条规则不可靠，而不是给出一个笼统的判断。
