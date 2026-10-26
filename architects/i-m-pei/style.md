# I. M. Pei — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。引用建筑师本人文字时只引短句并注明出处。材料色板只写通用材料色名，不编造实测 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of I. M. Pei: pure geometry, glass and stone in precise dialogue, light as structure, a pyramid or triangle resolving the impossible site`
- ZH: 贝聿铭风格：纯粹几何，玻璃与石材的精确对话，光即结构，金字塔或三角形解决不可能的场地。

## (2) 空间与体量

- 体量：纯几何体（金字塔、三角形、方形），精确。`artifact`
- 空间序列：几何轴线组织，中庭采光。`artifact`
- 尺度：纪念性与精确并存。`impression`

## (3) 材料与色彩

- 色板（6 色，通用材料色名）：玻璃蓝、石灰白、钢银、混凝土灰、木色、深灰。
- 主色玻璃蓝 + 石灰白；辅色钢银；禁色砖红、艳丽涂料、装饰线脚；冷色为主，精确而明亮。

## (4) 结构与构造

- 结构体系：钢框架 + 玻璃幕墙，几何即结构。`artifact`
- 构造细节：玻璃节点、钢构节点，毫米级精度。`artifact`

## (5) 光线与环境

- 光源：玻璃金字塔导光，室内光如天光。`artifact`
- 环境关系：几何体与历史环境对话（卢浮宫）。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：纯几何、玻璃金字塔、三角形平面、石材与玻璃对话、采光中庭、精确节点。
- 不该设计：曲线、装饰、砖墙、艳丽色彩、不对称杂乱。
- Negative prompt: `No curves, no applied ornament, no brick walls, no bright colours, no asymmetrical clutter, no fake antique cladding`

## (7) 测试提示词示例（现代题材：现代城市的一座地铁站入口小亭）

- Prompt: `In the style of I. M. Pei, a small subway station entrance pavilion in a modern city, a pure glass pyramid over a stone base, precise geometry, light pouring down into the hall, stone and glass in dialogue`
- 中文对照：贝聿铭风格：现代城市的一座地铁站入口小亭，石基座上的纯粹玻璃金字塔，精确的几何，光倾泻进大厅，石材与玻璃对话。
- Negative: `No curves, no applied ornament, no brick walls, no bright colours, no asymmetrical clutter, no fake antique cladding`
- 检验点：几何是否纯粹而不杂乱；玻璃与石材是否对话；光是否从几何中来。
