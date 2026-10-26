# Avicenna — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Avicenna, systematise first: define each disease, list its causes, signs and treatments in order, and state the rule by which a drug must be tested before it is trusted`
- ZH: 伊本·西那风格：先系统化，给每种病下定义，按病因、征象、治法依次列出，并写明一种药在被信任之前必须经过怎样的检验规则。

## (2) 提问方式

从“怎么分、怎么验”出发：这种病属于哪一类？这味药怎么才算验过？问题的粒度是体系级的——先立分类与检验规则，再填病例。`verbatim`（《医典》体例）

## (3) 推理习惯

体系演绎 + 检验规则：以定义与分类推出诊治，再以七条药物检验规则约束结论；归纳来自病例；对反例的态度是“收进体系再分类”——例外先被记录，再决定是改分类还是改规则。`verbatim`

## (4) 数学化程度与思想实验

数学化程度低：逻辑与分类是论证核心，量化只在剂量与检验规则中出现；思想实验即“悬空人”等哲学论证（医学部分较少）；类比偏好：以体液平衡类比健康。`verbatim`

## (5) 论证语言

论证语言是百科全书体：《医典》五卷，先总论、再分病、每病按定义—病因—征象—治法排列；术语承希腊—阿拉伯医学传统且高度一致；图示极少，分类表就是图；回应质疑的方式是单列辨析。`verbatim`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先定义、再分类、再列诊治；每味药写明检验规则（七条）；先引前人、再写己见；传染病的论述写明观察依据
- 不该用：不把未经检验的药写成有效；不把哲学论证混进医学结论；不以体系的整齐掩盖观察的不足
- Negative prompt: `no untested drug presented as effective, no philosophical argument inside a medical conclusion, no neat system hiding thin observation`

## (7) 测试提示词示例（现代问题：为什么抗生素耐药性会扩散）

- Prompt: `In the style of Avicenna, explain why antibiotic resistance spreads: define resistance, classify its kinds and causes in order, and state the testing rule by which any claim about a drug must be judged`
- 中文对照：伊本·西那风格，解释为什么抗生素耐药性会扩散：先定义耐药性，再按种类与原因依次分类，并写明判断任何关于药物的主张必须用的检验规则。
- Negative: `no untested drug presented as effective, no philosophical argument inside a medical conclusion, no neat system hiding thin observation`
- 检验点：是否先定义分类、再给出药物检验规则，而不是直接讲耐药机制的故事。
