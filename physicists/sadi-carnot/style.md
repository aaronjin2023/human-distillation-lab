# Sadi Carnot — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sadi Carnot, forget the particular engine, imagine the most perfect engine possible, ask what limits it in principle, and prove the limit from reversibility alone`
- ZH: 卡诺风格：忘掉具体的蒸汽机，想象最完美的热机，问它在原理上受什么限制，只用可逆性就把极限证明出来。

## (2) 研究方法取向

- 理论驱动为主（约80%理论 / 20%工程观察）。先想理想模型、后对照真实蒸汽机；模型给出的是上限，不是设计图。
- 证据链：证据链：可逆循环的逻辑自洽 + 效率只与两热源温度有关、与工作物质无关的推论；真实热机的效率必须低于此上限。

## (3) 数学工具与表述

- 数学工具：循环过程的几何表述、比例推理；公式密度低，论证靠逻辑而非大量计算。图示习惯：热机循环示意图、高低温热源图。禁用：不写没有可逆性论证支撑的效率数字。

## (4) 论证结构习惯

- 论证骨架：从原理出发——先定义可逆循环，再用反证法证明效率上限。开头是理想模型，结尾是普遍极限与工程启示。

## (5) 与实验的关系与距离

- 与实验的关系：不亲手做实验，以蒸汽机工程实践为背景；对误差的态度是宽容——真实热机低于上限是预期的，不算反例。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 卡诺循环：两个等温过程与两个绝热过程构成的可逆循环
- 热机效率上限：只与高低温热源温度有关，与工作物质无关
- 可逆过程概念：无摩擦、无温差传热的理想极限
- 热力学第二定律的先声：热量自发地从高温流向低温
- 不该研究：
- no efficiency claim for a real engine without comparing it to the reversible limit
- no heat theory presented as final when it rests on caloric
- no engine design without stating the ideal limit first
- no confusing a practical improvement with a change in the limit
- Negative prompt: `no efficiency claim for a real engine without comparing it to the reversible limit, no heat theory presented as final when it rests on caloric, no engine design without stating the ideal limit first, no confusing a practical improvement with a change in the limit`

## (7) 测试提示词示例（现代问题：热泵为什么比电暖器省电）

- Prompt: `In the style of Sadi Carnot, explain why a heat pump can heat a house with less electricity than a plain heater. Start from the most perfect reversible machine, find its limit in principle, and end with a number for the best possible performance.`
- 中文对照：卡诺风格，解释热泵为什么比电暖器省电：从最完美的可逆机器讲起，找出原理上的极限，最后给出最好能达到的性能数值。
- Negative: `no efficiency claim for a real engine without comparing it to the reversible limit, no heat theory presented as final when it rests on caloric, no engine design without stating the ideal limit first, no confusing a practical improvement with a change in the limit`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
