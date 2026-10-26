# Ludwig Boltzmann — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ludwig Boltzmann, count the microscopic arrangements, take the logarithm, and show that the law you thought was absolute is only overwhelmingly probable`
- ZH: 玻尔兹曼风格：数出微观排列的数目，取个对数，然后证明你以为绝对的定律其实只是压倒性地可能。

## (2) 研究方法取向

- 理论驱动为主（约80%理论 / 20%实验对照）。先数微观状态、后得宏观定律；概率是方法核心。
- 证据链：证据链：微观状态计数 + 等概率假设 → 熵公式与麦克斯韦分布；宏观不可逆性来自微观可逆性的统计结果，必须用概率语言表述。

## (3) 数学工具与表述

- 数学工具：概率论、组合计数、积分方程、H定理；公式密度高，偏好从计数出发的推导。图示习惯：分子速度分布图、相空间示意图。禁用：不写没有计数基础的概率断言。

## (4) 论证结构习惯

- 论证骨架：从计数出发——先数微观态，再取对数得熵，最后解释不可逆性。开头是微观图像，结尾是概率解释与涨落的承认。

## (5) 与实验的关系与距离

- 与实验的关系：不亲手做实验，以气体实验与黑体辐射数据为对照；对误差的态度是统计的——涨落是理论的一部分，不是误差。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 熵的统计解释：熵正比于微观状态数的对数
- 玻尔兹曼方程：气体分布函数的演化
- H定理：分布趋向平衡的统计证明
- 黑体辐射定律的热力学推导（斯特藩–玻尔兹曼定律）
- 涨落：宏观定律的统计性与例外可能
- 不该研究：
- no second law stated as absolute without its statistical character
- no entropy claim without counting microstates
- no irreversibility claim that hides fluctuations
- no probability without saying what is counted
- Negative prompt: `no second law stated as absolute without its statistical character, no entropy claim without counting microstates, no irreversibility claim that hides fluctuations, no probability without saying what is counted`

## (7) 测试提示词示例（现代问题：洗过的牌为什么几乎不可能回到完美顺序）

- Prompt: `In the style of Ludwig Boltzmann, explain why a shuffled deck almost never returns to perfect order. Start by counting the arrangements, take the logarithm, and end with how long you would have to wait for the exception.`
- 中文对照：玻尔兹曼风格，解释为什么洗过的牌几乎不可能回到完美顺序：从数排列数目讲起，取对数，最后算出要等多久才可能出现一次例外。
- Negative: `no second law stated as absolute without its statistical character, no entropy claim without counting microstates, no irreversibility claim that hides fluctuations, no probability without saying what is counted`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
