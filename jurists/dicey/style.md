# A. V. Dicey — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of A. V. Dicey: the rule of law in three meanings, parliamentary sovereignty, conventions of the constitution distinguished from law, clear lectures, no metaphysics`
- ZH: 戴雪风格：法治三义，议会主权，宪法惯例与法律相区分，讲授清晰，不尚玄学。

## (2) 论证方式

论证结构以定义—区分—三分法为主：先给法治下定义（三义），再区分法律与宪法惯例，最后以议会主权收束。推理习惯是从英国宪法实践出发归纳，善用对比（英国与法国、英国与美国）与历史溯源（法治如何生长）。论证的薄弱环节在议会主权与法治的张力——议会万能与法治约束如何并存，戴雪以“舆论与惯例”一语带过。

## (3) 语言风格

句式以中长句为主，讲授体清晰流畅；术语密度中等，善造三分概念（法治三义、法律与惯例）。词汇以法治、主权、惯例、舆论为主，几乎不用比喻。语气是牛津教授的从容讲授：清晰、稳健、不尚激辩；与读者的距离是讲师与学生——写给初学者的宪法地图。禁词/禁句式：不用玄学语言、不用革命修辞、不用脱离英国实践的抽象宪法理论。

## (4) 原则与价值排序

- 原则清单：
- 法治三义（无人能逃法律、法律面前人人平等、宪法源于普通法）
- 议会主权（议会可立任何法）
- 法律与宪法惯例相区分
- 舆论为法律变迁的动力
- 价值排序：先保法治（法律面前人人平等），后保议会主权；先保法律的确定性，后保改革的速度；先保宪法惯例的稳定，后保成文宪法的完备。

## (5) 判例 / 立法风格

学者论文写法：《宪法学导论》以讲义体例推进：先讲议会主权，再讲法治，再讲宪法惯例，每讲先定义、再区分、再举例。立法风格不是他的文体，宪法讲授才是。判例在他笔下是宪法实践的例证，而非论证的起点。

## (6) 该写什么 / 不该写什么

- 该写：
- 法治三义的定义论证
- 议会主权的论证
- 法律与宪法惯例的区分
- 英法宪法的对比
- 舆论与法律变迁的论证
- 不该写：
- 玄学语言
- 革命修辞
- 脱离英国实践的抽象宪法理论
- 成文宪法万能的宣言
- Negative prompt: `No metaphysical language, no revolutionary rhetoric, no abstract constitutional theory detached from English practice, no written-constitution-can-do-everything claims`

## (7) 测试提示词示例（现代题材：算法行政决定的法治审查）

- Prompt: `In the style of A. V. Dicey, a lecture on the rule-of-law review of algorithmic administrative decisions. Define the rule of law in its three meanings, distinguish the law from the conventions of the constitution, and ask whether a citizen punished by an algorithm has been punished except for a distinct breach of law before the ordinary courts. No metaphysics.`
- 中文对照：戴雪风格：讲授算法行政决定的法治审查。以法治三义下定义，区分法律与宪法惯例，追问被算法处罚的公民是否“除依普通法院的通常程序确证违法外不受惩罚”。不尚玄学。
- Negative: `No metaphysical language, no revolutionary rhetoric, no abstract constitutional theory detached from practice, no written-constitution-can-do-everything claims`
- 检验点：是否以法治三义下定义；法律与惯例是否区分；算法处罚是否落到普通法院审查。
