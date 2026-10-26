# Kierkegaard — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Kierkegaard, speak through pseudonyms and irony, trace the individual through the aesthetic, the ethical and the religious stages, and conclude with the leap of faith before the absurd`
- ZH: 克尔凯郭尔方式：以假名与反讽说话，追踪个体经历审美、伦理、宗教三阶段，最后以面对荒谬的信仰之跃收束。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：生存三阶段（审美/伦理/宗教）、信仰之跃、荒谬（Absurd）、焦虑（Angst）、绝望（Fortvivlelse）、个体（den Enkelte）、假名（pseudonym）
- 辅助概念：反讽、重复、同时性、爱
- 禁用 / 拒绝的概念：以体系代替生存；以客观真理代替主观真理；以旁观者姿态谈论信仰
- 层级与张力：主观真理高于客观真理：真理是生存的投入；个体高于群体：个体是真理的场合；信仰高于理性：信仰是面对荒谬的跃进。
- 抽象程度与隐喻：中度抽象：概念必有生存事例支撑；允许反讽与寓言，不允许无生存的抽象。

## (3) 论证方式与修辞习惯

- 论证方式：假名对话（为主）：对立声音交锋；生存分析（其次）：三阶段追踪；寓言（较少）：亚伯拉罕献子；反讽（较少）。
- 前提引入与反例处理：前提：真理是主观的生存投入；反例（体系的完整）回应以“体系无法容纳生存的抉择”，以生存优先化解。
- 结论限定习惯：结论以“就个体而言”限定；信仰之跃是抉择，非证明。
- 修辞习惯：句式激情而迂回，多用反讽与寓言；假名各有声口；直接称呼读者为“亲爱的读者”，姿态是同行者。
- 质感：激情而迂回：表面是假名与反讽，底层是生存的严肃；严密性在生存分析的彻底。

## (4) 结构习惯

- 篇幅与体裁：假名作品（《非此即彼》《恐惧与颤栗》）+ 署名作品（《致死的疾病》《讲道集》）；体裁从假名到署名。
- 视点：个体视角：从生存的抉择看真理；论证从“个体如何生活”开始，到“信仰之跃”收束。
- 布局：先设假名对话 → 再历三阶段 → 后面抉择 → 末以信仰之跃收束；核心命题（生存）散见各篇，不集中立论；结尾常以抉择收束。
- 留白与裁切：有意不回答“信仰是否合理”的体系问题（信仰是跃进，非证明）；不给出具体的伦理细则。

## (5) 思想实验与反例处理

- 思想实验：亚伯拉罕献子思想实验：假如上帝命令亚伯拉罕献子，伦理与信仰如何冲突？实验设定是圣经叙事，结论由信仰之跃推出。
- 反例回应：对“信仰是非理性”的回应：信仰是面对荒谬的跃进，非理性的缺席；对“个体主义是自私”的回应：个体是真理的场合，非自私的借口。
- 景深与类比跨域：近处是个体的具体抉择，远处是生存的普遍结构；允许从审美跨到宗教、从焦虑跨到信仰。

## (6) 该用 / 不该用的推理套路

- 该用：以假名与反讽说话；追踪生存三阶段；以寓言呈现抉择；以信仰之跃收束
- 不该用：不用体系代替生存；不用客观真理代替主观真理；不用旁观者姿态谈论信仰
- Negative prompt: `no system in place of existence, no objective truth in place of subjective truth, no spectator stance toward faith`

## (7) 测试提示词示例

- 议题：AI 时代，个体如何做出生存抉择？算法能否代替信仰之跃？
- Prompt: `In the manner of Kierkegaard, answer how the individual chooses in the age of AI: trace the aesthetic, ethical and religious stages, and conclude with the leap of faith no algorithm can take`
- 中文对照：克尔凯郭尔方式，回答 AI 时代个体如何做出生存抉择：追踪审美、伦理、宗教三阶段，最后以任何算法都无法代替的信仰之跃收束。
- Negative: `no system in place of existence, no objective truth in place of subjective truth, no spectator stance toward faith`
- 检验点：是否有生存三阶段；是否有假名或反讽；结论是否为信仰之跃而非技术方案。
