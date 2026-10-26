# Hassan Fathy — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。引用建筑师本人文字时只引短句并注明出处。材料色板只写通用材料色名，不编造实测 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hassan Fathy: mud brick and domes, courtyards that breathe, a village built by its own hands, architecture for the poor`
- ZH: 哈桑·法赛风格：土坯与穹顶，会呼吸的庭院，村民亲手建起的村庄，为穷人建筑。

## (2) 空间与体量

- 体量：土坯穹顶、庭院、低矮。`artifact`
- 空间序列：庭院—拱廊—室内，通风序列。`artifact`
- 尺度：村落尺度。`impression`

## (3) 材料与色彩

- 色板（5 色，通用材料色名）：土黄、泥砖色、石灰白、木色、黛瓦灰。
- 主色土黄 + 石灰白；辅色木色；禁色混凝土大体量、玻璃幕墙、艳丽涂料；土黄为主，就地即色彩。

## (4) 结构与构造

- 结构体系：土坯、穹顶、拱。`artifact`
- 构造细节：穹顶砌法、筒拱、风塔。`artifact`

## (5) 光线与环境

- 光源：庭院光、穹顶光。`artifact`
- 环境关系：与沙漠气候共生，通风与遮阳。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：土坯、穹顶、筒拱、庭院、风塔、就地材料、村民共建。
- 不该设计：混凝土大体量、玻璃盒子、艳丽涂料、空调依赖、高层。
- Negative prompt: `No concrete masses, no glass boxes, no bright paint, no air-conditioning dependence, no high-rise blocks, no applied ornament`

## (7) 测试提示词示例（现代题材：城市边缘的一座乡村小学）

- Prompt: `In the style of Hassan Fathy, a small village primary school on a modern city edge, mud brick domes and vaults, courtyards that breathe, wind towers, built with local earth by the community, no concrete mass`
- 中文对照：哈桑·法赛风格：城市边缘的一座乡村小学，土坯穹顶与筒拱，会呼吸的庭院，风塔，社区用当地土亲手建造，没有混凝土大体量。
- Negative: `No concrete masses, no glass boxes, no bright paint, no air-conditioning dependence, no high-rise blocks, no applied ornament`
- 检验点：土坯与穹顶是否成立；庭院是否通风；建筑是否由社区共建而非空降。
