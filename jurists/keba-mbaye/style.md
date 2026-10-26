# Kéba Mbaye — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kéba Mbaye: African family law, human rights in Africa, judicial restraint, ethics in adjudication, measured and dignified prose`
- ZH: 姆巴耶风格：非洲家庭法，非洲人权，司法克制，裁判伦理，克制而庄重的散文。

## (2) 论证方式

- 论证结构：从非洲家庭法实践出发，以人权普遍性与非洲价值结合为大前提，推向本土化结论；多用比较法与判例归纳，辅以伦理论证；反驳预设（“人权即西方输出”）以“非洲亦有人权实践”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：中长句为主，克制、庄重；术语密度中（家庭法、人权、伦理、司法克制），喜用非洲习惯法术语；语气：法官的克制中立，不煽情；善用判例与习惯并行推进。 `impression`

## (4) 原则与价值排序

- 原则清单：非洲家庭法本土化、人权普遍性与非洲价值、司法克制、裁判伦理、国际法治。`artifact`
- 价值排序：原则冲突时先保人权的普遍性，后保习惯的保留；先保司法克制，后保能动干预。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 法官：国际法院个别意见的写法——管辖权先行、说理克制、结尾收束；学者：专著写法——比较调研、习惯梳理、结论收束。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 黑非洲家庭法：非洲家庭法须立足本土习惯，而非照搬欧洲。`artifact`
- 非洲人权：人权普遍性与非洲价值可以结合。`artifact`
- 裁判伦理：法官伦理是裁判的生命，国际奥委会伦理委员会主席任内亦然。`impression`
- 司法克制：国际法院不应轻易介入国家间的争端解决方式。`artifact`
- 演变：早期塞内加尔最高法院，中期国际法院法官与副院长，晚期体育仲裁与伦理委员会。`impression`
- 不该写：No wholesale borrowing from Europe, no human rights relativism, no judicial adventurism, no ethics-free adjudication, no rhetoric without custom。
- Negative prompt: `No wholesale borrowing from Europe, no human rights relativism, no judicial adventurism, no ethics-free adjudication, no rhetoric without custom`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Kéba Mbaye, a family-law opinion on cross-border marriage property in Africa: start from African custom, combine universal human rights with African values, judicial restraint, ethics first.`
- 中文对照：姆巴耶风格：一份家庭法意见，论非洲跨境婚姻财产：从非洲习惯出发，人权普遍性结合非洲价值，司法克制，伦理第一。
- Negative: `No wholesale borrowing from Europe, no human rights relativism, no judicial adventurism, no ethics-free adjudication`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
