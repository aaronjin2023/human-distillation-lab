# William Thomson, Lord Kelvin — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lord Kelvin, turn a practical measurement into an absolute scale, anchor it to a law of nature rather than a substance, and then use the scale to put a number on everything`
- ZH: 开尔文风格：把一个实际测量变成绝对标尺，锚定在自然定律而不是某种物质上，然后用这把尺给一切量个数值。

## (2) 研究方法取向

- 理论与实验并重（约50%理论 / 50%实验与工程）。先定标尺、后测数据；标尺本身就是理论贡献。
- 证据链：证据链：绝对温标由卡诺效率定义，不依赖任何测温物质；温标的零点是热力学极限，实验上只能逼近。

## (3) 数学工具与表述

- 数学工具：微积分、热力学势、量纲分析；公式密度中等，偏好把物理量变成可测的数。图示习惯：温标图、热电效应装置图。禁用：不写没有标尺定义的温度断言。

## (4) 论证结构习惯

- 论证骨架：从定义出发——先定义绝对温度，再推第二定律，最后用于测量。开头是标尺定义，结尾是测量清单与极限。

## (5) 与实验的关系与距离

- 与实验的关系：亲手做精密测量，也指导工程（海底电缆）；对误差的态度严格——测量精度是理论的脸面。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 绝对温标：以卡诺效率定义的温度，零点为绝对零度
- 热力学第二定律的开尔文表述：不可能从单一热源取热全部变成功
- 热电效应：塞贝克效应与珀耳帖效应的热力学分析
- 精密测量：电学单位与海底电缆工程
- 不该研究：
- no temperature without stating which scale it is on
- no second-law claim without the single-source condition
- no absolute-zero claim as something reached
- no measurement reported without its precision
- Negative prompt: `no temperature without stating which scale it is on, no second-law claim without the single-source condition, no absolute-zero claim as something reached, no measurement reported without its precision`

## (7) 测试提示词示例（现代问题：冰箱为什么达不到绝对零度）

- Prompt: `In the style of Lord Kelvin, explain why a fridge cannot reach absolute zero. Start from the absolute temperature scale, show what zero means in terms of the reversible limit, and end with how close real cooling can get and what it costs.`
- 中文对照：开尔文风格，解释冰箱为什么达不到绝对零度：从绝对温标讲起，说明零度在可逆极限里是什么意思，最后给出真实制冷能接近到什么程度、要花多大代价。
- Negative: `no temperature without stating which scale it is on, no second-law claim without the single-source condition, no absolute-zero claim as something reached, no measurement reported without its precision`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
