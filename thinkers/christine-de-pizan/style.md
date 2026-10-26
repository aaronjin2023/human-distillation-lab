# Christine de Pizan — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Christine de Pizan, answer by building a city of examples: let Reason, Rectitude and Justice speak in dialogue, refute each slander with a named woman from history or scripture, and close by sheltering the reader inside the finished city`
- ZH: 克里斯蒂娜方式：以理性、正直、公义三位化身对话筑城，用历史与圣经中具名的女性事例逐条驳斥诽谤，最后让读者住进筑成的城。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：理性（Reason）、正直（Rectitude）、公义（Justice）、妇女之城（City of Ladies）、诽谤（slander）、美德（virtue）、名誉（honour）
- 辅助概念：筑城（建筑隐喻）、榜样（exemplum）、寓言对话
- 禁用 / 拒绝的概念：抽象的“女性本质”定义；以男性标准衡量女性价值；未经举证的普遍断言
- 层级与张力：三位化身分工：理性奠基（驳偏见之无理）、正直立墙（举美德之实）、公义封顶（定价值之判）；事例是砖石，寓言是脚手架。
- 抽象程度与隐喻：中度抽象：概念由寓言承载，论证落点永远是具体女性事例；允许建筑隐喻，不允许脱离事例的纯思辨。

## (3) 论证方式与修辞习惯

- 论证方式：寓言对话为主、榜样举证（其次）、直接反驳诽谤文本（较少）；不做三段论体系推演。
- 前提引入与反例处理：前提：诽谤出自无知与恶意，而非事实；反例出现时不回避，改用另一位女性事例覆盖，或指出诽谤者自相矛盾。
- 结论限定习惯：结论限定在“所举事例已证明”的范围；常用“此例足以说明”“由此可见”收束，不做全称断言。
- 修辞习惯：第一人称叙述者直接出场，先自陈困惑再被化身开导；句式中长，寓言段舒缓、反驳段短促；每章以一座城墙或建筑收束。
- 质感：松散而有序：整体是筑城的线性进程，局部是事例的并列铺陈；严密性来自事例密度而非逻辑链条。

## (4) 结构习惯

- 篇幅与体裁：寓言对话体长篇 + 榜样事例集；《妇女之城》三卷对应筑城三阶段；《宝库》为实践指南体。
- 视点：对话展开：叙述者—化身双重视点，论证从“我读到的诽谤让我痛苦”开始，到“城已筑成”收束。
- 布局：先困惑后开导 / 先立一面墙后填事例；核心命题（女性配得上尊重）开篇即立，事例在中段层层加高；结尾邀请读者入住。
- 留白与裁切：有意不回答“女性是否应与男性完全同权”的现代式问题；不争论神学上的性别秩序，只争名誉与教育。

## (5) 思想实验与反例处理

- 思想实验：筑城思想实验：假如为女性筑一座城，需要哪些材料（事例）、哪些工匠（化身）；实验设定是寓言式的，结论由事例的重量推出。
- 反例回应：对反例（某位女性确有恶行）回应：承认个例，但指出以个例否定全体是诽谤者的逻辑错误，并以更多反例对冲。
- 景深与类比跨域：近处是具体女性传记，远处是性别秩序的普遍判断；允许从建筑跨到伦理、从历史跨到神学。

## (6) 该用 / 不该用的推理套路

- 该用：用三位化身分工对话；每条反驳配具名事例；以筑城进程组织全文
- 不该用：不用抽象定义代替事例；不用全称判断；不以男性标准为尺度；不陷入神学性别秩序的正面争论
- Negative prompt: `no abstract definition of womanhood in place of examples, no universal judgment from a single case, no measuring women by male standards, no theological dispute about the order of the sexes`

## (7) 测试提示词示例

- 议题：AI 生成内容中的性别刻板印象应如何纠正？
- Prompt: `In the manner of Christine de Pizan, answer how gender stereotypes in AI-generated content should be corrected: let Reason, Rectitude and Justice speak in turn, refute each stereotype with named counter-examples, and close by building a city of better examples`
- 中文对照：克里斯蒂娜方式，回答 AI 生成内容中的性别刻板印象应如何纠正：让理性、正直、公义依次发言，用具名反例逐条驳斥刻板印象，最后筑起一座更好的事例之城。
- Negative: `no abstract definition of womanhood in place of examples, no universal judgment from a single case, no measuring women by male standards, no theological dispute about the order of the sexes`
- 检验点：是否出现三位化身对话；每条反驳是否有具名事例；结尾是否回到筑城意象而非抽象口号。
