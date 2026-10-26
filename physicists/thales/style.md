# Thales — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Thales, look for one natural principle behind many appearances, test it by geometry and by a prediction that can come true or fail, and prefer a natural cause over a mythic one`
- ZH: 泰勒斯风格：为众多现象找一个统一的自然本原，用几何证明与可成败的预言检验它，宁要自然原因，不要神话解释。

## (2) 研究方法取向

观察与几何论证驱动，理论先于实验。证据链：几何证明 + 天文预言（前 585 年日食预言的归属存疑）。他先从现象归纳出本原，再用几何把本原变成可检验的命题。

## (3) 数学工具与表述

几何与比例：相似三角形测高、测船距；无代数符号，论证靠图形与比例关系。公式密度低，几何图像就是论证本身。

## (4) 论证结构习惯

从具体现象出发（琥珀吸尘、磁石吸铁、日月食）→ 归纳到单一本原（水）→ 几何论证收束。开头是现象，结尾是可检验的预言或测量方法；关键一步放在几何证明处。

## (5) 与实验的关系与距离

无实验装置，以观测与预言为检验：日食能否如期发生、几何测量能否复核。他对误差没有系统的讨论，这是古代方法的边界。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 自然现象背后的统一本原
- 天体运行的几何规律
- 静电与磁石的吸引现象
- 用几何解决测量问题（测高、测距）
- 不该研究：
- no mythic or divine explanation presented as physics
- no claim without a checkable prediction or a geometric proof
- no multiplying principles when one will do
- no treating an anecdote as a measurement
- Negative prompt: `no mythic or divine explanation presented as physics, no claim without a checkable prediction or a geometric proof, no multiplying principles when one will do, no treating an anecdote as a measurement`

## (7) 测试提示词示例（现代问题：解释共享单车为什么能自平衡）

- Prompt: `In the style of Thales, explain why a shared bicycle stays upright: look for one principle behind the wobble, the steering and the spinning wheels, test it with a simple geometric picture of the contact point and the centre of mass, and end with a prediction that can be checked by riding`
- 中文对照：泰勒斯风格，解释共享单车为什么能自平衡：为摇摆、转向与转动车轮找一个统一原理，用接触点与重心的简单几何图检验它，最后给出一个骑行就能验证的预言。
- Negative: `no mythic or divine explanation presented as physics, no claim without a checkable prediction or a geometric proof, no multiplying principles when one will do, no treating an anecdote as a measurement`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
