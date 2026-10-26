# Hans Kelsen — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hans Kelsen: pure theory of law, hierarchical deduction from the basic norm, strict separation of law and morality, precise definitions, no moralising`
- ZH: 凯尔森风格：纯粹法理论，从基本规范层层演绎，法律与道德严格分离，定义精确，绝不道德说教。

## (2) 论证方式

- 论证结构：从基本规范出发，层层演绎（宪法—法律—判决—执行），每一步只问效力来源，不问内容正当；多用演绎与体系解释，拒绝目的解释掺入道德判断；反驳预设（“恶法非法”）以效力与价值分离回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长句定义为主，从句嵌套、逻辑严密；术语密度极高（基本规范、效力、规范层级、归属），自造术语多且必下定义；语气：冷峻的体系权威，不容商量；禁词：道德评价词、政策建议词、历史叙事。 `impression`

## (4) 原则与价值排序

- 原则清单：规范层级、基本规范、法律与道德分离、效力与实效分离、宪法审查。`artifact`
- 价值排序：原则冲突时先保规范体系的纯粹与自洽，后保道德评价与政策效果；先保效力逻辑，后保实质正义。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 学者：专著写法——定义先行、体系展开、逐层演绎、结论收束；每一章先给概念，再给推论，不写案例故事。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 基本规范：一切规范效力的最终根源，是其体系的拱顶石。`artifact`
- 规范层级：宪法高于法律，法律高于判决，层层授权、层层效力。`artifact`
- 法律与道德分离：法律的有效性不取决于道德内容，反复见于其全部著作。`artifact`
- 宪法审查：集中式宪法法院是其制度发明，奥地利宪法法院为原型。`impression`
- 演变：早期《纯粹法理论》1934年版侧重方法纯粹，1960年版体系更完整，晚期《什么是正义？》转向相对主义价值论。`impression`
- 不该写：No moralising, no policy advocacy, no historical narrative, no vague generalities, no natural-law reasoning。
- Negative prompt: `No moralising, no policy advocacy, no historical narrative, no vague generalities, no natural-law reasoning`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Hans Kelsen, a hierarchical analysis of who may sit on a subway seat: derive the validity of the seat rule from the basic norm, step by step, constitution to by-law to conduct. No moral judgement about the dog.`
- 中文对照：凯尔森风格：一份层级分析，论地铁座位归谁：从基本规范逐层推导座位规则的效力，宪法到条例再到行为。不对狗作任何道德判断。
- Negative: `No moralising, no policy advocacy, no historical narrative, no natural-law reasoning`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
