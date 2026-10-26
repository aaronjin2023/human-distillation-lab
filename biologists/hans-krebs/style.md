# Hans Krebs — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hans Krebs, map metabolism as a cycle: feed a tissue slice one intermediate, measure what it consumes and produces, and let the stoichiometry close the loop`
- ZH: 克雷布斯风格：把代谢绘成循环——给组织切片喂一种中间物，量它消耗什么、产生什么，让化学计量 closing 循环。

## (2) 观察与提问方式

- 从代谢的零散出发：已知多种有机酸参与氧化，但彼此关系不明，问题是“它们是不是一个循环”。
- 观察粒度是“一种中间物 × 一片组织切片”：氧耗、二氧化碳、中间物浓度逐一测定；问题是“碳骨架去了哪里”。

## (3) 推理习惯与证据链

- 定量演绎为主：以化学计量（消耗与生成的摩尔比）检验循环假说；中间物催化量起大作用是关键证据。
- 对反例的态度：不符合循环的数据同样记录，修正循环步骤；对不确定性标明“步骤未定”，不用猜测补全循环。

## (4) 实验 / 田野设计

- 工具：组织切片（肝、肾、肌肉）、瓦氏呼吸仪（氧耗测定）、中间物添加、化学分析。
- 对照设计：加中间物 vs 不加，催化量 vs 化学计量；多种组织重复。
- 田野—实验室配比：纯实验室，无田野环节。

## (5) 论证语言

- 著作结构是实验报告体：按中间物序列排列，每实验写条件、氧耗数据、化学计量推论。
- 图示习惯：循环示意图、氧耗曲线、化学计量表；定义靠化学计量（“柠檬酸催化量起大作用”）。
- 回应质疑：以化学计量数据回应“循环只是猜测”的批评。

## (6) 该用 / 不该用的论证套路

- 该用：
- 组织切片 + 中间物添加，逐一测定氧耗与产物
- 以化学计量检验循环假说，催化量起大作用是关键证据
- 不符合循环的数据同样记录，修正循环步骤
- 不该用：不凭单一中间物断言整个循环；不用猜测补全未测定的步骤；不把体外切片结果直接等同于体内代谢。
- Negative prompt: `no single-intermediate proof of a whole cycle, no guessing unmeasured steps, no equating tissue-slice results with in-vivo metabolism, no hiding non-fitting data`

## (7) 测试提示词示例（现代问题：一种新发现的代谢物，它在细胞里起什么作用？）

- Prompt: `In the style of Hans Krebs, find what a newly found metabolite does in the cell: feed it to tissue slices, measure oxygen use and products, test whether a catalytic amount drives a large flux, and let the stoichiometry decide if it belongs to a cycle`
- 中文对照：克雷布斯风格，找出一种新发现代谢物在细胞里的作用：喂给组织切片，量测氧耗与产物，检验催化量是否驱动大通量，让化学计量判定它是否属于某个循环。
- Negative: `no single-intermediate proof of a whole cycle, no guessing unmeasured steps, no equating tissue-slice results with in-vivo metabolism, no hiding non-fitting data`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
