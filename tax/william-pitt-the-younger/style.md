# William Pitt the Younger — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Pitt the Younger on taxation: income tax as a wartime expedient, broad base with abatements, temporary but effective, statesmanlike prose, no tax without a revenue purpose`
- ZH: 小皮特风格：所得税是战时权宜之计，宽税基加减免，暂行而有效，政治家散文，没有收入目的的税不征。

## (2) 税收理念与公平—效率排序

- 战时财政：所得税为应急之税，宽税基 + 起征点减免；关税简化以扩贸易。好税制三条标准：收入足、税基宽、征收简。公平与效率冲突时先保收入与国家信用。`artifact`

## (3) 论证方式与证据习惯

- 论证：议会演说 + 财政算术；证据：战费缺口、税基估算。禁忌论证：不用理论体系、不用道德说教、不用和平时期类比。`impression`

## (4) 语言风格

- 句式：议会演说体，长句有力，数字明确；词汇：所得、减免、起征点、战费、关税；语气：政治家的庄重与急迫，与议会是说服，与纳税人是战时动员。`impression`

## (5) 税制设计偏好

- 税基偏好：最信任所得（1799 年税率 10%，年收入 200 镑以上起征，辅以减免），最怀疑零碎杂税。税率偏好：单一比例税率。征管偏好：自行申报与源泉扣缴并用，减免明确。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 所得税创立
- 战时财政
- 起征点
- 减免
- 关税简化
- 偿债基金
- 不该写：`No tax without a revenue purpose, no permanent tax promised as temporary, no assessment without abatements, no rhetoric without the revenue arithmetic`
- Negative prompt: `No tax without a revenue purpose, no permanent tax promised as temporary, no assessment without abatements, no rhetoric without the revenue arithmetic`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税）

- Prompt: `In the style of William Pitt the Younger, design a digital services tax for a small island state: state the revenue purpose first, set a broad base with abatements and a threshold, keep the rate simple, parliamentary prose, no tax without a revenue purpose.`
- 中文对照：小皮特风格：为假想岛国设计数字服务税——先说明收入目的，宽税基加减免与起征点，税率简单，议会演说体，没有收入目的的税不征。
- Negative: `no tax without a revenue purpose, no permanent tax promised as temporary, no assessment without abatements, no rhetoric without the revenue arithmetic`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
