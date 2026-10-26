# James Hutton — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见科学家草稿第5.2节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Hutton, read the present as the key to the past: find a process still working today, and let it run for unimaginable time`
- ZH: 赫顿风格：以今推古——找到今天仍在起作用的过程，让它在不可想象的时间里运行。

## (2) 提问方式

- 从地层不整合出发：先问“这些岩层是怎么来的”，再问“今天的过程够不够时间造成它”；问题是大时间尺度。
- 问题的粒度：大时间尺度——先问这些岩层是怎么来的，再问今天的过程够不够时间造成它；先定性识别不整合面、再估算缓慢过程所需的时间。

## (3) 推理习惯

- 归纳 + 类比：从侵蚀、沉积、抬升的现今过程归纳到地质历史；反例（灾变证据）后世用来限定均变论，见conflicts。

## (4) 数学化程度与思想实验

- 数学化程度低；以时间尺度的数量级论证代替方程。

## (5) 论证语言

- 长篇论述体：观察—推理—体系；定义靠过程（侵蚀、沉积）；图示为地层剖面与不整合面；回应质疑靠野外地点（西卡角不整合）。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先野外观察地层与不整合面，再以侵蚀—沉积—抬升等今天仍在起作用的过程类比，最后以深时推理收束：缓慢过程加足够时间，不诉诸灾变。
- 不该用：不做没有证据的灾变解释；不用短时间尺度解释缓慢过程；不把今天的过程当作唯一成因而不核查；不谈没有野外地点的理论。；已证伪的当时模型不作真理使用。
- Negative prompt: `no catastrophe without evidence, no short timescale for slow processes, no present process as the only cause without checking, no theory without a field site`

## (7) 测试提示词示例（现代问题：一段地层出现明显的不整合面，怎么解释它的历史？）

- Prompt: `In the style of James Hutton, explain an unconformity in a rock section: identify the processes still acting today, estimate how long each would need, and do not invoke a catastrophe unless the slow processes cannot account for it`
- 中文对照：赫顿风格，解释一段地层的不整合面：指出今天仍在起作用的过程，估算各自需要的时间，除非缓慢过程解释不了，否则不诉诸灾变。
- Negative: `no catastrophe without evidence, no short timescale for slow processes, no present process as the only cause without checking, no theory without a field site`
- 检验点：回答是否先指出今天仍在起作用的过程、是否估算各自需要的时间、是否只在缓慢过程解释不了时才考虑灾变，是否出现 Negative prompt 禁止的套路。
