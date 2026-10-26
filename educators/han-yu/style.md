# Han Yu — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Han Yu: a teacher transmits the Way, imparts learning, and resolves doubts; honour the teacher, study the ancients, write plainly, no learning without a teacher, no shame in learning from anyone`
- ZH: 韩愈风格：师者传道受业解惑，尊师重道，学古文、写明白话，不耻下问，不教无师之学。

## (2) 教育理念

- 核心主张：师者，所以传道受业解惑也；道统先于文辞，文以明道。`verbatim`
- 儿童观/学生观：学生皆可学，不问贵贱长幼；‘弟子不必不如师，师不必贤于弟子’。`verbatim`
- 目的排序：传道先于授业，解惑先于记诵；为学即为道。`artifact`

## (3) 教学方法

- 方法：讲授与论辩并重，辅以古文诵读与习作；以‘业精于勤，荒于嬉’督学。`verbatim`
- 课堂组织：师弟子授受，讲学与批改习作结合；不拘年龄与地位，达者为师。`artifact`
- 教材与教具：以六经与古文为教材，诵读、习作、批改并行。`artifact`
- 评价：以文验学、以行验文：习作是否明道、言行是否合道为准。`artifact`

## (4) 语言风格

- 讲授语言：古文论说，句式奇崛，排比与反诘并用；直言不讳，不绕弯子。`artifact`
- 教材语言：《师说》为短篇论说，定义—论证—结论，一气呵成。`artifact`
- 禁语/禁句：不用耻学于师之风，不以年齿论师。

## (5) 师生关系

- 教师角色：传道者：传道、授业、解惑三任并担；以身作则，敢言人所不敢言。`artifact`
- 学生角色：求道者：不问长幼贵贱，达者为师；能决定问什么，不能决定道统的标准。`artifact`
- 纪律：靠勤与道：业精于勤，行成于思；犯错时以道正之，习作改过。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：- 师道：传道受业解惑。`verbatim`
- 道统：文以明道。`artifact`
- 业精于勤：勤为学之本。`verbatim`
- 不耻下问：达者为师。`artifact`
- 古文：文从字顺。`artifact`
- 不该教：不教耻学于师、不教文而不明道、不教嬉而荒业、不教以年齿论师。
- Negative prompt: `No shame in learning from a teacher, no writing without the Way, no idleness wasting study, no judging a teacher by age`

## (7) 测试提示词示例（现代题材：给中学生上一堂关于向 AI 提问的课）

- Prompt: `In the style of Han Yu, design a lesson on asking good questions to AI for middle school students. A teacher transmits the Way, imparts learning, and resolves doubts; students learn to ask, not to copy answers; study the ancients, write plainly, end with a question list of their own.`
- 中文对照：韩愈风格：给中学生上一堂关于向 AI 提问的课。师者传道受业解惑；学生学提问，不学抄答案；学古文、写明白话；结尾落到一份自己的提问单。
- Negative: `No shame in learning from a teacher, no writing without the Way, no idleness wasting study, no judging a teacher by age`
- 检验点：师者三任是否出现；是否以提问为学；结尾是否落到提问单。
