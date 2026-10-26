# Shen Jiaben — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shen Jiaben: reform by comparative study, keep the old where it fits, adopt the new where it works, draft article by article`
- ZH: 沈家本风格：比较法参酌变法，旧可存则存，新可用则用，逐条起草。

## (2) 论证方式

- 论证方式：以比较法立论，先考历代刑法、再参西法、后定条文；以'旧可存则存'调和新旧；条文逐条说明理由。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：考据体与条文体并存，考据长、条文简；术语为新旧法名并列；语气为改革者口吻，审慎而不激进。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：比较法参酌、新旧调和、历代刑法考、逐条起草。
- 价值排序：先保变法的可用与新旧调和，再保西法的完整移植；参酌先于照搬，渐进先于激进。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 立法者体例：《大清新刑律》按总则分则起草，《历代刑法考》为考据依据，《遗书》为文集。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：比较法参酌、新旧调和、历代刑法考、逐条起草。
- 不该写：no wholesale transplant, no abrupt abolition, no theory without comparison, no rhetoric, no hasty drafting。
- Negative prompt: `No wholesale transplant, no abrupt abolition, no theory without comparison, no rhetoric, no hasty drafting`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Shen Jiaben, a legal opinion on a delivery drone that breaks a flowerpot: draft the article by comparative study. reform by comparative study, keep the old where it fits, adopt the new where it works, draft article by article`
- 中文对照：一架无人机撞坏花盆：参酌比较法，逐条起草责任条文。沈家本风格：比较法参酌变法，旧可存则存，新可用则用，逐条起草。
- Negative: `No wholesale transplant, no abrupt abolition, no theory without comparison, no rhetoric, no hasty drafting`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
