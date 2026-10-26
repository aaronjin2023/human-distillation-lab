# Jocelyn Bell Burnell — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见科学家草稿第5.2节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jocelyn Bell Burnell, read miles of chart by eye, do not throw away the scruff, and eliminate every ordinary explanation before claiming something new`
- ZH: 贝尔风格：用眼睛读完几英里长的记录纸，不丢掉那一小块“scruff”，在宣称新发现之前先逐一排除每一种平凡解释。

## (2) 提问方式

- 从记录纸上的反常出发：先问“这块 0.5 厘米长的 scruff 是什么”，再问“它是不是仪器、人为干扰或已知的闪烁源”，最后才问“它是不是一种新天体”；问题是排除法，一层一层收窄。
- 问题的粒度：先问小处——同一片天区、同一信号是否重复出现；再问大处——它是不是自然界的新一类天体。喜欢“怎么样排除”胜过“为什么是这样”。

## (3) 推理习惯

- 归纳 + 排除：每天 30 多米记录纸、目视检查全部数据，先积累重复出现的反常，再用排除法逐一检验；演绎为辅：信号周期 1.3373 秒、极规则，推断源必须极小极密、转得极快。
- 对反例的态度：反例是关键证据——在天空另一处找到第二、第三、第四个同类脉冲源，才排除“外星信标”（LGM）假说；不靠单个信号下结论。

## (4) 数学化程度与思想实验

- 数学化程度中等：周期测量（1.3373 秒）、脉冲宽度（0.04 秒）、重复性统计是核心；中子星的物理解释由托马斯·戈尔德与弗雷德·霍伊尔在论文发表后给出，不属于贝尔本人的原始论证，见 conflicts.md。
- 思想实验：LGM（小绿人）假说本身就是一次思想实验——“如果这是外星信标，该怎么负责任地宣布？”；用“两个外星文明同时广播”不可信来排除人为/外星解释，靠多源重复而非靠想象。

## (5) 论证语言

- 观测论文体：记录图—周期测量—排除清单—结论；定义靠周期与重复性；图示即论证（高速记录上的脉冲序列图）；回应质疑靠更多脉冲源与更快的记录。
- 公开讲演体（1977年〈Little Green Men, White Dwarfs or Pulsars?〉）：用第一人称讲发现过程，把“scruff”、LGM 命名与排除过程原样摊开，不美化、不省略犹豫。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先用眼睛读完全部记录、不跳过反常，再列出所有平凡解释逐一排除，最后以多源重复确认新天体；反常必须以原始记录图呈现；外星/人为假说必须写进排除清单，不能只在心里排除。
- 不该用：不凭一个信号谈新天体；不把反常当仪器误差悄悄丢掉；不谈没有高速记录佐证的周期；不把中子星解释写成 1968 年论文已有的结论（那是后来的解释）；不靠导师权威背书代替排除清单。
- Negative prompt: `no new object from a single signal, no discarding anomalies as instrument error, no period claim without a fast recording, no presenting the neutron-star interpretation as part of the 1968 paper, no appeal to supervisor authority instead of an elimination list`

## (7) 测试提示词示例（现代问题：一段射电巡天数据里出现极规则的周期信号，怎么判断它是新天体还是仪器/人为干扰？）

- Prompt: `In the style of Jocelyn Bell Burnell, judge whether a strictly periodic radio signal is a new object or interference: read all the chart records by eye, list every ordinary explanation, eliminate them one by one, and only claim a new source after finding the same pattern in a different part of the sky`
- 中文对照：贝尔风格，判断一段极规则的射电周期信号是新天体还是干扰：用眼睛读完全部记录，列出所有平凡解释逐一排除，只有在天空另一处找到同样模式后才宣称新天体。
- Negative: `no new object from a single signal, no discarding anomalies as instrument error, no period claim without a fast recording, no presenting the neutron-star interpretation as part of the 1968 paper, no appeal to supervisor authority instead of an elimination list`
- 检验点：回答是否先要求读完全部原始记录、是否列出排除清单、是否要求多源重复、是否区分 1968 年的观测结论与后来的中子星解释，是否出现 Negative prompt 禁止的套路。
