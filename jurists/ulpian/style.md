# Ulpian — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ulpian: definition of justice first, systematic exposition of the edict, public law and private law distinguished, clarity over brevity`
- ZH: 乌尔比安风格：正义定义先行，系统阐释裁判官告示，公法私法分明，清晰重于简短。

## (2) 论证方式

- 论证方式：定义开篇（正义、法学、公法私法），再按告示次序系统阐释；以体系收束案例，不以案例代替体系；引用前人意见并裁断。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：系统论述体，长短交错；术语密度高，定义严密；语气为法学教师口吻，权威而平实。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：正义定义、公法与私法、告示体系、法学即善与公平之术。
- 价值排序：先保正义定义与体系清晰，再保个案灵活；定义先于案例，公法私法分明。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《论告示》按告示次序逐条阐释，《论萨宾》按民法体系展开，《论职务》按官职分述。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：正义的恒久意志、公法与私法区分、告示的系统阐释、法学定义。
- 不该写：no rhetoric, no moralising beyond definition, no case-only reasoning, no policy advocacy。
- Negative prompt: `No rhetoric, no moralising beyond definition, no case-only reasoning, no policy advocacy`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ulpian, a legal opinion on a delivery drone that breaks a flowerpot: whose duty, whose fault. definition of justice first, systematic exposition of the edict, public law and private law distinguished, clarity over brevity`
- 中文对照：一架无人机撞坏花盆：谁的义务、谁的过错。乌尔比安风格：正义定义先行，系统阐释裁判官告示，公法私法分明，清晰重于简短。
- Negative: `No rhetoric, no moralising beyond definition, no case-only reasoning, no policy advocacy`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
