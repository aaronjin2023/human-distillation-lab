# Iktinos — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。材料色只写通用材料色名，不编造实测 HEX 值。引用建筑师本人文字时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Iktinos: Doric peristyle temple in Pentelic marble, subtle optical refinements, entasis and curvature, calm monumental colonnade, no arches, no domes, no applied colour beyond restrained polychromy`
- ZH: 伊克蒂诺斯风格：彭特利大理石多立克围柱神庙，精微视错觉修正，柱身收分与台基微曲，庄重纪念性柱廊，无拱、无穹顶，彩绘克制。

## (2) 空间与体量

- 体量：长方形围柱式，水平舒展而庄重；空间序列：台阶—柱廊—前廊—内殿，仪式轴线居中；尺度：柱高与柱距按多立克比例，台基与柱身均有肉眼难察的微曲修正。 `impression`

## (3) 材料与色彩

- 主材：彭特利大理石，精细打磨；色板：大理石白、暖灰、赭石（彩绘残迹）、深蓝（局部）；禁色：不大面积涂彩，不用金色贴面。 `impression`

## (4) 结构与构造

- 结构：梁柱体系，大理石梁跨柱距，柱身收分（entasis）与角柱加粗；无拱，靠石梁与榫卯节点。 `verbatim` / `artifact`

## (5) 光线与环境

- 光线：柱廊光影节奏是主角——柱影随日照移动；内殿幽暗，仅东门进光；环境：立于卫城高台，顺应地形，远望即城市地标。 `impression`

## (6) 该设计什么 / 不该设计什么

- 该设计：多立克围柱与柱廊、柱身收分与台基微曲等视错觉修正、三角楣与檐部、大理石台阶与柱基、长方形内殿与前廊。`verbatim`
- 不该设计：拱与穹顶、爱奥尼涡卷的繁复、大面积彩绘、不对称平面。
- Negative prompt: `No arches, no domes, no large areas of polychromy, no asymmetrical plan, no applied ornament, no glass or steel`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Iktinos, a small community library on a modern city street corner, Doric peristyle in white marble, subtle entasis on the columns, stepped platform, calm colonnade with moving shadows, restrained colour`
- 中文对照：伊克蒂诺斯风格：现代城市街角的一座社区图书馆，白色大理石多立克围柱，柱身微收分，阶梯台基，柱廊光影节奏，色彩克制。
- Negative: `No arches, no domes, no large areas of polychromy, no asymmetrical plan, no glass curtain wall`
- 检验点：母题是否出现（多立克围柱与柱廊、柱身收分与台基微曲等视错觉修正、三角楣与檐部、大理石台阶与柱基、长方形内殿与前廊）；禁区是否避开（拱与穹顶、爱奥尼涡卷的繁复、大面积彩绘、不对称平面）；空间、材料、结构是否仍是此人的语言，而不是通用现代建筑。
