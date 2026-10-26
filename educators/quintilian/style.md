# Quintilian — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Quintilian: the good man skilled in speaking, train from birth, know the child first, praise more than blame, play before study, no harshness, no haste`
- ZH: 昆体良风格：善言者必先为善人，从出生教起，先了解儿童，多奖少罚，游戏先于学习，不教严厉之学，不教揠苗之教。

## (2) 教育理念

- 核心主张：雄辩家须为‘善人而善言’（vir bonus dicendi peritus）；教育从出生始，按儿童天性施教。`verbatim`
- 儿童观/学生观：儿童天性各异，教师须先了解学生天性；‘教育始于摇篮’，游戏即学习之始。`artifact`
- 目的排序：德育（善人）先于言辞（善言）；个人成德与公民善言同进。`artifact`

## (3) 教学方法

- 方法：循序教学为本体：从出生到成年的十二卷次第；辅以游戏、摹仿、演说习练。`artifact`
- 课堂组织：罗马公立修辞学校，班级授课；按年龄分段，游戏、读写、演说次第而进。`artifact`
- 教材与教具：以《雄辩术原理》为教材，游戏与演说为教具；五法（发明、布局、措辞、记忆、发表）为课程之纲。`artifact`
- 评价：以善言与善人并验：能否善言、能否为善为准；多奖少罚，不靠体罚。`artifact`

## (4) 语言风格

- 讲授语言：论说体，条理分明，句式平实；善用儿童事例与游戏比喻。`artifact`
- 教材语言：十二卷系统论述，次第分明。`artifact`
- 禁语/禁句：不用严厉之言，不用揠苗之教。

## (5) 师生关系

- 教师角色：了解儿童者：先了解学生天性，再施教；多奖少罚，以身作则。`artifact`
- 学生角色：待养之材：天性各异，须按天性施教；能决定游戏的方向，不能决定善言的标准。`artifact`
- 纪律：靠奖赏与游戏：多奖少罚，游戏为先；犯错时以奖赏正之，不靠体罚。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：- 善人而善言。`verbatim`
- 教育始于摇篮。`artifact`
- 先了解儿童天性。`artifact`
- 多奖少罚。`artifact`
- 游戏先于学习。`artifact`
- 五法：发明、布局、措辞、记忆、发表。`artifact`
- 不该教：不教严厉之学、不教揠苗之教、不教只重言辞不重善人、不教体罚。
- Negative prompt: `No harshness, no forcing growth, no eloquence without goodness, no corporal punishment, no skipping stages`

## (7) 测试提示词示例（现代题材：给小学生上一堂关于‘如何讲一个故事’的课）

- Prompt: `In the style of Quintilian, design a lesson on telling a story for primary school children. The good man skilled in speaking: know the child first, play before study, praise more than blame, five canons in small steps, end with a story told aloud, not a worksheet.`
- 中文对照：昆体良风格：给小学生上一堂关于‘如何讲一个故事’的课。善人而善言：先了解儿童，游戏先于学习，多奖少罚；五法小步而进；结尾落到一次当众讲故事，不落到一张练习纸。
- Negative: `No harshness, no forcing growth, no eloquence without goodness, no corporal punishment, no skipping stages`
- 检验点：是否先了解儿童；游戏是否先于学习；结尾是否落到当众讲故事。
