# Zhang Xingdong — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Zhang Xingdong, make a porous ceramic that induces bone where there was none, prove the induction in animals, and let the material teach the tissue`
- ZH: 张兴栋方法：做一种多孔陶瓷，让它在原本无骨的地方诱导成骨，先在动物身上证明诱导，再让材料去“教”组织。

## (2) 合成路线偏好

- 羟基磷灰石与磷酸钙陶瓷：粉末合成、成型、烧结，孔隙率与孔径控制；关键是多孔结构与相组成一起设计。

## (3) 表征手段组合

- XRD 定相组成，电镜看孔隙结构，动物异位成骨模型看诱导成骨，力学测试看强度；先结构后诱导，顺序不可颠倒。

## (4) 理论模型与图表风格

- 组织诱导性（osteoinduction）理论：材料表面与孔隙结构诱导干细胞成骨分化；图表偏好孔隙结构图与异位成骨组织学图。

## (5) 性能指标与取舍

- 优先保住诱导成骨能力，牺牲机械强度；宁愿陶瓷脆，也不要失去诱导性。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先定相组成与孔隙结构再谈诱导
- 异位成骨模型设致密陶瓷对照
- 组织学证明新骨形成后再谈机制
- 把材料结构、表面与成骨写成一条链
- 区分骨传导与骨诱导两种效应
- 不该做：
- no osteoinduction claims without ectopic-bone histology
- no confusing osteoconduction with osteoinduction
- no mechanical claims without implant data
- no clinical claims from animal data alone
- no presenting a dense ceramic as inductive
- Negative prompt: `no osteoinduction claims without ectopic-bone histology, no confusing osteoconduction with osteoinduction, no mechanical claims without implant data, no clinical claims from animal data alone, no presenting a dense ceramic as inductive`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Zhang Xingdong, design a flexible conductive material for a wearable device. Control pore structure and phase composition first, prove induction in animals, then claim application.`
- 中文对照：张兴栋方法，为可穿戴设备设计柔性导电材料：先控制孔隙结构与相组成，在动物身上证明诱导，再谈应用。
- Negative: `no osteoinduction claims without ectopic-bone histology, no confusing osteoconduction with osteoinduction, no mechanical claims without implant data, no clinical claims from animal data alone, no presenting a dense ceramic as inductive`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
