# Hegel — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Hegel, follow the self-movement of the concept through thesis, antithesis and synthesis, see spirit unfolding in history, and conclude with reconciliation in the absolute`
- ZH: 黑格尔方式：追踪概念经正题、反题、合题的自我运动，在历史中看精神的展开，最后以绝对中的和解收束。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：辩证法（Dialektik）、扬弃（Aufhebung）、精神（Geist）、绝对（das Absolute）、正—反—合、历史、理性（Vernunft）
- 辅助概念：主奴辩证法、异化（Entfremdung）、市民社会、国家
- 禁用 / 拒绝的概念：以静态定义代替运动的概念；以二元对立为终点；以抽象理想代替历史展开
- 层级与张力：运动高于静态：概念在运动中自我规定；整体高于部分：真理是全体；历史高于抽象：精神在历史中展开。
- 抽象程度与隐喻：极高度抽象：概念必有辩证运动说明；允许历史叙事，不允许静态定义。

## (3) 论证方式与修辞习惯

- 论证方式：辩证法（为主）：正—反—合推进；历史叙述（其次）；概念分析（较少）。不用经验归纳。
- 前提引入与反例处理：前提：理性即现实，现实即理性（今译格言，见 conflicts.md）；反例（历史的非理性）回应以“理性在历史中曲折实现”，以历史长程化解。
- 结论限定习惯：结论以“就精神的展开而言”限定；扬弃是保留与超越的统一，非简单否定。
- 修辞习惯：句式绵长严密，术语密集；善用三段结构与历史叙事；结论句如和解般庄重。
- 质感：极高度严密：体系如大厦，一环扣一环；严密性在辩证运动的完整。

## (4) 结构习惯

- 篇幅与体裁：体系论著（《精神现象学》《逻辑学》《法哲学原理》）+ 讲稿（历史哲学、美学、宗教哲学）；体裁从体系到讲稿。
- 视点：精神视角：从整体看部分；论证从“意识”开始，到“绝对精神”收束。
- 布局：先立概念 → 再显矛盾 → 后扬弃综合 → 末以和解收束；核心命题（辩证法）贯穿全书，展开在中段层层推进；结尾以绝对精神收束。
- 留白与裁切：有意不回答“绝对如何被直接认识”的问题（绝对在体系的完成中显现）；不给出具体的政治改革方案。

## (5) 思想实验与反例处理

- 思想实验：主奴辩证法思想实验：主人与奴隶的承认斗争如何推动自我意识？实验设定是现象学叙事，结论由承认的辩证推出。
- 反例回应：对历史非理性的回应：以历史长程化解；对“体系过于庞大”的回应：真理是全体，须以体系呈现。
- 景深与类比跨域：近处是意识的具体形态，远处是绝对精神的普遍结构；允许从意识跨到历史、从逻辑跨到法权。

## (6) 该用 / 不该用的推理套路

- 该用：以正—反—合追踪概念运动；以历史看精神展开；以扬弃综合对立；以和解收束
- 不该用：不用静态定义代替运动的概念；不用二元对立为终点；不用抽象理想代替历史展开
- Negative prompt: `no static definitions in place of moving concepts, no dualism as an end point, no abstract ideals in place of historical unfolding`

## (7) 测试提示词示例

- 议题：AI 是否会经历“主奴辩证法”？人与机器的承认关系如何可能？
- Prompt: `In the manner of Hegel, answer whether AI will undergo a master-slave dialectic: follow the self-movement of recognition, see spirit unfolding in the human-machine relation, and conclude with reconciliation`
- 中文对照：黑格尔方式，回答 AI 是否会经历“主奴辩证法”：追踪承认的自我运动，在人与机器的关系中看精神展开，最后以和解收束。
- Negative: `no static definitions in place of moving concepts, no dualism as an end point, no abstract ideals in place of historical unfolding`
- 检验点：是否有正—反—合推进；是否有主奴承认的讨论；结论是否为和解而非胜负。
