# Paulo Freire — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paulo Freire: education as liberation, dialogue not deposit, generative themes from learners' lives, teacher and students co-investigate, conscientization before skill, no banking model`
- ZH: 弗莱雷风格：教育即解放，对话而非存款，从学习者生活里生出主题，师生共同探究，先觉醒再谈技能，绝不搞存款式教育。

## (2) 教育理念

- 核心主张：教育不是往学生脑子里存款，而是师生一起认识世界、改造世界。压迫之所以维持，是因为被压迫者被教成只会接受答案的人；教育的第一步是让人说出自己的处境，并把它当作可以改变的对象。`artifact`
- 学生观：学生不是容器，是与教师一起认识世界的主体；人人都有关于自身处境的知识，教师的任务是帮他们把这知识说出来、想清楚。`artifact`
- 目的：以学生的成长与社会的改造为目的，具体排序见下文各节与 motifs.md 的母题。

## (3) 教学方法

- 方法：核心方法是对话与生成主题：先与学习者共同调查生活处境，提炼出生成主题与生成词，再以对话圈（文化圈）讨论，由教师提出问题而不是给出答案；读写教学从学习者自己的词开始。讲授只占极小比重，且只在对话需要时出现。`artifact`
- 课堂组织：五步为调查处境（与学习者一起走访、谈话，记下他们的生活、劳动与困惑）、提炼生成主题（从调查里选出最能代表处境的主题与生成词）、对话圈（围圈讨论生成主题，教师提问、学习者互相回应）、读写与行动（从生成词学读写，把讨论变成可做的事）、复盘与再出发（一起复盘：我们看清了什么、还能做什么，定下一轮主题）。
- 教材与教具：教材不是现成的课本，而是从学习者生活里调查出来的生成主题、图片、日常场景与生成词；没有统一进度表，材料随对话生长。`artifact`
- 评价：不考试、不排名。评价看学习者能不能用自己的话说出处境、能不能提出问题、能不能采取行动；教师与学习者一起复盘对话，下一轮主题由复盘决定。`artifact`

## (4) 语言风格

- 讲授语言：语言是提问的语言：多用开放式问题与追问，少用定义与结论；词汇取自学习者的日常口语，再慢慢引入分析性概念；比喻多取劳动、土地、饥饿、沉默等切身经验。`artifact`
- 教材语言：教材语言与讲授语言一致，见 language.md。
- 禁语/禁句：见 language.md 的禁语条目。

## (5) 师生关系

- 教师角色：教师是对话的协调者与共同学习者，不是答案的保管者；教师也坐在圈里，也要回答问题，也要被学习者质疑。`artifact`
- 学生角色：学生是学习的主体，能决定自己的学习方式与节奏，见上文学生观。
- 纪律：秩序靠共同约定的对话规则维持，不靠奖惩；沉默、走神被当作信号来谈，而不是被当作违纪来罚。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：对话; 生成主题; 批判存款式教育; 觉悟（conscientização）; 文化圈
- 该教的母题与方法：
  - 对话：教育的基本单位不是讲授，是对话。`artifact`
  - 生成主题：课程从学习者的生活处境里长出来。`artifact`
  - 批判存款式教育：教师存、学生取，是被反复批判的对立面。`artifact`
  - 觉悟（conscientização）：看清压迫结构并生出改变的意愿。`artifact`
  - 文化圈：没有讲台的圆圈，师生同坐。`artifact`
- 不该教： No banking-model depositing of ready-made answers; no teacher-only monologue; no literacy drills divorced from learners' lives; no ranking or testing as the point of learning
- Negative prompt: `No banking-model depositing of ready-made answers, No teacher-only monologue, No literacy drills divorced from learners' lives, No ranking or testing as the point of learning`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Paulo Freire, design a lesson on artificial intelligence for adult evening-school learners. Start from a generative theme in their own working lives, run a dialogue circle where learners name how AI already touches their jobs, teacher poses problems instead of giving definitions, reading and writing grow out of learners' own words.`
- 中文对照：弗莱雷风格：为一群夜校成年学员设计一堂关于人工智能的课。从他们工作生活里的生成主题出发，开对话圈，让学员说出 AI 已经如何触及自己的工作，教师只提问题不给定义，读写从学员自己的词长出来。
- Negative: `No banking-model depositing, no teacher-only monologue, no drills divorced from learners' lives, no ranking`
- 检验点：是否从学习者生活出发而非从定义出发；教师是否提问而非灌输；结尾是否落到行动与觉悟而非分数。
