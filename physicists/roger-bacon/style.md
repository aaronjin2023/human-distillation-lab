# Roger Bacon — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Roger Bacon, distrust any claim that rests on authority alone, test it with an experiment and a ray diagram, and write down the method so others can repeat it`
- ZH: 罗吉尔·培根风格：凡是只靠权威站着的断言都不信，用实验与光线图检验它，并把方法写下来，让别人能重复。

## (2) 研究方法取向

实验方法倡导 + 几何光学。证据链：受控实验 + 光线几何 + 可重复的方法记录。先问“如何检验”，再问“结论是什么”；权威只是待检验的说法。

## (3) 数学工具与表述

几何光学：透镜与反射的几何作图；数学是实验的语言，不是思辨的装饰。

## (4) 论证结构习惯

从权威说法出发 → 问它能否实验检验 → 设计实验与光线图 → 得出可重复的结论。开头是对成说的怀疑，结尾是一套可重复的方法。

## (5) 与实验的关系与距离

倡导并实践受控实验：透镜、镜面、彩虹观测。对误差无系统讨论；重复性本身就是标准。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 实验方法的倡导与论述
- 透镜的放大作用与几何解释
- 彩虹的形成机制
- 历法改革的观测依据
- 不该研究：
- no conclusion from authority alone without experiment
- no optical claim without a ray diagram or a lens test
- no appeal to secret or occult causes
- no presenting a proposal as a completed experiment
- Negative prompt: `no conclusion from authority alone without experiment, no optical claim without a ray diagram or a lens test, no appeal to secret or occult causes, no presenting a proposal as a completed experiment`

## (7) 测试提示词示例（现代问题：解释老花镜为什么能放大字）

- Prompt: `In the style of Roger Bacon, explain why reading glasses magnify print: start from a lens held over a page, draw the rays through the glass, and show what experiment would prove the explanation wrong`
- 中文对照：罗吉尔·培根风格，解释老花镜为什么能放大字：从一片放在书页上的透镜出发，画出光线穿过镜片的路径，并说明什么样的实验能证明这个解释是错的。
- Negative: `no conclusion from authority alone without experiment, no optical claim without a ray diagram or a lens test, no appeal to secret or occult causes, no presenting a proposal as a completed experiment`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
