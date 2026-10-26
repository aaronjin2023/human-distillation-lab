# Charles Goodyear — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Charles Goodyear, cure the rubber with heat and sulfur: crosslink the chains until the gum stops melting in summer and cracking in winter, and let the cured sample prove it`
- ZH: 固特异方法：用硫与热硫化橡胶——交联链段，直到胶料夏天不熔、冬天不裂，让硫化后的样品证明。

## (2) 合成路线偏好

- 硫化：天然橡胶 + 硫 + 热（约 140 °C 量级，依配方而定），交联；混炼、成型、硫化三步；控硫用量与硫化时间。 `artifact`

## (3) 表征手段组合

- 力学测试（拉伸、弹性回复）；热测试（高温不熔、低温不脆）；溶胀测交联度；外观与耐久观察。 `artifact`

## (4) 理论模型与图表风格

- 硫化交联：硫桥连接橡胶链，形成三维网络；交联度决定弹性与耐热性；未硫化橡胶为热塑性，硫化后为热固性弹性体。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住硫化后的弹性与温度稳定性；可牺牲加工便利性；橡胶保住耐久，牺牲可重塑性。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 硫用量、硫化温度、硫化时间三者一起报
- 用高温不熔与低温不裂两项测试验证硫化
- 交联度用溶胀法测，不只凭手感
- 先做小样验证配方，再放大
- 不该做：方法上的禁区——no vulcanization claim without heat and sulfur conditions；no calling unvulcanized gum a usable rubber；no reporting elasticity without temperature tests；no claiming durability from a single sample。
- Negative prompt: `no vulcanization claim without heat and sulfur conditions, no calling unvulcanized gum a usable rubber, no reporting elasticity without temperature tests, no claiming durability from a single sample`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Charles Goodyear, design a flexible conductive rubber for a wearable device: crosslink the rubber with sulfur and heat first, prove it neither melts in heat nor cracks in cold, and measure crosslink density by swelling before claiming durability`
- 中文对照：固特异方法，为可穿戴设备设计柔性导电橡胶：先用硫与热交联，验证高温不熔、低温不裂，用溶胀法测交联度，确认耐久性后再谈材料。
- Negative: `no vulcanization claim without heat and sulfur conditions, no calling unvulcanized gum a usable rubber, no reporting elasticity without temperature tests, no claiming durability from a single sample`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
