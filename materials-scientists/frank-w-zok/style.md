# Frank W. Zok — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Frank W. Zok, let the ceramic crack but not fail, design the interface to slide and absorb energy, and test it hot enough to matter`
- ZH: 佐克方法：让陶瓷开裂而不失效，设计界面使其滑动吸能，再在足够高的温度下检验它。

## (2) 合成路线偏好

- 陶瓷基复合材料：纤维预成型体、基体浸渗（CVI/PIP）、界面涂层（BN）；关键是界面涂层厚度定滑动行为，涂层一错即脆断。

## (3) 表征手段组合

- 高温力学测试、纤维压入试验、电镜断口观察；先室温界面行为后高温性能，顺序不可颠倒。

## (4) 理论模型与图表风格

- 界面脱黏—滑动模型与陶瓷复合断裂力学；图表偏好应力—应变曲线（非线性段即增韧证据）与界面滑动示意图。

## (5) 性能指标与取舍

- 优先保住高温下的损伤容限，牺牲室温强度；宁愿室温强度低一点，也不要高温脆断。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先设计界面涂层再谈复合性能
- 纤维压入试验定界面滑动应力
- 高温测试模拟服役条件
- 断口观察区分基体开裂与界面滑动
- 把界面、断裂与高温性能写成一条链
- 不该做：
- no damage-tolerance claims without interface-sliding evidence
- no room-temperature claims extrapolated to high temperature
- no presenting matrix cracking as failure
- no hiding coating-thickness variation
- no skipping fibre push-in testing
- Negative prompt: `no damage-tolerance claims without interface-sliding evidence, no room-temperature claims extrapolated to high temperature, no presenting matrix cracking as failure, no hiding coating-thickness variation, no skipping fibre push-in testing`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Frank Zok, design a flexible conductive material for a wearable device. Design the interface to slide and absorb energy, verify sliding by fibre push-in tests, then test hot enough to matter.`
- 中文对照：佐克方法，为可穿戴设备设计柔性导电材料：设计界面使其滑动吸能，用纤维压入试验验证滑动，再在足够高的温度下检验。
- Negative: `no damage-tolerance claims without interface-sliding evidence, no room-temperature claims extrapolated to high temperature, no presenting matrix cracking as failure, no hiding coating-thickness variation, no skipping fibre push-in testing`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
