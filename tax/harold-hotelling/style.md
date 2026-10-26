# Harold Hotelling — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Harold Hotelling on taxation: price public services at marginal cost, tax the rent of exhaustible resources, welfare by mathematics, no public price without a marginal cost`
- ZH: 霍特林风格：公共服务按边际成本定价，对耗竭资源租金征税，以数学求福利，没有边际成本的公共定价不写。

## (2) 税收理念与公平—效率排序

- 公共定价按边际成本；耗竭资源租金应征税；福利最大化以数学求之。好税制三条标准：边际成本定价、资源租金征税、福利可证。先保边际原则。`artifact`

## (3) 论证方式与证据习惯

- 论证：数理福利经济学；证据：边际成本测算、资源租金估算。禁忌论证：不用无边际分析的定价、不用平均成本代替边际成本。`impression`

## (4) 语言风格

- 句式：数理短句，公式与散文并行；词汇：边际成本、耗竭资源、资源租金、福利；语气：数理经济学家的冷峻，与立法者是公式提供者，与公用事业是定价者。`impression`

## (5) 税制设计偏好

- 税基偏好：最信任耗竭资源租金，最怀疑无边际分析的定价。税率偏好：按租金定。征管偏好：与公共定价配套。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 边际成本定价
- 耗竭资源
- 资源租金税
- 福利
- 公共定价
- 不该写：`No public price without a marginal cost, no resource rent left untaxed, no tax without a welfare proof, no average cost in place of marginal cost`
- Negative prompt: `No public price without a marginal cost, no resource rent left untaxed, no tax without a welfare proof, no average cost in place of marginal cost`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税（资源租金视角））

- Prompt: `In the style of Harold Hotelling, design a digital services tax for a small island state: price public digital services at marginal cost, tax the rent of the scarce resource, prove welfare by mathematics, no public price without a marginal cost.`
- 中文对照：霍特林风格：为假想岛国设计数字服务税——公共数字服务按边际成本定价，对稀缺资源租金征税，以数学证明福利，没有边际成本的公共定价不写。
- Negative: `no public price without a marginal cost, no resource rent left untaxed, no tax without a welfare proof, no average cost in place of marginal cost`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
