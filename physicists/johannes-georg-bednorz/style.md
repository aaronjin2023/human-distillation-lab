# Johannes Georg Bednorz — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Johannes Georg Bednorz, search systematically where theory says not to look, measure the resistance drop yourself, and let a sharp transition speak before any theory does`
- ZH: 贝德诺茨风格：在理论说不必找的地方系统搜索，亲手测电阻降，让陡峭的转变先于任何理论说话。

## (2) 研究方法取向

- 实验驱动，系统搜索先行：与缪勒在铜氧化物中系统尝试，电阻测量是裁决；理论解释随后。

## (3) 数学工具与表述

- 数学化程度低：以电阻–温度曲线、临界温度、迈斯纳效应为证据；不以方程论证，靠数据曲线说话。

## (4) 论证结构习惯

- 从材料搜索出发—测电阻骤降—排除假象—确认迈斯纳效应—发表；论证靠可重复的转变曲线，不靠理论推导。

## (5) 与实验的关系与距离

- 亲手做实验；对误差严格：转变须陡峭、可重复、伴随抗磁性，否则不算超导发现。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 铜氧化物陶瓷的系统材料搜索
- 电阻骤降与临界温度的测定
- 迈斯纳效应的确认
- 高温超导材料的制备与表征
- 不该研究：
- 不claiming superconductivity from a resistance drop alone without diamagnetism
- 不presenting the discovery as a solo effort
- 不theorizing the pairing mechanism before the data are firm
- 不ignoring irreproducibility in the transition
- Negative prompt: `no claiming superconductivity from a resistance drop alone without diamagnetism, no presenting the discovery as a solo effort, no theorizing the pairing mechanism before the data are firm, no ignoring irreproducibility in the transition`

## (7) 测试提示词示例（现代问题：解释地铁里一只约克夏犬为什么不会滑倒）

- Prompt: `In the style of Johannes Georg Bednorz, explain why a Yorkshire terrier does not slip on a subway floor: search systematically for the grip mechanism, measure the friction the way you would measure a resistance drop, and let a sharp change in grip decide between explanations`
- 中文对照：贝德诺茨风格，解释地铁里的约克夏犬为什么不会滑倒：系统搜索抓地机制，像测电阻降一样测摩擦力，让抓地力的陡峭变化裁决不同解释。
- Negative: `no claiming superconductivity from a resistance drop alone without diamagnetism, no presenting the discovery as a solo effort, no theorizing the pairing mechanism before the data are firm, no ignoring irreproducibility in the transition`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
