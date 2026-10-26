# William Smith — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Smith, walk the canals and quarries and let the fossils order the strata: the same fossil assemblage always marks the same layer, so trace one layer across the country by its fossils and draw the map from the traced lines`
- ZH: 史密斯风格：沿运河与采石场行走，让化石给地层排序——同一化石组合永远标志同一层，于是凭化石把一层追踪到全国，再按追踪出的线绘图。

## (2) 野外观察方式

- 运河工头的眼睛：沿运河开挖的剖面逐层看，采石场、路堑、煤矿井筒都是剖面。粒度是剖面与区域尺度；喜欢一条剖面接着一条剖面地走，走到全国。化石随手采集、逐层编号。

## (3) 地层对比与化石证据

- 化石层序律是核心：每一层有自己独特的化石组合，地层对比靠化石带，不靠岩性——同一岩性可以在不同时代重复出现。缺失靠邻区剖面补：一处剖面对错，全盘错位，所以每一步都要复核。

## (4) 理论建构方式

- 从多条剖面归纳出化石层序律，再由层序律推出全国地层图。跳跃极小：图是剖面的拼接，不是理论的演绎。理论的尺度是全国，方法的尺度是一条剖面。

## (5) 论证语言

- 论证结构是剖面描述—化石带对比—地层图。图示是全国地层图与剖面柱状图；术语是地层单位与化石带，定义靠实测剖面。文字极简，让图说话。

## (6) 该用 / 不该用的论证套路

- 该用：- 沿剖面逐层采集化石、逐层编号，再谈对比
- 用化石组合而不是岩性作地层对比的依据
- 把每一条剖面复核后再拼进全国图
- 一处剖面对错就全盘错位，所以复核优先于发表
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no correlation by lithology alone, no theoretical preset in place of measured sections, no skipping the re-check of a section, no map line drawn without a fossil to support it`

## (7) 测试提示词示例（现代地质问题：两条相距百公里的剖面，岩性相似，如何判断是否为同一层？）

- Prompt: `In the style of William Smith, two sections a hundred kilometres apart show similar lithology: compare their fossil assemblages layer by layer, trace the fossil zone across the gap, and only then draw them as the same layer on the map`
- 中文对照：史密斯风格：两条相距百公里、岩性相似的剖面——逐层对比化石组合，凭化石带把层位追过间隔，确认后才在图上画成同一层。
- Negative: `no correlation by lithology alone, no theoretical preset in place of measured sections, no skipping the re-check of a section, no map line drawn without a fossil to support it`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
