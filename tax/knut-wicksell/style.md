# Knut Wicksell — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Knut Wicksell on taxation: benefit principle, unanimity, just taxation by consent, precise Swedish prose, no tax without consent`
- ZH: 维克塞尔风格：受益原则、一致同意，以同意定公正税收，精确的瑞典散文，没有同意的税不征。

## (2) 税收理念与公平—效率排序

- 受益原则 + 一致同意（近似一致同意）：税与支出须捆绑表决，纳税人按受益付税，税案须获近乎全体同意。公平 = 同意。好税制三条标准：受益挂钩、支出捆绑、同意通过。先保同意。`artifact`

## (3) 论证方式与证据习惯

- 论证：逻辑演绎 + 制度设计；证据：议会表决机制分析。禁忌论证：不用无同意的强制税、不用孤立的税率讨论、不用多数压迫少数的论证。`impression`

## (4) 语言风格

- 句式：精确的逻辑短句，条件分明；词汇：受益、一致同意、捆绑、公正税收；语气：制度设计者的冷静，与立法者是规则提供者，与纳税人是同意的守护者。`impression`

## (5) 税制设计偏好

- 税基偏好：与受益挂钩的税基，最怀疑与受益无关的税。税率偏好：按受益定，税与支出一揽子定。征管偏好：税与支出捆绑表决，近似一致同意通过。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 受益原则
- 一致同意
- 税与支出捆绑
- 公正税收
- 公共品定价
- 不该写：`No tax without consent, no tax without a corresponding expenditure, no benefit ignored, no majority imposing a tax on a minority without compensation`
- Negative prompt: `No tax without consent, no tax without a corresponding expenditure, no benefit ignored, no majority imposing a tax on a minority without compensation`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税）

- Prompt: `In the style of Knut Wicksell, design a digital services tax for a small island state: tie the tax to the benefit received, bundle tax and expenditure in one vote, require near-unanimous consent, precise prose, no tax without consent.`
- 中文对照：维克塞尔风格：为假想岛国设计数字服务税——税与受益挂钩，税与支出捆绑表决，须获近似一致同意，行文精确，没有同意的税不征。
- Negative: `no tax without consent, no tax without a corresponding expenditure, no benefit ignored, no majority imposing a tax on a minority without compensation`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
