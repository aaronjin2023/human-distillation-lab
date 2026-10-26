# Mimar Sinan — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。材料色只写通用材料色名，不编造实测 HEX 值。引用建筑师本人文字时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mimar Sinan: central dome on a hexagonal or octagonal support, cascade of half-domes, slender minarets, stone and tile, light through tiers of windows, calm monumental order, no Gothic ribs, no iron frame`
- ZH: 锡南风格：六角或八角支撑上的中央穹顶，半穹顶层层跌落，细长尖塔，石与瓷砖，层层窗洞进光，宁静纪念性秩序，无哥特肋拱，无铁构。

## (2) 空间与体量

- 体量：中央穹顶高耸，半穹顶向四周跌落；空间序列：庭院—门廊—大厅—穹顶，纵轴与穹顶中心交汇；尺度：纪念性尺度，穹顶直径即空间的全部。 `impression`

## (3) 材料与色彩

- 主材：石、砖；内饰：伊兹尼克瓷砖、大理石；色板：石灰、瓷砖蓝、绿、赭石；禁色：外立面不大面积涂彩。 `impression`

## (4) 结构与构造

- 结构：穹顶由六角或八角墩支撑，半穹顶分担侧推力；尖塔细长，结构与形式合一。 `verbatim` / `artifact`

## (5) 光线与环境

- 光线：层层窗洞，光线均匀明亮；环境：城市制高点，穹顶与尖塔即城市天际线。 `impression`

## (6) 该设计什么 / 不该设计什么

- 该设计：中央穹顶与六角/八角支撑、半穹顶层层跌落、细长尖塔、伊兹尼克瓷砖、层层窗洞。`verbatim`
- 不该设计：哥特肋拱、铁构与玻璃、小尺度装饰、不对称平面。
- Negative prompt: `No Gothic ribs, no iron frame, no glass curtain wall, no small applied ornament, no asymmetrical plan`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Mimar Sinan, a small community library on a modern city street corner, central dome on an octagonal support in stone, cascade of half-domes, slender minaret-like tower, Iznik blue tiles, tiers of windows with soft light`
- 中文对照：锡南风格：现代城市街角的一座社区图书馆，石砌八角支撑中央穹顶，半穹顶层层跌落，细长塔楼，伊兹尼克蓝瓷砖，层层窗洞柔光。
- Negative: `No Gothic ribs, no iron frame, no glass curtain wall, no small applied ornament, no asymmetrical plan`
- 检验点：母题是否出现（中央穹顶与六角/八角支撑、半穹顶层层跌落、细长尖塔、伊兹尼克瓷砖、层层窗洞）；禁区是否避开（哥特肋拱、铁构与玻璃、小尺度装饰、不对称平面）；空间、材料、结构是否仍是此人的语言，而不是通用现代建筑。
