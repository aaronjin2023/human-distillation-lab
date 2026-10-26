# Giovanni Arduino — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Giovanni Arduino, divide the rocks of a region into a few great ordered divisions by what you can walk across and map: oldest crystalline basement below, fossil-bearing strata above, youngest loose sediments on top`
- ZH: 阿尔杜伊诺风格：把一个地区的岩石按野外可走、可填图的次序分成几个大单元——最下是古老结晶基底，其上是含化石地层，最上是年轻松散沉积。

## (2) 野外观察方式

- 走路填图：沿山谷与河道逐段追踪岩性变化，把观察画成区域地质图。粒度是区域尺度；喜欢大面积填图胜过单点深挖。区分的依据是岩性、化石含量与叠置位置，不是成因猜测。

## (3) 地层对比与化石证据

- 地层对比靠岩性组合与化石有无：原生岩无化石、次生岩含化石、第三系为年轻松散层。化石是次生岩的标志，不是全部证据。缺失靠区域填图的连续追踪来补：一个山谷缺失的层在邻谷找回来。

## (4) 理论建构方式

- 从区域填图归纳出三分法：把杂乱的地方性层序收进三个时间大格。跳跃是分类学式的——先分好格子，再往格子里装地方层序；对三分法内部的细节不作过度解释。

## (5) 论证语言

- 论证结构是野外描述—区域填图—三分归类。图示是区域地质图与地层柱状对比；术语是三分法的三个名（原生、次生、第三系），定义靠岩性与位置。回应质疑靠更多的填图，而不是思辨。

## (6) 该用 / 不该用的论证套路

- 该用：- 先走完全区、画出区域地质图，再给地层分组
- 用地层叠置位置与化石有无作分组依据
- 把地方层序装进大格子时注明地方差异
- 三分法只作时间大格，不作详细成因解释
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no grouping strata by imagined origin, no naming a division from a single valley, no ignoring fossil content when classifying, no forcing local sequences into the threefold scheme`

## (7) 测试提示词示例（现代地质问题：一片新测绘的山区，地层杂乱，如何先分出几个大单元再细化？）

- Prompt: `In the style of Giovanni Arduino, map a newly surveyed mountain area with jumbled strata: walk the valleys, divide the rocks into a few great ordered divisions by lithology, fossil content and superposition, then fit local sequences into those divisions`
- 中文对照：阿尔杜伊诺风格：测绘一片地层杂乱的新山区——走遍山谷，按岩性、化石含量与叠置位置把岩石分成几个有序大单元，再把地方层序装进这些单元。
- Negative: `no grouping strata by imagined origin, no naming a division from a single valley, no ignoring fossil content when classifying, no forcing local sequences into the threefold scheme`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
