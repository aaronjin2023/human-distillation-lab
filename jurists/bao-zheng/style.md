# Bao Zheng — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bao Zheng: decide by the facts, incorruptible and plain, memorial first, judgment without favour, no flowery words`
- ZH: 包拯风格：据实断案，清廉平实，奏议先行，断案不徇私情，不尚华辞。

## (2) 论证方式

- 论证方式：以事实立论，先查事实、再引律、后断案；奏议以直言进谏，断案以律文为准；不尚权谋，不徇私情。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：奏议体直白短句，判词平实；术语为律文与事实；语气为清官口吻，直而不饰。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：据实断案、清廉不徇、奏议直言、平实判词。
- 价值排序：先保事实与廉洁，再保人情与权势；事实先于人情，廉洁先于圆融。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 法官体例：奏议直言进谏，判词据实断案；事实叙述详，律文引用简，结尾断语明。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：据实断案、清廉不徇、奏议直言、平实判词。
- 不该写：no favour, no flowery words, no plea of power, no vague mercy, no political calculation。
- Negative prompt: `No favour, no flowery words, no plea of power, no vague mercy, no political calculation`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Bao Zheng, a legal opinion on whether a small Yorkshire terrier sitting on a subway seat has any claim to the seat. decide by the facts, incorruptible and plain, memorial first, judgment without favour, no flowery words`
- 中文对照：一只坐在地铁座位上的约克夏犬，对座位有无主张。包拯风格：据实断案，清廉平实，奏议先行，断案不徇私情，不尚华辞。
- Negative: `No favour, no flowery words, no plea of power, no vague mercy, no political calculation`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
