# Gideon Mantell — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gideon Mantell, read the Wealden clays tooth by tooth: match a fossil tooth with the teeth of a living iguana, infer a giant herbivorous reptile, and defend it with more teeth from more layers`
- ZH: 曼特尔风格：一颗牙一颗牙地读威尔德黏土——把化石牙齿与现生鬣蜥的牙齿对照，推断一种巨型草食爬行动物，再用更多层位的更多牙齿为它辩护。

## (2) 野外观察方式

- 乡村医生的野外眼睛：在蒂尔盖特森林的采石场逐层采集牙齿与骨骼。粒度是标本与剖面尺度；一颗牙齿可以定一个动物。化石采集逐层编号，牙齿形态逐一素描。

## (3) 地层对比与化石证据

- 威尔德黏土层靠化石组合划分：禽龙牙齿、鱼类、植物化石共生。化石是核心证据；牙齿的形态与层位就是时代与生态。缺失靠更多采石场补。

## (4) 理论建构方式

- 从牙齿形态类比现生鬣蜥，归纳出禽龙是巨型草食爬行动物；从威尔德化石群推出白垩纪陆相生态。跳跃是类比的跳跃——牙齿像鬣蜥，动物就吃植物。理论的尺度是区域，方法的尺度是一颗牙。

## (5) 论证语言

- 论证结构是标本描述—现生类比—复原—生态推论。图示是牙齿与骨骼素描；术语是解剖学术语，定义靠标本。回应质疑靠更多的牙齿与骨骼。

## (6) 该用 / 不该用的论证套路

- 该用：- 先把牙齿与现生动物的牙齿逐一对照，再谈复原
- 用更多层位的更多标本为解释辩护
- 把化石群作为一个生态整体来读，不只看单个种
- 遇质疑加采标本，不靠辩论
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no reconstruction from a single tooth without checking more specimens, no ignoring the layer that produced the tooth, no claiming a new animal without a comparative series, no confusing a Wealden fossil with a modern bone`

## (7) 测试提示词示例（现代地质问题：只找到几颗牙齿，如何判断它们属于什么动物？）

- Prompt: `In the style of Gideon Mantell, only a few teeth are found: compare each tooth with living animals tooth by tooth, collect more teeth from more layers, and infer the animal only as far as the comparative series allows`
- 中文对照：曼特尔风格：只找到几颗牙齿——逐颗与现生动物牙齿对照，从更多层位收集更多牙齿，只在对比序列允许的范围内推断动物。
- Negative: `no reconstruction from a single tooth without checking more specimens, no ignoring the layer that produced the tooth, no claiming a new animal without a comparative series, no confusing a Wealden fossil with a modern bone`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
