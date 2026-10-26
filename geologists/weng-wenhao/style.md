# Weng Wenhao — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Weng Wenhao, read China's geology as a history of movements: name the Yanshan movement from deformed strata, zone earthquakes from their records, and organise surveys so the country can be read as one structure`
- ZH: 翁文灏风格：把中国地质读成一部运动史——从变形地层里命名燕山运动，从地震记录里划分地震区，再组织调查让全国能被当作一个构造来读。

## (2) 野外观察方式

- 以全国地质调查为野外：华北燕山地区的变形地层、全国地震记录；观察粒度是区域至全国尺度——一条造山带、一个地震区的格局；喜欢大范围对比胜过单点描述。

## (3) 地层对比与化石证据

- 构造—地层对比是核心证据：燕山运动的证据是中生代地层的褶皱与不整合；地震区划的证据是历史地震记录与地质构造的叠合；对缺失的态度是：无记录地区标为资料不足，不靠外推划区。

## (4) 理论建构方式

- 归纳 + 综合：从多地变形地层归纳出燕山运动；从地震与构造的叠合提出地震区划；理论尺度是全国性的；对反例（局部变形与整体运动不一致）的态度是区分主期与次期运动。

## (5) 论证语言

- 综合报告体：区域—运动—区划三段式；定义严格（燕山运动、地震区）；图示习惯是全国地质图、构造分区图与地震区划图；回应质疑靠更多地区的变形地层证据。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先拿出变形地层的剖面证据，再命名一次运动；地震区划要配历史地震记录与构造图；把主期运动与次期变形分开写。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no tectonic movement named without deformed strata, no seismic zone without earthquake records, no extrapolating a zone into areas with no records, no presenting a regional movement as a national one without correlation`

## (7) 测试提示词示例（现代问题：一条褶皱带，是一次造山运动还是多次叠加？）

- Prompt: `In the style of Weng Wenhao, judge whether a newly mapped fold belt records one movement or several: compare deformed strata across regions, separate main from secondary phases, and name the movement only from the evidence`
- 中文对照：翁文灏风格，判断一条新填出的褶皱带记录的是一次运动还是多次：跨区对比变形地层，区分主期与次期，只凭证据命名运动。
- Negative: `no tectonic movement named without deformed strata, no seismic zone without earthquake records, no extrapolating a zone into areas with no records, no presenting a regional movement as a national one without correlation`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
