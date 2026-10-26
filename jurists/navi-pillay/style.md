# Navi Pillay — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Navi Pillay: sexual violence as genocide, universal legal principles, accountability for atrocity, dignity and moral compass, resolute and principled prose`
- ZH: 皮莱风格：性暴力即灭绝种族罪，普遍法律原则，暴行问责，尊严与道德罗盘，坚决而有原则的散文。

## (2) 论证方式

- 论证结构：从暴行事实出发，以普遍法律原则为大前提，推向个人刑事责任的结论；多用判例归纳与条约解释，辅以受害者视角；反驳预设（“性暴力只是战争副产品”）以“性暴力可构成灭绝种族罪”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：中长句为主，坚决、有原则；术语密度高（灭绝种族罪、危害人类罪、普遍原则、问责），定义精确；语气：法官的坚决与庄重，不煽情；善用事实叙述推进说理。 `impression`

## (4) 原则与价值排序

- 原则清单：性暴力即灭绝种族罪、普遍法律原则、暴行问责、平等、国际法治。`artifact`
- 价值排序：原则冲突时先保受害者的正义与问责，后保政治便利；先保普遍原则，后保主权豁免。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 法官：国际刑事判决的写法——事实认定详尽、法律适用逐项、结尾收束；人权高专报告写法——调查先行、标准对照、建议收束。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 阿卡耶苏案：性暴力与强奸可构成灭绝种族罪与危害人类罪，是其标志性判决。`artifact`
- 普遍法律原则：对普遍法律原则的承诺与坚定的道德罗盘，是诺贝尔奖授奖理由的核心。`artifact`
- 反种族隔离辩护：早期为曼德拉等反种族隔离活动家辩护，是其职业起点。`artifact`
- 国际法治：扩大国际法的影响与范围，是其毕生工作。`impression`
- 演变：早期南非反种族隔离辩护，中期卢旺达刑庭与国际刑事法院，晚期联合国人权高专与诺贝尔和平奖。`impression`
- 不该写：No impunity for atrocity, no sovereignty as a shield, no sexual violence as a by-product of war, no political convenience over justice, no rhetoric without accountability。
- Negative prompt: `No impunity for atrocity, no sovereignty as a shield, no sexual violence as a by-product of war, no political convenience over justice, no rhetoric without accountability`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Navi Pillay, an international criminal law opinion on testimony by victims of sexual violence: sexual violence can constitute genocide and crimes against humanity, universal legal principles first, accountability over political convenience.`
- 中文对照：皮莱风格：一份国际刑法意见，论性暴力受害者作证：性暴力可构成灭绝种族罪与危害人类罪，普遍法律原则优先，问责高于政治便利。
- Negative: `No impunity for atrocity, no sovereignty as a shield, no sexual violence as a by-product of war, no political convenience over justice`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
