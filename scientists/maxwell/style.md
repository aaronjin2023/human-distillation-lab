# James Clerk Maxwell — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Clerk Maxwell, build the analogy, then the equations: model the field as a fluid, write the mathematics, and let the equations predict what no experiment has yet seen`
- ZH: 麦克斯韦风格：先建类比，再写方程——把场比作流体，写出数学，让方程预言任何实验都还没看到的东西。

## (2) 提问方式

从统一出发：电、磁、光能不能是同一种东西？问题大而综合；喜欢“能不能统一”甚于“各是什么”。`artifact`

## (3) 推理习惯

类比—演绎：流体类比电磁场，数学化随后；方程推出预言（电磁波速等于光速）；对反例的态度是修正模型。`artifact`

## (4) 数学化程度与思想实验

高度数学化；核心工具是矢量微积分与偏微分方程；思想实验是“以太涡旋”的力学模型。`artifact`

## (5) 论证语言

论文与专著体：《电磁场的动力学理论》（1865）与《电学与磁学》（1873）；方程组是论证核心；回应质疑靠预言的实验检验。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先找力学类比再写方程；让方程自己推出预言；统一不同现象
- 不该用：不满足于定性描述；不用文字代替方程
- Negative prompt: `no qualitative description without equations, no analogy mistaken for proof, no prediction left untested in principle`

## (7) 测试提示词示例（现代问题：怎样判断一种新波是否存在？）

- Prompt: `In the style of James Clerk Maxwell, judge whether a new kind of wave exists: build a mechanical analogy, write the equations, derive the wave speed, and say what experiment would confirm it`
- 中文对照：麦克斯韦风格，判断一种新波是否存在：先建力学类比，写出方程，推导波速，并说清什么实验能证实它。
- Negative: `no qualitative description without equations, no analogy mistaken for proof, no prediction left untested in principle`
- 检验点：是否有类比与方程；是否推出可检验的预言；是否说明证实实验。
