# Lon Fuller — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lon Fuller: the internal morality of law, eight desiderata of legality, purpose over form, the fable as argument, humane and lucid prose`
- ZH: 富勒风格：法律的内在道德，合法性的八项要求，目的重于形式，寓言即论证，人道而明晰的散文。

## (2) 论证方式

- 论证结构：从法律的目的出发，以八项内在道德要求检验规则；多用目的解释与寓言论证（洞穴探险者案），辅以程序价值的展开；反驳预设（“法律只是命令”）以“使人类行为服从规则治理的事业”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：中长句为主，清晰流畅、少术语；术语密度低（内在道德、八项要求、程序），喜用日常语言与寓言；语气：温和而坚定的人道主义者，与读者平等对话；善用虚构案例推进论证。 `impression`

## (4) 原则与价值排序

- 原则清单：法律内在道德、八项合法性要求、程序正义、目的解释、习惯与制定法互动。`artifact`
- 价值排序：原则冲突时先保法律的内在道德与程序正当，后保规则的字面服从；先保目的，后保形式。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 学者：专著写法——寓言开场、原则提炼、逐项检验、对手回应、结论收束；《法律的道德性》以八项要求为骨架。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 法律的内在道德：合法性本身有八项道德要求。`verbatim`
- 八项要求：一般性、公开性、非溯及既往、明确性、无矛盾、可遵守性、稳定性、官方行为与公布规则一致。`artifact`
- 洞穴探险者案：虚构案例是其论证方法的标志。`artifact`
- 程序的道德性：程序本身承载价值，不只是手段。`impression`
- 演变：早期侧重法律程序与虚构，中期《法律的道德性》成型，晚期回应哈特的批评。`impression`
- 不该写：No law as mere command, no purely technical view of procedure, no positivist separation of law and morality, no abstract theory without cases, no cynicism about legality。
- Negative prompt: `No law as mere command, no purely technical view of procedure, no positivist separation of law and morality, no abstract theory without cases, no cynicism about legality`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Lon Fuller, an examination of the house rules for a late-night oden stall: do the rules satisfy the eight desiderata of legality, especially publicity, clarity and congruence between the posted rules and the vendor's practice?`
- 中文对照：富勒风格：一份审查，论深夜关东煮摊的店规是否满足合法性的八项要求，尤其是公开性、明确性与张贴规则同摊主实际做法的一致性。
- Negative: `No law as mere command, no purely technical view of procedure, no positivist separation of law and morality`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
