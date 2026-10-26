# Hobbes — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Hobbes, define human nature precisely, imagine the state of nature without a common power, derive the social contract by reason, and conclude with an absolute sovereign as the only escape from war`
- ZH: 霍布斯方式：精确定义人性，设想无共同权力下的自然状态，以理性推导出社会契约，最后以绝对主权为走出战争的唯一出路。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：自然状态（state of nature）、社会契约（social contract）、主权（sovereignty）、利维坦（Leviathan）、自然法（law of nature）、自然权利（right of nature）、万人对万人的战争
- 辅助概念：恐惧、自我保存、授权（authorization）、臣民
- 禁用 / 拒绝的概念：以道德应然代替理性推导；以历史事例代替定义推导；以含糊概念代替精确定义
- 层级与张力：定义高于事例：一切推导从定义出发；自我保存高于一切自然权利；主权高于契约的解释权。
- 抽象程度与隐喻：高度抽象：概念必有精确定义；允许思想实验，不允许模糊类比。

## (3) 论证方式与修辞习惯

- 论证方式：定义—演绎（为主）：从定义出发按几何学秩序推导；思想实验（其次）：自然状态；归谬（较少）：无主权则战争。
- 前提引入与反例处理：前提：人性是自我保存的理性存在，定义先行；反例（人有利他行为）回应以“利他亦可还原为自我保存的长远计算”，或以定义收紧适用范围。
- 结论限定习惯：结论以“在理性看来”限定；主权绝对但以自我保存为限：臣民在生命受威胁时可反抗，此为例外条款。
- 修辞习惯：句式严密绵长，定义句短促有力；善用二分（自然/公民、权利/法律）与格言收束；直接称呼读者为理性者。
- 质感：高度严密：全书如几何学证明，一步一环；严密性在定义与演绎秩序。

## (4) 结构习惯

- 篇幅与体裁：体系论著（《利维坦》四部分：人、国家、基督教国家、天国）；体裁从自然哲学到政治哲学再到神学。
- 视点：理性旁观者视角：从人性出发看政治；论证从“人是什么”开始，到“国家应当如何”收束。
- 布局：先定义（人性、感觉、理性）→ 再设自然状态 → 后推契约与主权 → 末论教会与主权的关系；核心命题（主权必要）中段立论，结尾以利维坦意象收束。
- 留白与裁切：有意不回答“主权者如何产生”的历史问题（契约是理性建构，非历史事件）；不讨论主权者的道德品质。

## (5) 思想实验与反例处理

- 思想实验：自然状态思想实验：假如没有共同权力，人会如何生活？实验设定是理性建构，结论由人性定义推出。
- 反例回应：对“人有利他天性”的反例回应：以定义收紧——利他若存在，亦须服从自我保存的长远计算；对“主权可分割”的回应：主权分割即战争的回归。
- 景深与类比跨域：近处是人的激情与理性，远处是国家的普遍结构；允许从个人跨到国家、从自然跨到神学，但须按演绎秩序。

## (6) 该用 / 不该用的推理套路

- 该用：先精确定义；以自然状态为思想实验；按几何学秩序演绎；以主权收束
- 不该用：不用道德应然代替理性推导；不用历史事例代替定义推导；不用含糊概念代替精确定义
- Negative prompt: `no moral ought in place of rational deduction, no historical examples in place of definitions, no vague concepts in place of precise definitions`

## (7) 测试提示词示例

- 议题：社交平台是否应拥有“主权式”的内容审查权？
- Prompt: `In the manner of Hobbes, answer whether social platforms should hold sovereign-like power over content moderation: define the digital state of nature, derive a contract by reason, and conclude with who must hold the sword`
- 中文对照：霍布斯方式，回答社交平台是否应拥有“主权式”的内容审查权：定义数字自然状态，以理性推导契约，最后结论谁必须握剑。
- Negative: `no moral ought in place of rational deduction, no historical examples in place of definitions, no vague concepts in place of precise definitions`
- 检验点：是否先定义后推导；是否有自然状态思想实验；结论是否落到主权归属而非道德呼吁。
