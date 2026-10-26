# Jacques Herzog & Pierre de Meuron — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。引用建筑师本人文字时只引短句并注明出处。材料色板只写通用材料色名，不编造实测 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Herzog & de Meuron: material as concept, a simple box transformed by its skin, brick, glass and steel woven into a new texture, quiet monumentality`
- ZH: 赫尔佐格与德梅隆风格：材料即概念，简单的盒子被表皮变形，砖、玻璃与钢编织成新质感，安静的纪念性。

## (2) 空间与体量

- 体量：简单几何体（盒子、塔、碗）+ 表皮变形，变化全在表皮。`artifact`
- 空间序列：外表克制、内部戏剧性反差，入口安静、内部豁然。`impression`
- 尺度：纪念性公共尺度与人体尺度的细部并置。`impression`

## (3) 材料与色彩

- 色板（6 色，通用材料色名）：砖红、清水混凝土灰、玻璃蓝、钢银、铜绿、陶土。
- 主色依项目而变（鸟巢钢灰、泰特砖红、信号塔铜绿）；辅色玻璃蓝；禁色艳丽涂料、仿古石材贴面；冷暖随材料而变，质感即色彩。

## (4) 结构与构造

- 结构体系：结构即表皮——鸟巢钢网既是结构又是表皮。`artifact`
- 构造细节：表皮节点、穿孔板、编织与叠层，表皮精度决定成败。`artifact`

## (5) 光线与环境

- 光源：表皮透光（玻璃砖、穿孔板），室内光柔和漫射。`artifact`
- 环境关系：建筑以材料回应场地与城市肌理，不求形态张扬。`impression`

## (6) 该设计什么 / 不该设计什么

- 该设计：简单几何体、表皮即形式、材料实验（穿孔、编织、叠层）、外露结构网、砖与玻璃的质感对比、克制立面下的戏剧性内部。
- 不该设计：流线曲面、装饰线脚、古典对称、艳丽色彩、仿古贴面。
- Negative prompt: `No fluid curves, no applied ornament, no classical symmetry, no bright paint, no fake stone cladding, no pitched roofs`

## (7) 测试提示词示例（现代题材：现代城市街角的一座社区图书馆）

- Prompt: `In the style of Herzog & de Meuron, a small community library on a modern city street corner, a simple brick box transformed by a woven perforated skin, quiet facade, dramatic top-lit reading hall inside, material as the concept`
- 中文对照：赫尔佐格与德梅隆风格：现代城市街角的一座社区图书馆，简单的砖盒子被编织的穿孔表皮变形，立面安静，内部是戏剧性的顶部采光阅览大厅，材料即概念。
- Negative: `No fluid curves, no applied ornament, no classical symmetry, no bright paint, no fake stone cladding, no pitched roofs`
- 检验点：体块是否简单而表皮是否成立；内外反差是否在；材料质感是否真实而不贴皮。
