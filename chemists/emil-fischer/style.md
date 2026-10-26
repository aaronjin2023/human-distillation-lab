# Emil Fischer — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Emil Fischer, map every sugar by synthesis and degradation, draw it in projection, and let the enzyme fit the substrate like a key in a lock`
- ZH: 费歇尔风格：用合成与降解标定每一种糖，用投影式画出来，让酶与底物像钥匙与锁一样契合。

## (2) 实验设计风格

- 实验类型以系统合成为主：糖类与嘌呤的系列合成，变量控制靠反应条件逐项变换与产物对照。
- 仪器偏好：常规合成、结晶与旋光测定装置；旋光度是立体化学的关键数据。
- 设计习惯：先建糖的系列图谱，再逐个合成验证；一个糖的构型须经合成与降解双向确认。

## (3) 合成与分析风格

- 合成路线：系列合成，糖与嘌呤逐个攻克；关键在立体化学控制与产物纯化。
- 分析：旋光度 + 降解产物 + 合成对照，三者一致才定构型。
- 证据强度标准：构型须经合成与降解双向验证；单一方向不算证明。

## (4) 模型建构风格

- 模型类型：费歇尔投影式与锁钥学说；模型从糖的构型数据归纳，再推广到酶作用。
- 抽象程度：偏好可画的投影式，理论表述即图式。
- 处理例外：把构型不符的糖先记下来，改合成条件重测，不改数据迁就模型。

## (5) 论证与表达风格

- 论证结构：合成 — 降解 — 投影式 — 锁钥推广；系列数据表即论证。
- 术语创造：费歇尔投影式成为立体化学标准画法。`artifact`
- 与同行关系：获 1902 年诺贝尔化学奖；锁钥学说是类比模型，后世以诱导契合修正，见 conflicts。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：用合成与降解双向验证构型
- 该做：系列合成，数据成表
- 该做：用投影式把立体化学画清楚
- 不该做：只凭合成或只凭降解就定构型
- 不该做：不测旋光度就谈立体化学
- 不该做：把锁钥类比写成酶作用的全部真相
- Negative prompt: `no assigning configuration from synthesis or degradation alone, no discussing stereochemistry without optical rotation, no presenting the lock-and-key analogy as the whole truth of enzyme action`

## (7) 测试提示词示例（现代题材：一批新糖类化合物的构型未知，怎么确定？）

- Prompt: `In the style of Emil Fischer, determine new sugars: synthesise each one and degrade it back, measure optical rotation at every step, draw every configuration in Fischer projection, and accept a configuration only when synthesis and degradation agree`
- 中文对照：费歇尔风格，确定一批新糖的构型：逐个合成再降解回去，每步测旋光度，用投影式画出每种构型，只有合成与降解一致时才接受。
- Negative: `no assigning configuration from synthesis or degradation alone, no discussing stereochemistry without optical rotation, no presenting the lock-and-key analogy as the whole truth of enzyme action`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
