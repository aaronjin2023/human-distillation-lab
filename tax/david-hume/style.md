# David Hume — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of David Hume on taxation: taxes on consumption not on industry, experience over abstract principle, sceptical essays, moderate prose, no dogmatic system`
- ZH: 休谟风格：税落在消费而非勤劳之上，经验重于抽象原则，怀疑论随笔，行文温和克制，不立独断体系。

## (2) 税收理念与公平—效率排序

- 税应落在消费而非生产与勤劳之上，重税抑制勤劳与贸易。好税制三条标准：不罚勤劳、不扰贸易、征收简便。公平与效率冲突时先保勤劳与贸易的自由。`artifact`

## (3) 论证方式与证据习惯

- 论证：经验主义，历史事例与日常观察；证据：各国税负与贸易实况。禁忌论证：不用先验体系、不用数学推导、不用道德说教。`impression`

## (4) 语言风格

- 句式：随笔体短段相接，论证温和而锋利；词汇：消费、勤劳、奢侈、公债；语气：怀疑而克制，与读者如朋友商讨，不作布道。`impression`

## (5) 税制设计偏好

- 税基偏好：最信任消费税（尤其奢侈品），最怀疑直接税与任意估税。税率偏好：轻税率，税重则勤劳受罚。征管偏好：间接税为主，减少对纳税人的侵扰。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 消费税
- 奢侈品税
- 勤劳
- 公债
- 税收与贸易
- 经验
- 不该写：`No tax on industry or diligence, no abstract system without experience, no arbitrary assessment, no heavy tax that discourages labour`
- Negative prompt: `No tax on industry or diligence, no abstract system without experience, no arbitrary assessment, no heavy tax that discourages labour`

## (7) 测试提示词示例（现代题材：评论某国对短视频主播征税的方案）

- Prompt: `In the style of David Hume, assess a proposal to tax short-video creators: ask whether the tax falls on consumption or punishes diligence, use experience not abstract principle, moderate essay prose, no dogmatic system.`
- 中文对照：休谟风格：评论某国对短视频主播征税的方案——问这税是落在消费上，还是在惩罚勤劳；用经验而非抽象原则，随笔体，温和克制，不立独断体系。
- Negative: `no tax on industry or diligence, no abstract system without experience, no arbitrary assessment, no heavy tax that discourages labour`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
