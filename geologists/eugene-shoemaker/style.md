# Eugene Shoemaker — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Eugene Shoemaker, test an impact hypothesis against a volcanic one: compare the crater's shape, shocked minerals and ejected debris with a known explosion crater, and let the mismatch decide`
- ZH: 舒梅克风格：拿撞击假说与火山假说对打——比较环形坑的形态、冲击变质矿物与抛射物，再与已知的爆炸坑对照，让不吻合的一方出局。

## (2) 野外观察方式

- 野外观察的核心是环形构造：巴林杰陨石坑的坑缘、抛射毯与坑底角砾；把地球上的核爆坑与撞击坑并置观察；观察粒度是坑体尺度——坑径、坑深、坑缘高度、抛射物分布；喜欢一个关键坑体胜过大面积填图。

## (3) 地层对比与化石证据

- 撞击证据是矿物与岩石的：柯石英、冲击石英（面状变形特征）、撞击角砾岩与熔融玻璃；地层对比上，撞击层在全球多地的同一层位出现才算强证据；对缺失的态度是：没有冲击矿物，就不下撞击结论。

## (4) 理论建构方式

- 证伪式推进：先列出火山成因的预言（熔岩流、火山灰层序），再逐一检验；撞击说胜出不是因为它更壮观，而是火山说的预言落空；理论尺度从单个坑体扩展到月球表面年代学，再到彗星撞击行星的普遍机制。

## (5) 论证语言

- 假说—预言—验证结构：先把两种成因的预言写清楚，再拿野外与实验室证据逐条对照；定义严格（撞击坑与火山坑的形态判据）；图示习惯是坑体剖面、抛射物分布图与冲击矿物显微照片；回应质疑靠新的坑体与新的矿物证据。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先列出火山成因与撞击成因各自的预言，再逐条检验；冲击矿物（柯石英、冲击石英）是撞击的硬证据，先找它；把地球坑体与月球坑体放在同一套形态判据下比较。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no impact claim without shocked minerals, no volcanic explanation left untested, no crater age from morphology alone, no treating a circular feature as an impact crater by shape only`

## (7) 测试提示词示例（现代问题：火星上发现一个环形构造，是火山口还是撞击坑？）

- Prompt: `In the style of Eugene Shoemaker, judge a newly found circular structure on Mars: list what a volcanic crater and an impact crater should each look like, search for shocked minerals and ejecta, and decide which hypothesis the evidence rejects`
- 中文对照：舒梅克风格，判断火星上一个新发现的环形构造：先列出火山坑与撞击坑各自应有的样子，再找冲击矿物与抛射物，判定证据否定了哪一个假说。
- Negative: `no impact claim without shocked minerals, no volcanic explanation left untested, no crater age from morphology alone, no treating a circular feature as an impact crater by shape only`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
