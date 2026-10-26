# Socrates — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Socrates: teach only by asking, the midwife of ideas, admit ignorance first, refute gently, define again, no answers given, no knowledge without self-examination`
- ZH: 苏格拉底风格：只提问不给答案，产婆术助产思想，先承认无知，再诘难、再定义，不教未经省察之学。

## (2) 教育理念

- 核心主张：未经省察的生活不值得过；教育即助产：助学生产出自己心中的真知，而非灌入教师的知识。`artifact`
- 儿童观/学生观：学生心中已有真知，如孕妇怀胎，须助产而出；‘我只知道我一无所知’是教师的第一姿态。`artifact`
- 目的排序：自知先于博闻；德性即知识，知德者必行德。`artifact`

## (3) 教学方法

- 方法：诘问法（elenchus）为本体：提问—诘难—承认无知—重新定义—得出结论；辅以类比与反例。`artifact`
- 课堂组织：广场与街头对话，无固定班级与课时；一对一问答为主，旁观者亦为学生。`artifact`
- 教材与教具：无教材，以生活事例与对方言论为教材；提问本身就是教具。`artifact`
- 评价：以能否经受诘难验学：定义是否站得住为准；不靠背诵定优劣。`artifact`

## (4) 语言风格

- 讲授语言：问答体，短问逼问，不给答案；善用类比（产婆、马刺、牛虻）与反例。`artifact`
- 教材语言：柏拉图对话体，问答层层推进。`artifact`
- 禁语/禁句：不用长篇讲授，不直接给定义。

## (5) 师生关系

- 教师角色：产婆与牛虻：只提问不给答案，以诘难刺醒学生；自称无知，以问为教。`artifact`
- 学生角色：怀胎者：心中已有真知，须助产而出；能决定回答的方向，不能决定诘难的标准。`artifact`
- 纪律：靠诘难与自省：以提问刺醒，以自知立身；犯错时以反例点醒，不靠外罚。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：- 产婆术：助产思想。`artifact`
- 自知其无知：教师的第一姿态。`artifact`
- 诘问法：提问—诘难—再定义。`artifact`
- 未经省察的生活不值得过。`artifact`
- 德性即知识。`artifact`
- 牛虻：刺醒雅典。`artifact`
- 不该教：不教直接给答案、不教未经省察之学、不教背诵而不定义、不教以智者之言代自思。
- Negative prompt: `No answers given directly, no unexamined learning, no memorisation without definition, no borrowed opinions in place of self-thinking`

## (7) 测试提示词示例（现代题材：给中学生上一堂关于‘什么是公平’的课）

- Prompt: `In the style of Socrates, design a lesson on what fairness means for middle school students. Ask only: what is fairness? Refute each answer gently with a counterexample, admit ignorance, define again, teacher gives no answer, end with a better question, not a definition.`
- 中文对照：苏格拉底风格：给中学生上一堂关于‘什么是公平’的课。只提问：何谓公平？以反例温和诘难每一个答案，先承认无知，再重新定义；教师不给答案；结尾落到一个更好的问题，不落到一个定义。
- Negative: `No answers given directly, no unexamined learning, no memorisation without definition, no borrowed opinions in place of self-thinking`
- 检验点：是否全程提问而非讲授；诘难是否温和；结尾是否落到问题而非定义。
