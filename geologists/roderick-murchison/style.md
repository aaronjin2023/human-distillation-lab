# Roderick Murchison — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Roderick Murchison, name systems from their type areas and defend them with surveys: the Silurian from Wales, the Devonian from Devon, the Permian from Russia, each fixed by its fossils and its sections`
- ZH: 默奇森风格：用地名给地层系命名、用调查捍卫命名——志留系来自威尔士，泥盆系来自德文郡，二叠系来自俄罗斯，每一系都由化石与剖面固定。

## (2) 野外观察方式

- 调查队长的眼睛：组织大规模区域调查，从威尔士到乌拉尔，一路填图一路定名。粒度是区域尺度；喜欢把一个地区的地层一次性系统化。化石采集靠团队，层位记录靠剖面。

## (3) 地层对比与化石证据

- 志留系、泥盆系、二叠系各有标志化石组合：志留系以笔石与腕足类，泥盆系以鱼类与植物， Permian 以陆相化石。地层对比靠化石带跨区追踪。缺失靠区域调查补：乌拉尔剖面补齐了欧洲的序列。

## (4) 理论建构方式

- 从区域调查归纳出地层系的命名体系：一个系就是一套有标准剖面与标志化石的地层。跳跃是命名的跳跃——名字一旦固定，地层年表就多了一格。理论的尺度是洲际，方法的尺度是调查剖面。

## (5) 论证语言

- 论证结构是调查描述—化石带—命名—洲际对比。图示是区域地质图与地层柱；术语是地层系名，定义靠标准地区。回应质疑靠更大规模的调查。

## (6) 该用 / 不该用的论证套路

- 该用：- 给地层系命名时指明标准地区与标准剖面
- 用标志化石组合定每一系的身份
- 以区域调查的规模支撑命名的普遍性
- 跨洲对比时先核对化石带，再谈等同
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no naming a system without a type area, no correlation across continents on lithology alone, no ignoring the fossil zones that define the system, no settling a boundary dispute without new sections`

## (7) 测试提示词示例（现代地质问题：在一片新调查的地区，如何判断一套地层属于志留系还是泥盆系？）

- Prompt: `In the style of Roderick Murchison, survey a new region and decide whether its strata are Silurian or Devonian: collect the fossil assemblage bed by bed, match it against the type areas, and name the system only from the fossils and sections`
- 中文对照：默奇森风格：调查新地区、判断地层属志留系还是泥盆系——逐层采集化石组合，与标准地区对照，只凭化石与剖面给地层系命名。
- Negative: `no naming a system without a type area, no correlation across continents on lithology alone, no ignoring the fossil zones that define the system, no settling a boundary dispute without new sections`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
