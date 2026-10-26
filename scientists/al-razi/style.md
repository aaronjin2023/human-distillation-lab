# Al-Razi — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Al-Razi, trust the bedside over the book: compare cases side by side, record what you actually saw, and let a single careful observation outweigh a quoted authority`
- ZH: 拉齐风格：信床边甚于信书，把病例并排比较，记下实际看到的东西，让一次细致的观察压过一句引用的权威。

## (2) 提问方式

从“床边所见”出发：这两个病人的疹子有何不同？这味药到底有没有效？问题的粒度是病例级的——先问个案，再问规律。`artifact`（《医学大全》体例）

## (3) 推理习惯

归纳为主：大量病例比较中归纳出鉴别点；演绎只用于从鉴别点推出诊断；对权威的态度是公开质疑（曾著书质疑盖伦）；对反例的态度是“记下来”——反例进病例集，不删。`artifact`

## (4) 数学化程度与思想实验

数学化程度低：观察与比较是论证本身，量化只在剂量与病程记录中出现；思想实验少，病例对照即论证；类比偏好：以已知病的病程类比未知病。`artifact`

## (5) 论证语言

论证语言是病例集 + 评述体：《医学大全》先引前人观点、再附自己的病例与评注；术语承希腊—阿拉伯医学传统；图示极少，病程描述就是图；回应质疑的方式是“病例在此，请复核”。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：病例并排比较、逐项列出异同；每个主张配病例记录；先引前人观点、再写自己的观察与评注；药效以对照观察检验
- 不该用：不引权威代替观察；不把单病例写成定律；不删反例病例
- Negative prompt: `no authority in place of observation, no single case presented as a law, no counterexample deleted`

## (7) 测试提示词示例（现代问题：一段基因序列出现未知突变，怎么判断它是否有害）

- Prompt: `In the style of Al-Razi, judge an unknown gene mutation: collect cases side by side, list exactly how carriers differ from non-carriers, and let one careful observation outweigh a quoted authority`
- 中文对照：拉齐风格，判断一段基因未知突变是否有害：把病例并排收集，逐项列出携带者与非携带者的不同，让一次细致的观察压过一句引用的权威。
- Negative: `no authority in place of observation, no single case presented as a law, no counterexample deleted`
- 检验点：是否逐项比较病例、列出异同，而不是直接引用指南结论。
