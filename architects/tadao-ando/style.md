# Tadao Ando — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。引用建筑师本人文字时只引短句并注明出处。材料色板只写通用材料色名，不编造实测 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tadao Ando: exposed fair-faced concrete, minimal geometric volumes, a single slit of light, quiet enclosed courtyard, water and shadow as materials, no ornament`
- ZH: 安藤忠雄风格：清水混凝土，极简几何体块，一道光缝，安静的围合庭院，水与影即材料，没有装饰。

## (2) 空间与体量

- 体量：清水混凝土盒子，几何纯粹。`artifact`
- 空间序列：围墙—庭院—室内，封闭而后开。`artifact`
- 尺度：人体尺度，克制。`impression`

## (3) 材料与色彩

- 色板（5 色，通用材料色名）：清水混凝土灰、光影白、水色、木色、玻璃蓝。
- 主色清水混凝土灰 + 光影白；辅色水色；禁色彩色涂料、装饰、砖墙；灰与白为主，光即色彩。

## (4) 结构与构造

- 结构体系：清水混凝土墙承重。`artifact`
- 构造细节：混凝土模板、光缝节点、收边做法，模板精度即建筑精度。`artifact`

## (5) 光线与环境

- 光源：一字光缝、天窗，暗与亮的对比。`artifact`
- 环境关系：围墙隔绝城市，内部见自然（阳光与风）。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：清水混凝土、光缝、围合庭院、水面、几何盒子、极简。
- 不该设计：彩色涂料、装饰、坡屋顶、砖墙、玻璃幕墙。
- Negative prompt: `No coloured cladding, no applied ornament, no pitched roofs, no brick walls, no glass curtain walls, no decorative mouldings`

## (7) 测试提示词示例（现代题材：现代城市街角的一座社区图书馆）

- Prompt: `In the style of Tadao Ando, a small community library on a modern city street corner, exposed fair-faced concrete walls, a single vertical slit of light, quiet enclosed courtyard with still water, minimal geometric volume, no ornament, architecture photography, soft daylight`
- 中文对照：安藤忠雄风格：现代城市街角的一座社区图书馆，清水混凝土墙，一道垂直光缝，安静的围合庭院与静水，极简几何体块，没有装饰，建筑摄影，柔和日光。
- Negative: `No coloured cladding, no applied ornament, no pitched roofs, no brick walls, no glass curtain walls, no decorative mouldings`
- 检验点：混凝土是否清水而不贴面；光缝是否一道而不泛滥；庭院是否围合而安静。
