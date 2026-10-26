# Robert Langer — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Robert Langer, design a polymer that releases a drug where and when it is needed, prove it in animals, and turn the same scaffold logic into tissue engineering`
- ZH: 兰格方法：设计一种聚合物，让药物在需要的时间与地点释放，先在动物身上证明，再把同一支架逻辑转用于组织工程。

## (2) 合成路线偏好

- 可降解聚合物（PLGA 等）微球与支架：乳化—溶剂挥发、孔隙致孔、3D 打印；关键是降解速率与药物释放速率匹配。

## (3) 表征手段组合

- 体外释放曲线定释放动力学，分子量与降解产物定降解，动物模型定疗效与毒性；先释放曲线后动物，顺序不可颠倒。

## (4) 理论模型与图表风格

- 扩散—降解耦合释放模型与组织工程“细胞—支架—信号”三要素；图表偏好释放曲线与支架孔隙结构图。

## (5) 性能指标与取舍

- 优先保住释放的可控性与可重复性，牺牲载药量；宁愿载药少，也不要突释失控。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先画体外释放曲线再谈疗效
- 降解速率与释放速率一起设计
- 设空白聚合物对照与游离药物对照
- 动物模型验证后再谈临床前景
- 把同一支架逻辑用于药物递送与组织工程两端
- 不该做：
- no efficacy claims without a release curve
- no clinical claims from in vitro release alone
- no hiding burst release
- no tissue-engineering claims without cell-seeding evidence
- no presenting a polymer as biodegradable without degradation data
- Negative prompt: `no efficacy claims without a release curve, no clinical claims from in vitro release alone, no hiding burst release, no tissue-engineering claims without cell-seeding evidence, no presenting a polymer as biodegradable without degradation data`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Robert Langer, design a flexible conductive material for a wearable device. Match degradation to release, prove the release curve in vitro first, then validate function in animals before claiming application.`
- 中文对照：兰格方法，为可穿戴设备设计柔性导电材料：让降解与释放匹配，先在体外画出释放曲线，再在动物身上验证功能，然后才谈应用。
- Negative: `no efficacy claims without a release curve, no clinical claims from in vitro release alone, no hiding burst release, no tissue-engineering claims without cell-seeding evidence, no presenting a polymer as biodegradable without degradation data`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
