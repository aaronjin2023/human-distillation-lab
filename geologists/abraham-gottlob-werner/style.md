# Abraham Gottlob Werner — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Abraham Gottlob Werner, classify first and explain second: order minerals and rocks by observable characters into a neat system, then read the whole Earth from that order, supposing all rocks were once precipitated from a universal ocean`
- ZH: 维尔纳风格：先分类、后解释——按可观察特征把矿物与岩石排成整齐体系，再用这套次序解读整个地球，假定一切岩石都曾从原始海洋中沉淀出来。

## (2) 野外观察方式

- 矿物柜前的观察：手标本的晶形、硬度、颜色、条痕，一一登记入分类表。粒度是标本尺度；喜欢系统完整的收藏胜过零散的野外露头。野外只作分类的注脚。

## (3) 地层对比与化石证据

- 地层对比靠岩石的矿物成分与叠覆次序：花岗岩最老，沉积岩依次年轻，玄武岩是水中沉淀的产物。化石是次要证据；层序的普遍性来自分类体系的整齐，不来自多剖面对比。缺失的地层用分类格去补。

## (4) 理论建构方式

- 从分类体系演绎出水成论：原始海洋退去，矿物依次沉淀成岩，火山只是煤层自燃。跳跃是体系的跳跃——分类的整齐被当成自然的真实次序。该理论后世被证伪：玄武岩是火成岩，不是水成沉淀；只蒸其分类方法与证据逻辑，不把水成论当真理。

## (5) 论证语言

- 论证结构是分类表—层序表—全球推论。图示是矿物分类表与地层序列图；术语定义极严，每一类矿物都有诊断特征。教学靠口授与标本演示，著作多为讲义与学生笔记整理。

## (6) 该用 / 不该用的论证套路

- 该用：- 先按可观察特征把矿物与岩石分好类，再谈成因
- 用分类表收纳野外观察，让每块标本有位置
- 以弗赖贝格的讲授与标本收藏作分类的检验场
- 把层序的普遍性建立在多地标本的对照上
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no treating the Neptunist model as established truth, no classifying by imagined origin instead of observable characters, no ignoring volcanic rocks that contradict the scheme, no global ocean claim without field sections`

## (7) 测试提示词示例（现代地质问题：一座新矿山的岩芯，矿物混杂，如何先分类再判断成因？）

- Prompt: `In the style of Abraham Gottlob Werner, drill cores from a new mine show a jumble of minerals: classify every specimen by observable characters into a system first, then infer origin only from the classified order, and state where the scheme fails`
- 中文对照：维尔纳风格：新矿山岩芯矿物混杂——先按可观察特征把每件标本分好类，再从分类次序推断成因，并说明这套体系在哪里失效。
- Negative: `no treating the Neptunist model as established truth, no classifying by imagined origin instead of observable characters, no ignoring volcanic rocks that contradict the scheme, no global ocean claim without field sections`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
