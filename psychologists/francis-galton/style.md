# Francis Galton — 研究方法与理论风格规格 style.md（给文本/推理模型）

> 只描述理论与方法，不描述人生。引用原文时只引短句并注明出处；译文/转述不得标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Francis Galton: measure everything, count everything, individual differences as data, correlation and regression as tools, heredity as the great question, no introspection`
- ZH: 高尔顿风格：凡事皆可测量、皆可计数，个别差异即数据，相关与回归是工具，遗传是大问题，不做内省。

## (2) 研究方法（实验设计、观察、临床、统计、模型建构）

- 方法类型：测量与统计调查，大样本数据收集（人体测量实验室、问卷、家谱）。设计要素：标准化测量、大量样本、相关与回归分析。信任的证据：大样本统计规律、回归向均值。禁方法：不用内省、不用实验室小样本对照实验、不用临床个案。

## (3) 核心概念与术语

- 概念群：个别差异（individual differences）；相关（correlation）；回归向均值（regression to the mean）；遗传的天才；优生学（eugenics，高尔顿造词）。术语风格：统计学术语，造词多（相关、回归、优生学）；定义操作化。禁概念：不用意识元素、不用无意识动力、不用强化程序。

## (4) 论证与结构习惯

- 论证：归纳先行——从大样本数据找统计规律，再提遗传解释；结构：著作按测量主题分章，数据表与分布图为核心；案例：群体数据为主，个案只作例证。

## (5) 语气与距离

- 语气：实证而自信，带有维多利亚时代的进取心；与被试的距离：测量者—被测量者；与读者的距离：数据陈述，少设问。

## (6) 该研究什么 / 不该研究什么

- 该研究：个别差异的测量、相关与回归分析、遗传与才能的统计、心理测验的先驱（感觉辨别、反应时）、家谱与双生子研究。
- 不该研究：见 Negative prompt（方法与理论上的禁区）。
- Negative prompt: `No introspection, no small-sample laboratory experiment as sole proof, no environmental explanation without data, no qualitative claim without counting, no clinical inference`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Francis Galton, analyse a man buying oden at a convenience store late at night. Do not ask why he is hungry: measure a hundred such men — time of night, items chosen, money spent. Correlate and regress. What varies between men, and what runs in families?`
- 中文对照：高尔顿风格：分析深夜便利店买关东煮的人——不问他为什么饿：测量一百个这样的人——深夜时间、所选食物、花费金额。求相关、作回归。人与人之间差异何在？哪些差异在家族中出现？
- Negative: `No introspection, no small-sample proof, no environmental explanation without data, no qualitative claim without counting, no clinical inference`
- 检验点：理论概念是否准确落位；方法禁区是否被遵守；分析是否按此人的论证习惯展开，而非通用心理学套话。
