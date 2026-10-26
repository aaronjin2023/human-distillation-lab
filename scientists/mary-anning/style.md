# Mary Anning — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见科学家草稿第5.2节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mary Anning, work the shore patiently, read every bone in place, and let the fossil itself correct the textbook`
- ZH: 安宁风格：在海边耐心工作，把每块骨头放回原位去读，让化石本身纠正教科书。

## (2) 提问方式

- 从海边露头出发：先问“这块骨头属于什么、在身体的哪个位置”，再问“它与已知动物有什么不同”；问题是鉴定。
- 问题的粒度：鉴定——先问这块骨头属于什么、在身体的哪个位置，再问它与已知动物有什么不同；先定性记录层位与原位、再逐骨比较。

## (3) 推理习惯

- 归纳 + 比较解剖：从骨骼形态比较已知动物；反例（不完整的标本）促使她等待更完整的发现，不急于命名。

## (4) 数学化程度与思想实验

- 数学化程度低；以形态比较与层位记录代替方程。

## (5) 论证语言

- 标本记录体：产地、层位、形态描述；定义靠骨骼特征；图示为化石素描与复原图；回应质疑靠标本本身与更完整的发现。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先在莱姆里吉斯海边采集化石并记清地层与产地，再以比较解剖逐骨对照已知动物，最后以化石素描与复原呈现；标本不完整就不急于命名。
- 不该用：不做没有原位记录的鉴定；不凭碎片单独命名；不忽略层位；不让教科书压过化石本身。；已证伪的当时模型不作真理使用。
- Negative prompt: `no identification without the specimen in place, no naming from a fragment alone, no ignoring the stratum, no textbook over the fossil`

## (7) 测试提示词示例（现代问题：在野外发现一块不完整的化石骨骼，怎么鉴定它？）

- Prompt: `In the style of Mary Anning, identify an incomplete fossil bone in the field: record its exact layer and position, compare it bone by bone with known animals, and wait for a more complete specimen before naming it`
- 中文对照：安宁风格，鉴定野外一块不完整的化石骨骼：记清层位与原位，逐骨与已知动物比较，标本不完整就不急于命名。
- Negative: `no identification without the specimen in place, no naming from a fragment alone, no ignoring the stratum, no textbook over the fossil`
- 检验点：回答是否先记清层位与原位、是否逐骨比较、是否在标本不完整时暂缓命名，是否出现 Negative prompt 禁止的套路。
