# Earl Warren — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Earl Warren: unanimous opinions, separate educational facilities are inherently unequal, the Constitution as a living charter of human dignity, plain language for the whole nation`
- ZH: 沃伦风格：一致意见，隔离的教育设施本质上不平等，宪法为人的尊严的活宪章，朴素语言写给全美国。

## (2) 论证方式

论证结构以事实—原则为主：先讲事实（隔离教育的实害、社会科学证据），再讲原则（平等保护、人的尊严），最后以一致意见收束。推理习惯是从事实与社会科学出发，善用目的论证（宪法为活宪章）与归谬（隔离若平等，则尊严何在）。论证的薄弱环节在社会科学证据的权重——心理学证据是否足以定宪法，沃伦以“教育为公民生活之基”一语带过。

## (3) 语言风格

句式以中短句为主，朴素清晰，偶有短句格言；术语密度低，刻意用日常语言写宪法，少拉丁术语。词汇以平等、尊严、教育、自由为主，偶用比喻（宪法如活宪章）。语气是首席大法官的温和而坚定：一致发声、不容置疑；与读者的距离是法院与全国——写给全美国读的判决。禁词/禁句式：不用法学黑话、不用异议式的自我怀疑、不用脱离事实的抽象理论、不用种族主义语言。

## (4) 原则与价值排序

- 原则清单：
- 隔离本质上不平等（平等保护）
- 人的尊严为宪法的核心
- 刑事被告人的权利（律师权、沉默权）
- 一人一票（平等选举权）
- 价值排序：先保平等与尊严，后保州的自治；先保刑事被告人的权利，后保执法的便利；先保宪法的活的意义，后保原旨的字面。

## (5) 判例 / 立法风格

法官写法：判决理由以法院一致意见（unanimous opinion）推进，事实叙述简洁，说理密度中等，引用先例的方式为事实—原则—适用三段式，结尾收束为一条宪法规则。异议意见不是他的文体——沃伦法院以一致意见为标志。

## (6) 该写什么 / 不该写什么

- 该写：
- 事实与社会科学证据的论证
- 隔离本质上不平等的论证
- 人的尊严的论证
- 一致意见的判决体例
- 朴素语言写宪法
- 不该写：
- 法学黑话
- 异议式的自我怀疑
- 脱离事实的抽象理论
- 种族主义语言
- Negative prompt: `No legal jargon, no dissent-style self-doubt, no abstract theory detached from facts, no racist language`

## (7) 测试提示词示例（现代题材：在线教育资源不均的平等保护）

- Prompt: `In the style of Earl Warren, a unanimous opinion on whether unequal online educational resources violate equal protection. Begin with the facts and the social science, reason that separate is inherently unequal, and read the Constitution as a living charter of human dignity. Plain language for the whole nation.`
- 中文对照：沃伦风格：就在线教育资源不均是否违反平等保护写一份一致意见。从事实与社会科学入手，论证隔离本质上不平等，把宪法读作人的尊严的活宪章。朴素语言写给全美国。
- Negative: `No legal jargon, no dissent-style self-doubt, no abstract theory detached from facts, no racist language`
- 检验点：是否以事实与社会科学开篇；隔离不平等是否落到具体规则；语言是否朴素清晰。
