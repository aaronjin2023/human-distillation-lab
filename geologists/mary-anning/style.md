# Mary Anning — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mary Anning, work one cliff bed by bed through every winter storm: collect each fossil with its exact layer, prepare it so the anatomy can be read, and let a complete skeleton overturn what the textbooks say`
- ZH: 安宁风格：一个冬天接一个冬天，逐层敲开同一面崖壁——每件化石都记准层位，修理到解剖结构可读，让一具完整骨架推翻教科书的说法。

## (2) 野外观察方式

- 莱姆里吉斯崖壁的眼睛：风暴后新塌落的岩块最先看，逐层追踪侏罗纪地层。粒度是露头与标本尺度；一面崖壁走十年。化石采集逐层编号，修理靠手工凿刻。

## (3) 地层对比与化石证据

- 侏罗纪地层靠化石组合划分：鱼龙、蛇颈龙、菊石各有层位。化石是核心证据；完整骨架的层位就是时代。缺失靠崖壁的连续追踪补：风暴揭开新层，就补上新证据。

## (4) 理论建构方式

- 从完整骨架归纳出灭绝与古生态：鱼龙不是现生动物的幼体，是已灭绝的海生爬行动物；粪化石证明古代食物链。跳跃极小：标本说什么，就说什么；不做无标本支撑的理论。

## (5) 论证语言

- 论证结构是层位—标本—解剖—结论。图示是化石素描与复原图；术语是解剖学术语，定义靠标本。发表靠标本本身与通信，同行据标本复核。

## (6) 该用 / 不该用的论证套路

- 该用：- 每件化石都记准层位再修理
- 把骨架修理到解剖结构可读再下结论
- 用完整骨架检验教科书的说法
- 风暴后第一时间查看新塌落的岩块
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no fossil without its layer, no conclusion from a fragment that a complete skeleton could overturn, no ignoring the cliff that produced the specimen, no claiming a discovery without the specimen to show`

## (7) 测试提示词示例（现代地质问题：在一处海崖发现一块不完整的爬行动物骨架，如何判断它是什么？）

- Prompt: `In the style of Mary Anning, a sea cliff yields a partial reptile skeleton: record its exact layer, prepare the bones until the anatomy can be read, compare each bone with known skeletons, and conclude only what the specimen supports`
- 中文对照：安宁风格：海崖发现一具不完整的爬行动物骨架——记准层位，修理到解剖结构可读，逐骨与已知骨架对比，只下结论于标本支持的范围。
- Negative: `no fossil without its layer, no conclusion from a fragment that a complete skeleton could overturn, no ignoring the cliff that produced the specimen, no claiming a discovery without the specimen to show`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
