# Charles Doolittle Walcott — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charles Doolittle Walcott, split a shale and find a world: quarry the Burgess Shale bed by bed, collect the soft-bodied animals the textbooks said could not fossilise, and read the Cambrian explosion from their anatomy`
- ZH: 沃尔科特风格：劈开一页页岩就找到一个世界——逐层采石伯吉斯页岩，收集教科书说不可能化石化的软躯体动物，从它们的解剖读出寒武纪生命大爆发。

## (2) 野外观察方式

- 页岩采石者的眼睛：在加拿大落基山伯吉斯页岩逐层劈开，软躯体化石一片一片地取。粒度是标本与剖面尺度；一处页岩可以改写生命史。化石采集逐层编号，标本数量以万计。

## (3) 地层对比与化石证据

- 伯吉斯页岩是寒武纪中期的海相页岩，化石群靠层位定时代。化石是核心证据；软躯体保存是关键——没有硬壳的动物也能成化石。缺失靠更多采石补。

## (4) 理论建构方式

- 从伯吉斯化石群归纳出寒武纪生命大爆发：几乎所有动物门类在寒武纪早期快速出现。跳跃是多样性的跳跃——把一处页岩的动物群读成全球生命事件。理论的尺度是全球，方法的尺度是一页页岩。

## (5) 论证语言

- 论证结构是采石描述—化石鉴定—动物群复原—大爆发推论。图示是化石图版与复原图；术语是解剖学与分类学术语。回应质疑靠更多的标本。

## (6) 该用 / 不该用的论证套路

- 该用：- 逐层采石，不跳层、不混层
- 把软躯体化石当作与硬壳化石同等重要的证据
- 用动物群的整体多样性谈大爆发，不靠单个奇异种
- 标本数量要大，统计才有意义
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no Cambrian claim from a single odd fossil, no mixing shale beds, no ignoring the soft-bodied animals that the textbooks said could not fossilise, no reading a local fauna as a global event without comparison`

## (7) 测试提示词示例（现代地质问题：一处页岩里出现大量软躯体化石，如何判断它是不是生命大爆发的证据？）

- Prompt: `In the style of Charles Doolittle Walcott, a shale yields many soft-bodied fossils: quarry it bed by bed, identify the whole fauna, compare it with other Cambrian faunas, and argue what the diversity does and does not prove about the Cambrian explosion`
- 中文对照：沃尔科特风格：一处页岩出现大量软躯体化石——逐层采石、鉴定整个动物群，与其他寒武纪动物群对比，论证多样性能证明什么、不能证明什么。
- Negative: `no Cambrian claim from a single odd fossil, no mixing shale beds, no ignoring the soft-bodied animals that the textbooks said could not fossilise, no reading a local fauna as a global event without comparison`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
