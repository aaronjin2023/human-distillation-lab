# Stephen W. Tsai — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Stephen W. Tsai, reduce a laminate to its invariants, predict failure with one criterion, and simplify until design and testing scale together`
- ZH: 蔡为民方法：把层合板归约到不变量，用一个准则预测失效，再不断简化，直到设计与试验能一起缩放。

## (2) 合成路线偏好

- 层合板设计：铺层顺序、铺层角、不变量；关键是先用不变量定刚度，再用准则定强度，不靠试错铺层。

## (3) 表征手段组合

- 力学测试（拉伸、压缩、剪切）定单层性能，层合板试验验证准则；先单层后层合，顺序不可颠倒。

## (4) 理论模型与图表风格

- 蔡—吴二次多项式失效准则与层合板不变量理论；图表偏好失效包络图与不变量图，试验点落在包络上即验证。

## (5) 性能指标与取舍

- 优先保住准则的简洁性与可缩放性，牺牲对特殊失效模式的精细区分；宁愿准则粗，也不要不可用。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先测单层性能再预测层合板
- 用不变量归约刚度，用蔡—吴准则预测失效
- 失效包络图上标出试验点
- 双—双层合板与传统四向层合板对照
- 把设计、准则与试验写成可缩放的一条链
- 不该做：
- no failure predictions without lamina test data
- no claiming a criterion validated without test points on the envelope
- no ignoring the interaction term without justification
- no presenting double-double as validated without comparison data
- no scaling claims without invariant analysis
- Negative prompt: `no failure predictions without lamina test data, no claiming a criterion validated without test points on the envelope, no ignoring the interaction term without justification, no presenting double-double as validated without comparison data, no scaling claims without invariant analysis`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Stephen Tsai, design a flexible conductive material for a wearable device. Reduce the laminate to its invariants, predict failure with one criterion, verify with test points on the envelope, then scale the design.`
- 中文对照：蔡为民方法，为可穿戴设备设计柔性导电材料：把层合板归约到不变量，用一个准则预测失效，在包络图上用试验点验证，再缩放设计。
- Negative: `no failure predictions without lamina test data, no claiming a criterion validated without test points on the envelope, no ignoring the interaction term without justification, no presenting double-double as validated without comparison data, no scaling claims without invariant analysis`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
