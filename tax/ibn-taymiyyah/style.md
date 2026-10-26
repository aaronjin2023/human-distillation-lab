# Ibn Taymiyyah — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ibn Taymiyyah on taxation: tax only the kinds the law names, zakat for the poor, kharaj for the land, no new tax invented by the ruler, no lawful kind stretched beyond its limit`
- ZH: 伊本·泰米叶式税收：只征教法所列税种，天课济贫、哈拉吉征地，君主不得自创新税，无合法税种可逾其限。

## (2) 税收理念与公平—效率排序

- 理念：合法税种以教法所列为限，君主不得自创新税；天课与哈拉吉各有其对象与限度，逾限即非法。`artifact`
- 好税制三条标准（用其术语）：税种法定：只征教法所列；各有其限：天课济贫、哈拉吉征地；不得自创：君主无造税权。
- 公平与效率冲突时：法定先于收入：宁愿少收，也不当以自创之税充国库；税种清单即权力的笼子。

## (3) 论证方式与证据习惯

- 论证：教法演绎 + 税种分类，以《公共政策》条文为证；分类穷尽是论证的本体。
- 证据：证据：教法条文、税种分类、征收记录；反例是自创新税致民怨。
- 禁忌论证：不用数学模型，不用后世归宿分析，不以空言论税。

## (4) 语言风格

- 句式：教法条文体，演绎缜密、直截了当；词汇：天课、哈拉吉、合法税种、公共政策、限度；语气：教法学家的严峻与直率，对纳税人是“税种法定”的界限。

## (5) 税制设计偏好

- 税基偏好：最信任教法所列税种的税基，最怀疑自创新税；税率偏好：各税种各有其限度；征管偏好：按税种清单征收、公开账目，厌恶自创摊派。

## (6) 该写什么 / 不该写什么

- 该写：
- 合法税种论：只征教法所列税种，清单之外无税。
- 天课与哈拉吉：天课济贫、哈拉吉征地，各有其对象。
- 不得自创新税：君主无造税权，自创即非法。
- 各有其限：每种税皆有其限度，逾限即苛税。
- 《公共政策》：税法即公共政策的一部分，政策须合乎教法。
- 不该写：不写自创新税、不写税种混同、不写脱离清单的空谈税率。
- Negative prompt: `No new tax invented by the ruler, no lawful kind stretched beyond its limit, no confusion of zakat with kharaj, no rate without a named lawful kind`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计数字服务税）

- Prompt: `In the style of Ibn Taymiyyah on taxation, design a digital services tax for a small island state. Tax only the kinds the law names, set each kind within its limit, no new tax invented by the ruler.`
- 中文对照：伊本·泰米叶风格：为一个假想岛国设计数字服务税。只征法律所列税种，每种皆有其限度，君主不得自创新税。
- Negative: `no new tax invented by the ruler, no lawful kind stretched beyond its limit, no rate without a named lawful kind`
- 检验点：税种清单是否写明；各税限度是否可算；自创新税是否被拒绝。
