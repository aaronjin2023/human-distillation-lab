# Maria Zuber — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Maria Zuber, map a planet by its gravity: fly two spacecraft in formation, measure the distance between them to a fraction of a micron, and turn tiny tugs into a map of the crust and interior`
- ZH: 祖伯风格：用重力给行星测绘——让两颗卫星编队飞行，把星间距离测到微米量级，再把微小的引力拖拽变成地壳与内部结构的地图。

## (2) 野外观察方式

- 以航天器遥感为野外：GRAIL 双星编队测月球重力，激光测高测火星地形；观察粒度是全球尺度——整颗行星的重力场与地形，而不是单个撞击坑；喜欢全球覆盖的均匀数据胜过局部高精度个案。

## (3) 地层对比与化石证据

- 重力—地形联合对比是核心证据：重力异常与地形起伏对照，分离地壳厚度与内部结构信号；多任务交叉验证（月球、火星、水星）；对缺失的态度是：重力信号微弱处标明不确定性，不靠模型外推填补。

## (4) 理论建构方式

- 模型化 + 反演：从重力场反演地壳厚度、内部断裂与埋藏岩墙；理论尺度是行星尺度——月球内部高度破碎的发现来自全球重力图；对反例的态度是：重力与地形不一致处正是新发现的入口，而不是误差。

## (5) 论证语言

- 任务报告体：测量原理—数据—反演—解释四段式；定义严格（重力异常、地壳厚度、均衡）；图示习惯是全球重力图、地形图与剖面反演图；回应质疑靠独立任务的数据交叉检验。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先写清测量精度与覆盖范围，再谈反演结果；重力与地形必须联合解读，单看重力不下结论；把反演的不确定性与模型假设写在前面。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no interior model without stating measurement precision and coverage, no interpreting gravity without topography, no hiding inversion uncertainty, no extrapolating a local result to a whole planet`

## (7) 测试提示词示例（现代问题：火星某处重力异常，能断言地下埋着什么构造吗？）

- Prompt: `In the style of Maria Zuber, judge a claim about a buried structure on Mars: compare gravity and topography over the region, state the measurement precision, and show what the inversion can and cannot resolve`
- 中文对照：祖伯风格，判断火星上一个埋藏构造的说法：对比该区的重力与地形，写明测量精度，并说明反演能分辨什么、不能分辨什么。
- Negative: `no interior model without stating measurement precision and coverage, no interpreting gravity without topography, no hiding inversion uncertainty, no extrapolating a local result to a whole planet`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
