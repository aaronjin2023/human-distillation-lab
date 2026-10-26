# Katherine T. Faber — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Katherine Faber, toughen a brittle ceramic by deflecting its cracks: choose second-phase particles by shape and spacing, measure real crack tortuosity from images, and let the twist of the crack front do the work`
- ZH: 法伯方法：用裂纹偏转增韧脆性陶瓷——按颗粒形貌与间距选第二相，从图像实测裂纹迂曲度，让裂纹前沿的扭转来做功。

## (2) 合成路线偏好

- 两相陶瓷烧结：基体粉末 + 第二相颗粒（球形、棒状、片状），控制粒径分布窄、体积分数与间距；热压 / 无压烧结，烧结温度与气氛按基体（氧化铝、碳化硅、莫来石）定。 `artifact`

## (3) 表征手段组合

- 断裂韧性测试（SENB / 压痕法）先行于机理解释；光学与电子显微成像实测裂纹偏转角与扭转角，直接输入模型；XRD 与 SEM 看界面与第二相分布。 `artifact`

## (4) 理论模型与图表风格

- Faber–Evans 模型：裂纹偏转（倾斜 + 扭转）降低裂纹尖端应力强度因子；棒状高长径比颗粒最有效，扭转分量主导增韧；能量释放率与平直裂纹对比量化增韧倍数。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住断裂韧性与裂纹偏转带来的有效延性；可牺牲部分强度与各向同性；热障涂层应用中保住热稳定性，牺牲致密度。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 按颗粒形貌（球 / 棒 / 片）、长径比、间距与体积分数设计第二相
- 从显微图像实测裂纹迂曲度与偏转角、扭转角，再输入模型
- 用能量释放率与平直裂纹对比，量化增韧倍数
- 热失配应变与界面微开裂阻力一起算，不只算颗粒尺寸
- 不该做：方法上的禁区——no toughness claim without measured crack deflection angles；no assuming equiaxed grains toughen as much as high-aspect-ratio rods；no ignoring particle spacing and size distribution；no reporting strength without fracture toughness。
- Negative prompt: `no toughness claim without measured crack deflection angles, no assuming equiaxed grains toughen as much as high-aspect-ratio rods, no ignoring particle spacing and size distribution, no reporting strength without fracture toughness`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Katherine Faber, design a flexible conductive ceramic-polymer composite for a wearable device: choose rod-shaped second-phase particles to deflect cracks, measure real crack tortuosity from images, and quantify toughness gain against a flat crack before claiming durability`
- 中文对照：法伯方法，为可穿戴设备设计柔性导电陶瓷-聚合物复合材料：选棒状第二相颗粒偏转裂纹，从图像实测裂纹迂曲度，先与平直裂纹对比量化增韧倍数，再谈耐久性。
- Negative: `no toughness claim without measured crack deflection angles, no assuming equiaxed grains toughen as much as high-aspect-ratio rods, no ignoring particle spacing and size distribution, no reporting strength without fracture toughness`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
