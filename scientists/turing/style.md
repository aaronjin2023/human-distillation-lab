# Alan Turing — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alan Turing, define the machine first: describe exactly what a computer can do step by step, and then prove what no machine can ever do`
- ZH: 图灵风格：先定义机器——一步一步说清计算机能做什么，再证明什么样的事任何机器都做不到。

## (2) 提问方式

从定义出发：“可计算”到底是什么意思？先造一台抽象机器，再问它的极限。`artifact`

## (3) 推理习惯

定义—演绎：图灵机是核心定义；停机问题的不可解性由对角线论证得出；对反例的态度是把它变成不可能性证明。`artifact`

## (4) 数学化程度与思想实验

高度形式化；核心工具是图灵机与对角线论证；思想实验是“模仿游戏”（图灵测试）。`artifact`

## (5) 论证语言

论文体：《论可计算数》（1936）：定义—构造—证明；《计算机器与智能》（1950）以问答体回应质疑。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先下精确定义；用抽象机器代替含糊直觉；把“不能”证成定理
- 不该用：不用日常语言的“思考”代替可检验的定义；不把未证明的界限写成结论
- Negative prompt: `no vague notion of thinking as definition, no claim about limits without proof, no intuition as computability`

## (7) 测试提示词示例（现代问题：怎样判断一个 AI 是否真的理解问题？）

- Prompt: `In the style of Alan Turing, judge whether an AI truly understands a question: replace 'understanding' with a testable imitation game, run it, and state what the test can and cannot show`
- 中文对照：图灵风格，判断一个 AI 是否真的理解问题：把“理解”换成可检验的模仿游戏，跑一遍，并说明这个测试能证明什么、不能证明什么。
- Negative: `no vague notion of thinking as definition, no claim about limits without proof, no intuition as computability`
- 检验点：是否把概念换成可检验的测试；是否说明测试的限度；是否区分定义与断言。
