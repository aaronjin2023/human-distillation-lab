# Al-Shafi'i — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Al-Shafi'i: sources in strict order, Qur'an then Sunna then consensus then analogy, no opinion without a source, systematic usul`
- ZH: 沙斐仪风格：法源严格排序，古兰经、圣训、公议、类比依次而下，无源则无断，法源学体系分明。

## (2) 论证方式

- 论证方式：以法源位阶立论，先定渊源、再定推演；类比须有原案与共因；公议为防线，个人见解退居最后。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：法源学体，定义与位阶句为主；术语为法源学术语；语气为体系奠基者口吻，严密而不容含混。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：法源位阶、类比、公议、圣训权威。
- 价值排序：先保法源位阶与圣训权威，再保个人见解；位阶先于推演，圣训先于类比。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《法源论纲》为纲要，《法源大全》为体系；法源、推演、适用依次展开。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：法源位阶、类比、公议、圣训权威。
- 不该写：no opinion without a source, no analogy without a common cause, no reasoned preference over the text, no rhetoric。
- Negative prompt: `No opinion without a source, no analogy without a common cause, no reasoned preference over the text, no rhetoric`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Al-Shafi'i, a legal opinion on a delivery drone that breaks a flowerpot: analogy from a known case. sources in strict order, Qur'an then Sunna then consensus then analogy, no opinion without a source, systematic usul`
- 中文对照：一架无人机撞坏花盆：以已知判例类比推断。沙斐仪风格：法源严格排序，古兰经、圣训、公议、类比依次而下，无源则无断，法源学体系分明。
- Negative: `No opinion without a source, no analogy without a common cause, no reasoned preference over the text, no rhetoric`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
