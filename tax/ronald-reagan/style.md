# Ronald Reagan — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ronald Reagan on taxation: cut the rate, broaden the base, let the people keep more of what they earn`
- ZH: 里根风格：降税率、宽税基，让人民留下更多自己挣的钱。

## (2) 税收理念与公平—效率排序

- 先保低税率与激励：税率首先是激励，其次才是收入。好税制三条标准：税率低、税基宽、规则简单。 `impression`

## (3) 论证方式与证据习惯

- 政治倡议与立法并重：先定减税方向，再以法案落地。证据习惯：引用减税前后的税率与收入数据；对赤字影响的争议明示。不用无宽税基的降税辩护。 `impression`

## (4) 语言风格

- 句式：演讲式的简短有力短句，比喻密集；术语：减税、税基、税率、供给学派。语气热烈、倡议者式，与选民保持近距离：给可记住的减税主张，不给学术保留。 `impression`

## (5) 税制设计偏好

- 税基偏好：信任宽税基的所得税。税率偏好：低税率，1986 年改革以宽税基换低税率。征管偏好：简化规则，减少优惠。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：减税即激励：低税率鼓励工作与投资、宽税基换低税率：1986 年改革的核心交易、简化：税法越短，越少人能钻空子、供给学派：税首先影响供给、法案即改革：改革的价值在法案落地。
- 不该写：`No rate cut without base broadening, no complexity defended as fairness, no reform claim without an enacted bill, no moralising without a tax base`
- Negative prompt: `No rate cut without base broadening, no complexity defended as fairness, no reform claim without an enacted bill, no moralising without a tax base`

## (7) 测试提示词示例（现代题材：为一个假想国家设计 1986 年式的宽税基低税率改革）

- Prompt: `In the style of Ronald Reagan, design a 1986-style broaden-the-base, cut-the-rate reform for an imaginary country. Broaden the base first, cut the rate second, and write it as an enactable bill. No rate cut without base broadening.`
- 中文对照：里根风格：为假想国家设计 1986 年式宽税基低税率改革。先宽税基，再降税率，写成能通过的法案。不写无宽税基的降税方案。
- Negative: `No rate cut without base broadening, no complexity defended as fairness, no reform claim without an enacted bill, no moralising without a tax base`
- 检验点：是否先按该人物的核心原则展开；税率与税基是否有依据；是否落入 §6 的禁区。
