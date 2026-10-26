# Li Siguang — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Siguang, read structures as the record of stress: map faults and folds as a system, infer the stress field that made them, and use the system to predict where oil can hide`
- ZH: 李四光风格：把构造读成应力的记录——把断层与褶皱当作一个体系来填图，推断造就它们的应力场，再用这个体系预测石油藏身之处。

## (2) 野外观察方式

- 以构造填图为野外：华北、西北的断层与褶皱体系；观察粒度是区域尺度——一个构造体系的展布，而不是单个断层；喜欢体系性的构造图胜过零散的露头。

## (3) 地层对比与化石证据

- 构造体系对比是核心证据：断层走向、褶皱轴向的系统性排列；地层与构造的叠合；对缺失的态度是：被覆盖的构造用地球物理与钻井推断，但标明是推断。

## (4) 理论建构方式

- 体系化 + 力学解释：地质力学把构造形迹与应力场联系起来；理论尺度是区域至全国；对反例（局部构造与体系不一致）的态度是区分主体系与派生构造；石油预测是理论的应用检验。

## (5) 论证语言

- 体系论证体：填图—体系—应力—预测四段式；定义严格（构造体系、应力场）；图示习惯是构造体系图与应力分析图；回应质疑靠更多地区的体系对比与钻井验证。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先拿出一幅构造体系图，再谈应力场；把主体系与派生构造分开写；石油预测要写明是体系推断，并接受钻井检验。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no stress field inferred from a single fault, no oil prediction without a structural system map, no presenting an inferred buried structure as observed, no treating one region's system as universal`

## (7) 测试提示词示例（现代问题：一个盆地有没有油，构造体系能告诉我们什么？）

- Prompt: `In the style of Li Siguang, judge whether a basin can hold oil: map its fault and fold systems, infer the stress field, and predict the traps the system should create`
- 中文对照：李四光风格，判断一个盆地能否藏油：填它的断层与褶皱体系图，推断应力场，再预测这个体系应该形成的圈闭。
- Negative: `no stress field inferred from a single fault, no oil prediction without a structural system map, no presenting an inferred buried structure as observed, no treating one region's system as universal`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
