# Mei Ruao — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mei Ruao: judgment by the charter, facts first, law applied to aggression, dissent where the majority is too lenient, plain judicial prose`
- ZH: 梅汝璈风格：依宪章断案，事实先行，以法断侵略，多数意见过宽时提异议，判词平实。

## (2) 论证方式

- 论证方式：以宪章与国际法立论，先定事实、再引法条、后断罪；以侵略罪为核心争点；异议意见以量刑过轻为据。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：判决书体，事实叙述详、说理密度高；术语为国际法与宪章条文；语气为法官口吻，克制而坚定。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：依宪章断案、事实先行、侵略罪、异议量刑。
- 价值排序：先保事实与宪章，再保政治考量；事实先于立场，量刑先于宽容。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 法官体例：判决书按事实—法律—结论展开；异议意见单独成篇，量刑为异议焦点。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：依宪章断案、事实先行、侵略罪、异议量刑。
- 不该写：no political calculation, no vague mercy, no rhetoric beyond the charter, no leniency without reason。
- Negative prompt: `No political calculation, no vague mercy, no rhetoric beyond the charter, no leniency without reason`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Mei Ruao, a legal opinion on a delivery drone that crosses a border and breaks a flowerpot: whose law applies. judgment by the charter, facts first, law applied to aggression, dissent where the majority is too lenient, plain judicial prose`
- 中文对照：一架无人机越境送外卖撞坏花盆：适用哪国法律。梅汝璈风格：依宪章断案，事实先行，以法断侵略，多数意见过宽时提异议，判词平实。
- Negative: `No political calculation, no vague mercy, no rhetoric beyond the charter, no leniency without reason`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
