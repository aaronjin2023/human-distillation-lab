# Accursius — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Accursius: gloss upon gloss, the standard gloss as authority, every word of the Corpus explained, no word unexplained`
- ZH: 阿库修斯风格：注上加注，普通注释即权威，法典每词皆有解释，无词不注。

## (2) 论证方式

- 论证方式：以注释立论，逐词释义、逐句疏通；以普通注释为权威，注释即裁判依据；不尚体系，不尚创新。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：注释体，注文附于正文之旁；术语精确，注中见定义；语气为注释者口吻，忠实而不演说。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：普通注释、逐词释义、注释即权威、无词不注。
- 价值排序：先保注释的完备与权威，再保体系的创新；注释先于立论，忠实先于创新。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《普通注释》附于《民法大全》正文之旁，按条附注；注文汇集前人注释，删繁就简。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：普通注释、逐词释义、注释即权威、无词不注。
- 不该写：no unexplained word, no innovation without a gloss, no system without the text, no rhetoric。
- Negative prompt: `No unexplained word, no innovation without a gloss, no system without the text, no rhetoric`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Accursius, a legal opinion on a delivery drone that breaks a flowerpot: gloss every word of the article. gloss upon gloss, the standard gloss as authority, every word of the Corpus explained, no word unexplained`
- 中文对照：一架无人机撞坏花盆：为条文每词作注。阿库修斯风格：注上加注，普通注释即权威，法典每词皆有解释，无词不注。
- Negative: `No unexplained word, no innovation without a gloss, no system without the text, no rhetoric`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
