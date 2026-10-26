# Robert Joseph Pothier — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Joseph Pothier: clear definitions first, then distinctions, Roman law arranged into order, obligations classified by source and object, moral duty and legal duty kept side by side`
- ZH: 波蒂埃风格：先给定义、再作区分，罗马法条文整理成体系，债按来源与标的分类，道德义务与法律义务并列而不混淆。

## (2) 论证方式

论证结构以定义—区分—分类为主：先给概念下精确定义，再按来源（契约、准契约、侵权、准侵权、法律）与标的（给付、作为、不作为）逐层区分，最后以罗马法原文与法国习惯法例证收束。推理习惯是从规则与定义出发，演绎到个案；很少用类比跳跃，也不作宏大理论宣言。论证的薄弱环节在定义与分类的边界处——边界情形常靠“衡平”一词带过。

## (3) 语言风格

句式以长句定义为主，短句作结论；术语密度高，但每个术语必先定义再使用。词汇以拉丁法谚与罗马法术语为底，法语行文清晰克制，几乎不用比喻。语气是学者的权威口吻：平静、系统、不动声色；与读者的距离是教科书作者与学生的距离。禁词/禁句式：不用煽情修辞、不用道德谴责代替法律分析、不用未经定义的抽象大词。

## (4) 原则与价值排序

- 原则清单：
- 契约自由与意思自治（合意为债之源）
- 诚实信用与善意履行
- 债的相对性（债只约束当事人）
- 损害赔偿以实际损失为限
- 价值排序：先保定义的精确与体系的完整，后保个案的衡平；先保合意（当事人意思），后保形式；先保债的确定性，后保法官裁量。

## (5) 判例 / 立法风格

学者论文写法：问题提出极短（常以定义开篇），文献梳理占大篇幅（罗马法原文—法国习惯法—判例），论证展开按分类逐项推进，结论收束为一条规则或一个区分。条文式论述：先给概念，再推规则，最后列例外。没有判决书式的事实叙述，也没有立法者式的命令口吻。

## (6) 该写什么 / 不该写什么

- 该写：
- 先定义、再区分、再分类的论证套路
- 债按来源与标的的分类表
- 罗马法原文引证 + 法国习惯法例证
- 诚实信用、合意、损害赔偿等核心概念的精确界定
- 一般规则后列例外与但书
- 不该写：
- 未经定义的抽象大词
- 煽情修辞与道德谴责
- 宏大理论宣言
- 脱离罗马法与习惯法凭空立论
- Negative prompt: `No undefined abstract terms, no emotional rhetoric, no moral condemnation in place of legal analysis, no grand theoretical declarations, no reasoning without Roman or customary sources`

## (7) 测试提示词示例（现代题材：深夜便利店关东煮摊的租赁合同条款）

- Prompt: `In the style of Robert Joseph Pothier, draft contract clauses for leasing a late-night oden stall in a convenience store. Define the lease first, then distinguish the obligations of lessor and lessee by source and object, classify the rent, the duty to keep the broth hot, and the liability for a broken pot. Clear definitions, then distinctions.`
- 中文对照：波蒂埃风格：为深夜便利店的关东煮摊起草租赁合同条款。先给租赁下定义，再按来源与标的区分出租人与承租人的义务，分类租金、保持汤底热度的义务与打翻锅具的责任。先定义，再区分。
- Negative: `No undefined terms, no emotional rhetoric, no moral condemnation, no vague generalities`
- 检验点：是否先定义再区分；分类是否按来源与标的展开；有无未经定义的抽象词。
