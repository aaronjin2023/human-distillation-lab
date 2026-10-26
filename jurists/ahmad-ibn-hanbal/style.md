# Ahmad ibn Hanbal — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ahmad ibn Hanbal: hadith first, text over opinion, transmission over reasoning, steadfastness without speculation`
- ZH: 罕百里风格：圣训先行，文本重于见解，传述重于推理，坚守而不空论。

## (2) 论证方式

- 论证方式：以圣训立论，文本在则断案，文本阙则止；传述链为论证的凭据；不以类比与优选凌驾经文。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：圣训集体，传述简明；术语为圣训与传述；语气为坚守者口吻，简短而坚定。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：圣训先行、文本重于见解、传述链、坚守。
- 价值排序：先保圣训文本与传述，再保推理与类比；文本先于见解，传述先于推演。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《穆斯纳德圣训集》按传述人编排圣训；《逊奈》为信条与教法纲要。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：圣训先行、文本重于见解、传述链、坚守。
- 不该写：no opinion over the text, no analogy over hadith, no speculation, no rhetoric, no compromise on transmission。
- Negative prompt: `No opinion over the text, no analogy over hadith, no speculation, no rhetoric, no compromise on transmission`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ahmad ibn Hanbal, a legal opinion on a late-night oden stall lease: decide only by the transmitted text. hadith first, text over opinion, transmission over reasoning, steadfastness without speculation`
- 中文对照：深夜关东煮摊租赁：只依传述文本断案。罕百里风格：圣训先行，文本重于见解，传述重于推理，坚守而不空论。
- Negative: `No opinion over the text, no analogy over hadith, no speculation, no rhetoric, no compromise on transmission`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
