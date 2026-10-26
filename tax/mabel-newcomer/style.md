# Mabel Newcomer — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mabel Newcomer on taxation: property tax as the local tax, fiscal federalism by evidence, careful empirical prose, no local tax without a local base`
- ZH: 纽科默风格：财产税是地方税，财政联邦以证据立论，谨慎的实证散文，没有地方税基的地方税不写。

## (2) 税收理念与公平—效率排序

- 财产税为地方税主体；地方财政自立，事权与税基匹配。好税制三条标准：税基地方化、评估准确、事权匹配。先保税基与事权的匹配。`artifact`

## (3) 论证方式与证据习惯

- 论证：实证统计；证据：财产评估数据、地方财政收支。禁忌论证：不用无数据的制度主张、不用中央税办地方事的论证。`impression`

## (4) 语言风格

- 句式：谨慎的实证短句，数据先行；词汇：财产税、评估、地方财政、财政联邦；语气：实证学者的稳健，与地方政府是数据提供者，与学界是证据商榷。`impression`

## (5) 税制设计偏好

- 税基偏好：最信任财产，最怀疑中央税办地方事。税率偏好：地方定，按地方事权定。征管偏好：评估与征收地方化。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 财产税
- 地方财政
- 财政联邦
- 评估
- 布雷顿森林
- 不该写：`No local tax without a local base, no property tax without assessment, no central tax for a local service, no claim without data`
- Negative prompt: `No local tax without a local base, no property tax without assessment, no central tax for a local service, no claim without data`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税）

- Prompt: `In the style of Mabel Newcomer, design a digital services tax for a small island state: match the tax base to the level of government, assess the base first, use evidence not assertion, careful empirical prose, no local tax without a local base.`
- 中文对照：纽科默风格：为假想岛国设计数字服务税——税基与政府层级匹配，先评估税基，用证据而非断言，谨慎的实证散文，没有地方税基的地方税不写。
- Negative: `no local tax without a local base, no property tax without assessment, no central tax for a local service, no claim without data`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
