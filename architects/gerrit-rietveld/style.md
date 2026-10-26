# Gerrit Rietveld — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。色板只写通用材料色名，不编造实测 HEX 值。引用建筑师本人文字时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gerrit Rietveld: De Stijl planes in red yellow blue black white, sliding walls, open corner windows, primary colour accents on white, no ornament, no pitched roof`
- ZH: 里特维尔德风格：风格派红黄蓝黑白平面、可移动隔墙、开放角窗、白底上的原色点缀，没有装饰，没有坡屋顶。

## (2) 空间与体量

体量为水平与垂直平面的自由组合，施罗德住宅上层以可移动隔墙实现可变平面，角窗一开即去掉墙角；梵高博物馆以矩形体量与窗格网格组织。空间序列由平面滑动与开合取定。`artifact`

## (3) 材料与色彩

主材：白色抹灰、钢材、玻璃、木材；色彩以红、黄、蓝原色作点缀。色板：白、黑、红、黄、蓝；禁石材纪念性与繁复装饰。冷暖偏冷，以原色的跳跃取胜。

## (4) 结构与构造

结构以钢框架与砌体为主，施罗德住宅的悬挑与角窗以钢构实现；屋顶为平屋顶，节点重在平面交接与可移动隔墙轨道。`artifact`

## (5) 光线与环境

光线以大窗与角窗引入，室内以白墙反射提亮；施罗德住宅上层隔墙一移，光线与空间同时变化，角窗打开后室内外贯通。

## (6) 该设计什么 / 不该设计什么

- 该设计：
- 红黄蓝黑白的风格派平面
- 可移动隔墙与可变平面
- 开放角窗：窗一开墙角即消失
- 白色底面上的原色点缀
- 水平与垂直平面的自由组合
- 平屋顶与悬挑体量
- 不该设计：
- No applied ornament
- No pitched roof
- No symmetrical classical facade
- No stone monumentality
- No fixed heavy partitions
- Negative prompt: `No applied ornament, no pitched roof, no symmetrical classical facade, no stone monumentality, no fixed heavy partitions`

## (7) 测试提示词示例（现代题材：一座建在山坡上的小住宅）

- Prompt: `In the style of Gerrit Rietveld, a small house on a hillside in a modern city, De Stijl planes in red yellow blue black and white, sliding walls, open corner windows, flat roof, no ornament, architecture photography, soft daylight`
- 中文对照：里特维尔德风格：现代城市山坡上的一座小住宅，风格派红黄蓝黑白平面，可移动隔墙，开放角窗，平屋顶，没有装饰。
- Negative: `No applied ornament, no pitched roof, no classical facade, no stone monumentality, no fixed heavy partitions`
- 检验点：原色平面与角窗是否出现；隔墙是否可移动；有无装饰与坡屋顶混入。
