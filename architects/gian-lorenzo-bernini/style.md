# Gian Lorenzo Bernini — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。材料色只写通用材料色名，不编造实测 HEX 值。引用建筑师本人文字时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gian Lorenzo Bernini the architect: vast elliptical colonnade embracing a piazza, bronze baldachin under a dome, oval church with a dome, travertine and bronze, theatrical light, no Gothic detail, no iron frame`
- ZH: 贝尼尼（建筑部分）风格：巨大椭圆形柱廊环抱广场，穹顶下青铜华盖，椭圆形教堂配穹顶，石灰华与青铜，戏剧性光线，无哥特细部，无铁构。

## (2) 空间与体量

- 体量：柱廊环抱、椭圆收束；空间序列：广场—柱廊—教堂—华盖，层层收束到穹顶中心；尺度：广场纪念性尺度，教堂人体尺度。 `impression`

## (3) 材料与色彩

- 主材：石灰华、青铜、大理石；色板：石灰华暖白、青铜深绿、金；禁色：不大面积涂彩。 `impression`

## (4) 结构与构造

- 结构：柱廊梁柱体系，青铜华盖以螺旋柱承托；圣安德烈亚的椭圆形平面与穹顶是其建筑手笔。 `verbatim` / `artifact`

## (5) 光线与环境

- 光线：广场露天强光，教堂穹顶天窗聚光；环境：圣彼得广场以柱廊收束城市视线。 `impression`

## (6) 该设计什么 / 不该设计什么

- 该设计：椭圆形柱廊广场、青铜华盖与螺旋柱、椭圆形教堂与穹顶、石灰华与青铜、戏剧性聚光。`verbatim`
- 不该设计：哥特尖拱、铁构与玻璃、平淡对称、琐碎装饰。
- Negative prompt: `No Gothic pointed arches, no iron frame, no glass curtain wall, no flat symmetry, no fussy ornament`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Gian Lorenzo Bernini the architect, a small community library on a modern city street corner, elliptical colonnade embracing a forecourt, bronze canopy over the entrance, oval reading hall with a dome, travertine and bronze, theatrical light`
- 中文对照：贝尼尼（建筑部分）风格：现代城市街角的一座社区图书馆，椭圆形柱廊环抱前院，入口青铜华盖，椭圆形阅览厅配穹顶，石灰华与青铜，戏剧性光线。
- Negative: `No Gothic pointed arches, no iron frame, no glass curtain wall, no flat symmetry, no fussy ornament`
- 检验点：母题是否出现（椭圆形柱廊广场、青铜华盖与螺旋柱、椭圆形教堂与穹顶、石灰华与青铜、戏剧性聚光）；禁区是否避开（哥特尖拱、铁构与玻璃、平淡对称、琐碎装饰）；空间、材料、结构是否仍是此人的语言，而不是通用现代建筑。
