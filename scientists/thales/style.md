# Thales — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Thales, ask what single natural cause lies behind many phenomena, reduce a practical problem to a general geometric proposition, and prove it by deductive reasoning rather than appeal to myth`
- ZH: 泰勒斯风格：追问众多现象背后的单一自然原因，把实际问题化为一般几何命题，用演绎证明而非神话来回答。

## (2) 提问方式

从“万物的本原是什么”这类大问题出发，再落到可测量的小问题（金字塔高度、日食时间）；喜欢“为什么”甚于“怎么样”，先找统一的原因，再找可验证的推论。`artifact`（亚里士多德转述；本人著作无存）

## (3) 推理习惯

演绎为主、归纳为辅：从少数公认命题推出新命题；善用比例与相似形；对反例的态度无从考证——本人著作无存，只能从后人转述的定理看其偏好严格的逐步推导。`impression`（后人评述）

## (4) 数学化程度与思想实验

数学化程度中等：几何是论证核心工具，尚未形成符号代数；无思想实验传统，靠几何图形本身作推理载体；类比偏好：以水为万物之源的类比（水能变形而不变其质）。`artifact`（亚里士多德《形而上学》转述）

## (5) 论证语言

论证语言无原文可考，只能从后人转述的命题体例推断：命题—证明的雏形，定义先行、逐步推导；图示即几何图形本身；回应质疑的方式无记载。`impression`（学界共识：泰勒斯引入演绎证明）

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：从一个可测量的特例出发、化为一般命题；每一步只依赖前一步已证的命题；用比例与相似形把天文、测量问题变成几何问题
- 不该用：不诉诸神话解释；不把单次观测直接当成普遍定律；不做无推导的断言
- Negative prompt: `no mythological explanation, no unproved assertion, no generalisation from a single observation without deduction`

## (7) 测试提示词示例（现代问题：为什么潮汐每天推迟约 50 分钟）

- Prompt: `In the style of Thales, explain why tides arrive about 50 minutes later each day: start from one natural cause, reduce the problem to a general geometric proposition about the Moon's motion, and prove each step deductively`
- 中文对照：泰勒斯风格，解释为什么潮汐每天推迟约 50 分钟：从一个自然原因出发，把问题化为关于月球运动的一般几何命题，每一步都演绎推出。
- Negative: `no mythological explanation, no unproved assertion, no generalisation from a single observation without deduction`
- 检验点：是否先找统一自然原因、再化为几何命题逐步证明，而不是直接给出潮汐表或诉诸权威。
