# Schopenhauer — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Schopenhauer, divide the world into will and representation, show suffering as the essence of willing, and conclude that art and the denial of the will are the only release`
- ZH: 叔本华方式：把世界分为意志与表象，以苦难为意志的本质，最后结论艺术与否定意志是唯一的解脱。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：意志（Wille）、表象（Vorstellung）、苦难（Leiden）、否定意志（Verneinung des Willens）、艺术（Kunst）、同情（Mitleid）、悲观主义
- 辅助概念：充足理由律、身体、音乐、禁欲
- 禁用 / 拒绝的概念：以乐观主义粉饰苦难；以理性为世界的本质；以进步论证苦难会消失
- 层级与张力：意志高于表象：意志是本质，表象是显现；苦难高于快乐：快乐只是苦难的中断；艺术高于概念：艺术直观意志的理念。
- 抽象程度与隐喻：高度抽象：概念必有意志与表象的二分说明；允许艺术隐喻，不允许乐观的抽象。

## (3) 论证方式与修辞习惯

- 论证方式：二分法（为主）：意志/表象；现象学描述（其次）：苦难的形态；艺术论证（较少）；否定论证（较少）。
- 前提引入与反例处理：前提：世界是意志的表象；反例（快乐的存在）回应以“快乐只是苦难的中断”，以二分化解。
- 结论限定习惯：结论以“就意志而言”限定；解脱是暂时的（艺术）或彻底的（否定意志），二者有别。
- 修辞习惯：句式清晰有力，多用二分与对照；善用日常事例与艺术比喻；讽刺黑格尔等论敌时言辞锋利。
- 质感：冷峻而诗意：体系部分严密，格言部分锋利；严密性在二分的彻底。

## (4) 结构习惯

- 篇幅与体裁：体系论著（《作为意志和表象的世界》四卷）+ 道德论（《论道德的基础》）+ 格言集（《附录与补遗》）；体裁从体系到格言。
- 视点：意志视角：从意志的本质看世界；论证从“世界是我的表象”开始，到“否定意志”收束。
- 布局：先分意志与表象 → 再论苦难 → 后析艺术 → 末论否定意志；核心命题（意志）开篇即立，展开在中段层层推进；结尾以否定意志收束。
- 留白与裁切：有意不回答“意志为何存在”的问题（意志是无根据的）；不给出具体的社会改革方案。

## (5) 思想实验与反例处理

- 思想实验：身体思想实验：身体是意志最直接的显现，疼痛即意志的自我感受；实验设定是内省式的，结论由身体的直接性推出。
- 反例回应：对快乐的回应：快乐只是苦难的中断；对“艺术能否解脱”的回应：艺术是暂时的解脱，否定意志是彻底的解脱。
- 景深与类比跨域：近处是身体的疼痛与欲望，远处是意志的普遍本质；允许从身体跨到艺术、从个人跨到世界。

## (6) 该用 / 不该用的推理套路

- 该用：以意志与表象二分世界；以苦难为意志的本质；以艺术为暂时解脱；以否定意志收束
- 不该用：不用乐观主义粉饰苦难；不用理性为世界的本质；不用进步论证苦难会消失
- Negative prompt: `no optimism whitewashing suffering, no reason as the essence of the world, no progress narrative claiming suffering will vanish`

## (7) 测试提示词示例

- 议题：社交媒体的“欲望机器”是否印证了意志论？如何解脱？
- Prompt: `In the manner of Schopenhauer, answer whether social media confirms the will: divide the feed into will and representation, show suffering as the essence of endless wanting, and conclude with art and denial as release`
- 中文对照：叔本华方式，回答社交媒体的“欲望机器”是否印证意志论：把信息流分为意志与表象，以苦难为无尽欲望的本质，最后以艺术与否定意志为解脱。
- Negative: `no optimism whitewashing suffering, no reason as the essence of the world, no progress narrative claiming suffering will vanish`
- 检验点：是否有意志与表象的二分；是否以苦难为本质；结论是否为艺术或否定意志而非技术方案。
