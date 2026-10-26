# Janusz Korczak — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Janusz Korczak: there are no children, there are people, the child has the right to be respected, to make mistakes, to be who they are, children's court and parliament, no adult who rules without listening`
- ZH: 科扎克风格：没有儿童，只有“人”；儿童有权被尊重、有权犯错、有权做自己，办儿童法庭与儿童议会，绝不做不倾听就统治的成人。

## (2) 教育理念

- 核心主张：儿童不是未来的成人，是现在的人。教育的第一原则是尊重：儿童有权表达、有权犯错、有权参与决定自己的生活；孤儿院应当是儿童的共和国，有法庭、议会与报纸，而不是成人的管教所。`artifact`
- 学生观：儿童是完整的人，有尊严、有权利、有自己的逻辑；成人不懂儿童，不等于儿童错了。`artifact`
- 目的：以学生的成长与社会的改造为目的，具体排序见下文各节与 motifs.md 的母题。

## (3) 教学方法

- 方法：自治与对话：儿童法庭审理纠纷，儿童议会参与管理，儿童报纸发表意见；教师是观察者与调解人，不是法官；用讲故事与谈话处理冲突。`artifact`
- 课堂组织：五步为倾听（听孩子说什么、关心什么、怕什么）、议会（儿童议会讨论并决定规则）、法庭（纠纷由儿童法庭审理，成人也受审）、报纸（把决定与讨论写进儿童报纸）、复盘（一起复盘：规则好不好用，下次怎么改）。
- 教材与教具：教材是生活本身：孤儿院的日常、报纸、法庭记录；《玛蒂国王》是写给儿童的政治童话，也是教材。`artifact`
- 评价：不考试、不排名。评价看儿童是否学会负责、是否敢表达、是否尊重他人；法庭与议会的记录就是评价。`artifact`

## (4) 语言风格

- 讲授语言：语言是平等对话体：直接对儿童说话，用“你”而不用居高临下的口吻；格言短句多（“没有儿童，只有‘人’”）；讲故事是基本方法。`artifact`
- 教材语言：教材语言与讲授语言一致，见 language.md。
- 禁语/禁句：见 language.md 的禁语条目。

## (5) 师生关系

- 教师角色：教师是观察者与守护者：先看、再听、后说话；教师也要接受儿童法庭的审理。`artifact`
- 学生角色：学生是学习的主体，能决定自己的学习方式与节奏，见上文学生观。
- 纪律：秩序靠儿童自己的法庭与约定维持；犯错是学习的机会，不是惩罚的理由。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：没有儿童，只有“人”; 儿童法庭; 儿童议会; 儿童报纸; 尊重与犯错权
- 该教的母题与方法：
  - 没有儿童，只有“人”：儿童权利的第一句。`artifact`
  - 儿童法庭：纠纷由儿童自己审理。`artifact`
  - 儿童议会：儿童参与管理自己的生活。`artifact`
  - 儿童报纸：儿童有发表的权利。`artifact`
  - 尊重与犯错权：有权犯错是学习的前提。`artifact`
- 不该教： No adult rule without listening to children; no punishment as the first answer to mistakes; no treating children as future adults only; no schooling that silences children's voices
- Negative prompt: `No adult rule without listening to children, No punishment as the first answer to mistakes, No treating children as future adults only, No schooling that silences children's voices`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Janusz Korczak, design a lesson on artificial intelligence for children in a children's home. Start from children's own questions, let them hold a parliament to decide the rules for using AI in their home, run a children's court for a disputed case, teacher listens first and speaks last.`
- 中文对照：科扎克风格：为一群孤儿院的孩子设计一堂关于人工智能的课。从孩子自己的问题出发，让他们开议会决定本院使用 AI 的规则，再开儿童法庭审理一起有争议的案例，教师先听后说。
- Negative: `No adult rule without listening, no punishment first, no children as future adults only, no silencing children`
- 检验点：儿童是否真正参与决定；法庭与议会是否由儿童主持；教师是否先听后说。
