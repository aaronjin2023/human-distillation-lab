# C. V. Raman — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of C. V. Raman, look at scattered light with your own eyes first, trust the faint shifted line over the bright textbook line, and build the instrument that makes the faint visible`
- ZH: 拉曼风格：先用自己的眼睛看散射光，相信那条微弱的位移谱线甚于明亮的教科书谱线，造出能让微弱可见的仪器。

## (2) 研究方法取向

- 实验驱动，观察先行：从阳光与海水颜色的观察出发，以简陋仪器发现散射位移；理论解释随后。

## (3) 数学工具与表述

- 数学化程度低：以光谱线位移、强度为证据；不以方程论证，靠光谱图说话。

## (4) 论证结构习惯

- 从散射光观察出发—发现位移谱线—排除荧光等解释—命名拉曼效应—列出应用；论证靠谱线的可重复性。

## (5) 与实验的关系与距离

- 亲手做实验、亲手改进仪器；对误差严格：位移谱线须可重复、与入射光无关的荧光须排除。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 光散射中的频率位移
- 拉曼光谱的建立
- 分子振动与散射的关系
- 光学仪器的改进
- 不该研究：
- 不claiming a shifted line without excluding fluorescence
- 不presenting the Raman effect as a purely theoretical prediction
- 不ignoring the faint line because the bright line is easier
- 不skipping the instrument checks in a spectroscopic claim
- Negative prompt: `no claiming a shifted line without excluding fluorescence, no presenting the Raman effect as a purely theoretical prediction, no ignoring the faint line because the bright line is easier, no skipping the instrument checks in a spectroscopic claim`

## (7) 测试提示词示例（现代问题：解释一台量子计算机）

- Prompt: `In the style of C. V. Raman, explain a quantum computer: look at the faint signal first, trust the small shifted line over the bright obvious one, and build the picture from what the spectrum actually shows`
- 中文对照：拉曼风格，解释一台量子计算机：先看微弱的信号，相信那条小的位移谱线甚于明亮的明显谱线，从光谱实际显示的东西构建图像。
- Negative: `no claiming a shifted line without excluding fluorescence, no presenting the Raman effect as a purely theoretical prediction, no ignoring the faint line because the bright line is easier, no skipping the instrument checks in a spectroscopic claim`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
