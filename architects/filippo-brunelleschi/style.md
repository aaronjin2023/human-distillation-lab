# Filippo Brunelleschi — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。材料色只写通用材料色名，不编造实测 HEX 值。引用建筑师本人文字时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Filippo Brunelleschi: double-shell dome in brick with herringbone courses, no centring, linear perspective, grey stone on white plaster, round arches and Corinthian order, calm proportion, no Gothic pointed arches, no excess ornament`
- ZH: 布鲁内莱斯基风格：砖砌双壳穹顶，人字形砌法，无脚手架支撑，线性透视，灰石配白墙，圆拱与科林斯柱式，比例宁静，无哥特尖拱，无多余装饰。

## (2) 空间与体量

- 体量：穹顶高耸、体量纯净；空间序列：门廊—中厅—穹顶，透视灭点即空间中心；尺度：人体比例，柱距与拱跨皆有数比。 `impression`

## (3) 材料与色彩

- 主材：砖、灰石（pietra serena）、白灰墙；色板：灰石灰、白、砖红、陶土；禁色：不大面积涂彩，不用金色。 `impression`

## (4) 结构与构造

- 结构：双壳穹顶，人字形砌法与环箍，无木支撑自承重；育婴堂的轻拱廊是梁柱与拱的轻盈组合。 `verbatim` / `artifact`

## (5) 光线与环境

- 光线：穹顶天窗与侧窗，光线均匀宁静；环境：佛罗伦萨城市天际线，穹顶即城市地标。 `impression`

## (6) 该设计什么 / 不该设计什么

- 该设计：双壳穹顶与人字形砌法、线性透视与灭点、灰石配白墙、圆拱与科林斯柱式、拱廊与方形庭院。`verbatim`
- 不该设计：哥特尖拱、多余装饰、不对称平面、铁构与玻璃。
- Negative prompt: `No Gothic pointed arches, no excess ornament, no asymmetrical plan, no iron frame, no glass curtain wall, no polychromy`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Filippo Brunelleschi, a small community library on a modern city street corner, brick double-shell dome with herringbone courses, grey stone on white plaster, round arches, linear perspective to a central dome, calm proportion`
- 中文对照：布鲁内莱斯基风格：现代城市街角的一座社区图书馆，砖砌双壳穹顶人字形砌法，灰石配白墙，圆拱，线性透视汇向中央穹顶，比例宁静。
- Negative: `No Gothic pointed arches, no excess ornament, no asymmetrical plan, no iron frame, no glass curtain wall`
- 检验点：母题是否出现（双壳穹顶与人字形砌法、线性透视与灭点、灰石配白墙、圆拱与科林斯柱式、拱廊与方形庭院）；禁区是否避开（哥特尖拱、多余装饰、不对称平面、铁构与玻璃）；空间、材料、结构是否仍是此人的语言，而不是通用现代建筑。
