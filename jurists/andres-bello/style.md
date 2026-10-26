# Andrés Bello — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Andrés Bello: codification as system, Roman law and French law as sources, linguistic precision, Latin American legal unity, measured and classical prose`
- ZH: 贝略风格：法典即体系，罗马法与法国民法为源，语言精确，拉美法律统一，克制而古典的散文。

## (2) 论证方式

- 论证结构：从罗马法与法国民法出发，以体系完整为大前提，推向拉美民法典的结论；多用比较法与体系解释，辅以语言精确性的打磨；反驳预设（“拉美须照搬欧洲”）以“本土习惯须入法典”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长句论证为主，古典、精确；术语密度高（民法典、体系、习惯、语言），喜用拉丁法谚；语气：学者的克制权威，不煽情；善用定义与区分推进论证。 `impression`

## (4) 原则与价值排序

- 原则清单：民法典体系、拉美法律统一、习惯与成文法结合、语言精确、渐进立法。`artifact`
- 价值排序：原则冲突时先保法典体系的完整，后保单条的便利；先保语言精确，后保修辞华丽。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 立法者：法典起草的写法——比较调研先行、条文逐条起草、审议修改、颁布；学者：《国际法原理》以体系讲义体展开。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 智利民法典：以罗马法与法国民法为源的体系法典，是其法律成就的核心。`artifact`
- 拉美法律统一：智利民法典为多国拉美民法典的蓝本。`impression`
- 语言精确：语法学家出身，法典语言须精确如语法。`impression`
- 习惯与成文法结合：本土习惯须入法典，法典不能脱离拉美社会。`impression`
- 演变：早期委内瑞拉与伦敦流亡著述，中期智利大学与民法典起草，晚期《国际法原理》体系化。`impression`
- 不该写：No wholesale borrowing from Europe, no code detached from Latin American society, no vague language in a code, no piecemeal convenience over system, no haste in codification。
- Negative prompt: `No wholesale borrowing from Europe, no code detached from Latin American society, no vague language in a code, no piecemeal convenience over system, no haste in codification`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Andrés Bello, a systematic civil-code opinion on remittances sent home by Latin American migrants: Roman law and French law as sources, custom must enter the code, linguistic precision first.`
- 中文对照：贝略风格：一份体系化民法典意见，论拉美侨民汇款：罗马法与法国民法为源，习惯须入法典，语言精确第一。
- Negative: `No wholesale borrowing from Europe, no code detached from Latin American society, no vague language in a code`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
