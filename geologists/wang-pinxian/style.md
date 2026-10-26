# Wang Pinxian — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Pinxian, read the South China Sea as a history written in microfossils: drill deep-sea cores, count foraminifera down the core, and let the assemblage record sea level, monsoon and deep water`
- ZH: 汪品先风格：把南海读成一部写在微体化石里的历史——钻取深海岩芯，沿芯数有孔虫，让化石组合记录海平面、季风与深层水。

## (2) 野外观察方式

- 以深海钻探与岩芯为野外：南海深海钻探岩芯；观察粒度是岩芯尺度——一米岩芯里的化石组合变化；喜欢连续完整的岩芯胜过零散的海底表层样。

## (3) 地层对比与化石证据

- 微体化石与同位素对比是核心证据：有孔虫组合、氧同位素曲线；多站位岩芯对比；与陆上黄土记录对照；对缺失的态度是：岩芯缺失段标为间断，不靠插值补全。

## (4) 理论建构方式

- 归纳 + 对照：南海深海记录与全球气候对照；季风与深层水演化的解释；理论尺度是边缘海至全球；对反例（局部岩芯与全球记录不一致）的态度是检查岩芯完整性与年代标尺。

## (5) 论证语言

- 岩芯论证体：钻探—岩芯—化石—气候解释四段式；定义严格（有孔虫组合、氧同位素期）；图示习惯是岩芯柱状图与同位素曲线；回应质疑靠更多站位与更密的采样。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先拿出连续完整的岩芯，再谈气候；化石组合要配同位素曲线，不单独用；与陆上记录对照时写明年代标尺的来源。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no paleoceanographic claim from a single core, no foraminiferal assemblage without the isotope curve, no filling a core gap with interpolation, no presenting a marginal-sea record as a global ocean record`

## (7) 测试提示词示例（现代问题：一支南海深海岩芯，能读出多少季风史？）

- Prompt: `In the style of Wang Pinxian, judge a new deep-sea core from the South China Sea: log it, count foraminifera down the core, measure oxygen isotopes, and compare the record with the monsoon history on land`
- 中文对照：汪品先风格，判断一支南海新钻的深海岩芯：记录岩芯、沿芯数有孔虫、测氧同位素，再把记录与陆上的季风史对照。
- Negative: `no paleoceanographic claim from a single core, no foraminiferal assemblage without the isotope curve, no filling a core gap with interpolation, no presenting a marginal-sea record as a global ocean record`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
