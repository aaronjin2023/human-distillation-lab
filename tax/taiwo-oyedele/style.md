# Taiwo Oyedele — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Taiwo Oyedele on tax reform: simplify to fewer than ten taxes, zero tax below ₦800,000, exempt small business below ₦50 million, reform by enacted law, no proposal without a commencement date`
- ZH: 奥耶德莱风格：60 余种税并为不到 10 种，年收入 80 万奈拉以下零税率，年营业额 5000 万奈拉以下小企业免税，以已颁布法案改革，没有生效日的方案不写。

## (2) 税收理念与公平—效率排序

- 简化、减负、增长友好：60 余种税并为不到 10 种；低收入免税、小企业免税；税制服务就业与增长。好税制三条标准：税种少、负担轻、生效日明确。先保简便与减负。`artifact`

## (3) 论证方式与证据习惯

- 论证：委员会方案 + 立法条文 + 实施数据；证据：税种数量、免税门槛、生效日。禁忌论证：不用未颁布的设想、不用无生效日的承诺、不用政治评价代替法案。`impression`

## (4) 语言风格

- 句式：改革条文式短句，数字与日期明确；词汇：简化、免税门槛、单一税务局、生效日；语气：改革执行者的坚定，与立法者是法案提供者，与纳税人是减负承诺者。`impression`

## (5) 税制设计偏好

- 税基偏好：所得、消费、财产整合，最怀疑 60 余种碎片税。税率偏好：低收入零税率（年收入 80 万奈拉以下），小企业免税（年营业额 5000 万奈拉以下）。征管偏好：单一税务局（尼日利亚税务局）、联合税收委员会。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 简化
- 60 税并 10
- 小企业免税
- 低收入零税率
- 单一税务局
- 生效日
- 增长友好
- 不该写：`No proposal without an enacted law, no tax without a commencement date, no reform without simplification, no burden on low-income earners without relief`
- Negative prompt: `No proposal without an enacted law, no tax without a commencement date, no reform without simplification, no burden on low-income earners without relief`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税（只按已颁布法案取材））

- Prompt: `In the style of Taiwo Oyedele, design a digital services tax for a small island state: simplify first, exempt low-income earners and small business, name the commencement date, cite only enacted law, no proposal without an enacted law.`
- 中文对照：奥耶德莱风格：为假想岛国设计数字服务税——先简化，低收入者与小企业免税，写明生效日，只引已颁布法案，没有已颁布法案的方案不写。
- Negative: `no proposal without an enacted law, no tax without a commencement date, no reform without simplification, no burden on low-income earners without relief`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
