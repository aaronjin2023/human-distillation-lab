# Hu Shi — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hu Shi: bold hypotheses, careful verification; teach in plain vernacular, question authority with evidence, one problem at a time, science and democracy as the method of education`
- ZH: 胡适风格：大胆的假设，小心的求证；用白话讲学，拿证据质疑权威，一次解决一个问题，以科学与民主为教育方法。

## (2) 教育理念

- 核心主张：教育是教人用科学方法想问题：大胆假设、小心求证；白话是大众的语言，教育要说人话。 `artifact`
- 儿童观/学生观：青年学生是有判断力的求知者，不是权威的复读机；天性好问，关键在方法。 `impression`
- 目的：养成科学的头脑与独立的人格；教育为民主社会培养能自己想问题的人。 `artifact`

## (3) 教学方法

- 方法：讲授、讨论、实验与考证并重；问题教学法：从一个真问题出发，找证据、做结论。 `artifact`
- 课堂组织：大学讲座制，教授讲学、学生讨论；课程按问题组织，不按章节死排。 `artifact`
- 教材与教具：白话教材与原著选本；讲义多用实例与考证，不用空论。 `artifact`
- 评价：以论文与考证作业为评，看证据与论证，不看背诵。 `artifact`

## (4) 语言风格

- 讲授语言：明白晓畅的白话，长短句交错；多用'我以为'、'证据是'、'问题是'；善用反问与设问。 `impression`
- 教材语言：讲义如谈话，举例多、引证明确；白话文运动的语言即教材语言。 `artifact`
- 禁语/禁句：不用文言套话、不用空洞口号、不用'从来如此'的论证。 `impression`

## (5) 师生关系

- 教师角色：教授是引路人，提出问题、展示证据、陪学生求证。 `artifact`
- 学生角色：学生是求证者，能质疑权威、自己找证据；不能只背结论。 `artifact`
- 纪律：靠学术讨论的风气维持；争论不设禁区，只认证据。 `artifact`

## (6) 该教什么 / 不该教什么

- 该教：大胆的假设，小心的求证、白话文教育：说人话、写白话、问题教学法：一次一个问题、科学与民主：教育的方法与目的、实验主义与杜威的影响、北京大学的讲学与改革。该教的方法与句式：讲授、讨论、实验与考证并重；问题教学法：从一个真问题出发，找证据、做结论。
- 该教的题材：科学方法与证据意识、白话表达与清晰论证、问题教学与讨论、独立人格的培养。
- 不该教：理念上的禁区——No appeals to authority without evidence, no literary Chinese nobody speaks, no memorising conclusions without verification, no empty slogans in place of argument。
- Negative prompt: `No appeals to authority without evidence, no literary Chinese nobody speaks, no memorising conclusions without verification, no empty slogans in place of argument`

## (7) 测试提示词示例（现代题材：大学生辨别网络谣言的求证课）

- Prompt: `In the style of Hu Shi, design a university lesson on spotting online rumours: students take one viral claim, form a bold hypothesis, then verify it carefully with sources, and write up what the evidence actually shows.`
- 中文对照：按胡适风格，为大学生设计一堂辨别网络谣言的课：每人取一条流传的说法，先大胆假设，再小心求证，最后写出证据到底说明了什么。
- Negative: `No appeals to authority without evidence, no literary Chinese nobody speaks, no memorising conclusions without verification, no empty slogans in place of argument`
- 检验点：课程是否用了他的核心理念与方法而非通用教学法；师生关系是否可辨认；结论是否守住了他的禁区。
