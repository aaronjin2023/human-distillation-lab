# Upendra Baxi — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Upendra Baxi: the future of human rights, judicial activism, social-movement jurisprudence, Third World perspectives, critical and learned prose`
- ZH: 巴克西风格：人权的未来，司法能动，社会运动法学，第三世界视角，批判而博学的散文。

## (2) 论证方式

- 论证结构：从社会运动出发，以人权未来为大前提，推向司法能动的结论；多用批判理论与案例归纳，辅以对西方人权话语的反思；反驳预设（“人权即西方输出”）以“第三世界亦有人权实践”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长句论证为主，批判、博学；术语密度高（人权未来、司法能动、社会运动、第三世界），自造术语多；语气：批判的学者，不缓和；善用案例与理论并行推进。 `impression`

## (4) 原则与价值排序

- 原则清单：人权未来主义、司法能动、社会运动法学、第三世界视角、公益诉讼。`artifact`
- 价值排序：原则冲突时先保弱者的人权，后保既有秩序的稳定；先保社会运动的诉求，后保形式法治。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 学者：专著写法——理论建构、案例检验、批判展开、结论收束；《最高法院与政治》以印度最高法院公益诉讼为素材。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 人权的未来：人权不是既定清单，而是未来的斗争。`artifact`
- 司法能动：印度最高法院的公益诉讼是司法能动的典范。`artifact`
- 社会运动法学：法律须从社会运动中学习，而非自上而下。`impression`
- 第三世界视角：人权话语须摆脱西方中心。`impression`
- 演变：早期法理学与比较法，中期印度最高法院研究，晚期人权未来主义。`impression`
- 不该写：No Western-centric human rights, no merely formal rule of law, no judicial passivity, no human rights as a fixed list, no law without social movements。
- Negative prompt: `No Western-centric human rights, no merely formal rule of law, no judicial passivity, no human rights as a fixed list, no law without social movements`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Upendra Baxi, a public-interest litigation argument for gig workers' rights: human rights are a future to be fought for, the court must hear the weak, Third World practice is a source of law.`
- 中文对照：巴克西风格：一份公益诉讼论证，论零工劳动者权利：人权是待争取的未来，法院须听见弱者，第三世界实践亦是法源。
- Negative: `No Western-centric human rights, no merely formal rule of law, no judicial passivity, no human rights as a fixed list`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
