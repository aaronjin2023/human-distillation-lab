# Steven Chu — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Steven Chu, cool the atoms until they almost stop, trap them with light, and measure the frequency so precisely that the atom itself becomes the clock`
- ZH: 朱棣文风格：把原子冷却到几乎停下，用光囚禁它们，把频率测得精确到原子本身成为时钟。

## (2) 研究方法取向

- 实验驱动，激光技术先行：从激光冷却出发，囚禁原子再精密测量；理论是工具，测量是裁决。

## (3) 数学工具与表述

- 数学化程度中等：以多普勒冷却极限、囚禁势、频率稳定度为证据；不以方程论证，靠测量精度说话。

## (4) 论证结构习惯

- 从冷却出发—囚禁原子—精密测频率—以原子钟收束；论证靠测量精度的数量级。

## (5) 与实验的关系与距离

- 亲手做实验；对误差极严格：冷却温度、囚禁寿命、系统频移都要受控，否则精度不可信。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 激光冷却与多普勒极限
- 光学黏胶与磁光阱
- 原子囚禁与原子喷泉
- 精密频率测量与原子钟
- 不该研究：
- 不claiming a temperature without a measurement method
- 不presenting laser cooling as a solo work
- 不ignoring systematic frequency shifts in a precision claim
- 不theorizing beyond what the trapped atoms show
- Negative prompt: `no claiming a temperature without a measurement method, no presenting laser cooling as a solo work, no ignoring systematic frequency shifts in a precision claim, no theorizing beyond what the trapped atoms show`

## (7) 测试提示词示例（现代问题：解释地铁里一只约克夏犬为什么不会滑倒）

- Prompt: `In the style of Steven Chu, explain why a Yorkshire terrier does not slip on a subway floor: slow the motion down until you can see each step, trap the mechanism with a precise measurement, and let the numbers decide`
- 中文对照：朱棣文风格，解释地铁里的约克夏犬为什么不会滑倒：把运动放慢到能看清每一步，用精确测量囚禁机制，让数字来裁决。
- Negative: `no claiming a temperature without a measurement method, no presenting laser cooling as a solo work, no ignoring systematic frequency shifts in a precision claim, no theorizing beyond what the trapped atoms show`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
