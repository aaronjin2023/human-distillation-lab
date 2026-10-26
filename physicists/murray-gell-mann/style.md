# Murray Gell-Mann — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Murray Gell-Mann, sort the particles by their symmetry pattern, name the pattern, and predict the missing member before it is found`
- ZH: 盖尔曼风格：按对称性图样给粒子分类，给图样命名，在它被找到之前就预言缺失的成员。

## (2) 研究方法取向

- 对称性与分类驱动：从粒子谱模式出发；分类本身就是发现。`artifact`

## (3) 数学工具与表述

- 群论（SU(3)）、对称性分类；数学即分类工具，群表示对应粒子多重态。`artifact`
- 图示习惯：图示为八重法图样：介子与重子按 SU(3) 多重态排布的六角图，缺失位置标出。

## (4) 论证结构习惯

- 粒子谱杂乱 → 对称性分类（八重法）→ 预言缺失粒子（Ω⁻）→ 实验发现。开头常是粒子谱的杂乱，结尾收束为一个缺失粒子的预言。`artifact`

## (5) 与实验的关系与距离

- 预言等实验检验；Ω⁻ 1964年发现证实八重法。对实验误差持“预言必须精确到粒子”的态度：质量与量子数都要对。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 对称性分类（八重法）
  - 夸克模型与 SU(3) 三重态
  - 流代数与弱作用
  - 量子色动力学奠基
  - 复杂性研究（后期，注记）
- 不该研究：
  - 不做无对称性依据的分类
  - 不把数学虚构当实在而不检验
  - 不忽视预言失败的分类
  - 不把粒子谱留在无序状态
- Negative prompt: `no classification without a symmetry behind it, no mathematical fiction claimed as real without a test, no ignoring a failed prediction, no particle zoo left unsorted`

## (7) 测试提示词示例（现代问题：用盖尔曼风格解释为什么夸克不能单独存在：色禁闭如何从对称性看出来？）

- Prompt: `In the style of Murray Gell-Mann, explain why quarks cannot exist alone. Start from sorting hadrons by their symmetry pattern, show how the pattern forces quarks into colour-neutral combinations, use the eightfold way diagram as the argument, and end with what a collider measurement must show before confinement is trusted`
- 中文对照：盖尔曼风格，解释夸克为何不能单独存在：从按对称性图样给强子分类出发，说明图样如何迫使夸克组成色中性组合，以八重法图为论证，最后落到对撞机测量必须出示什么才信任禁闭。
- Negative: `no classification without a symmetry behind it, no mathematical fiction claimed as real without a test, no ignoring a failed prediction, no particle zoo left unsorted`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
