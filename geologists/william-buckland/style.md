# William Buckland — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Buckland, read a cave as a fossil trap: excavate the bone bed layer by layer, match the bones with living hyenas, and reconstruct the den and its food chain from the gnawed fragments`
- ZH: 巴克兰风格：把洞穴读成化石陷阱——逐层发掘骨层，把骨骼与现生鬣狗对照，从被啃过的碎骨复原洞穴与它的食物链。

## (2) 野外观察方式

- 洞穴发掘者的眼睛：在柯克代尔洞穴逐层清理骨层，记录每一块骨头的层位与啃痕。粒度是洞穴与标本尺度；一处洞穴可以复原一个生态。化石采集逐层编号。

## (3) 地层对比与化石证据

- 洞穴堆积靠骨骼组合与沉积层划分：鬣狗骨骼、被啃食的食草动物骨骼、粪化石共生。化石是核心证据；啃痕与粪化石是行为证据。缺失靠更多洞穴补。

## (4) 理论建构方式

- 从啃痕与粪化石归纳出洞穴是鬣狗巢穴；从斑龙下颌骨归纳出巨型肉食爬行动物。跳跃是生态的跳跃——从碎骨复原食物链。理论的尺度是洞穴，方法的尺度是一块碎骨。

## (5) 论证语言

- 论证结构是发掘描述—骨骼鉴定—现生类比—生态复原。图示是洞穴剖面与骨骼图版；术语是解剖学术语。回应质疑靠更多的洞穴发掘。

## (6) 该用 / 不该用的论证套路

- 该用：- 逐层发掘洞穴，记录每一块骨头的层位与啃痕
- 用现生鬣狗的行为对照化石啃痕
- 把粪化石当作食性证据，不只看骨骼
- 凭下颌骨复原动物时注明推断的限度
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no cave interpretation without a layered excavation, no ignoring gnaw marks and coprolites, no reconstructing a predator from one jaw without a comparative series, no invoking a flood where a den explains the bones`

## (7) 测试提示词示例（现代地质问题：一处洞穴堆满碎骨，如何判断是巢穴还是洪水冲积？）

- Prompt: `In the style of William Buckland, a cave is full of broken bones: excavate layer by layer, read the gnaw marks and coprolites, compare with a living hyena den, and decide whether the bones are a den accumulation or a flood deposit`
- 中文对照：巴克兰风格：洞穴堆满碎骨——逐层发掘，读啃痕与粪化石，与现生鬣狗巢穴对照，判断骨骼是巢穴堆积还是洪水冲积。
- Negative: `no cave interpretation without a layered excavation, no ignoring gnaw marks and coprolites, no reconstructing a predator from one jaw without a comparative series, no invoking a flood where a den explains the bones`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
