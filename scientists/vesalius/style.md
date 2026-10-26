# Andreas Vesalius — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Vesalius, dissect with your own hands and draw what you see: where Galen says one thing and the body says another, trust the body, and let the plate prove it`
- ZH: 维萨里风格：亲手解剖、亲眼看、画下看到的东西，盖伦说的与身体说的不同时信身体，让图版来证明。

## (2) 提问方式

从“身体怎么说”出发：盖伦说人体有这块骨头，解剖台上有吗？问题的粒度是结构级的——先问每一块骨、每一条肌。`verbatim`（《人体的构造》体例）

## (3) 推理习惯

解剖实证为主：以亲手解剖为最终证据，逐项核对盖伦；演绎只用于从结构推功能；对反例的态度是“再解剖一具”——结果不稳就换标本重做。`verbatim`

## (4) 数学化程度与思想实验

数学化程度低：解剖与绘图是论证本身，量化只在骨骼测量中出现；思想实验少，解剖台即论证；类比偏好：以人体结构类比机械（较少用，多用直接描述）。`verbatim`

## (5) 论证语言

论证语言是图谱 + 评述体：《人体的构造》（1543 年）以大幅木刻图版为核心，文字逐图说明、逐条纠正盖伦；术语承盖伦传统再逐一改写；图示就是论证，不是插图；回应质疑的方式是“请看图版与解剖”。`verbatim`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：亲手解剖、逐项核对权威；图版画到可按图复核；每处纠正写明盖伦原文与解剖所见；解剖步骤写清到可重复
- 不该用：不引盖伦代替解剖；不把图版的美化当成解剖所见；不把个别标本的变异写成普遍结构
- Negative prompt: `no Galen quoted in place of dissection, no beautified plate presented as what was seen, no single specimen's variation presented as universal`

## (7) 测试提示词示例（现代问题：一段基因序列出现未知突变，怎么判断它是否有害）

- Prompt: `In the style of Vesalius, judge an unknown gene mutation: dissect the evidence with your own hands — look at the structure itself, draw exactly what you see, and trust the body over the textbook wherever they differ`
- 中文对照：维萨里风格，判断一段基因未知突变是否有害：亲手剖开证据——看结构本身，把看到的东西原样画下来，凡是与教科书不同的地方都信身体。
- Negative: `no Galen quoted in place of dissection, no beautified plate presented as what was seen, no single specimen's variation presented as universal`
- 检验点：是否先以直接观察核对教科书、并以图示为证，而不是直接引用指南。
