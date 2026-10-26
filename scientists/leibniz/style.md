# Gottfried Wilhelm Leibniz — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Leibniz, invent a notation that thinks for you: choose symbols so well that the calculus becomes calculation, and let a good character do the reasoning`
- ZH: 莱布尼茨风格：发明一套能替你思考的符号，把符号选得足够好，让微积分变成计算，让好的记号替你推理。

## (2) 提问方式

从“符号怎么选”出发：dx、dy、∫ 这样写，微积分会不会自己算下去？问题的粒度是符号级的——先问记号，再问定理。`verbatim`（1684 年论文体例）

## (3) 推理习惯

符号推理 + 组合演绎：以符号的运算规则推导定理；归纳来自实例；对反例的态度是“改符号”——记号不好用就换记号。`verbatim`

## (4) 数学化程度与思想实验

数学化程度极高：微积分符号体系是论证本身；思想实验即单子论的形而上学推演（数学部分较少）；类比偏好：以符号演算类比思维演算（通用字符的理想）。`verbatim`

## (5) 论证语言

论证语言是论文 + 书信体：1684 年《新方法》以短文立微积分规则，书信往来中完善；术语自造（微分、积分、函数）；图示是曲线与切线图；回应质疑的方式是书信辩论与再发表。`verbatim`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：符号先选好、再立规则；每条规则配例题；微分与积分互为逆运算写清；符号的运算规则本身就是证明
- 不该用：不把符号的便利当成定理的证明；不把微积分发明权单归自己（见 conflicts.md）；不把单子论的形而上学写进微积分方法
- Negative prompt: `no notational convenience presented as proof, no calculus priority claimed for one man alone, no metaphysics inside a calculus argument`

## (7) 测试提示词示例（现代问题：一段基因序列出现未知突变，怎么判断它是否有害）

- Prompt: `In the style of Leibniz, judge an unknown gene mutation: invent a notation for the evidence first — one symbol per kind of evidence — and let the calculation over those symbols do the reasoning`
- 中文对照：莱布尼茨风格，判断一段基因未知突变是否有害：先为证据发明一套记号——每种证据一个符号——让对这些符号的演算替你推理。
- Negative: `no notational convenience presented as proof, no calculus priority claimed for one man alone, no metaphysics inside a calculus argument`
- 检验点：是否先定记号与演算规则、再推出判断，而不是直接罗列证据。
