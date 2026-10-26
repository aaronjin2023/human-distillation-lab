# Christopher Wren — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。材料色只写通用材料色名，不编造实测 HEX 值。引用建筑师本人文字时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Christopher Wren: great dome on a drum with a lantern, classical portico and towers, stone in Portland white, calm English Baroque order, no Gothic pointed arches, no iron frame`
- ZH: 雷恩风格：鼓座上的大穹顶配采光塔，古典门廊与塔楼，波特兰白石，宁静英国巴洛克秩序，无哥特尖拱，无铁构。

## (2) 空间与体量

- 体量：穹顶高耸、双塔立面；空间序列：门廊—中厅—穹顶—圣坛，纵轴清晰；尺度：纪念性尺度，穹顶即伦敦天际线。 `impression`

## (3) 材料与色彩

- 主材：波特兰石、砖；色板：白石、石灰灰；禁色：不大面积涂彩。 `impression`

## (4) 结构与构造

- 结构：三层穹顶（内穹顶、砖锥、外穹顶），塔楼与门廊承托；圣保罗的三层穹顶是其结构发明。 `verbatim` / `artifact`

## (5) 光线与环境

- 光线：穹顶采光塔与高侧窗，光线均匀；环境：伦敦城市制高点，穹顶即城市地标。 `impression`

## (6) 该设计什么 / 不该设计什么

- 该设计：三层穹顶与采光塔、古典门廊与双塔立面、波特兰白石、纵轴中厅、穹顶天际线。`verbatim`
- 不该设计：哥特尖拱、铁构与玻璃、多余装饰、不对称立面。
- Negative prompt: `No Gothic pointed arches, no iron frame, no glass curtain wall, no excess ornament, no asymmetrical facade`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Christopher Wren, a small community library on a modern city street corner, great dome on a drum with a lantern in Portland white stone, classical portico and twin towers, calm English Baroque order`
- 中文对照：雷恩风格：现代城市街角的一座社区图书馆，波特兰白石鼓座大穹顶配采光塔，古典门廊与双塔立面，宁静英国巴洛克秩序。
- Negative: `No Gothic pointed arches, no iron frame, no glass curtain wall, no excess ornament, no asymmetrical facade`
- 检验点：母题是否出现（三层穹顶与采光塔、古典门廊与双塔立面、波特兰白石、纵轴中厅、穹顶天际线）；禁区是否避开（哥特尖拱、铁构与玻璃、多余装饰、不对称立面）；空间、材料、结构是否仍是此人的语言，而不是通用现代建筑。
