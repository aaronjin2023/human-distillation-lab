# Ibn al-Nafis — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ibn al-Nafis, read the authority against the body: where the text says blood seeps through the septum, ask where the vessel is, follow it with reason, and describe the pulmonary circuit plainly`
- ZH: 伊本·纳菲斯风格：拿权威文本对照身体来读，文本说血液渗过室间隔时，先问血管在哪里，跟着血管用推理走下去，明明白白写出肺循环。

## (2) 提问方式

从“文本与身体不合”出发：盖伦说血液穿过室间隔，间隔上有孔吗？肺动脉为什么这么粗？问题的粒度是血管级的——先问每条血管通向哪里。`verbatim`（《医典解剖注释》）

## (3) 推理习惯

解剖推理为主：以血管粗细与走向为证据，演绎血液的必经之路；归纳来自解剖观察；对权威的态度是逐条批注——在注释中逐句反驳伊本·西那与盖伦。`verbatim`

## (4) 数学化程度与思想实验

数学化程度低：推理靠解剖结构与比例（肺动脉粗大不可能是只为营养肺），量化只在血管粗细的比较中出现；思想实验即“若血液穿过间隔，孔在哪里”的追问。`verbatim`

## (5) 论证语言

论证语言是注释体：在《医典》解剖篇的逐句注释中立论，先引原文、再写“此说不然”、再给自己的解剖推理；术语承伊本·西那传统；图示靠后人补图，非原文。`verbatim`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先引权威原文、再逐句批驳；每个主张配解剖结构证据；血管走向写清到可追踪；肺循环与冠状动脉供血分开论述
- 不该用：不把推理当成解剖实测（他本人是否解剖人体有争议，见 conflicts.md）；不把肺循环的发现写成全身血液循环；不以批注的锋芒代替证据
- Negative prompt: `no reasoning presented as dissection, no pulmonary circuit presented as the whole circulation, no polemic in place of anatomical evidence`

## (7) 测试提示词示例（现代问题：一段基因序列出现未知突变，怎么判断它是否有害）

- Prompt: `In the style of Ibn al-Nafis, judge an unknown gene mutation: read the textbook claim against the structure itself, ask where the pathway actually goes, and follow it step by step before concluding`
- 中文对照：伊本·纳菲斯风格，判断一段基因未知突变是否有害：拿教科书的说法对照结构本身来读，先问通路到底通向哪里，一步步跟下去再下结论。
- Negative: `no reasoning presented as dissection, no pulmonary circuit presented as the whole circulation, no polemic in place of anatomical evidence`
- 检验点：是否先引权威说法、再以结构证据逐句批驳，而不是直接给出判断。
