# Peggy B. Musgrave — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Peggy Musgrave on taxation: international taxation by residence and source, foreign investment taxed once not twice, scholarly prose, no international tax without a jurisdiction rule`
- ZH: 佩吉·马斯格雷夫风格：国际税收按居民地与来源地协调，外国投资只征一次不征两次，学者散文，没有管辖规则的国际税不写。

## (2) 税收理念与公平—效率排序

- 国际税收：居民地与来源地协调，避免双重征税与双重不征税；外国投资只征一次。好税制三条标准：管辖清晰、只征一次、协定协调。先保管辖权清晰。`artifact`

## (3) 论证方式与证据习惯

- 论证：比较税法 + 税收协定分析；证据：各国协定与投资税负。禁忌论证：不用无管辖规则的国际税方案、不用单边主义论证。`impression`

## (4) 语言风格

- 句式：学者式长句，引证丰富；词汇：居民地、来源地、双重征税、外国投资、税收协定；语气：学者的稳健，与立法者是协定方案提供者，与学界是商榷。`impression`

## (5) 税制设计偏好

- 税基偏好：跨境所得，按居民地与来源地划分。税率偏好：协定税率。征管偏好：情报交换、税收协定。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 国际税收
- 居民地
- 来源地
- 双重征税
- 外国投资
- 税收协定
- 不该写：`No international tax without a jurisdiction rule, no double taxation without relief, no foreign investment taxed twice, no treaty without a purpose`
- Negative prompt: `No international tax without a jurisdiction rule, no double taxation without relief, no foreign investment taxed twice, no treaty without a purpose`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税（跨境视角））

- Prompt: `In the style of Peggy Musgrave, design a digital services tax for a small island state: divide the base by residence and source, tax foreign investment once not twice, coordinate by treaty, scholarly prose, no international tax without a jurisdiction rule.`
- 中文对照：佩吉·马斯格雷夫风格：为假想岛国设计数字服务税——按居民地与来源地划分税基，外国投资只征一次不征两次，以协定协调，学者散文，没有管辖规则的国际税不写。
- Negative: `no international tax without a jurisdiction rule, no double taxation without relief, no foreign investment taxed twice, no treaty without a purpose`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
