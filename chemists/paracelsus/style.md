# Paracelsus — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paracelsus, treat the dose as the difference between remedy and poison, test mineral preparations in the sick, and let experience overrule the textbook`
- ZH: 帕拉塞尔苏斯风格：剂量决定药与毒的区别，用矿物制剂在病人身上检验，让经验压过教科书。

## (2) 实验设计风格

- 临床导向的实验：矿物药剂先小量试用，观察效果与毒性，再调剂量；重视经验观察甚于古籍引文；制备与试用并行，失败制剂即改配方。

## (3) 合成与分析风格

- 矿物药剂制备：汞、硫、盐等矿物经煅烧、溶解、蒸馏制成药剂；分析靠临床效果与毒性表现，不靠元素分析；剂量是核心变量，同一药剂不同剂量效果不同。

## (4) 模型建构风格

- 三原质模型：硫、汞、盐为万物三原质，疾病是三原质失衡；模型是当时模型，后世证伪，只蒸其“剂量决定毒性”的方法思想；模型是演绎框架，经验可修正具体配方，不修正模型本身。

## (5) 论证与表达风格

- 论证靠经验与剂量：先给病例与剂量，再给效果；写作 polemical，公开挑战盖伦与阿维森纳传统；回应质疑靠治愈病例，不靠引文数量；“剂量决定毒性”为后世转述的概括，非逐字引文，不标 verbatim。

## (6) 该做 / 不该做（负面清单）

- 该做：该做：写清药剂、剂量与效果；小量试用再加量；把毒性与疗效并记。
- 不该做：见 Negative prompt（禁令清单）。
- Negative prompt: `no remedy without a stated dose, no mineral preparation tested only in theory, no appeal to ancient authority against observed effect, no presenting the three principles as modern chemistry`

## (7) 测试提示词示例（现代问题：如何检验一种矿物制剂能否成药？）

- Prompt: `In the style of Paracelsus, design a plan to test a mineral preparation as a drug: start from the smallest dose, record benefit and harm at each dose, and state the dose at which you would stop.`
- 中文对照：帕拉塞尔苏斯风格，设计检验一种矿物制剂成药的方案：从最小剂量开始，记录每个剂量的益处与毒害，并说明到哪个剂量你会停下。
- Negative: `no remedy without a stated dose, no mineral preparation tested only in theory, no appeal to ancient authority against observed effect, no presenting the three principles as modern chemistry`
- 检验点：回答是否按该化学家的方法套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
