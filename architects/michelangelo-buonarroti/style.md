# Michelangelo Buonarroti — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。材料色只写通用材料色名，不编造实测 HEX 值。引用建筑师本人文字时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Michelangelo the architect: massive dome on a tall drum, giant order pilasters, sculptural stair and vestibule, trapezoidal piazza, stone with strong chiaroscuro, no Gothic detail, no light iron frame`
- ZH: 米开朗基罗（建筑部分）风格：高鼓座上的巨大穹顶，巨柱式壁柱，雕塑感楼梯与前厅，梯形广场，石材明暗对比强烈，无哥特细部，无轻质铁构。

## (2) 空间与体量

- 体量：穹顶高耸、体量雄浑；空间序列：楼梯—前厅—阅览室（劳伦齐亚纳），广场—台阶—市政厅（卡比托利欧）；尺度：巨柱式压倒人体尺度，楼梯如雕塑。 `impression`

## (3) 材料与色彩

- 主材：石、砖、灰泥；色板：石灰灰、大理石白、深灰阴影；禁色：不大面积涂彩。 `impression`

## (4) 结构与构造

- 结构：穹顶双壳与鼓座，巨柱式壁柱承托檐部；劳伦齐亚纳楼梯以石阶的雕塑感组织流线。 `verbatim` / `artifact`

## (5) 光线与环境

- 光线：穹顶窗环与高侧窗，明暗对比强烈；环境：卡比托利欧广场以梯形收束城市视线。 `impression`

## (6) 该设计什么 / 不该设计什么

- 该设计：高鼓座巨大穹顶、巨柱式壁柱、雕塑感楼梯、梯形广场、强烈的明暗对比。`verbatim`
- 不该设计：哥特尖拱、轻质铁构、琐碎装饰、平淡对称。
- Negative prompt: `No Gothic pointed arches, no light iron frame, no fussy ornament, no flat symmetry, no glass curtain wall`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Michelangelo the architect, a small community library on a modern city street corner, massive dome on a tall drum, giant order pilasters, sculptural stone stair, trapezoidal forecourt, strong chiaroscuro in stone`
- 中文对照：米开朗基罗（建筑部分）风格：现代城市街角的一座社区图书馆，高鼓座巨大穹顶，巨柱式壁柱，雕塑感石楼梯，梯形前院，石材明暗对比强烈。
- Negative: `No Gothic pointed arches, no light iron frame, no fussy ornament, no flat symmetry, no glass curtain wall`
- 检验点：母题是否出现（高鼓座巨大穹顶、巨柱式壁柱、雕塑感楼梯、梯形广场、强烈的明暗对比）；禁区是否避开（哥特尖拱、轻质铁构、琐碎装饰、平淡对称）；空间、材料、结构是否仍是此人的语言，而不是通用现代建筑。
