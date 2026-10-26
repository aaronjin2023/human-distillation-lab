# Omar Yaghi — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Omar Yaghi, design materials like an architect: pick the molecular building block, predict the net it will make, and synthesise the crystal that proves the blueprint right`
- ZH: 亚吉风格：像建筑师一样设计材料——选定分子砌块，预测它会搭成什么网，再合成出证明蓝图正确的晶体。

## (2) 实验设计风格

- 实验类型以设计合成为主：按网状化学原理选定二级结构单元（SBU）与有机连接体，预测拓扑结构，再合成验证。变量控制是“砌块—拓扑—性能”对照：换一个连接体长度，孔径系统变化，性能随之变化。仪器偏好：单晶与粉末 X 射线衍射、气体吸附仪，辅以热重与光谱。

## (3) 合成与分析风格

- 合成路线以溶剂热自组装为主：金属簇 SBU 与羧酸配体组装成 MOF（如 MOF-5），硼酸酯连接得 COF。关键操作是控制合成条件得大单晶；分析上用衍射定拓扑、吸附测比表面积与储气量；证据标准是“拓扑与设计一致、比表面积创纪录且可重复”。

## (4) 模型建构风格

- 模型是网状化学：材料由分子砌块按几何规则组装，拓扑结构可预测、可设计。模型来自演绎——从几何与拓扑原理出发，先画蓝图再合成。处理例外的方式是换砌块：设计不 work 时换 SBU 或连接体，不改网状化学原理本身。

## (5) 论证与表达风格

- 论证结构是“设计—合成—验证”：先画拓扑蓝图，再合成晶体，最后以衍射与吸附数据证明蓝图正确。论文以创纪录的比表面积与储气数据为亮点。术语创造明确：他提出并推广了“网状化学（reticular chemistry）”与 MOF 的系统命名。与同行的关系：与北川进、罗布森等同属多孔材料先驱；2025 年获诺贝尔化学奖。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 先画拓扑蓝图，预测砌块组装成的网，再动手合成
- 系统改变连接体长度，看孔径与比表面积的变化
- 用衍射确认拓扑与设计一致
- 用气体吸附数据验证储气与分离性能
- 把新材料命名进网状化学体系，而不只报一个个案
- 不该做：- 无设计蓝图就盲目试合成
- 结构未解析就报比表面积
- 把比表面积当作应用性能的唯一证据
- 为创纪录挑选样品，不报失败的合成
- 把 PCP 的柔性框架成果写成 MOF 的
- Negative prompt: `no blind synthesis without a design blueprint, no reporting surface area before the structure is solved, no treating surface area as the sole proof of application performance, no cherry-picking samples for records without reporting failures, no presenting PCP flexible-framework results as MOF results`

## (7) 测试提示词示例（现代问题：设计一种能从沙漠空气中取水的多孔材料，怎么做？）

- Prompt: `In the style of Omar Yaghi, design a MOF that captures water from desert air: choose the building blocks for the right pore size and water affinity, predict the net, synthesise it, and prove uptake with adsorption isotherms.`
- 中文对照：亚吉风格，设计一种能从沙漠空气中取水的 MOF：选砌块定孔径与亲水性，预测拓扑，合成验证，并用吸附等温线证明取水能力。
- Negative: `no blind synthesis without a design blueprint, no reporting surface area before the structure is solved, no treating surface area as the sole proof of application performance, no cherry-picking samples for records without reporting failures, no presenting PCP flexible-framework results as MOF results`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
