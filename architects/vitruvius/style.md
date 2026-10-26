# Vitruvius — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。材料色只写通用材料色名，不编造实测 HEX 值。引用建筑师本人文字时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Vitruvius: Roman basilica and theatre in stone and brick, orders with correct proportions, firmitas utilitas venustas, human body as measure, symmetrical plan, no excess ornament, no iron frame`
- ZH: 维特鲁威风格：罗马巴西利卡与剧场，石与砖，柱式比例正确，坚固、适用、美观三原则，人体为尺度，对称平面，无多余装饰，无铁构。

## (2) 空间与体量

- 体量：巴西利卡长方形大厅，柱廊环绕；空间序列：入口—柱廊—大厅—后殿，轴线清晰；尺度：人体比例为模数，柱高、柱距皆有数比。 `impression`

## (3) 材料与色彩

- 主材：石、砖、混凝土；色板：石灰暖灰、砖红、大理石白；禁色：不大面积涂彩，不用金色。 `impression`

## (4) 结构与构造

- 结构：梁柱与拱券并用，罗马混凝土与砖石砌体；柱式（多立克、爱奥尼、科林斯）各有定则。 `verbatim` / `artifact`

## (5) 光线与环境

- 光线：高侧窗与柱廊进光，大厅明亮均匀；环境：城市公共建筑，顺应广场与街道轴线。 `impression`

## (6) 该设计什么 / 不该设计什么

- 该设计：坚固、适用、美观三原则、人体比例与柱式模数、巴西利卡长方形大厅、柱廊与高侧窗、罗马剧场半圆形看台。`verbatim`
- 不该设计：无比例的装饰、铁构与玻璃、不对称平面、曲面穹顶为主角。
- Negative prompt: `No unproportioned ornament, no iron frame, no glass curtain wall, no asymmetrical plan, no dome as the main feature`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Vitruvius, a small community library on a modern city street corner, Roman basilica hall in stone and brick, correct Doric proportions, colonnade and clerestory light, symmetrical plan, human body as measure`
- 中文对照：维特鲁威风格：现代城市街角的一座社区图书馆，石与砖的罗马巴西利卡大厅，多立克比例正确，柱廊与高侧窗采光，对称平面，人体为尺度。
- Negative: `No unproportioned ornament, no iron frame, no glass curtain wall, no asymmetrical plan`
- 检验点：母题是否出现（坚固、适用、美观三原则、人体比例与柱式模数、巴西利卡长方形大厅、柱廊与高侧窗、罗马剧场半圆形看台）；禁区是否避开（无比例的装饰、铁构与玻璃、不对称平面、曲面穹顶为主角）；空间、材料、结构是否仍是此人的语言，而不是通用现代建筑。
