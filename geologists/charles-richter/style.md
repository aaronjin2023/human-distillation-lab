# Charles Richter — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charles Richter, report one earthquake with both magnitude and intensity: compute magnitude from calibrated log amplitudes, describe intensity from observed damage, and explain why the two numbers answer different questions`
- ZH: 查尔斯·里克特风格：地震大小如何用一个数字说清？

## (2) 野外观察方式

- 南加州台网观测：用伍德—安德森地震仪记录大量地方震，以最大振幅的对数为震级标度。观察粒度是区域台网的地方震。 `artifact`

## (3) 地层对比与化石证据

- 振幅记录是核心证据：同一地震多台振幅经距离校正后一致；震级—频度关系可统计；目录使大小可比较。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 对数标度：震级是振幅对数加距离校正；标度先为南加州地方震设计，后推广；大震饱和是标度边界，后世由矩震级接替。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 操作定义语言：论文先给震级的计算步骤，再给应用；《地震学基础》以教科书体例系统整理；区分震级（仪器量）与烈度（地面效应）。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先给可操作的计算定义再谈大小
- 多台振幅经距离校正后取一致值
- 明确标出标度的适用范围
- 不该用：no magnitude without log-amplitude calibration, no applying local magnitude to great earthquakes, no confusing magnitude with intensity, no magnitude from a single amplitude reading
- Negative prompt: `no magnitude without log-amplitude calibration, no applying local magnitude to great earthquakes, no confusing magnitude with intensity, no magnitude from a single amplitude reading`

## (7) 测试提示词示例（现代问题：为一次地震同时给出震级与烈度说明，两者有何不同？）

- Prompt: `In the style of Charles Richter, report one earthquake with both magnitude and intensity: compute magnitude from calibrated log amplitudes, describe intensity from observed damage, and explain why the two numbers answer different questions`
- 中文对照：查尔斯·里克特风格，为一次地震同时给出震级与烈度说明，两者有何不同？
- Negative: `no magnitude without log-amplitude calibration, no applying local magnitude to great earthquakes, no confusing magnitude with intensity, no magnitude from a single amplitude reading`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
