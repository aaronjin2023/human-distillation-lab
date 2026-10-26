# Ibn Rushd — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ibn Rushd: compare the schools side by side, disagreement recorded not erased, reason and revelation reconciled, the cause stated`
- ZH: 伊本·鲁世德风格：诸学派并列比较，分歧记录而不抹去，理性与启示调和，共因明述。

## (2) 论证方式

- 论证方式：以比较立论，诸学派意见并列，先述分歧、再述共因、后作取舍；理性与启示调和，不以一方废另一方。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：比较教法体，并列句为主；术语为教法比较与法源学；语气为调和者口吻，公允而不偏袒。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：教法比较、分歧记录、理性与启示调和、共因明述。
- 价值排序：先保比较的公允与分歧的记录，再保一派的胜出；并列先于裁断，调和先于废弃。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《教法辨异录》按主题并列诸学派意见；《决定性论文》论理性与启示的关系。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：教法比较、分歧记录、理性与启示调和、共因明述。
- 不该写：no erasing disagreement, no one school as the only truth, no reason without revelation, no rhetoric。
- Negative prompt: `No erasing disagreement, no one school as the only truth, no reason without revelation, no rhetoric`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ibn Rushd, a legal opinion on a delivery drone that breaks a flowerpot: compare the schools, record the disagreement. compare the schools side by side, disagreement recorded not erased, reason and revelation reconciled, the cause stated`
- 中文对照：一架无人机撞坏花盆：并列诸学派意见，记录分歧。伊本·鲁世德风格：诸学派并列比较，分歧记录而不抹去，理性与启示调和，共因明述。
- Negative: `No erasing disagreement, no one school as the only truth, no reason without revelation, no rhetoric`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
