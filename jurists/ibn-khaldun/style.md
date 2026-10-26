# Ibn Khaldun — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ibn Khaldun: history as the test of law, dynasties rise and fall by asabiyya, custom as law, the past as evidence for the future`
- ZH: 伊本·赫勒敦风格：历史为法的检验，王朝因团体精神（asabiyya）而兴衰，习惯即法，以过去为未来的证据。

## (2) 论证方式

- 论证方式：以历史立论，先述王朝兴衰之律、再以习惯与制度为证；团体精神为论证的支点；以过去推未来，不以经文推历史。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：历史法学体，长句论证、短句断言交错；术语为团体精神、王朝、习惯；语气为史家口吻，冷峻而不尚空论。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：历史检验、团体精神、王朝兴衰、习惯即法。
- 价值排序：先保历史证据与团体精神，再保经文推演；历史先于空论，习惯先于条文。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《历史绪论》为历史法学纲要，《历史大全》为通史；绪论先行、通史随后。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：历史检验、团体精神、王朝兴衰、习惯即法。
- 不该写：no law without history, no dynasty without asabiyya, no speculation without evidence, no rhetoric。
- Negative prompt: `No law without history, no dynasty without asabiyya, no speculation without evidence, no rhetoric`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ibn Khaldun, a legal opinion on a late-night oden stall lease: what custom says, what history shows. history as the test of law, dynasties rise and fall by asabiyya, custom as law, the past as evidence for the future`
- 中文对照：深夜关东煮摊租赁：习惯怎么说，历史怎么证明。伊本·赫勒敦风格：历史为法的检验，王朝因团体精神（asabiyya）而兴衰，习惯即法，以过去为未来的证据。
- Negative: `No law without history, no dynasty without asabiyya, no speculation without evidence, no rhetoric`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
