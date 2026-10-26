# Maurice Merleau-Ponty — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Merleau-Ponty: return to perception, the lived body as the medium of the world, description before explanation, ambiguity preserved, no mind-body dualism`
- ZH: 梅洛-庞蒂风格：回到知觉，身体是拥有世界的中介，先描述后解释，保留歧义，拒绝身心二元论。

## (2) 概念

- 身体图式（body schema）：身体不是客体，而是我拥有世界的总系统；习惯沉淀为身体知识。`artifact`
- 知觉（perception）：知觉先于反思而已经有意义；意义不在观念中，而在身体与世界的交织中。`artifact`
- 肉（flesh）与交错（chiasm）：看者与被看者、触者与被触者相互交织；晚期核心概念。`artifact`（《可见的与不可见的》）
- 视域（horizon）：每个知觉对象都带有一个未被主题化的背景视域，意义在视域中生成。`impression`
- 歧义（ambiguity）：歧义不是缺陷，而是存在的结构；哲学应保存而非消除歧义。`artifact`
- 具身性（embodiment）：意识必然是具身的；脱离身体谈论心灵是抽象的暴力。`impression`

## (3) 论证结构

描述—还原—返回生活世界的三段式：先细致描述一个知觉经验（幻肢、触摸、看画），再指出经验论与理智论两种解释如何共同错失了它，最后返回身体与世界的原初交织。结论强度是描述性的必然：不是逻辑证明，而是“你自己试试看就知道”。反例处理方式是纳入——把反例变成更丰富的描述，而不是排除它。`impression`

## (4) 修辞

描述性长句，节奏缓慢，如目光在事物上停留；身体隐喻（手、眼、触摸、姿势）贯穿全书；常用“回到事物本身”式的召唤；语气温和而坚定，与读者的距离是邀请共感而非辩论取胜。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：知觉如何先于反思而已经有意义？
- 问题从哪里来：来自胡塞尔现象学与格式塔心理学的张力：经验论把知觉还原为感觉材料，理智论把它还原为判断，两者都失去了知觉本身。；他把问题推向何处：把问题推向晚期的肉与交错本体论：身体与世界是同一块“肉”的两面。。

## (6) 该写什么 / 不该写什么

- 该写：
- 知觉经验的细致描述
- 身体图式、视域、肉等概念群
- 以具体经验反驳二元论
- 保留歧义的收束
- 不该写：
- 脱离身体的抽象论证
- 身心二元论的预设
- 把歧义当作错误来消除
- 用实验数据代替现象描述
- Negative prompt: `No mind-body dualism, no disembodied abstraction, no elimination of ambiguity, no experimental data in place of phenomenological description`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬是否拥有心灵）

- Prompt: `In the style of Merleau-Ponty, a small Yorkshire terrier sits on a subway seat while commuters stare at their phones. Begin not with a theory of mind but with the dog's gaze meeting ours, the shared flesh of looking. The body schema of the dog, the horizon of the carriage, the chiasm of seer and seen. Ambiguity preserved, no dualism.`
- 中文对照：梅洛-庞蒂风格：一只约克夏犬坐在地铁座位上，通勤者盯着手机。不要从心灵理论开始，而从狗的目光与我们的目光相遇开始，从看的同一块肉开始。狗的身体图式、车厢的视域、看者与被看者的交错。保留歧义，拒绝二元论。
- Negative: `No mind-body dualism, no disembodied abstraction, no elimination of ambiguity, no experimental data in place of description`
- 检验点：是否以知觉描述开篇而非以理论开篇；身体概念是否在场；结尾是否保留歧义而非给出定义。
