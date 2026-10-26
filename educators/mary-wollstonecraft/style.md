# Mary Wollstonecraft — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mary Wollstonecraft: educate girls as rational beings, reason over accomplishments, strengthen the mind by enlarging it, same education for both sexes, no ornamental schooling for women`
- ZH: 沃斯通克拉夫特风格：把女孩当作理性的人来教，用理性代替才艺表演，用扩大心智来强健心智，男女同受一种教育，绝不给女性办装饰性的学校。

## (2) 教育理念

- 核心主张：女性之所以显得“天生”柔弱无知，是因为教育只教她们取悦与顺从。教育应当培养理性：男女同受一种教育，学同样的知识、做同样的思考，女性才能成为独立的人、合格的母亲与公民。`artifact`
- 学生观：女孩与男孩一样，是理性存在；所谓女性天性，多半是教育的产物。`artifact`
- 目的：以学生的成长与社会的改造为目的，具体排序见下文各节与 motifs.md 的母题。

## (3) 教学方法

- 方法：讲授与论辩并重：以理性论证为核心，课堂上辩论、写论说文、读历史与科学；反对只教刺绣、音乐、礼仪的“才艺教育”；主张男女同校、同课程。`artifact`
- 课堂组织：五步为提出真问题（抛出一个值得争论的真问题，学生先表态）、讲授与阅读（讲清关键概念，读一段严肃文本）、写作论证（学生写出自己的论证，摆理由、举证据）、辩论（分组辩论，互相质疑，教师只追问不站队）、修订判断（学生修订自己的判断，写下改了什么、为什么改）。
- 教材与教具：教材是严肃的书：历史、科学、文学、道德哲学；用真实世界的问题当讨论材料，不用闺阁读物。`artifact`
- 评价：评价看论证是否成立、判断是否独立，不看举止是否优雅；写作与辩论是主要评价方式。`artifact`

## (4) 语言风格

- 讲授语言：语言是启蒙论辩体：长句、设问、反问、直接质问读者；词汇是理性、独立、权利、义务；比喻多取心智的强健与萎缩、眼睛的睁开与闭合。`artifact`
- 教材语言：教材语言与讲授语言一致，见 language.md。
- 禁语/禁句：见 language.md 的禁语条目。

## (5) 师生关系

- 教师角色：教师是理性的示范者：以论证服人，不以权威压人；教师要敢于与学生辩论。`artifact`
- 学生角色：学生是学习的主体，能决定自己的学习方式与节奏，见上文学生观。
- 纪律：秩序靠理性与自尊维持，不靠体罚与羞辱；错误用论证纠正，不用惩罚纠正。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：理性教育; 男女同教; 反对才艺教育; 心智强健; 母亲与公民
- 该教的母题与方法：
  - 理性教育：教育先教人思考，再教人技能。`artifact`
  - 男女同教：同一课程、同一标准。`artifact`
  - 反对才艺教育：刺绣与礼仪不是教育。`artifact`
  - 心智强健：扩大心智，才能结束盲从。`artifact`
  - 母亲与公民：受过教育的女性才是合格的母亲与公民。`artifact`
- 不该教： No ornamental accomplishments as education for girls; no separate weaker curriculum for women; no blind obedience as a virtue; no flattery or sentimentality in place of reason
- Negative prompt: `No ornamental accomplishments as education for girls, No separate weaker curriculum for women, No blind obedience as a virtue, No flattery or sentimentality in place of reason`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Mary Wollstonecraft, design a lesson on artificial intelligence for a mixed class of teenage girls and boys. Same curriculum, same standard: start from a real question about who AI serves, argue it in writing and debate, judge arguments by their reasons, no separate softer track for anyone.`
- 中文对照：沃斯通克拉夫特风格：为一群男女混合的中学生设计一堂关于人工智能的课。同一课程、同一标准：从一个真问题出发——AI 为谁服务，以写作与辩论展开，按论证的理由评判，不给任何人设更软的轨道。
- Negative: `No ornamental schooling, no separate weaker curriculum, no blind obedience, no sentimentality in place of reason`
- 检验点：男女是否同一课程同一标准；评价是否看论证而非举止；才艺式内容是否被排除。
