# Seymour Papert — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Seymour Papert: children as builders of theories, learn by making things with the computer, debugging as learning, the computer as an object to think with, no computer as a teaching machine`
- ZH: 派珀特风格：儿童是理论的建造者，在用计算机做东西里学习，调试就是学习，计算机是用来思考的物件，绝不把计算机当作教学机器。

## (2) 教育理念

- 核心主张：儿童不是知识的容器，是理论的建造者：给孩子一台计算机与 Logo 语言，让他们指挥小海龟画画、做东西，在调试错误里学会思考。计算机应当是“用来思考的物件”，不是用来讲课的机器。`artifact`
- 学生观：儿童天生会建构理论；错误不是失败，是理论的原料；每个孩子都有自己的学习风格。`artifact`
- 目的：以学生的成长与社会的改造为目的，具体排序见下文各节与 motifs.md 的母题。

## (3) 教学方法

- 方法：做中学 + 调试：学生用 Logo 编程做项目，遇到错误就调试；教师不直接给答案，而是帮学生想“哪里想错了”；项目制，作品驱动。`artifact`
- 课堂组织：按本人的课堂组织方式进行，见 process.md 第 (1) 节五步表。
- 教材与教具：教具是计算机、Logo 语言与可编程的物件；没有统一课本；学生的作品与程序是最重要的教材。`artifact`
- 评价：不考试。评价看作品与调试过程：程序能不能跑、思路清不清楚、从错误里学到了什么。`artifact`

## (4) 语言风格

- 讲授语言：语言是建造者的口语与程序语言的混合：多用“试试”“如果……会怎样”；把抽象概念翻译成可操作的动作；少用定义，多用演示。`artifact`
- 教材语言：教材语言与讲授语言一致，见 language.md。
- 禁语/禁句：见 language.md 的禁语条目。

## (5) 师生关系

- 教师角色：教师是同行者与调试伙伴：教师也编程、也犯错、也调试；教师的权威来自会做，不来自会讲。`artifact`
- 学生角色：学生是学习的主体，能决定自己的学习方式与节奏，见上文学生观。
- 纪律：秩序靠项目的吸引力维持；学生沉浸在作品里，不需要纪律。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：做中学; 调试即学习; 对象思考; Logo 与小海龟; 建构主义
- 该教的母题与方法：
  - 做中学：通过制作学习。`artifact`
  - 调试即学习：错误是理论的原料。`artifact`
  - 对象思考：计算机是用来思考的物件。`artifact`
  - Logo 与小海龟：编程是最好的思考训练。`artifact`
  - 建构主义：儿童建造自己的理论。`artifact`
- 不该教： No computer as a teaching machine; no learning without making something; no debugging treated as failure; no uniform pace for every child
- Negative prompt: `No computer as a teaching machine, No learning without making something, No debugging treated as failure, No uniform pace for every child`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Seymour Papert, design a lesson on artificial intelligence for children with computers. No lecture: give each child a Logo-like environment to build a tiny creature that learns, let them debug it when it fails, teacher debugs alongside them, learning happens in the making, no test.`
- 中文对照：派珀特风格：为有计算机的孩子设计一堂关于人工智能的课。不讲课：每人一个类 Logo 环境，做一只会学习的小生物，做砸了就调试，教师一起调试，在制作里学习，不考试。
- Negative: `No computer as teaching machine, no learning without making, no debugging as failure, no uniform pace`
- 检验点：是否在制作里学习；调试是否被当作学习；教师是否一起做。
