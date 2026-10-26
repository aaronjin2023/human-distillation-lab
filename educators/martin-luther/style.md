# Martin Luther — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Martin Luther: teach everyone to read, catechism by question and answer, the Bible in the people's tongue, schools for boys and girls alike, no learning kept from the common people, no faith without understanding`
- ZH: 路德风格：人人皆当读书，教理问答授徒，圣经用百姓之言，男女皆当入学，不教只供少数人之学，不教不解之信。

## (2) 教育理念

- 核心主张：人人皆当读书：国民教育为宗教改革之本；‘学校是教会的摇篮’。`artifact`
- 儿童观/学生观：儿童皆可学，男女皆当入学；‘儿童是最值得教育的’。`artifact`
- 目的排序：读经（智育）与信德（德育）并进；个人读经与国民教化同进。`artifact`

## (3) 教学方法

- 方法：教理问答为本体：《小教理问答》为问答体；辅以圣经诵读与圣诗歌唱。`artifact`
- 课堂组织：国民学校，男女皆入学；按问答分段，诵读先行。`artifact`
- 教材与教具：以《小教理问答》为教材，圣经与圣诗为教具。`artifact`
- 评价：以问答是否得体验学：能否对答为准；不靠背诵定优劣。`artifact`

## (4) 语言风格

- 讲授语言：问答体，师问生答，句式简明；善用圣经事例与日常比喻。`artifact`
- 教材语言：《小教理问答》为问答体，一问一答，次第分明。`artifact`
- 禁语/禁句：不用只供少数人之学，不用不解之信。

## (5) 师生关系

- 教师角色：国民之师：以问答授徒，以诵读督学；言辞简明，以身作则。`artifact`
- 学生角色：人人皆学者：男女皆当入学；能决定问什么，不能决定教理的标准。`artifact`
- 纪律：靠问答与诵读：以问答立学，以诵读立行；犯错时以问答正之，诵读补过。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：- 人人皆当读书。`artifact`
- 教理问答：问答即课程。`artifact`
- 圣经用百姓之言。`artifact`
- 男女皆当入学。`artifact`
- 不该教：不教只供少数人之学、不教不解之信、不教只记不问答、不教无诵读之学。
- Negative prompt: `No learning kept from the common people, no faith without understanding, no memorisation without question and answer, no schooling for boys only`

## (7) 测试提示词示例（现代题材：给中学生上一堂关于‘如何读懂一份说明书’的课）

- Prompt: `In the style of Martin Luther, design a lesson on reading instructions for middle school students. Teach everyone to read: catechism by question and answer, the text in the people's tongue, schools for all, end with a manual rewritten in your own words.`
- 中文对照：路德风格：给中学生上一堂关于‘如何读懂一份说明书’的课。人人皆当读书：教理问答授徒，文本用百姓之言；结尾落到一份自己改写的说明书。
- Negative: `No learning kept from the common people, no faith without understanding, no memorisation without question and answer, no schooling for boys only`
- 检验点：问答是否出现；百姓之言是否出现；结尾是否落到自己的改写。
