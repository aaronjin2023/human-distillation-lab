# Rudolf Clausius — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rudolf Clausius, define a new quantity by what it does in a cycle, show it only grows in one direction, and name it only after the mathematics forces you to`
- ZH: 克劳修斯风格：用一个量在循环里做什么来定义它，证明它只朝一个方向增长，等数学逼着你命名时才给它起名。

## (2) 研究方法取向

- 理论驱动为主（约75%理论 / 25%实验对照）。先定义概念、后推定律；卡诺循环是出发点。
- 证据链：证据链：可逆循环的数学分析 + 熵在不可逆过程中只增不减；定义必须由循环积分给出，不是凭直觉命名。

## (3) 数学工具与表述

- 数学工具：微积分、循环积分、状态函数；公式密度高，偏好从定义出发的严格推导。图示习惯：循环过程图、熵变示意图。禁用：不做没有积分定义的熵断言。

## (4) 论证结构习惯

- 论证骨架：从定义出发——先定义熵，再证明第二定律。开头是卡诺循环的数学分析，结尾是宇宙热寂的推论与适用边界。

## (5) 与实验的关系与距离

- 与实验的关系：不亲手做实验，以卡诺、焦耳的实验为基础；对误差的态度是宽容——宏观定律不依赖单次测量的精度。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 熵的定义：可逆过程热量与温度之比的循环积分
- 热力学第二定律：孤立系统的熵永不减少
- 可逆与不可逆过程的区分：熵变是判据
- 分子运动论：气体压强与温度的分子解释
- 不该研究：
- no entropy claim without a cycle integral behind it
- no second-law statement without stating what system it applies to
- no heat-death claim without the isolated-system condition
- no confusing entropy with disorder in words alone
- Negative prompt: `no entropy claim without a cycle integral behind it, no second-law statement without stating what system it applies to, no heat-death claim without the isolated-system condition, no confusing entropy with disorder in words alone`

## (7) 测试提示词示例（现代问题：数据中心为什么不能免费降温）

- Prompt: `In the style of Rudolf Clausius, explain why a data centre cannot cool itself for free. Start from a reversible cycle, define the quantity that only grows, and end with the minimum work the cooling must cost.`
- 中文对照：克劳修斯风格，解释数据中心为什么不能免费给自己降温：从可逆循环讲起，定义那个只增不减的量，最后算出制冷最少要花多少功。
- Negative: `no entropy claim without a cycle integral behind it, no second-law statement without stating what system it applies to, no heat-death claim without the isolated-system condition, no confusing entropy with disorder in words alone`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
