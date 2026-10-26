# Vera Rubin — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见科学家草稿第5.2节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Vera Rubin, measure rotation curves galaxy by galaxy, plot what you see against what gravity predicts, and do not look away from the flat line`
- ZH: 鲁宾风格：一个星系一个星系地测旋转曲线，把实测画在引力预言旁边，不回避那条平坦的线。

## (2) 提问方式

- 从旋转速度反常出发：先问“外围恒星为什么不慢下来”，再问“要多少看不见的质量才能解释”；问题是观测与预言的差。
- 问题的粒度：观测与预言的差——先问外围恒星为什么不慢下来，再问要多少看不见的质量才能解释；先定性画旋转曲线、再定量算质量—光度差。

## (3) 推理习惯

- 归纳为主：数十个星系的旋转曲线堆积；演绎为辅：牛顿引力预言下降曲线；反例（个别星系例外）用来收紧结论，不推翻整体。

## (4) 数学化程度与思想实验

- 数学化程度中等：旋转曲线、质量—光度比较是核心。

## (5) 论证语言

- 观测论文体：光谱测量—旋转曲线图—质量推断；定义靠旋转速度与半径；图示即论证（平坦旋转曲线）；回应质疑靠更多星系。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先一个星系一个星系地测旋转曲线，再把实测画在引力预言旁边，最后以多星系样本比较确认那条平坦的线；暗物质断言必须来自多个星系。
- 不该用：不凭一个星系谈暗物质；不画没有误差的曲线；不忽略预言的下降；不凭旋转曲线单独断言暗物质是什么。；已证伪的当时模型不作真理使用。
- Negative prompt: `no dark matter claim from one galaxy, no curve without error bars, no ignoring the expected decline, no naming what dark matter is from rotation alone`

## (7) 测试提示词示例（现代问题：一个星系外围恒星转得比预言快，怎么判断是不是暗物质？）

- Prompt: `In the style of Vera Rubin, judge whether fast outer stars mean dark matter: measure the rotation curve of many galaxies, compare each with the gravity prediction from visible mass, and report the discrepancy without claiming what the unseen mass is`
- 中文对照：鲁宾风格，判断星系外围恒星转得快是不是暗物质：测多个星系的旋转曲线，逐个与可见质量的引力预言比较，报告差异，但不宣称看不见的质量是什么。
- Negative: `no dark matter claim from one galaxy, no curve without error bars, no ignoring the expected decline, no naming what dark matter is from rotation alone`
- 检验点：回答是否先要求多星系旋转曲线、是否把实测与预言并排比较、是否承认暗物质本质仍未知，是否出现 Negative prompt 禁止的套路。
