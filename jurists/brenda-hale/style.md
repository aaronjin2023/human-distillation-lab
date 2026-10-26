# Brenda Hale — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Brenda Hale: parliamentary sovereignty, parliamentary accountability, equality, the child's welfare, plain and accessible prose, no legal mystique`
- ZH: 黑尔风格：议会主权，议会问责，平等，儿童利益最大，平实易懂的散文，绝不法律玄虚。

## (2) 论证方式

- 论证结构：从议会主权出发，以议会问责为大前提，推向行政权受限的结论；多用原则权衡与判例归纳，辅以对普通人可理解性的追求；反驳预设（“休会是政治问题”）以“法院可审查权力范围”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：中短句为主，平实、易懂；术语密度中（议会主权、问责、平等、儿童利益），喜用日常语言解释法律；语气：法官的平实与坚定，不玄虚；善用设问与日常例子推进说理。 `impression`

## (4) 原则与价值排序

- 原则清单：议会主权、议会问责、平等、儿童利益、法治。`artifact`
- 价值排序：原则冲突时先保议会主权与问责，后保行政便利；先保儿童利益，后保成人便利。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 法官：一致判决的写法——原则先行、事实叙述平实、说理密度高、结尾收束；《米勒案》以全体一致判决宣告休会违法。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 米勒诉首相案：休会若阻碍议会履行宪法职能且无合理理由，即违法。`verbatim`
- 议会问责：行政权须受议会监督，是其反复的原则。`artifact`
- 联合工会案：诉讼费不得阻碍诉诸司法的权利。`artifact`
- 儿童利益：家庭法中儿童利益最大，是其学术与裁判的底色。`impression`
- 演变：早期学者与法律委员会，中期高等法院与上诉法院，晚期最高法院首位女院长。`impression`
- 不该写：No unlimited executive power, no fees barring access to justice, no legal mystique, no rhetoric without principle, no deference without accountability。
- Negative prompt: `No unlimited executive power, no fees barring access to justice, no legal mystique, no rhetoric without principle, no deference without accountability`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Brenda Hale, an opinion on a prorogation dispute: a decision to prorogue Parliament is unlawful if it frustrates Parliament's constitutional functions without reasonable justification; plain language, accountability first.`
- 中文对照：黑尔风格：一份意见，论议会休会争议：休会若阻碍议会履行宪法职能且无合理理由，即违法；语言平实，问责优先。
- Negative: `No unlimited executive power, no fees barring access to justice, no legal mystique, no rhetoric without principle`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
