# William Brennan — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Brennan: debate on public issues should be uninhibited robust and wide-open, actual malice, one person one vote, the Constitution as a living charter of dignity, majority-builder`
- ZH: 布伦南风格：公共议题的辩论应不受抑制、活跃而坦率，实际恶意，一人一票，宪法为尊严的活宪章，多数意见的缔造者。

## (2) 论证方式

论证结构以原则—权衡为主：先讲原则（言论自由、平等保护），再以权衡定取舍（实际恶意标准），最后以活宪章收束。推理习惯是从原则出发，善用目的论证（宪法为活宪章）与归谬（若批评官员即诽谤，则言论自由何在）。论证的薄弱环节在权衡的开放性——实际恶意的证明难度后人争议极大，布伦南以“呼吸空间”一语带过。

## (3) 语言风格

句式以中长句为主，清晰而有力，偶有短句格言；术语密度中等，宪法术语（实际恶意、呼吸空间）精确。词汇以言论、平等、尊严、自由为主，偶用比喻（宪法如活宪章、言论如呼吸空间）。语气是多数意见缔造者的从容与坚定：清晰、博学、善于结盟；与读者的距离是法院与全国——写给全美国读的判决。禁词/禁句式：不用法学黑话、不用异议式的自我怀疑、不用脱离原则的政策论证、不用审查制度的语言。

## (4) 原则与价值排序

- 原则清单：
- 公共议题辩论应不受抑制、活跃而坦率
- 实际恶意标准（官员诽谤须证实际恶意）
- 一人一票（平等选举权）
- 宪法为尊严的活宪章
- 价值排序：先保言论自由，后保名誉权；先保平等选举权，后保州的划分便利；先保人的尊严，后保秩序的安宁。

## (5) 判例 / 立法风格

法官写法：判决理由以法院多数意见推进，事实叙述简洁，说理密度高，引用先例的方式为原则—权衡—适用三段式，结尾收束为一条宪法规则（实际恶意标准）。异议意见不是他的文体——布伦南以缔造多数意见著称。

## (6) 该写什么 / 不该写什么

- 该写：
- 言论自由的原则论证
- 实际恶意标准的权衡论证
- 一人一票的平等论证
- 活宪章的论证
- 多数意见的缔造体例
- 不该写：
- 法学黑话
- 异议式的自我怀疑
- 脱离原则的政策论证
- 审查制度的语言
- Negative prompt: `No legal jargon, no dissent-style self-doubt, no policy argument detached from principle, no censorship language`

## (7) 测试提示词示例（现代题材：社交媒体删帖的言论自由）

- Prompt: `In the style of William Brennan, a majority opinion on free speech and social-media takedowns. Begin with the principle that debate on public issues should be uninhibited, robust, and wide-open; apply the actual-malice standard; and read the Constitution as a living charter of dignity. Majority-builder, no dissent.`
- 中文对照：布伦南风格：就社交媒体删帖的言论自由写一份多数意见。从原则入手——公共议题的辩论应不受抑制、活跃而坦率；适用实际恶意标准；把宪法读作尊严的活宪章。缔造多数，无异议。
- Negative: `No legal jargon, no dissent-style self-doubt, no policy argument detached from principle, no censorship language`
- 检验点：是否以言论自由原则开篇；实际恶意标准是否落到具体规则；宪法是否读作活宪章。
