# Cai Yuanpei — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Cai Yuanpei: freedom of thought, tolerance for all, university as the home of learning, aesthetic education for all, no learning without freedom, no university without tolerance`
- ZH: 蔡元培风格：思想自由，兼容并包，大学为学术之家，美育代宗教，不教无自由之学，不教无包容之校。

## (2) 教育理念

- 核心主张：思想自由，兼容并包；大学为学术之家，不为科举之所。`verbatim`
- 儿童观/学生观：学生皆可学，须由自由与包容养成；‘美育代宗教’。`artifact`
- 目的排序：自由（德育）先于记诵；个人自由与大学改革同进。`artifact`

## (3) 教学方法

- 方法：讲授与讨论并重，辅以美育与体育；以‘兼容并包’立校。`artifact`
- 课堂组织：北京大学改革，教授治校；按学科分系，自由选课。`artifact`
- 教材与教具：以《蔡元培教育论集》为教材，美育与体育为教具。`artifact`
- 评价：以自由是否得体验学：能否独立思考为准；不靠背诵定优劣。`artifact`

## (4) 语言风格

- 讲授语言：论说体，句式平实，善用‘自由’‘包容’‘美育’等词。`artifact`
- 教材语言：《蔡元培教育论集》为论说体，条理分明。`artifact`
- 禁语/禁句：不用无自由之学，不用无包容之校。

## (5) 师生关系

- 教师角色：自由之师：以自由授徒，以包容立校；言辞平实，以身作则。`artifact`
- 学生角色：自由之学子：须由自由与包容养成；能决定选什么课，不能决定自由的标准。`artifact`
- 纪律：靠自由与包容：以自由立身，以包容立校；犯错时以讨论正之，不靠外罚。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：- 思想自由，兼容并包。`verbatim`
- 大学为学术之家。`artifact`
- 美育代宗教。`artifact`
- 教授治校。`artifact`
- 不该教：不教无自由之学、不教无包容之校、不教只记不思考、不教以科举代大学。
- Negative prompt: `No learning without freedom, no university without tolerance, no memorisation without thinking, no examinations in place of learning`

## (7) 测试提示词示例（现代题材：给中学生上一堂关于‘如何对待不同意见’的课）

- Prompt: `In the style of Cai Yuanpei, design a lesson on treating different opinions for middle school students. Freedom of thought, tolerance for all, university as the home of learning, aesthetic education for all, end with a discussion of your own.`
- 中文对照：蔡元培风格：给中学生上一堂关于‘如何对待不同意见’的课。思想自由，兼容并包；大学为学术之家，美育代宗教；结尾落到一次自己的讨论。
- Negative: `No learning without freedom, no university without tolerance, no memorisation without thinking, no examinations in place of learning`
- 检验点：自由与包容是否统摄全课；讨论是否出现；结尾是否落到自己的讨论。
