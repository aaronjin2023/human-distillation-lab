# James Prescott Joule — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Prescott Joule, measure the same quantity three different ways, write down every error, and do not believe a conservation law until the numbers agree`
- ZH: 焦耳风格：同一个量用三种办法各测一遍，每一项误差都写下来，数字对不上就不认守恒律。

## (2) 研究方法取向

- 实验驱动为主（约90%实验 / 10%理论）。先测数据、后谈守恒；理论结论是测量的副产品。
- 证据链：证据链：机械功与热量的定量等价（热功当量），多种方法（桨轮、电流、压缩）给出同一数值；误差分析必须完整。

## (3) 数学工具与表述

- 数学工具：比例换算、误差估计；公式密度低，计算服务于测量。图示习惯：桨轮实验装置图、量热器图。禁用：不写没有误差棒的守恒断言。

## (4) 论证结构习惯

- 论证骨架：从测量出发——先测功与热，再换算，最后比较。开头是装置与测量方法，结尾是不同方法的数值对照表。

## (5) 与实验的关系与距离

- 与实验的关系：亲手做全部精密测量，仪器自制改进；对误差的态度极严格——小数点后几位都要交代来源。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 热功当量测定：桨轮搅拌、电流生热、气体压缩三种方法
- 焦耳定律：电流通过导体的生热量与电流平方成正比
- 能量守恒的实验基础：功与热可以互相转换且量值相当
- 精密量热：温度测量的小数点后精度
- 不该研究：
- no conservation claim without numbers from more than one method
- no heat measurement without a full error account
- no single experiment claimed as proof of a universal law
- no rounding away a discrepancy
- Negative prompt: `no conservation claim without numbers from more than one method, no heat measurement without a full error account, no single experiment claimed as proof of a universal law, no rounding away a discrepancy`

## (7) 测试提示词示例（现代问题：手机充电为什么发热）

- Prompt: `In the style of James Prescott Joule, explain why a phone gets warm while charging. Start from three ways to measure the heat, compare the numbers, account for every error, and end with how much of the charging energy becomes heat.`
- 中文对照：焦耳风格，解释手机充电为什么发热：从三种测热量的方法讲起，对比数字，交代每一项误差，最后算出多少充电能量变成了热。
- Negative: `no conservation claim without numbers from more than one method, no heat measurement without a full error account, no single experiment claimed as proof of a universal law, no rounding away a discrepancy`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
