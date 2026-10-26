# Imhotep — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。材料色只写通用材料色名，不编造实测 HEX 值。引用建筑师本人文字时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Imhotep: stepped stone pyramid rising in six tiers, massive limestone mass, axial funerary courtyard, colonnaded court, stone imitating reed and wood, no curved surface, no glass, no ornament beyond carved relief`
- ZH: 伊姆霍特普风格：六级阶梯石金字塔，巨大石灰石体量，轴线葬祭庭院，柱廊庭院，石材仿芦苇与木构形态，无曲面、无玻璃、无多余雕饰。

## (2) 空间与体量

- 体量：阶梯收分、垂直拔起、单体纪念性；空间序列：入口柱廊—庭院—葬祭庙—金字塔，仪式轴线强烈，围合严密；尺度：纪念性尺度压倒人体尺度，石阶以人体攀登节奏收分。 `impression`

## (3) 材料与色彩

- 主材：石灰石（粗石砌筑、精细贴面并用）、花岗岩门楣；色板：石灰石暖灰、沙漠土黄、赭石红、矿物蓝（少量彩绘）；禁色：不做大面积亮彩平涂，不用金属光泽面。 `impression`

## (4) 结构与构造

- 结构：实心石砌阶梯体，荷载逐层内收；柱为石仿木束柱与凹槽柱，承重即形式；无拱、无穹顶，靠砌体自重稳定。 `verbatim` / `artifact`

## (5) 光线与环境

- 光线：露天庭院强光与柱廊深影对比强烈；室内葬祭空间幽暗，仅靠高侧开口进光；环境：与尼罗河西岸沙漠台地关系——建筑即人工山体，顺应台地高差。 `impression`

## (6) 该设计什么 / 不该设计什么

- 该设计：六级阶梯金字塔形、葬祭庭院与轴线、石仿芦苇束柱与凹槽柱、柱廊与门楼、阶梯收分与平台。`verbatim`
- 不该设计：曲面与穹顶、玻璃与钢构、对称古典立面以外的装饰、小尺度民居式开洞。
- Negative prompt: `No curved surfaces, no domes, no glass curtain wall, no steel frame, no applied classical ornament, no small domestic windows`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Imhotep, a small community library on a modern city street corner, stepped limestone mass in six receding tiers, axial colonnaded entrance court, stone columns imitating reed bundles, warm limestone grey, strong sunlight and deep shadow`
- 中文对照：伊姆霍特普风格：现代城市街角的一座社区图书馆，六级收分石灰石阶梯体量，轴线柱廊入口庭院，石柱仿芦苇束形态，石灰石暖灰色，强光与深影对比。
- Negative: `No curved surfaces, no glass curtain wall, no steel frame, no domes, no applied ornament`
- 检验点：母题是否出现（六级阶梯金字塔形、葬祭庭院与轴线、石仿芦苇束柱与凹槽柱、柱廊与门楼、阶梯收分与平台）；禁区是否避开（曲面与穹顶、玻璃与钢构、对称古典立面以外的装饰、小尺度民居式开洞）；空间、材料、结构是否仍是此人的语言，而不是通用现代建筑。
