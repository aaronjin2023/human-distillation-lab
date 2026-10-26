# Li Jie — 建筑风格规格 style.md（给图像模型）

> 只描述建筑，不描述人生。引用建筑师本人文字时只引短句并注明出处。材料色板只写通用材料色名，不编造实测 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Jie: the grammar of Song timber building, modular bays measured by cai-fen, bracket sets in strict order, roofs curving by juzhe, rules made visible`
- ZH: 李诫风格：宋代木构的语法，材分度量的模数开间，秩序井然的斗栱，举折而成的屋面曲线，规则本身可见。

## (2) 空间与体量

- 体量：木构殿堂，面阔进深按间数定。`artifact`
- 空间序列：台基—柱廊—殿身—屋顶，等级分明。`artifact`
- 尺度：材分模数，等级即尺度。`artifact`

## (3) 材料与色彩

- 色板（6 色，通用材料色名）：木色、朱红、黛瓦灰、石灰白、土黄、金黄。
- 主色木色 + 朱红；辅色黛瓦灰；禁色艳丽涂料、石材贴面、玻璃；暖木为主，朱红与金黄定等级。

## (4) 结构与构造

- 结构体系：抬梁式木构架、斗栱、材分八等。`artifact`
- 构造细节：铺作层数定等级，举折（juzhe）定屋面曲线。`artifact`

## (5) 光线与环境

- 光源：柱廊光影，殿内幽暗。`artifact`
- 环境关系：宫殿群中轴对称，顺应礼制。`artifact`

## (6) 该设计什么 / 不该设计什么

- 该设计：材分模数、斗栱、举折屋面、台基、柱廊、中轴对称、重檐。
- 不该设计：无模数、砖石大体量、拱顶、玻璃、装饰雕塑。
- Negative prompt: `No unmodulated masses, no masonry vaults, no glass curtain walls, no applied sculpture, no flat roofs, no random ornament`

## (7) 测试提示词示例（现代题材：现代城市街角的一座社区图书馆）

- Prompt: `In the style of Li Jie, a small community library on a modern city street corner, Song dynasty timber frame in modular bays, bracket sets in strict order, a gently curving roof by juzhe, timber colour and vermilion, raised platform, no concrete mass`
- 中文对照：李诫风格：现代城市街角的一座社区图书馆，宋代木构架模数开间，秩序井然的斗栱，举折而成的微微弯曲的屋面，木色与朱红，高台基，没有混凝土大体量。
- Negative: `No unmodulated masses, no masonry vaults, no glass curtain walls, no applied sculpture, no flat roofs, no random ornament`
- 检验点：开间是否有材分模数；斗栱是否有秩序；屋面曲线是否举折而成而不平直。
