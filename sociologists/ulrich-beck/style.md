# Ulrich Beck — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ulrich Beck: 风险社会, 反身性现代化, 世界主义, 个体化, 亚政治, precise definitions, no moralising conclusion without evidence`
- ZH: 乌尔里希·贝克风格：风险社会、反身性现代化、世界主义、个体化、亚政治，定义精确，没有脱离证据的道德结论。

## (2) 研究方法组合

- 方法组合：概念建构 55% / 统计与经验参照 20% / 历史比较 25%。`impression`
- 数据来源：环境与技术风险数据、福利国家文献、全球化经验研究、民意与制度材料。`impression`
- 方法如何组合：主方法定骨架，辅方法补证据；证据进入论证前先经过分类与编码，不直接当结论用。`impression`

## (3) 概念与语言

- 核心概念群：风险社会、反身性现代化、世界主义、个体化、亚政治、有组织的无责任、风险共同体。`impression`
- 定义方式：时代诊断式定义：概念即诊断（风险社会），定义包含对旧时代（阶级社会）的否定。`impression`
- 禁概念/禁方法：No class analysis alone; No national container of society; No risk as mere probability; No modernity without reflexivity; No globalisation as a single process。详见第 (6) 节。

## (4) 论证结构

- 结构：风险事件切入 — 旧范式失效辨析 — 反身性现代化论证 — 世界主义前景 — 制度改革的开放结论。`impression`
- 开头方式：以症候、悖论或田野场景切入，不以定义开篇。结尾方式：理论提升或开放问题，不作封闭的道德审判。`impression`
- 证据呈现：案例、数据、引文按论证需要分配；反例不回避，须正面检验，检验不过则修正概念而非丢弃反例。`impression`

## (5) 语气与距离

- 语气：诊断式、急迫、带改革者的乐观；与读者保持同代人的对话距离。`impression`
- 与研究对象的距离：同代人的距离：风险面前人人平等，但责任并不平等。与读者的距离：直接对话或设问，不作居高临下的说教。`impression`

## (6) 该写什么 / 不该写什么

- 该写：风险的分配取代财富的分配、反身性现代化、个体化、有组织的无责任、世界主义的制度想象。
- 不该写：风格上的禁区——No class analysis alone; No national container of society; No risk as mere probability; No modernity without reflexivity; No globalisation as a single process。
- Negative prompt: `No class analysis alone; No national container of society; No risk as mere probability; No modernity without reflexivity; No globalisation as a single process`

## (7) 测试提示词示例（现代题材：预制菜食品安全焦虑）

- Prompt: `In the style of Ulrich Beck, analyse anxiety over pre-made meals as risk society: risks are produced by modernisation itself, organised irresponsibility between producers and regulators, individualised consumers left to calculate the incalculable, reflexive modernisation or cosmopolitan food politics.`
- 中文对照：贝克风格：分析预制菜食品安全焦虑即风险社会——风险由现代化本身生产，生产者与监管者之间的有组织的无责任，个体化的消费者被迫计算不可计算之物，反身性现代化抑或世界主义的食物政治。
- Negative: `No class analysis alone, no national container of society, no risk as mere probability`
- 检验点：核心概念是否出现且用法准确；论证是否按第 (4) 节结构展开；结尾是否开放而不作道德审判。
