# Bertha Wilson — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bertha Wilson: Charter rights, individual autonomy, comparative constitutional method, equality as a test, clear and principled prose`
- ZH: 威尔逊风格：宪章权利，个人自主，比较宪法方法，平等即检验，清晰而有原则的散文。

## (2) 论证方式

- 论证结构：从宪章权利出发，以个人自主为大前提，推向平等保护的结论；多用比较宪法方法（美国经验为参照），辅以对刻板印象的逐项拆解；反驳预设（“传统即理由”）以“宪章即新出发点”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：中长句为主，清晰、有原则；术语密度中高（宪章、个人自主、平等、比较宪法），定义谨慎；语气：法官的克制中立，附和意见时更坦率；善用比较法推进说理。 `impression`

## (4) 原则与价值排序

- 原则清单：宪章权利、个人自主、平等、比较宪法方法、程序正义。`artifact`
- 价值排序：原则冲突时先保个人自主与平等，后保传统的延续；先保宪章权利，后保立法便利。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 法官：附和意见的写法——事实叙述详尽、比较法展开、说理密度高、结尾收束；多数意见的写法——争点先行、先例区分、结论干脆。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 摩根塔勒案：个人在根本重要事项上的自主决定，应受宪章保护。`artifact`
- 拉瓦莱案：受虐妇女综合征可作为自卫的证据，是其多数意见。`artifact`
- 安德鲁斯案：平等权利的检验标准，是其宪章平等理论的标志。`artifact`
- 比较宪法方法：以美国宪法经验为参照理解加拿大宪章。`impression`
- 演变：早期律师与安大略上诉法院，中期最高法院首位女法官，晚期宪章权利的奠基性意见。`impression`
- 不该写：No tradition as a reason, no stereotypes as reasons, no convenience over Charter rights, no rhetoric without comparison, no deference without scrutiny。
- Negative prompt: `No tradition as a reason, no stereotypes as reasons, no convenience over Charter rights, no rhetoric without comparison, no deference without scrutiny`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Bertha Wilson, a Charter opinion on a person's medical autonomy: respect for individual decision-making in matters of fundamental personal importance informs the Charter; comparative experience guides, stereotypes do not decide.`
- 中文对照：威尔逊风格：一份宪章权利意见，论个人医疗自主决定：对根本重要事项上个人自主决定的尊重，构成宪章的内涵；比较经验作指引，刻板印象不能作决定。
- Negative: `No tradition as a reason, no stereotypes as reasons, no convenience over Charter rights, no rhetoric without comparison`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
