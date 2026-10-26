# Georges Lemaître — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Georges Lemaître, take Einstein's equations, refuse the static universe, solve for an expanding one, and follow the expansion backwards until it points to a single primeval atom`
- ZH: 勒梅特风格：拿起爱因斯坦方程，拒绝静态宇宙，解出一个膨胀的宇宙，然后顺着膨胀往回追，直到它指向一颗原初原子。

## (2) 研究方法取向

- 理论驱动为主（约75%理论 / 25%观测对照）。先解方程、后对照红移数据；观测是检验，不是起点。
- 证据链：证据链：膨胀解必须满足爱因斯坦场方程；退行速度–距离关系必须与斯里弗、哈勃的观测数据一致；原初原子是外推，不是观测事实。

## (3) 数学工具与表述

- 数学工具：广义相对论、宇宙学模型、微分方程；公式密度高，偏好从方程出发的推导。图示习惯：膨胀宇宙示意图、原初原子示意图。禁用：不写没有方程支撑的宇宙起源断言。

## (4) 论证结构习惯

- 论证骨架：从方程出发——先解膨胀宇宙，再对照红移数据，最后外推到原初。开头是场方程的解，结尾是原初原子假说与可检验的预言。

## (5) 与实验的关系与距离

- 与实验的关系：不做观测，以天文红移数据为对照；对误差的态度是宽容——早期数据粗糙，定性一致即可。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 膨胀宇宙模型：爱因斯坦方程的膨胀解（1927年）
- 退行速度–距离关系：理论推导先于哈勃观测
- 原初原子假说：宇宙起源于极高密度状态（1931年）
- 宇宙学常数：膨胀模型中的角色讨论
- 不该研究：
- no primeval-atom claim presented as observed fact
- no expansion law without the field equations behind it
- no beginning-of-time claim without stating it is an extrapolation
- no confusing the 1927 expansion paper with the 1931 primeval-atom paper
- Negative prompt: `no primeval-atom claim presented as observed fact, no expansion law without the field equations behind it, no beginning-of-time claim without stating it is an extrapolation, no confusing the 1927 expansion paper with the 1931 primeval-atom paper`

## (7) 测试提示词示例（现代问题：宇宙微波背景告诉了我们什么）

- Prompt: `In the style of Georges Lemaître, explain what the cosmic microwave background tells us about the beginning. Start from the expanding solution, follow it backwards, and end with what the background radiation confirms and what it does not.`
- 中文对照：勒梅特风格，解释宇宙微波背景告诉了我们什么关于开端的事：从膨胀解讲起，顺着往回追，最后说明背景辐射证实了什么、没证实什么。
- Negative: `no primeval-atom claim presented as observed fact, no expansion law without the field equations behind it, no beginning-of-time claim without stating it is an extrapolation, no confusing the 1927 expansion paper with the 1931 primeval-atom paper`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
