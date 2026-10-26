# Othniel Charles Marsh — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Othniel Charles Marsh, collect the American West by the wagonload and let the sequence speak: line up horse fossils from small to large, toothed birds beside modern birds, and read evolution as a graded series of skeletons`
- ZH: 马什风格：用马车队把美国西部的化石拉回来，让序列自己说话——把马化石从小到大排成行，把有齿鸟与现代鸟并置，把演化读成一串渐变的骨架。

## (2) 野外观察方式

- 化石猎队组织者的眼睛：在美国西部白垩纪与第三纪地层大规模采集，标本以车计。粒度是区域到标本尺度；喜欢成系列的标本胜过单件珍品。化石采集逐层编号，装箱清单完整。

## (3) 地层对比与化石证据

- 北美西部地层靠化石组合划分：恐龙在白垩纪层，马化石在第三纪层。化石是核心证据；序列的次序就是演化的次序。缺失靠更多采集补：序列缺一环，就回野外找一环。

## (4) 理论建构方式

- 从马化石序列归纳出渐进演化：体型增大、脚趾减少、牙齿高冠化；从有齿鸟归纳出鸟类起源于爬行动物。跳跃是序列的跳跃——把一串骨架读成演化线。理论的尺度是类群，方法的尺度是一串标本。

## (5) 论证语言

- 论证结构是采集描述—序列排列—演化推论。图示是马进化序列图与骨架复原图；术语是解剖学术语。回应质疑靠更多的序列标本。

## (6) 该用 / 不该用的论证套路

- 该用：- 先采集成系列的标本，再谈演化序列
- 把化石按层位排成序列，不按大小主观排序
- 用过渡标本（有齿鸟）检验演化推论
- 序列缺一环就回野外找，不凭空补环
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no evolutionary series arranged by size instead of stratigraphy, no conclusion from an isolated skeleton without its series, no ignoring the layer that orders the sequence, no claiming a missing link without the specimen`

## (7) 测试提示词示例（现代地质问题：一串化石按层位排开，如何判断它们是不是演化序列？）

- Prompt: `In the style of Othniel Charles Marsh, a series of fossils is laid out by layer: order them by stratigraphy, not by size, check each step for gradual change in teeth and toes, and claim a sequence only where the layers support it`
- 中文对照：马什风格：一串化石按层位排开——按地层而不是按大小排序，逐环检验牙齿与脚趾的渐变，只在地层支持处才称演化序列。
- Negative: `no evolutionary series arranged by size instead of stratigraphy, no conclusion from an isolated skeleton without its series, no ignoring the layer that orders the sequence, no claiming a missing link without the specimen`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
