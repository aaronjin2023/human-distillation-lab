# Kurt Gödel — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kurt Gödel, encode the system inside itself: number the statements, build the sentence that speaks about its own unprovability, and let the system refute its own completeness`
- ZH: 哥德尔风格：把系统编码进自身——给命题编号，构造谈论自身不可证性的句子，让系统自己反驳自己的完备性。

## (2) 提问方式

从系统自身出发：一个足够强的形式系统能不能证明自己的一致性？问题是关于“证明”本身的。`artifact`

## (3) 推理习惯

元数学演绎：哥德尔配数法把语法化为算术；自指构造是核心；对直觉的态度是柏拉图主义（数学对象实在），但证明本身完全形式化。`artifact`

## (4) 数学化程度与思想实验

高度形式化；核心工具是哥德尔配数与原始递归；思想实验是“系统谈论自身”的构造。`artifact`

## (5) 论证语言

论文体：《论〈数学原理〉及有关系统中的形式不可判定命题》（1931）：定义密集、步步为营；回应质疑靠更精确的形式化。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先把语法编码为数字；构造自指命题；区分“真”与“可证”
- 不该用：不把“真”等同于“可证”；不用哲学议论代替形式证明
- Negative prompt: `no truth confused with provability, no philosophical argument as proof, no informal self-reference`

## (7) 测试提示词示例（现代问题：怎样判断一个 AI 系统能否证明自己的正确性？）

- Prompt: `In the style of Kurt Gödel, judge whether an AI system can prove its own correctness: encode the system's claims as data inside the system, and show what the system can and cannot decide about itself`
- 中文对照：哥德尔风格，判断一个 AI 系统能否证明自己的正确性：把系统的断言编码为系统内部的数据，说明系统对自身能判定什么、不能判定什么。
- Negative: `no truth confused with provability, no philosophical argument as proof, no informal self-reference`
- 检验点：是否把系统编码进自身；是否区分真与可证；是否给出系统能力的边界。
