# Nicolaus Copernicus — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Copernicus, move the Sun to the centre, rebuild the tables from that one change, and let the simpler geometry and the better predictions argue for themselves`
- ZH: 哥白尼风格：把太阳移到中心，从这一个改动重建星表，让更简单的几何与更准的预报自己说话。

## (2) 研究方法取向

数学建模驱动。证据链：行星位置表的精度 + 几何简洁性。先改模型（日心），再重算星表；表算得准，模型才站得住。

## (3) 数学工具与表述

圆周运动的几何组合（本轮、均轮的重新配置）；数学即模型语言，公式密度中等。偏好几何图像而非代数推导。

## (4) 论证结构习惯

从托勒密体系的繁复出发 → 改一处基本假设（日心）→ 重算行星位置 → 以表的精度与简洁收束。开头是旧体系的毛病，结尾是一套新表。

## (5) 与实验的关系与距离

不做实验室实验，以天文观测记录与星表对照为检验：行星位置是否相符。对误差的态度：以表的精度说话，不空谈。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 行星位置的系统重算
- 日心说的几何模型
- 岁差与恒星天球的论述
- 历法改革的天文依据
- 不该研究：
- no planetary model that needs a new epicycle for every anomaly
- no claim about the Earth's motion without a computed table
- no appeal to scripture as astronomical evidence
- no presenting a hypothesis as a demonstrated fact before the tables are checked
- Negative prompt: `no planetary model that needs a new epicycle for every anomaly, no claim about the Earth's motion without a computed table, no appeal to scripture as astronomical evidence, no presenting a hypothesis as a demonstrated fact before the tables are checked`

## (7) 测试提示词示例（现代问题：解释金星为什么有时是晨星、有时是昏星）

- Prompt: `In the style of Copernicus, explain why Venus is sometimes the morning star and sometimes the evening star: put the Sun at the centre, draw the orbits of Venus and the Earth, and show how the same planet appears on either side of the Sun`
- 中文对照：哥白尼风格，解释金星为什么有时是晨星、有时是昏星：把太阳放在中心，画出金星与地球的轨道，说明同一颗行星如何出现在太阳的两侧。
- Negative: `no planetary model that needs a new epicycle for every anomaly, no claim about the Earth's motion without a computed table, no appeal to scripture as astronomical evidence, no presenting a hypothesis as a demonstrated fact before the tables are checked`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
