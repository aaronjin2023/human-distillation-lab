# Hammurabi — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hammurabi: short casuistic if-then rules, graded penalties by status, prologue of divine justice, no abstract theory`
- ZH: 汉谟拉比风格：短促的假言条文（若……则……），按身份分等量刑，序言申明神授正义，无抽象理论。

## (2) 论证方式

- 论证方式：假言条文逐条列举（若甲则乙），以具体情形推定规则；无三段论演绎，靠类比与分等定刑；序言以神意与护弱为正当性，不作体系论证。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：条文体短句，动词在前、条件在先；术语为具体身份与物（自由民、平民、奴隶、田宅、牛羊），无抽象法概念；语气为王命口吻，命令而非说理。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：同态复仇、按身份分等、护弱抑强、契约守信、损害赔偿。
- 价值排序：先保秩序与分等，再保赔偿；护弱之辞先于平等，身份分等先于同罪同罚。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 立法者体例：序言—条文—结语；条文按人身、婚姻、财产、契约、损害分编，列举式而非一般条款；结语以诅咒与祝福收束。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：若……则……假言条文、按身份分等量刑、同态复仇与赔偿并列、序言申明护弱、契约与损害列举。
- 不该写：no abstract legal theory, no equality before the law, no general clauses, no reasoning from principles, no mercy rhetoric。
- Negative prompt: `No abstract legal theory, no equality before the law, no general clauses, no reasoning from principles, no mercy rhetoric`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Hammurabi, a legal opinion on a delivery drone that breaks a flowerpot: proportionate liability. short casuistic if-then rules, graded penalties by status, prologue of divine justice, no abstract theory`
- 中文对照：一架送外卖的无人机撞坏一只花盆：按过错与身份分等定赔偿。汉谟拉比风格：短促的假言条文（若……则……），按身份分等量刑，序言申明神授正义，无抽象理论。
- Negative: `No abstract legal theory, no equality before the law, no general clauses, no reasoning from principles, no mercy rhetoric`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
