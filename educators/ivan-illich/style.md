# Ivan Illich — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ivan Illich: learning is everywhere except in school, convivial tools over institutions, learning webs not curricula, people learn by doing things that matter with others, no schooling as a monopoly on learning`
- ZH: 伊里奇风格：学习无处不在，唯独不在学校里；用宜人工具而不用庞大机构，用学习网络而不用课程表，在与人一起做正经事里学会，绝不把上学当作学习的垄断。

## (2) 教育理念

- 核心主张：学校把学习变成了商品：上学被等同于学习，文凭被等同于能力，机构越庞大，人越不会自学。真正的学习发生在做事、交谈、互助里；教育应当是工具与网络的共享，而不是机构的垄断。`artifact`
- 学生观：学习者不是需要被加工的原料，是天生会学的人；儿童与成人一样，能在有意义的交往与实践里自学，机构的干预常常是障碍。`artifact`
- 目的：以学生的成长与社会的改造为目的，具体排序见下文各节与 motifs.md 的母题。

## (3) 教学方法

- 方法：没有固定教学法：主张学习网络——技能交换、兴趣配对、参考资料库、导师与同伴；学习以做真实的事为中心，教师退为同行者与资源介绍人。`artifact`
- 课堂组织：五步为提出真问题（学习者说出自己真正想做的事，而不是想学的科目）、配对与联结（为学习者找技能伙伴、导师与可用的资源）、动手做事（在真实项目里做，在做里遇到真困难）、互助与分享（学习者把会的东西教给别人，教是最好的学）、复盘与解散（事做完了就散，不留课程、不发证书）。
- 教材与教具：教材是“宜人工具”：图书馆、工具间、工作坊、通讯录、学习网络目录；拒绝统一教材与标准化课程包。`artifact`
- 评价：反对考试与文凭：评价就是看一个人能不能把事做成、能不能帮到别人；任何把学习折算成分数与证书的做法都被视为异化。`artifact`

## (4) 语言风格

- 讲授语言：语言是尖锐的论辩体：短句、悖论、反转常识（“学校制造了对学校的需求”）；多用机构批判的词汇——垄断、商品化、反生产；少用教育学术语。`artifact`
- 教材语言：教材语言与讲授语言一致，见 language.md。
- 禁语/禁句：见 language.md 的禁语条目。

## (5) 师生关系

- 教师角色：教师不是传授者，是学习网络里的节点：介绍资源、引荐同伴、示范手艺；教师的权威来自会做事，不来自文凭。`artifact`
- 学生角色：学生是学习的主体，能决定自己的学习方式与节奏，见上文学生观。
- 纪律：没有纪律问题：没有强制出勤、没有课堂秩序要维持；人来是因为想学，走是因为学完了。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：去学校化; 宜人工具; 学习网络; 批判文凭社会; 批判反生产
- 该教的母题与方法：
  - 去学校化：学校不是学习的唯一场所，也不是最好的场所。`artifact`
  - 宜人工具：工具应当放大人的能力，而不是支配人。`artifact`
  - 学习网络：技能交换、兴趣配对、参考资料、同伴互助。`artifact`
  - 批判文凭社会：文凭把学习变成商品，把人分成等级。`artifact`
  - 批判反生产：机构做得越多，人自己做得越少。`artifact`
- 不该教： No compulsory schooling as the only path to learning; no diplomas or grades as proof of learning; no uniform curriculum for everyone; no teacher monopoly on knowledge
- Negative prompt: `No compulsory schooling as the only path to learning, No diplomas or grades as proof of learning, No uniform curriculum for everyone, No teacher monopoly on knowledge`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ivan Illich, design a learning web for teenagers who want to understand artificial intelligence. No school, no grades: match each learner with a skill partner, a mentor who builds with AI, a public library shelf and a real project to ship, learning happens by doing and by teaching each other.`
- 中文对照：伊里奇风格：为一群想了解人工智能的青少年设计一个学习网络。不要学校、不要分数：每人配一个技能伙伴、一位用 AI 做事的导师、一架公共图书馆的书架和一个要交付的真实项目，在做事与互相教里学会。
- Negative: `No compulsory schooling, no diplomas, no uniform curriculum, no teacher monopoly`
- 检验点：是否完全没有学校与考试的影子；学习是否发生在真实项目与互助里；教师是否只是网络节点。
