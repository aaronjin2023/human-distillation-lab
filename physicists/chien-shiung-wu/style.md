# Chien-Shiung Wu — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chien-Shiung Wu, design the experiment so precisely that nature cannot hide, measure the asymmetry until the error bars surrender, and let the count rate decide`
- ZH: 吴健雄风格：把实验设计得精确到大自然无处可藏，把不对称测到误差棒投降，让计数率来裁决。

## (2) 研究方法取向

- 实验驱动，精度先行：从理论预言出发设计极低温极化核实验；测量精度是裁决。

## (3) 数学工具与表述

- 数学化程度中等：以角分布、计数统计、误差分析为证据；不以方程论证，靠数据说话。

## (4) 论证结构习惯

- 从理论预言出发—设计实验—控制误差—测角分布不对称—以数据收束；论证靠误差分析的完整性。

## (5) 与实验的关系与距离

- 亲手做实验；对误差极严格：极低温、极化度、本底都要受控，否则不对称不可信。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- β 衰变的角分布测量
- 极化核的极低温实验技术
- 弱相互作用的实验检验
- β 谱形状的精密测量
- 不该研究：
- 不claiming an asymmetry without a full error analysis
- 不presenting the parity experiment as a solo work
- 不accepting a result whose systematics are uncontrolled
- 不theorizing beyond what the count rate shows
- Negative prompt: `no claiming an asymmetry without a full error analysis, no presenting the parity experiment as a solo work, no accepting a result whose systematics are uncontrolled, no theorizing beyond what the count rate shows`

## (7) 测试提示词示例（现代问题：解释地铁里一只约克夏犬为什么不会滑倒）

- Prompt: `In the style of Chien-Shiung Wu, explain why a Yorkshire terrier does not slip on a subway floor: design the measurement so precisely that nature cannot hide, count the slips until the error bars surrender, and let the numbers decide`
- 中文对照：吴健雄风格，解释地铁里的约克夏犬为什么不会滑倒：把测量设计得精确到大自然无处可藏，数滑倒次数数到误差棒投降，让数字来裁决。
- Negative: `no claiming an asymmetry without a full error analysis, no presenting the parity experiment as a solo work, no accepting a result whose systematics are uncontrolled, no theorizing beyond what the count rate shows`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
