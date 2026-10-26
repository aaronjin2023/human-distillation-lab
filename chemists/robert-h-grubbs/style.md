# Robert H. Grubbs — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert H. Grubbs, build a ruthenium catalyst that tolerates real functional groups, prove it on a broad scope, and let the user, not the inventor, decide what it is good for`
- ZH: 格拉布斯风格：建一种能容忍真实官能团的钌催化剂，在宽底物谱上证明它，让使用者而不是发明者决定它有什么用。

## (2) 实验设计风格

- 实验类型以催化剂开发与底物谱验证为主；变量控制靠催化剂结构系统变化与平行筛选。
- 仪器偏好：常规合成、色谱与光谱；催化剂稳定性与官能团容忍度是核心数据。
- 设计习惯：先定催化剂的实用标准（稳定、易得、容忍度高），再优化活性。

## (3) 合成与分析风格

- 合成路线：钌卡宾催化剂系列开发，第一代、第二代逐代改进；关键在配体调控。
- 分析：底物谱 + 产率 + 官能团容忍度成表，应用实例越多方法价值越高。
- 证据强度标准：催化剂须经宽底物谱与应用验证；单一反应高产率不算方法。

## (4) 模型建构风格

- 模型类型：烯烃复分解机理（金属环丁烷）；模型从催化实验归纳，再指导配体设计。
- 抽象程度：偏好具体催化事实，机理服务于催化剂改进。
- 处理例外：把催化剂失活的例子记下来，改配体重试，不删数据。

## (5) 论证与表达风格

- 论证结构：催化剂 — 底物谱 — 应用；底物谱与应用实例即论证。
- 语言：论文以催化剂结构、产率表与应用实例为主。
- 与同行关系：获 2005 年诺贝尔化学奖（与肖万、施罗克共享）；格拉布斯催化剂已商业化，学术与商业贡献分开记。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先定催化剂实用标准再优化活性
- 该做：宽底物谱验证官能团容忍度
- 该做：催化剂失活例子也记录
- 不该做：只用一个反应就宣称通用催化剂
- 不该做：忽视催化剂失活数据
- 不该做：把商业化写成学术发现
- Negative prompt: `no claiming a general catalyst from one reaction, no ignoring catalyst deactivation data, no presenting commercialisation as academic discovery`

## (7) 测试提示词示例（现代题材：一种新催化剂号称通用，怎么检验它？）

- Prompt: `In the style of Robert H. Grubbs, test a claimed general catalyst: set practical standards first, run it across a broad substrate scope with real functional groups, tabulate yields and failures, and accept generality only when scope and stability hold`
- 中文对照：格拉布斯风格，检验一种号称通用的新催化剂：先定实用标准，再带真实官能团测遍底物谱，产率与失败成表，只有底物谱与稳定性都成立时才接受通用。
- Negative: `no claiming a general catalyst from one reaction, no ignoring catalyst deactivation data, no presenting commercialisation as academic discovery`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
