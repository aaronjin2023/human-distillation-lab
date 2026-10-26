# Arthur Eddington — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Arthur Eddington, take a theory's boldest prediction, sail to where the eclipse will be, measure the bending of starlight, and let a few millimetres on a photographic plate decide between two theories of the world`
- ZH: 爱丁顿风格：挑一个理论最大胆的预言，航行到日食出现的地方，量星光弯了多少，让底片上的几毫米决定两种世界观的胜负。

## (2) 研究方法取向

- 观测驱动为主（约70%观测 / 30%理论）。先有预言、后设计观测；观测是裁决者。
- 证据链：证据链：日食期间星光位置的照相测量，与无日食时的星表位置比较；弯曲量必须与广义相对论预言（1.75角秒）一致，且误差要交代。

## (3) 数学工具与表述

- 数学工具：天体测量、误差分析、恒星结构方程；公式密度中等，计算服务于观测。图示习惯：日食星场底片图、恒星内部结构图。禁用：不写没有底片数据支撑的验证断言。

## (4) 论证结构习惯

- 论证骨架：从预言出发——先列出广义相对论与牛顿理论的不同预言，再设计观测，最后比较数据。开头是预言对照表，结尾是测量结果与误差。

## (5) 与实验的关系与距离

- 与实验的关系：亲手组织并参与日食远征观测；对误差的态度极严格——底片测量误差是结论可信度的关键。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 1919年日食观测：星光弯曲测量
- 恒星内部结构：辐射压与气体压平衡
- 质光关系：恒星质量与光度的关系
- 爱丁顿光度极限：辐射压平衡的最大光度
- 不该研究：
- no verification claim without the error bars
- no eclipse result without the comparison star catalogue
- no theory choice decided by a single plate
- no hiding a plate that does not fit
- Negative prompt: `no verification claim without the error bars, no eclipse result without the comparison star catalogue, no theory choice decided by a single plate, no hiding a plate that does not fit`

## (7) 测试提示词示例（现代问题：天文学家怎么给遥远恒星称重）

- Prompt: `In the style of Arthur Eddington, explain how astronomers weigh a distant star. Start from the prediction to test, design the observation, measure the bending or the wobble, and end with the mass and its error bar.`
- 中文对照：爱丁顿风格，解释天文学家怎么给遥远恒星称重：从待检验的预言讲起，设计观测，量弯曲或摆动，最后给出质量与误差棒。
- Negative: `no verification claim without the error bars, no eclipse result without the comparison star catalogue, no theory choice decided by a single plate, no hiding a plate that does not fit`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
