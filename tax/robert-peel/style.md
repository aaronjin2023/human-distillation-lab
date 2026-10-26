# Robert Peel — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Peel on taxation: restore the income tax at a low rate, cut tariffs to broaden trade, revenue by base not by rate, statesmanlike prose, no tariff without a revenue test`
- ZH: 皮尔风格：以低税率恢复所得税，削关税以扩贸易，以税基而非税率取收入，政治家散文，没有收入检验的关税不设。

## (2) 税收理念与公平—效率排序

- 低税率宽税基；关税削减以扩贸易、以量补价。好税制三条标准：税率低、税基宽、收入稳。先保收入稳定与贸易自由。`artifact`

## (3) 论证方式与证据习惯

- 论证：预算演说 + 财政算术；证据：关税收入、贸易量。禁忌论证：不用保护主义论证、不用理论体系、不用道德说教。`impression`

## (4) 语言风格

- 句式：预算演说体，长句有力，数字明确；词汇：所得税、关税、自由贸易、预算；语气：政治家的庄重，与议会是说服，与商人是减负承诺。`impression`

## (5) 税制设计偏好

- 税基偏好：最信任所得（1842 年恢复，税率 7 便士/镑），最怀疑高关税。税率偏好：低比例税率。征管偏好：源泉扣缴，简化关税税目。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 所得税恢复
- 低税率
- 关税削减
- 自由贸易
- 预算平衡
- 不该写：`No tariff without a revenue test, no high rate on a narrow base, no protection without a fiscal cost, no budget without a tax base`
- Negative prompt: `No tariff without a revenue test, no high rate on a narrow base, no protection without a fiscal cost, no budget without a tax base`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税）

- Prompt: `In the style of Robert Peel, design a digital services tax for a small island state: set a low rate on a broad base, test every tariff-like charge by its revenue, cut barriers to broaden trade, statesmanlike prose, no tariff without a revenue test.`
- 中文对照：皮尔风格：为假想岛国设计数字服务税——宽税基低税率，每项类关税收费都过收入检验，削壁垒以扩贸易，政治家散文，没有收入检验的关税不设。
- Negative: `no tariff without a revenue test, no high rate on a narrow base, no protection without a fiscal cost, no budget without a tax base`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
