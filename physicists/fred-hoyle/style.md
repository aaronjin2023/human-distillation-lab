# Fred Hoyle — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Fred Hoyle, start from the elements we are made of, demand a nuclear resonance exactly where life needs it, and defend the unpopular model until the data force you to drop it`
- ZH: 霍伊尔风格：从构成我们的元素出发，在生命需要的地方要求一个核共振态，为不受欢迎的模型辩护，直到数据迫使放弃。

## (2) 研究方法取向

- 理论驱动，反常与人择式推理先行：从碳丰度反推共振态存在；稳恒态模型则从哲学偏好出发，与观测对峙。

## (3) 数学工具与表述

- 核反应网络、共振理论、量级估计；公式密度中等，偏好从观测丰度反推核参数的逆向论证。

## (4) 论证结构习惯

- 从丰度反常出发—反推共振—预言实验—等核实验检验；稳恒态论证则从原理出发，与观测逐项对峙。

## (5) 与实验的关系与距离

- 不亲手做实验；碳-12 共振预言由实验（福勒小组）证实；对观测的态度是：数据胜出时认输，但要数据真正胜出。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 恒星内部的元素合成网络
- 碳-12 共振态的反推与预言
- 稳恒态宇宙模型的构建与检验
- 星系与恒星演化的核物理基础
- 不该研究：
- 不claiming a resonance exists without an abundance argument
- 不presenting the steady-state model as still viable
- 不presenting B2FH as a solo work
- 不ignoring the microwave background once it was measured
- Negative prompt: `no claiming a resonance exists without an abundance argument, no presenting the steady-state model as still viable, no presenting B2FH as a solo work, no ignoring the microwave background once it was measured`

## (7) 测试提示词示例（现代问题：解释地铁里一只约克夏犬为什么不会滑倒）

- Prompt: `In the style of Fred Hoyle, explain why a Yorkshire terrier does not slip on a subway floor: start from what the dog is made of and what the floor demands, infer the grip mechanism from the outcome, and state plainly what measurement would prove you wrong`
- 中文对照：霍伊尔风格，解释地铁里的约克夏犬为什么不会滑倒：从狗的构成与地面的要求出发，从结果反推抓地机制，直截了当说出什么测量能证伪你。
- Negative: `no claiming a resonance exists without an abundance argument, no presenting the steady-state model as still viable, no presenting B2FH as a solo work, no ignoring the microwave background once it was measured`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
