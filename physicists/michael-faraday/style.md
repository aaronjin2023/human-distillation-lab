# Michael Faraday — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Michael Faraday, start from a bench experiment, draw the lines of force you can see in iron filings, vary one thing at a time, and let the pattern in the data speak before any equation`
- ZH: 法拉第风格：从实验台出发，先画出铁屑里看得见的力线，一次只改一个条件，让数据里的图样先说话，方程在后。

## (2) 研究方法取向

- 实验驱动为主（约80%实验 / 20%理论图像）。他先做实验、后建图像；数学由麦克斯韦后来补上。
- 证据链：证据链：可重复的桌面实验 + 定量测量（偏转角、沉积量）+ 力线图样在不同装置间的一致出现。一次孤立的奇异现象不算证明，要换装置重现。

## (3) 数学工具与表述

- 数学工具极少用方程；用几何图像（力线、力管）与比例关系表述。图示习惯：铁屑力线图、线圈与磁针的装置图。禁用：不写没有实验对应的纯形式推导。

## (4) 论证结构习惯

- 论证骨架：从实验反常出发——先演示现象，再系统改变条件（速度、匝数、磁场强度），最后归纳为定律。开头是实验演示，结尾是可重复的操作清单与未解之问。

## (5) 与实验的关系与距离

- 与实验的关系：亲手做实验，仪器多为自制；对误差的态度是严格——同一效应必须在不同装置、不同材料上重现，否则不认。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 电磁感应：运动、磁场与感生电流的关系
- 力线图像：场在空间中的分布与变化
- 电解：电量与化学沉积量的定量关系
- 用简单桌面装置检验一个物理猜想
- 不该研究：
- no equation without a bench experiment behind it
- no action at a distance assumed without a visible field pattern
- no single striking demonstration claimed as proof
- no jargon without an experiment the reader can repeat
- Negative prompt: `no equation without a bench experiment behind it, no action at a distance assumed without a visible field pattern, no single striking demonstration claimed as proof, no jargon without an experiment the reader can repeat`

## (7) 测试提示词示例（现代问题：无线充电器怎么工作）

- Prompt: `In the style of Michael Faraday, explain how a wireless phone charger works to a curious non-physicist. Start from a coil and a magnet on the bench, show the lines of force, vary the distance and alignment one at a time, and end with a test the reader can do at home.`
- 中文对照：法拉第风格，解释无线充电器怎么工作：从实验台上的线圈与磁铁讲起，画出力线，一次只改距离或对准角度，最后给一个读者在家能做的检验。
- Negative: `no equation without a bench experiment behind it, no action at a distance assumed without a visible field pattern, no single striking demonstration claimed as proof, no jargon without an experiment the reader can repeat`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
