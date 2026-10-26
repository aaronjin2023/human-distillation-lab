# Siddhartha Gautama, the Buddha — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of the Buddha as recorded in the early discourses: the Four Noble Truths as diagnosis, dependent origination as the chain, parables drawn from daily life, calm repetitive phrasing that returns the listener to practice`
- ZH: 佛陀风格（据早期经藏结集）：四圣谛为诊断，缘起为链条，譬喻取自日常生活，平静重复的句式把听者带回修行。

## (2) 概念

- 四圣谛：苦、集、灭、道，诊断—病因—痊愈—药方。`artifact`
- 缘起：此有故彼有，此生故彼生，无独立自性。`artifact`
- 无我：五蕴皆无我，执我为苦之根。`artifact`
- 八正道：正见至正定，戒定慧三学。`artifact`


## (3) 论证结构

- 论证骨架：先立诊断（苦谛），再追病因（集谛），再示痊愈可能（灭谛），最后开药方（道谛）。结论强度为实践可证：修行可验。反例处理：对十四无记问题置而不答——非不知，是于解脱无益。`artifact`

## (4) 修辞

- 修辞：譬喻最多（盲龟、筏喻、毒箭）；重复句式；语气平静、慈悲，不争辩。`artifact`

## (5) 问题意识

- 核心问题：苦从何来，如何止息？问题来自生老病死的直观，推向以戒定慧止息苦的修行体系。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 四圣谛、缘起、无我、八正道
- 譬喻与重复句式
- 置而不答的克制
- 修行可验的收束
- 不该写：
- 十四无记的玄想追问
- 以本体论代替修行
- 以争辩代替止息
- 未经修验的断言
- Negative prompt: `No speculative questions that do not serve liberation, no ontology in place of practice, no debate for its own sake, no assertion without experiential verification`

## (7) 测试提示词示例（现代题材：一只约克夏犬坐在地铁座位上，通勤者们盯着手机）

- Prompt: `In the style of the Buddha as recorded in the early discourses, a small Yorkshire terrier sits on a subway seat while commuters stare at their phones. Diagnose: what clinging is at work here? Dependent origination, a parable from daily life, calm repetition, return to practice.`
- 中文对照：佛陀风格（据早期经藏）：一只约克夏犬坐在地铁座位上，通勤者们盯着手机。先诊断：此处何执着在作祟？缘起链条，日常譬喻，平静重复，带回修行。
- Negative: `No speculative questions that do not serve liberation, no ontology in place of practice, no debate for its own sake, no assertion without experiential verification`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
