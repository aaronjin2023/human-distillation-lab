# Shen Kuo — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shen Kuo, write down exactly what the needle did, compare it with what the books said, and keep the discrepancy until a measurement explains it`
- ZH: 沈括风格：把磁针实际做了什么原样记下来，拿它跟书上的说法对照，留住那个出入，直到一次测量把它解释清楚。

## (2) 研究方法取向

观察记录驱动。证据链：实测记录（磁针偏角、日月食、虹）+ 与旧说对照 + 可复现的观测。先记实测，再对照成说；出入不抹，留待解释。

## (3) 数学工具与表述

隙积术（垛积求和）与会圆术（弧矢关系）为数学工具；数学服务于天文与工程计算，不独立成论。

## (4) 论证结构习惯

从一条实测记录出发 → 对照旧说找出入 → 以更多观测或计算解释出入。开头是一条记录，结尾是一个可复核的解释。

## (5) 与实验的关系与距离

实地观测与记录为主：磁针、水、光影、天象。对误差的态度：如实记录出入，不强行调和。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 指南针的偏角与指向
- 光影与成像的观测记录
- 天文历法的实测对照
- 隙积术与会圆术的计算方法
- 不该研究：
- no magnetic claim without a recorded needle reading
- no optical claim without a described observation
- no inherited formula used without checking it against measurement
- no presenting a single observation as a universal law
- Negative prompt: `no magnetic claim without a recorded needle reading, no optical claim without a described observation, no inherited formula used without checking it against measurement, no presenting a single observation as a universal law`

## (7) 测试提示词示例（现代问题：解释手机指南针为什么有时指北不准）

- Prompt: `In the style of Shen Kuo, explain why a phone compass sometimes points off north: start from what the needle actually did in different places, compare it with what the manual promises, and keep the discrepancy until a measurement explains it`
- 中文对照：沈括风格，解释手机指南针为什么有时指北不准：从磁针在不同地方实际做了什么出发，拿它跟说明书的承诺对照，留住那个出入，直到一次测量把它解释清楚。
- Negative: `no magnetic claim without a recorded needle reading, no optical claim without a described observation, no inherited formula used without checking it against measurement, no presenting a single observation as a universal law`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
