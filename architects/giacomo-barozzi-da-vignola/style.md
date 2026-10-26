# Giacomo Barozzi da Vignola — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。材料色只写通用材料色名，不编造实测 HEX 值。引用建筑师本人文字时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Giacomo Barozzi da Vignola: Jesuit church with a wide barrel-vaulted nave, five orders by rule, side chapels as a row, volute facade, stone and stucco, calm Mannerist order, no Gothic detail, no excess ornament`
- ZH: 维尼奥拉风格：耶稣会教堂，宽阔筒形拱顶中厅，五柱式成法，侧礼拜堂成排，涡卷立面，石与灰泥，矫饰主义的宁静秩序，无哥特细部，无多余装饰。

## (2) 空间与体量

- 体量：纵深中厅、穹顶居中；空间序列：入口—中厅—穹顶—圣坛，纵轴一贯到底；尺度：中厅宽阔，侧堂低矮，对比强烈。 `impression`

## (3) 材料与色彩

- 主材：石、砖、灰泥；色板：石灰灰、大理石白、赭石；禁色：不大面积涂彩。 `impression`

## (4) 结构与构造

- 结构：筒形拱顶中厅，侧礼拜堂成排承托；五柱式成法是其设计工具，柱式皆有定则。 `verbatim` / `artifact`

## (5) 光线与环境

- 光线：中厅明亮，侧堂幽暗，明暗对比引导视线到圣坛；环境：城市教堂，立面即街道界面。 `impression`

## (6) 该设计什么 / 不该设计什么

- 该设计：宽阔筒形拱顶中厅、五柱式成法、侧礼拜堂成排、涡卷立面、纵深中厅与穹顶。`verbatim`
- 不该设计：哥特尖拱、多余装饰、不对称平面、铁构与玻璃。
- Negative prompt: `No Gothic pointed arches, no excess ornament, no asymmetrical plan, no iron frame, no glass curtain wall`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Giacomo Barozzi da Vignola, a small community library on a modern city street corner, wide barrel-vaulted hall, five orders by rule, side rooms as a row of chapels, volute facade, stone and white stucco`
- 中文对照：维尼奥拉风格：现代城市街角的一座社区图书馆，宽阔筒形拱顶大厅，五柱式成法，侧室成排如礼拜堂，涡卷立面，石与白灰泥。
- Negative: `No Gothic pointed arches, no excess ornament, no asymmetrical plan, no iron frame, no glass curtain wall`
- 检验点：母题是否出现（宽阔筒形拱顶中厅、五柱式成法、侧礼拜堂成排、涡卷立面、纵深中厅与穹顶）；禁区是否避开（哥特尖拱、多余装饰、不对称平面、铁构与玻璃）；空间、材料、结构是否仍是此人的语言，而不是通用现代建筑。
