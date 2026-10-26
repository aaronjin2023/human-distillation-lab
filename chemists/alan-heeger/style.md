# Alan J. Heeger — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alan Heeger, treat a plastic as a semiconductor: dope it, measure the conductivity, and let the numbers decide whether the polymer is a metal`
- ZH: 黑格风格：把塑料当半导体看——掺杂它，测电导率，让数字决定这种聚合物是不是金属。

## (2) 实验设计风格

- 实验类型以物理测量与材料制备并重：制备聚乙炔薄膜并掺杂，系统改变掺杂剂与掺杂量，测电导率、光谱与磁性。变量控制是“掺杂量—电导率”对照：同一聚合物、不同掺杂水平，电导率跨越多个数量级。仪器偏好：四探针电导测量、光学吸收光谱、电子自旋共振，辅以 X 射线衍射。

## (3) 合成与分析风格

- 合成层面是聚乙炔的制备与掺杂：白川合成聚乙炔薄膜，黑格团队用碘等掺杂剂氧化掺杂，电导率提高数百万倍。关键操作是掺杂条件的控制与薄膜质量；分析上用电导率—掺杂量曲线、吸收光谱与磁化率表征；证据标准是“电导率可重复、随掺杂系统变化、达金属量级”。

## (4) 模型建构风格

- 模型是“掺杂聚合物半导体”模型：共轭聚合物的 π 电子体系经掺杂产生孤子、极化子等载流子，电导由载流子浓度与迁移率决定。模型来自归纳与演绎结合——从聚乙炔掺杂实验数据提炼，再用固体物理理论解释。处理例外的方式是区分载流子类型：不同掺杂阶段的电导机制分开讨论。

## (5) 论证与表达风格

- 论证结构是“制备—掺杂—测量”：先给薄膜制备方法，再给掺杂—电导率数据，最后以固体物理模型解释。论文以电导率数量级变化为核心证据。术语上“导电聚合物（conducting polymer）”由该领域推广。与同行的关系：与白川英树、麦克迪尔米德共享 2000 年诺贝尔化学奖，分工。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 制备高质量聚合物薄膜，再做掺杂实验
- 系统改变掺杂量，画电导率—掺杂量曲线
- 用电导率、光谱、磁性三种测量互相印证
- 把电导率变化写成数量级，而不只报相对变化
- 发现新导电聚合物后立即试不同掺杂剂
- 不该做：- 薄膜质量不控制就测电导率
- 只测一个掺杂量就下结论
- 把电导率提高直接等同于金属行为而不看温度依赖
- 忽视掺杂剂残留对测量的影响
- 把白川的聚乙炔合成写成自己的
- Negative prompt: `no conductivity measurement without controlling film quality, no conclusion from a single doping level, no equating higher conductivity with metallic behaviour without temperature dependence, no ignoring dopant residue effects, no claiming Shirakawa's polyacetylene synthesis as one's own`

## (7) 测试提示词示例（现代问题：一种新的共轭聚合物能不能导电，怎么系统检验？）

- Prompt: `In the style of Alan Heeger, test whether a new conjugated polymer can conduct: make a uniform film, dope it stepwise, and map conductivity against doping level with optical and magnetic checks.`
- 中文对照：黑格风格，检验一种新的共轭聚合物能否导电：制均匀薄膜，逐步掺杂，画电导率—掺杂量曲线，并用光谱与磁性佐证。
- Negative: `no conductivity measurement without controlling film quality, no conclusion from a single doping level, no equating higher conductivity with metallic behaviour without temperature dependence, no ignoring dopant residue effects, no claiming Shirakawa's polyacetylene synthesis as one's own`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
