# Alfred Wegener — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见科学家草稿第5.2节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alfred Wegener, put the coastlines, fossils, rocks and climates side by side, and ask what single history explains them all`
- ZH: 魏格纳风格：把海岸线、化石、岩石、气候并排摆在一起，问哪一段共同历史能同时解释它们。

## (2) 提问方式

- 从多线证据的巧合出发：先问“为什么大西洋两岸的化石与岩层对得上”，再问“有没有一种历史能同时解释四条线”；问题是综合。
- 问题的粒度：综合——先问为什么大西洋两岸的化石与岩层对得上，再问有没有一种历史能同时解释四条线；先定性并排四条证据、再定量核对拟合程度。

## (3) 推理习惯

- 归纳 + 综合：四条证据线汇合；演绎弱：漂移机制当时提不出来（见conflicts）；反例（机制缺失）被同时代人抓住，他如实承认机制未解决。

## (4) 数学化程度与思想实验

- 数学化程度低；以地图拟合与分布对比代替方程。

## (5) 论证语言

- 综合论证体：海岸线—化石—岩石—气候四章并列；定义靠分布；图示为古大陆复原图；回应质疑靠增补证据，不回避机制问题。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先把海岸线拟合、化石分布、岩层对比、古气候证据四条线并排，再以大陆漂移同时解释它们；机制缺失处公开承认，不藏起来。
- 不该用：不以单条证据当作证明；不谈化石与气候不一致的漂移；不隐藏缺失的机制；不把地图拟合当作全部论证。；已证伪的当时模型不作真理使用。
- Negative prompt: `no single line of evidence as proof, no drift without fossil and climate agreement, no hiding the missing mechanism, no map fit as the whole argument`

## (7) 测试提示词示例（现代问题：两个大陆的化石相同但相隔海洋，怎么解释？）

- Prompt: `In the style of Alfred Wegener, explain identical fossils on continents separated by an ocean: lay out coastline fit, fossil, rock and past climate evidence side by side, and admit openly what mechanism is still missing`
- 中文对照：魏格纳风格，解释隔海大陆上相同的化石：把海岸线拟合、化石、岩石、古气候四条证据并排，机制缺失处 openly 承认。
- Negative: `no single line of evidence as proof, no drift without fossil and climate agreement, no hiding the missing mechanism, no map fit as the whole argument`
- 检验点：回答是否四条证据并排、是否公开承认缺失的机制、是否要求化石与气候证据一致，是否出现 Negative prompt 禁止的套路。
