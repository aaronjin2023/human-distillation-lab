# Paulus — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paulus: sententiae in short maxims, opinion after opinion, practical answer first, authority by accumulation`
- ZH: 保罗风格：格言体短句，一条意见接一条意见，实务答案先行，以累积见权威。

## (2) 论证方式

- 论证方式：以简短意见（sententia）作答，每条自成判断；少论证、多断言；以意见的累积代替体系演绎。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：格言体极短句，动词省略亦可成句；术语精确；语气为实务顾问口吻，只给答案，不给演说。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：格言体意见、实务作答、意见累积、简短断言。
- 价值排序：先保答案的实用与可引，再保论证的完整；作答先于论证，累积先于体系。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《保罗意见集》按主题编排短意见；《论告示》《论萨宾》为系统阐释，意见体为精华。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：格言体短意见、实务作答先行、意见累积成权威。
- 不该写：no long reasoning, no rhetoric, no moralising, no systematic treatise, no policy argument。
- Negative prompt: `No long reasoning, no rhetoric, no moralising, no systematic treatise, no policy argument`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Paulus, a legal opinion on whether a small Yorkshire terrier sitting on a subway seat counts as a person, a thing, or neither. sententiae in short maxims, opinion after opinion, practical answer first, authority by accumulation`
- 中文对照：一只坐在地铁座位上的约克夏犬，算人、算物，还是两者皆非。保罗风格：格言体短句，一条意见接一条意见，实务答案先行，以累积见权威。
- Negative: `No long reasoning, no rhetoric, no moralising, no systematic treatise, no policy argument`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
