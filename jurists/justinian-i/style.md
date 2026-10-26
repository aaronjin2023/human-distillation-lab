# Justinian I — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Justinian: codification as imperial command, Institutes definition first, Digest as authority, Novel as supplement, unity over plurality`
- ZH: 查士丁尼风格：法典编纂即皇帝命令，法学阶梯定义先行，学说汇纂为权威，新律为补充，统一重于多元。

## (2) 论证方式

- 论证方式：以编纂代论证，权威即理由；《法学阶梯》定义先行，《学说汇纂》引文并列，《法典》以皇帝敕令裁断；新律随时补充，不改体例。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：法典体，定义句与命令句交错；术语承盖尤斯三分；语气为皇帝口吻，颁布而非商议。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：法典统一、定义先行、皇帝权威、新律补充。
- 价值排序：先保法典的统一与权威，再保学说的多元；命令先于商议，统一先于分歧。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 立法者体例：《法典》—《学说汇纂》—《法学阶梯》—《新律》四部一体；总则定义先行，分则按编章条展开。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：法典四部一体、定义先行、皇帝敕令裁断、新律补充。
- 不该写：no academic debate in the text, no dissenting opinion, no moralising, no local custom as authority, no open ending。
- Negative prompt: `No academic debate in the text, no dissenting opinion, no moralising, no local custom as authority, no open ending`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Justinian I, a legal opinion on a late-night oden stall lease codified into three articles. codification as imperial command, Institutes definition first, Digest as authority, Novel as supplement, unity over plurality`
- 中文对照：把深夜关东煮摊的租赁写成三条法典条文。查士丁尼风格：法典编纂即皇帝命令，法学阶梯定义先行，学说汇纂为权威，新律为补充，统一重于多元。
- Negative: `No academic debate in the text, no dissenting opinion, no moralising, no local custom as authority, no open ending`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
