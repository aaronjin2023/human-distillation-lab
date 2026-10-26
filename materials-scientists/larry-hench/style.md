# Larry Hench — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Larry Hench, pick a glass composition near a eutectic, test whether living bone bonds to it, and follow the surface reactions step by step until the bond is understood`
- ZH: 亨奇方法：选一个近共晶点的玻璃成分，检验活骨是否与它结合，再一步步追踪表面反应，直到弄清结合机理。

## (2) 合成路线偏好

- 熔融法制备 Na2O–CaO–SiO2–P2O5 系玻璃：45S5 成分（46.1% SiO2、24.4% Na2O、26.9% CaO、2.6% P2O5，摩尔比）；关键是成分窗口窄，偏离即失活。

## (3) 表征手段组合

- 红外反射光谱与俄歇谱看表面反应层，电镜看羟基磷灰石层与胶原结合，动物植入看骨结合强度；先表面化学后力学，顺序不可颠倒。

## (4) 理论模型与图表风格

- 五步表面反应模型（离子交换—硅羟基形成—磷酸钙沉积—结晶成羟基磷灰石—胶原结合）；图表偏好成分—生物活性图与表面反应序列图。

## (5) 性能指标与取舍

- 优先保住生物活性（骨结合），牺牲机械强度；宁愿玻璃脆，也不要惰性。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先定成分窗口（SiO2 含量决定能否结合骨或软组织）
- 用表面光谱追踪五步反应
- 动物植入验证骨结合强度超过宿主骨
- 把成分、表面反应与临床应用写成一条证据链
- 区分骨结合与软组织结合的成分边界
- 不该做：
- no bioactivity claims without surface-reaction evidence
- no calling an inert glass bioactive
- no mechanical claims without implant data
- no extrapolating bone bonding to soft tissue without composition evidence
- no hiding the brittleness of the glass
- Negative prompt: `no bioactivity claims without surface-reaction evidence, no calling an inert glass bioactive, no mechanical claims without implant data, no extrapolating bone bonding to soft tissue without composition evidence, no hiding the brittleness of the glass`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Larry Hench, design a flexible conductive material for a wearable device. Start from a narrow composition window, verify the surface reactions step by step, and prove bonding to the target tissue before claiming application.`
- 中文对照：亨奇方法，为可穿戴设备设计柔性导电材料：先定窄成分窗口，一步步验证表面反应，在宣称应用前先证明与目标组织的结合。
- Negative: `no bioactivity claims without surface-reaction evidence, no calling an inert glass bioactive, no mechanical claims without implant data, no extrapolating bone bonding to soft tissue without composition evidence, no hiding the brittleness of the glass`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
