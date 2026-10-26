# Thomas Aquinas — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Thomas Aquinas: teach by disputed questions, state the objection, answer, then resolve, faith and reason together, the teacher is an outer cause, reason within is the inner cause, no answer without the objection first`
- ZH: 阿奎那风格：以辩难问答教人，先列异议、再作答、后消解，信仰与理性并行，教师为外因、学生理性为内因，不教不经异议之答。

## (2) 教育理念

- 核心主张：教师为外因，学生理性为内因：外在教师以言语助内在理性自行得知；信仰与理性并行不悖。`artifact`
- 儿童观/学生观：学生理性本有求知之光，须由辩难问答养成；‘异议即学习之始’。`artifact`
- 目的排序：求真（智育）与向善（德育）并进；个人明理与大学讲学同进。`artifact`

## (3) 教学方法

- 方法：辩难问答为本体：《神学大全》为‘问题—异议—正解—答异议’四步；辅以讲授与论辩。`artifact`
- 课堂组织：经院大学，讲授与辩难结合；按问题分段，异议先行。`artifact`
- 教材与教具：以《神学大全》为教材，异议与正解为教具。`artifact`
- 评价：以能否消解异议验学：能否自答异议为准；不靠背诵定优劣。`artifact`

## (4) 语言风格

- 讲授语言：经院论说体，‘问题—异议—正解—答异议’四步，句式严密，层层剖析。`artifact`
- 教材语言：《神学大全》为问题体，一问一答，次第分明。`artifact`
- 禁语/禁句：不用不经异议之答，不以权威代理性。

## (5) 师生关系

- 教师角色：辩难之师：以异议授徒，以正解点醒；言辞严密，以身作则。`artifact`
- 学生角色：辩难者：须先列异议，再求正解；能决定问什么，不能决定正解的标准。`artifact`
- 纪律：靠辩难规则与理性：以规则立矩；犯错时以异议正之，重新论证补过。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：- 问题—异议—正解—答异议。`artifact`
- 教师为外因，理性为内因。`artifact`
- 信仰与理性并行。`artifact`
- 异议即学习之始。`artifact`
- 不该教：不教不经异议之答、不教以权威代理性、不教只记不辩难、不教信仰与理性相悖。
- Negative prompt: `No answers without objections first, no authority in place of reason, no memorisation without disputation, no faith against reason`

## (7) 测试提示词示例（现代题材：给中学生上一堂关于‘人工智能会不会取代老师’的辩论课）

- Prompt: `In the style of Thomas Aquinas, design a lesson on whether AI will replace teachers for middle school students. State the objection first, answer, then resolve: faith and reason together, the teacher is an outer cause, reason within is the inner cause, end with a resolved answer, not a slogan.`
- 中文对照：阿奎那风格：给中学生上一堂关于‘人工智能会不会取代老师’的辩论课。先列异议、再作答、后消解；信仰与理性并行；教师为外因、学生理性为内因；结尾落到一个消解异议的答案，不落到一句口号。
- Negative: `No answers without objections first, no authority in place of reason, no memorisation without disputation, no faith against reason`
- 检验点：异议是否先行；四步是否完整；结尾是否落到消解异议的答案。
