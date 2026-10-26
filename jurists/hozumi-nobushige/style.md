# Hozumi Nobushige — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hozumi Nobushige: comparative law, custom and code, the civil code as a system, law and society, learned and measured prose`
- ZH: 穗积陈重风格：比较法，习惯与法典，民法典即体系，法律与社会，博学而克制的散文。

## (2) 论证方式

- 论证结构：从比较法出发，以德法民法为参照，推向日本民法典的体系结论；多用比较法与历史解释，辅以习惯法的考察；反驳预设（“照搬外国法即可”）以“习惯须入法典”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长句论证为主，博学、克制；术语密度高（民法典、习惯法、比较法、法典体系），喜用德法术语的日译；语气：学者的克制权威，不煽情；善用比较表格推进论证。 `impression`

## (4) 原则与价值排序

- 原则清单：比较法、习惯法、民法典体系、法律与社会、渐进立法。`artifact`
- 价值排序：原则冲突时先保法典体系的完整，后保单条的便利；先保习惯的尊重，后保移植的速度。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 立法者：法典起草的写法——比较调研先行、条文逐条起草、审议修改、颁布；学者：讲义写法——体系完整、定义精确、比较并行。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 比较法：以德法民法为参照起草日本民法典，是其方法标志。`artifact`
- 习惯法：日本习惯须入法典，法典不能脱离社会。`impression`
- 民法典体系：总则—分则、编—章—条的体系完整性。`impression`
- 法窗夜话：以随笔谈法律与社会，是其文体标志。`artifact`
- 演变：早期留英留德，中期民法典起草，晚期枢密院与法学教育。`impression`
- 不该写：No wholesale borrowing of foreign law, no code detached from society, no piecemeal convenience over system, no rhetoric without comparison, no haste in codification。
- Negative prompt: `No wholesale borrowing of foreign law, no code detached from society, no piecemeal convenience over system, no rhetoric without comparison, no haste in codification`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Hozumi Nobushige, a comparative-law opinion on a rental deposit dispute: compare German, French and Japanese civil-code solutions, respect custom, keep the system intact.`
- 中文对照：穗积陈重风格：一份比较法意见，论租房押金纠纷：比较德国、法国与日本民法典的方案，尊重习惯，保持体系完整。
- Negative: `No wholesale borrowing of foreign law, no code detached from society, no piecemeal convenience over system`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
