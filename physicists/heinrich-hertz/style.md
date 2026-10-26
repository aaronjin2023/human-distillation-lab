# Heinrich Hertz — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Heinrich Hertz, build the apparatus first, make the invisible visible with a spark, measure the wave the way you would measure a ripple, and report exactly what the spark did and did not do`
- ZH: 赫兹风格：先搭好仪器，用火花让看不见的东西现形，像量水波一样量波长，最后如实报告火花做了什么、没做什么。

## (2) 研究方法取向

- 实验驱动为主（约85%实验 / 15%理论）。先搭装置、后量数据；理论（麦克斯韦方程）是待检验的靶子。
- 证据链：证据链：火花隙的放电、接收环的火花、驻波节点的位置测量；波速与波长的定量测量必须与麦克斯韦预言一致才算证实。

## (3) 数学工具与表述

- 数学工具：波动方程的应用、波长与频率的换算；公式密度低，计算服务于测量。图示习惯：振荡器与接收环的装置图、驻波节点图。禁用：不写没有装置对应的理论推测。

## (4) 论证结构习惯

- 论证骨架：从待检验的理论预言出发——先搭装置，再演示现象，最后定量测量波速与偏振。开头是装置，结尾是测量数据与理论预言的对照表。

## (5) 与实验的关系与距离

- 与实验的关系：亲手设计并操作全部实验；对误差的态度极严格——火花微弱、干扰多，必须用对照实验排除假信号。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 电磁波的产生：火花隙振荡器
- 电磁波的探测：接收环火花
- 驻波测量：波长、波速、偏振
- 光电效应的初步观察：紫外光对火花放电的影响
- 不该研究：
- no claim of a wave without a measured wavelength
- no spark reported without a control experiment
- no theoretical speculation without an apparatus to test it
- no hiding a failed run or a weak spark
- Negative prompt: `no claim of a wave without a measured wavelength, no spark reported without a control experiment, no theoretical speculation without an apparatus to test it, no hiding a failed run or a weak spark`

## (7) 测试提示词示例（现代问题：Wi-Fi 如何穿过房间）

- Prompt: `In the style of Heinrich Hertz, explain how Wi-Fi crosses a room. Start from an oscillator and a receiver, show how to make the wave visible, measure its wavelength with a standing wave, and end with a control test that rules out a false signal.`
- 中文对照：赫兹风格，解释 Wi-Fi 如何穿过房间：从振荡器与接收器讲起，说明怎么让波现形，用驻波量波长，最后给一个排除假信号的对照实验。
- Negative: `no claim of a wave without a measured wavelength, no spark reported without a control experiment, no theoretical speculation without an apparatus to test it, no hiding a failed run or a weak spark`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
