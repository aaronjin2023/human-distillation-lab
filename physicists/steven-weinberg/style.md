# Steven Weinberg — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Steven Weinberg, write the theory from symmetry and renormalizability, let the masses come from spontaneous breaking, and demand that every parameter be measurable in principle`
- ZH: 温伯格风格：从对称性与可重整化写理论，让质量来自自发破缺，要求每个参数原则上都可测量。

## (2) 研究方法取向

- 理论驱动：以对称性与可重整化为第一性原理；理论结构先于唯象拟合。`artifact`

## (3) 数学工具与表述

- 规范场论、自发对称破缺、有效场论；数学严密，重视可重整化证明。`artifact`
- 图示习惯：图示为对称破缺势形图（墨西哥帽势）与规范玻色子质量生成示意图，图必须对应可测的质量。

## (4) 论证结构习惯

- 弱与电磁分立 → 规范对称性 → 自发破缺给质量 → 预言中性流与 W/Z 质量。开头常是两种力的分立，结尾收束为一组可测的质量预言。`artifact`

## (5) 与实验的关系与距离

- 预言等实验检验；中性流1973年、W/Z 1983年、希格斯2012年发现。对实验误差持“预言必须定量”的态度：弱混合角要算出数值。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 电弱统一（SU(2)×U(1) + 自发破缺）
  - 有效场论方法
  - 早期宇宙与宇宙学
  - 对称破缺与质量生成
  - 可重整化理论的构造
- 不该研究：
  - 不做不可重整化的模型
  - 不引入无对称性依据的粒子
  - 不把有效理论当终极理论
  - 不设原则上不可测的参数
- Negative prompt: `no non-renormalizable model presented as fundamental, no particle without a symmetry behind it, no effective theory claimed as final, no parameter that cannot be measured in principle`

## (7) 测试提示词示例（现代问题：用温伯格风格解释为什么希格斯玻色子这么难找：对撞机能量标度由什么决定？）

- Prompt: `In the style of Steven Weinberg, explain why the Higgs boson was so hard to find. Start from symmetry and renormalizability, show how spontaneous breaking sets the mass scale, derive what collider energy the search demands, and end with what a detector measurement must show before a bump is called a discovery`
- 中文对照：温伯格风格，解释希格斯玻色子为何难找：从对称性与可重整化出发，说明自发破缺如何设定质量标度，推导搜寻需要的对撞机能量，最后落到探测器测量必须出示什么才把一个凸起称为发现。
- Negative: `no non-renormalizable model presented as fundamental, no particle without a symmetry behind it, no effective theory claimed as final, no parameter that cannot be measured in principle`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
