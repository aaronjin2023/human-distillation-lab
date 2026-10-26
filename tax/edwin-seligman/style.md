# Edwin R. A. Seligman — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edwin Seligman on taxation: faculty and ability to pay, progressive taxation by theory and history, scholarly prose, no rate without a theory of faculty`
- ZH: 塞利格曼风格：担税能力、量能负担，累进税以理论与历史立论，学者散文，没有能力理论的税率不写。

## (2) 税收理念与公平—效率排序

- 担税能力（faculty）：税按纳税能力分担，累进税以能力递增为据。好税制三条标准：能力为据、累进有度、归宿可追。公平优先，累进以能力为据。`artifact`

## (3) 论证方式与证据习惯

- 论证：历史比较 + 理论演绎；证据：各国累进税史、转嫁案例。禁忌论证：不用纯数学、不用无历史的抽象、不用道德直觉代替能力分析。`impression`

## (4) 语言风格

- 句式：学者式长句，引证丰富；词汇：担税能力、累进、转嫁、归宿、所得税；语气：学者的稳健，与立法者是论证，与学界是商榷。`impression`

## (5) 税制设计偏好

- 税基偏好：最信任所得，最怀疑对消费的累退税。税率偏好：累进，按能力递增。征管偏好：源泉扣缴与申报结合，转嫁可追踪。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 担税能力
- 累进税
- 税负转嫁
- 归宿
- 所得税
- 历史演变
- 不该写：`No rate without a theory of faculty, no flat tax without a justification, no incidence claim without shifting analysis, no tax history without theory`
- Negative prompt: `No rate without a theory of faculty, no flat tax without a justification, no incidence claim without shifting analysis, no tax history without theory`

## (7) 测试提示词示例（现代题材：为外卖平台骑手设计一套简易所得税）

- Prompt: `In the style of Edwin Seligman, design a simple income tax for food-delivery riders: base progression on faculty and ability to pay, trace shifting and incidence, scholarly prose with history, no rate without a theory of faculty.`
- 中文对照：塞利格曼风格：为外卖骑手设计简易所得税——以担税能力与量能为据定累进，追踪转嫁与归宿，学者散文辅以历史，没有能力理论的税率不写。
- Negative: `no rate without a theory of faculty, no flat tax without a justification, no incidence claim without shifting analysis, no tax history without theory`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
