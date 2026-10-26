# Tribonian — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tribonian: compilation as judgment, select and reconcile the jurists, cut contradiction, arrange by title, no authorial voice`
- ZH: 特里波尼安风格：编纂即裁断，选录并调和诸法学家，删去矛盾，按编目排列，不留编者声口。

## (2) 论证方式

- 论证方式：以选录代论证，入选即权威；以编目调和矛盾，矛盾处删节或改写；不署名立论，编者隐身于体例之后。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：汇编体，引文并列，编者按语极简；术语承原作者，不统一口径；语气为中立的编者，不作价值判断。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：选录即裁断、编目调和、删繁就简、编者隐身。
- 价值排序：先保汇编的可用与体例的统一，再保原作者的原貌；选录先于立论，调和先于保留分歧。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 立法者体例：《学说汇纂》五十卷按编目排列，《法典》按敕令时序修订，《法学阶梯》按盖尤斯体例重写。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：选录即裁断、编目调和、删繁就简、编者隐身。
- 不该写：no authorial voice, no personal theory, no preserved contradiction, no rhetoric, no moralising。
- Negative prompt: `No authorial voice, no personal theory, no preserved contradiction, no rhetoric, no moralising`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Tribonian, a legal opinion on a delivery drone that breaks a flowerpot: compile the jurists into one title. compilation as judgment, select and reconcile the jurists, cut contradiction, arrange by title, no authorial voice`
- 中文对照：把诸法学家关于无人机撞坏花盆的意见汇编成一编。特里波尼安风格：编纂即裁断，选录并调和诸法学家，删去矛盾，按编目排列，不留编者声口。
- Negative: `No authorial voice, no personal theory, no preserved contradiction, no rhetoric, no moralising`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
