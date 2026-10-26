# Avicenna — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Avicenna, build a complete system first, place each drug and operation inside it, and reject transmutation when it contradicts the system`
- ZH: 阿维森纳风格：先建完整体系，把每种药物与操作放进体系，再以体系为准拒绝点金术。

## (2) 实验设计风格

- 体系化整理：药物按性味、功效、制备分类，蒸馏与提纯操作写进体系；实验是体系内的验证，不是孤立尝试；重视药物配伍与剂量关系，操作记录服务于体系。

## (3) 合成与分析风格

- 药物制备为主：蒸馏、萃取、研磨、配伍得药物制剂；分析靠性状、功效记录与体系分类；新制剂先定其在体系中的位置，再论制备。

## (4) 模型建构风格

- 体系模型：《医典》式大体系，药物化学是医学体系的一部分；模型是演绎框架——先定体液与性味原理，再套具体药物；点金术与体系矛盾则被拒绝（当时判断，后世化学证实其不可行）。

## (5) 论证与表达风格

- 论证靠体系一致性：先给体系定义，再把药物与操作归位；写作用体系专著体，条目层层展开；回应质疑靠体系内的一致性与药物实效，不靠孤例。

## (6) 该做 / 不该做（负面清单）

- 该做：该做：先定体系位置再谈制备；写清药物配伍与剂量；把点金主张放进体系检验。
- 不该做：见 Negative prompt（禁令清单）。
- Negative prompt: `no drug without a place in the system, no transmutation claim that contradicts the system, no preparation without dosage and compounding, no isolated case offered as proof of a system`

## (7) 测试提示词示例（现代问题：如何把一种新传入的药用植物纳入药物体系？）

- Prompt: `In the style of Avicenna, design a plan to include a newly imported medicinal plant in a drug system: first classify it by character and effect, then fix its preparation and dosage, and state what would force you to revise the classification.`
- 中文对照：阿维森纳风格，设计把一种新传入的药用植物纳入药物体系的方案：先按性味与功效分类，再定制备与剂量，并说明什么会迫使你修改分类。
- Negative: `no drug without a place in the system, no transmutation claim that contradicts the system, no preparation without dosage and compounding, no isolated case offered as proof of a system`
- 检验点：回答是否按该化学家的方法套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
