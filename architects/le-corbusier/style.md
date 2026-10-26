# Le Corbusier — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。色板只写通用材料色名，不编造实测 HEX 值。引用建筑师本人文字时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Le Corbusier: five points, pilotis, free plan, ribbon window, roof garden, raw concrete, Modulor proportion, no ornament, no pitched roof`
- ZH: 勒·柯布西耶风格：新建筑五点、底层架空柱、自由平面、横向长窗、屋顶花园、清水混凝土、模度比例，没有装饰，没有坡屋顶。

## (2) 空间与体量

体量以底层架空柱抬起，自由平面与横向长窗展开，屋顶花园收束；萨伏伊别墅以坡道组织空间，朗香教堂以厚墙与不规则开洞收束，马赛公寓以大体量加底层架空。尺度以模度（Modulor）取定。`artifact`

## (3) 材料与色彩

主材：钢筋混凝土、白色抹灰、玻璃、钢材；晚期以清水混凝土（粗野主义）为主。色板：白、混凝土灰、玻璃蓝、原色点缀（红、黄、蓝）；禁历史风格装饰。冷暖偏冷，晚期以混凝土的粗糙取胜。

## (4) 结构与构造

结构以钢筋混凝土框架为主，底层架空柱、自由平面、自由立面是结构宣言；朗香教堂以厚墙与壳体屋顶为结构，屋顶形式即结构。节点重在混凝土模板与开洞收边。`artifact`

## (5) 光线与环境

光线以横向长窗均匀引入，朗香教堂以不规则小窗与侧塔光缝形成神秘光影；萨伏伊别墅以坡道上的光线变化组织空间。

## (6) 该设计什么 / 不该设计什么

- 该设计：
- 底层架空柱（pilotis）
- 横向长窗与自由立面
- 屋顶花园
- 自由平面与坡道
- 清水混凝土与粗野质感
- 模度比例与原色点缀
- 不该设计：
- No applied ornament
- No pitched roof
- No symmetrical classical facade
- No small punched windows only
- No decorative mouldings
- Negative prompt: `No applied ornament, no pitched roof, no symmetrical classical facade, no small punched windows only, no decorative mouldings`

## (7) 测试提示词示例（现代题材：现代城市街角的一座社区图书馆）

- Prompt: `In the style of Le Corbusier, a small community library on a modern city street corner, pilotis lifting the volume, free plan, ribbon window, roof garden, raw concrete and white walls, ramp circulation, no ornament, architecture photography, soft daylight`
- 中文对照：勒·柯布西耶风格：现代城市街角的一座社区图书馆，底层架空柱抬起体量，自由平面，横向长窗，屋顶花园，清水混凝土与白墙，坡道流线，没有装饰。
- Negative: `No applied ornament, no pitched roof, no classical facade, no small punched windows only, no decorative mouldings`
- 检验点：架空柱与横向长窗是否出现；坡道与屋顶花园是否出现；有无装饰与坡屋顶混入。
