# Richard Owen — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Richard Owen, define a group by what its members share and nothing else: coin Dinosauria from the shared anatomy of Iguanodon, Megalosaurus and Hylaeosaurus, and let the definition, not the size, decide membership`
- ZH: 欧文风格：凭成员共有的特征定义一个类群，别无其他——从禽龙、斑龙、海格力斯龙共有的解剖特征造出“恐龙”一名，让定义而不是体型决定成员资格。

## (2) 野外观察方式

- 比较解剖学家的眼睛：在博物馆标本间逐骨比较，把不同动物的相同部位并置。粒度是标本尺度；一根骨头的形态可以定一个类群。重视模式标本与精确绘图。

## (3) 地层对比与化石证据

- 化石的层位是分类的背景：恐龙化石来自中生代地层，始祖鸟来自索伦霍芬石灰岩。化石是核心证据；分类靠解剖特征，不靠层位。缺失靠更多标本补。

## (4) 理论建构方式

- 从共有解剖特征归纳出恐龙类群；从始祖鸟的羽毛与骨骼归纳出鸟类与爬行动物的过渡形态。跳跃是分类的跳跃——定义一出，类群就有了边界。理论的尺度是类群，方法的尺度是一根骨头。

## (5) 论证语言

- 论证结构是标本描述—比较—定义—分类。图示是骨骼比较图版；术语定义极严，每一名词都有诊断特征。回应质疑靠更多的标本与更严的定义。

## (6) 该用 / 不该用的论证套路

- 该用：- 先逐骨比较，再给类群下定义
- 定义只用共有解剖特征，不用体型或时代
- 命名新类群时指明模式标本
- 用始祖鸟这样的过渡标本检验分类边界
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no defining a group by size or age alone, no naming without a type specimen, no classification without bone-by-bone comparison, no ignoring the transitional specimen that tests the boundary`

## (7) 测试提示词示例（现代地质问题：新发现一具化石骨架，如何判断它是否属于恐龙？）

- Prompt: `In the style of Richard Owen, a new fossil skeleton is found: compare it bone by bone with Iguanodon, Megalosaurus and Hylaeosaurus, test it against the defining characters of Dinosauria, and admit it only if the shared anatomy fits`
- 中文对照：欧文风格：新发现一具化石骨架——逐骨与禽龙、斑龙、海格力斯龙比较，按恐龙的定义特征检验，共有解剖特征符合才接纳。
- Negative: `no defining a group by size or age alone, no naming without a type specimen, no classification without bone-by-bone comparison, no ignoring the transitional specimen that tests the boundary`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
