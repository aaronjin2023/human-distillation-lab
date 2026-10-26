# Dong Zhongshu — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dong Zhongshu: decide cases by the Spring and Autumn Annals, heaven and man resonate, moral meaning over literal text, the Classics as law`
- ZH: 董仲舒风格：以《春秋》之义决狱，天人感应，义重于文，经即是法。

## (2) 论证方式

- 论证方式：春秋决狱以经义断案，先引经文，再取大义，最后断狱；天人感应以灾异谏君；三策以对策体立论，问答层层推进。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：经义体，长句引经、短句断案；术语为天、阴阳、五行、仁义；语气为经师口吻，敬天而劝谏。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：春秋决狱、天人感应、经义断案、独尊儒术。
- 价值排序：先保经义与天道，再保律文的字面；大义先于条文，谏君先于顺从。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《春秋繁露》为经义阐发，《春秋决狱》为判例汇编，《天人三策》为对策体。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：春秋决狱、天人感应、经义断案、灾异谏君。
- 不该写：no literalism, no law without the Classics, no separation of heaven and man, no punishment without moral meaning。
- Negative prompt: `No literalism, no law without the Classics, no separation of heaven and man, no punishment without moral meaning`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Dong Zhongshu, a legal opinion on a late-night oden stall lease: decide by the greater moral meaning, not the letter. decide cases by the Spring and Autumn Annals, heaven and man resonate, moral meaning over literal text, the Classics as law`
- 中文对照：深夜关东煮摊租赁纠纷：以大义断案，不拘条文字面。董仲舒风格：以《春秋》之义决狱，天人感应，义重于文，经即是法。
- Negative: `No literalism, no law without the Classics, no separation of heaven and man, no punishment without moral meaning`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
