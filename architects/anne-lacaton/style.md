# Anne Lacaton — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。引用建筑师本人文字时只引短句并注明出处。材料色板只写通用材料色名，不编造实测 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Anne Lacaton: never demolish, generous space added lightly, winter gardens and balconies, polycarbonate and greenhouse lightness, ordinary buildings made generous`
- ZH: 拉卡顿风格：永不拆除，轻盈地加上慷慨的空间，冬季花园与阳台，聚碳酸酯与温室的轻盈，平凡建筑变得慷慨。

## (2) 空间与体量

- 体量：轻、通透、附加的冬季花园与阳台。`artifact`
- 空间序列：原有空间 + 附加的半室外层，流线自由，使用方式开放。`artifact`
- 尺度：慷慨的面积，住宅尺度放大而不豪华。`impression`

## (3) 材料与色彩

- 色板（6 色，通用材料色名）：聚碳酸酯透明白、钢银、混凝土灰、植物绿、玻璃蓝、木色。
- 主色聚碳酸酯透明白 + 混凝土灰；辅色植物绿；禁色艳丽涂料、豪华石材、装饰线脚；明亮通透，光即色彩。

## (4) 结构与构造

- 结构体系：轻钢附加结构，温室式围护，不压旧楼。`artifact`
- 构造细节：轻钢节点、聚碳酸酯围护收边，附加结构可拆。`artifact`

## (5) 光线与环境

- 光源：聚碳酸酯漫射光，室内明亮均匀。`artifact`
- 环境关系：保留既有建筑与住户，改造而非拆除，时间痕迹被保留。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：冬季花园、附加阳台、聚碳酸酯围护、保留既有结构、慷慨的额外面积、轻钢附加、住户不搬迁。
- 不该设计：拆除重建、豪华饰面、封闭立面、装饰、缩小面积、驱逐住户。
- Negative prompt: `No demolition and rebuild, no luxury cladding, no sealed facades, no applied ornament, no reduction of living space, no displacement of residents`

## (7) 测试提示词示例（现代题材：现代城市街角一座旧图书馆的改造）

- Prompt: `In the style of Anne Lacaton, the transformation of an old community library on a modern city street corner, keep the existing structure, add a light polycarbonate winter garden and balconies, generous new reading space, nothing demolished`
- 中文对照：拉卡顿风格：现代城市街角一座旧图书馆的改造，保留既有结构，加上轻盈的聚碳酸酯冬季花园与阳台，慷慨的新阅览空间，什么都不拆除。
- Negative: `No demolition and rebuild, no luxury cladding, no sealed facades, no applied ornament, no reduction of space, no displacement of users`
- 检验点：既有结构是否保留；附加空间是否轻盈慷慨；是否“只加不拆”。
