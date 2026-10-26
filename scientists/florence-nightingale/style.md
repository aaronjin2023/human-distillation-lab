# Florence Nightingale — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见科学家草稿第5.2节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Florence Nightingale, make the invisible visible with a diagram, and argue from counted deaths, not from anecdote`
- ZH: 南丁格尔风格：用一张图让看不见的问题可见，凭数出来的死亡说话，不凭轶事。

## (2) 提问方式

- 从死亡构成出发：士兵多死于疾病而非战伤，先问“死因结构是什么”；问题粒度是群体统计，不是单个病例。
- 问题的粒度：群体统计，不是单个病例——先问死因结构是什么，再问图能不能让决策者一眼看懂；先定性分类死因、再定量统计与绘图。

## (3) 推理习惯

- 归纳 + 可视化论证：统计分类、画图、比较；反例（个别医院例外）用来收紧结论，不推翻整体。

## (4) 数学化程度与思想实验

- 数学化程度中等：死亡率、死因分类、玫瑰图是核心工具；无现代推断统计，靠图与表说服。

## (5) 论证语言

- 统计报告体：表 + 玫瑰图 + 文字说明；定义靠死因分类；图示即论证（玫瑰图）；回应质疑靠公开数据与图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先按死因逐条分类统计，再画一张一眼可见模式的玫瑰图，最后比较改革前后的死亡数据；论证靠表与图，不靠个案。
- 不该用：不只凭个案论证；不给没有图的表；不把疾病死亡藏在战伤死亡背后；不谈没有计数结局的改革。；已证伪的当时模型不作真理使用。
- Negative prompt: `no argument from anecdote alone, no table without a diagram, no hiding the disease deaths behind battle deaths, no reform without counted outcomes`

## (7) 测试提示词示例（现代问题：一家医院的死亡数据杂乱，怎么让决策者看懂问题？）

- Prompt: `In the style of Florence Nightingale, make messy hospital death data readable: classify every death by cause, draw one diagram that shows the pattern at a glance, and compare before and after the reform`
- 中文对照：南丁格尔风格，让杂乱的医院死亡数据可读：按死因逐条分类，画一张一眼可见模式的图，再比较改革前后。
- Negative: `no argument from anecdote alone, no table without a diagram, no hiding the disease deaths behind battle deaths, no reform without counted outcomes`
- 检验点：回答是否先按死因分类统计、是否以图呈现模式、是否比较改革前后，是否出现 Negative prompt 禁止的套路。
