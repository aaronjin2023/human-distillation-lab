# Walter Gropius — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。色板只写通用材料色名，不编造实测 HEX 值。引用建筑师本人文字时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Walter Gropius: Bauhaus glass curtain wall, cubic workshop volumes, steel and glass, flat roof, functional plan, no ornament, no historical style`
- ZH: 格罗皮乌斯风格：包豪斯玻璃幕墙、立方车间体量、钢与玻璃、平屋顶、功能平面，没有装饰，没有历史风格。

## (2) 空间与体量

体量为功能分区的立方体群，车间、宿舍、食堂各以体量表达功能，玻璃幕墙转角无柱；空间序列由桥体连接各功能块，流线即功能分区。`artifact`

## (3) 材料与色彩

主材：钢、玻璃、钢筋混凝土、白色抹灰。色板：白、钢灰、玻璃蓝、黑；禁历史风格的石材装饰与彩色涂料。冷暖偏冷，以玻璃的通透取胜。

## (4) 结构与构造

结构以钢框架与钢筋混凝土为主，玻璃幕墙挂于框架之外，转角玻璃无柱是结构宣言；屋顶为平屋顶，节点重在钢窗与幕墙收边。`artifact`

## (5) 光线与环境

光线以大面积玻璃幕墙引入，车间以均匀漫射光为主；玻璃的通透即包豪斯的光线语言，室内外视线贯通。

## (6) 该设计什么 / 不该设计什么

- 该设计：
- 玻璃幕墙与无柱转角
- 功能分区的立方体群
- 钢框架与平屋顶
- 桥体连接的功能块
- 白色抹灰与钢窗的组合
- 车间大窗与均匀漫射光
- 不该设计：
- No applied ornament
- No historical stone facade
- No pitched roof
- No symmetrical classical plan
- No coloured stucco decoration
- Negative prompt: `No applied ornament, no historical stone facade, no pitched roof, no symmetrical classical plan, no coloured stucco decoration`

## (7) 测试提示词示例（现代题材：现代城市街角的一座社区图书馆）

- Prompt: `In the style of Walter Gropius, a small community library on a modern city street corner, cubic volumes by function, glass curtain wall with corner glazing, steel frame, flat roof, white walls, no ornament, architecture photography, soft daylight`
- 中文对照：格罗皮乌斯风格：现代城市街角的一座社区图书馆，按功能分区的立方体量，玻璃幕墙与无柱转角，钢框架，平屋顶，白墙，没有装饰。
- Negative: `No applied ornament, no historical stone facade, no pitched roof, no classical plan, no coloured stucco`
- 检验点：玻璃幕墙转角是否无柱；体量是否按功能分区；有无历史风格装饰混入。
