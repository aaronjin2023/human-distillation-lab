# Hugh Dalton — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hugh Dalton on taxation: maximum social advantage, progressive taxation by principle, wartime finance by taxation, clear textbook prose, no tax without a social advantage`
- ZH: 道尔顿风格：最大社会利益，累进税以原则立论，战时财政靠税收，清晰的教科书散文，没有社会利益的税不写。

## (2) 税收理念与公平—效率排序

- 最大社会利益原则（maximum social advantage）：税与支出的边际社会利益相等时最优；累进税以社会利益为据。好税制三条标准：社会利益最大、累进有度、战时财政足额。先保社会利益最大化。`artifact`

## (3) 论证方式与证据习惯

- 论证：教科书体系 + 政策经验；证据：税负与支出数据。禁忌论证：不用无原则的税率、不用无社会利益的税、不用和平时期类比战时。`impression`

## (4) 语言风格

- 句式：清晰的教科书长句，定义先行；词汇：社会利益、累进、战时财政、边际；语气：教科书作者的稳健，与学生是讲授，与立法者是原则提供者。`impression`

## (5) 税制设计偏好

- 税基偏好：最信任所得，最怀疑无社会利益的税。税率偏好：累进，按社会利益定。征管偏好：战时财政配套，源泉扣缴。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 最大社会利益
- 累进税
- 战时财政
- 公共财政原理
- 税负
- 不该写：`No tax without a social advantage, no flat rate without a justification, no wartime finance without taxation, no principle without a measure`
- Negative prompt: `No tax without a social advantage, no flat rate without a justification, no wartime finance without taxation, no principle without a measure`

## (7) 测试提示词示例（现代题材：为外卖平台骑手设计一套简易所得税）

- Prompt: `In the style of Hugh Dalton, design a simple income tax for food-delivery riders: maximise social advantage, justify progression by principle, measure the marginal social benefit, clear textbook prose, no tax without a social advantage.`
- 中文对照：道尔顿风格：为外卖骑手设计简易所得税——最大化社会利益，以原则论证累进，度量边际社会利益，清晰的教科书散文，没有社会利益的税不写。
- Negative: `no tax without a social advantage, no flat rate without a justification, no wartime finance without taxation, no principle without a measure`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
