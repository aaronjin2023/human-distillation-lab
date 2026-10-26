# Daniel Libeskind — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。引用建筑师本人文字时只引短句并注明出处。材料色板只写通用材料色名，不编造实测 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Daniel Libeskind: sharp angular shards, tilted walls and voided axes, zinc and concrete, a line of memory cutting through the plan, no right angle left unchallenged`
- ZH: 李伯斯金风格：尖锐的碎片体、倾斜的墙与虚空轴线，锌板与混凝土，一条记忆之线切开平面，没有一块直角不被挑战。

## (2) 空间与体量

- 体量：尖锐的碎片体、倾斜的墙、折线平面，拒绝正交盒子。`artifact`
- 空间序列：一条“虚空”（void）轴线贯穿全楼，参观流线被刻意打断，情绪由建筑控制。`artifact`
- 尺度：纪念性与压抑感并存，低矮入口与高耸中庭形成强烈反差。`impression`

## (3) 材料与色彩

- 色板（6 色，通用材料色名）：锌板灰、清水混凝土灰、裸钢黑、玻璃蓝、砖红、钛白。
- 主色锌板灰 + 清水混凝土灰；辅色玻璃蓝；禁色暖木大面积、柔和粉彩、古典石材贴面；冷色为主，明暗对比强烈，暗部是内容的一部分。注：柏林犹太博物馆外覆锌板，丹佛艺术博物馆外覆 9,000 块钛板，材料按项目区分，不混用。

## (4) 结构与构造

- 结构体系：钢框架 + 倾斜剪力墙，结构即叙事——斜墙、裂缝、悬挑本身就是表达。`artifact`
- 构造细节：墙体倾斜，裂缝即采光缝；屋顶为折线尖顶，不规则天窗缝切开屋面。`artifact`

## (5) 光线与环境

- 光源：窄缝天窗、斜切光束，室内多暗部，光如刀。`artifact`
- 环境关系：建筑如伤口般切入城市肌理，与旧建筑并置对话，不求融入。`impression`

## (6) 该设计什么 / 不该设计什么

- 该设计：尖锐碎片体、倾斜墙面、折线平面、贯穿的虚空轴线、窄缝天窗、锌板 / 钛板立面、断裂的参观流线、纪念性中庭。
- 不该设计：对称古典立面、直角盒子、平整幕墙、柔和曲线、装饰线脚、暖色木饰面。
- Negative prompt: `No symmetrical classical facade, no orthogonal glass box, no flat curtain wall, no applied ornament, no soft curves, no warm timber cladding`

## (7) 测试提示词示例（现代题材：现代城市街角的一座社区图书馆）

- Prompt: `In the style of Daniel Libeskind, a small community library on a modern city street corner, sharp angular zinc-clad shards, tilted walls, a narrow slit of light cutting through a dark reading hall, fragmented plan, no right angles`
- 中文对照：李伯斯金风格：现代城市街角的一座社区图书馆，尖锐的锌板碎片体，倾斜的墙，一道窄窄的光缝切开黑暗的阅览大厅，折线平面，没有直角。
- Negative: `No symmetrical facade, no orthogonal glass box, no flat curtain wall, no applied ornament, no soft curves, no warm timber cladding`
- 检验点：碎片角度是否尖锐而不被拉直；虚空轴线是否贯穿平面；光缝是否如刀而不是均匀采光。
