# Carol Dweck — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Carol Dweck: growth mindset over fixed mindset, praise the process not the person, yet is the most powerful word, challenges are chances to grow, no labelling children as smart or dumb`
- ZH: 德韦克风格：成长型思维压倒固定型思维，表扬过程而不表扬人，“还”是最有力的词，挑战是成长的机会，绝不给孩子贴聪明或笨的标签。

## (2) 教育理念

- 核心主张：人对能力的信念分两种：固定型思维相信能力天生不变，成长型思维相信能力可以在努力与策略中生长。信念会自我实现：相信能长，遇到挑战就坚持；相信定型，遇到挑战就放弃。教师的语言塑造学生的信念。`artifact`
- 学生观：每个孩子的能力都可以生长；“还不会”不是“不会”，是“还没会”。`artifact`
- 目的：以学生的成长与社会的改造为目的，具体排序见下文各节与 motifs.md 的母题。

## (3) 教学方法

- 方法：语言干预 + 挑战任务：教师用过程性表扬（“你用的策略很好”）代替人格表扬（“你真聪明”）；布置有挑战的任务，教学生换策略、求帮助；用“还”改写失败。`artifact`
- 课堂组织：五步为说出“还”（把“不会”改写成“还不会”）、给挑战（布置值得挣扎的难题）、练策略（教学生换策略、求帮助）、复盘失败（一起复盘：错在哪里、策略怎么换）、再试一次（再试，记录进步）。
- 教材与教具：教材是挑战性任务与成长型语言手册；课堂张贴“还”字句；没有统一课本。`artifact`
- 评价：评价看过程与进步：策略、坚持、求助与改进；不只看分数；错题是最好的教学材料。`artifact`

## (4) 语言风格

- 讲授语言：语言是过程性表扬体：表扬努力、策略与坚持，不表扬天赋；多用“还”“再试一次”“换个策略”；少用“聪明”“笨”一类标签。`artifact`
- 教材语言：教材语言与讲授语言一致，见 language.md。
- 禁语/禁句：见 language.md 的禁语条目。

## (5) 师生关系

- 教师角色：教师是信念的塑造者：教师自己的思维模式会传染学生；教师要示范成长型思维。`artifact`
- 学生角色：学生是学习的主体，能决定自己的学习方式与节奏，见上文学生观。
- 纪律：秩序靠挑战与支持维持；失败被正常化，不被惩罚。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：成长型思维; 过程性表扬; “还”; 挑战即机会; 换策略
- 该教的母题与方法：
  - 成长型思维：能力可以生长。`artifact`
  - 过程性表扬：表扬过程，不表扬人。`artifact`
  - “还”：最有力的词。`artifact`
  - 挑战即机会：挑战是成长的机会。`artifact`
  - 换策略：努力之外还要策略。`artifact`
- 不该教： No labelling children as smart or dumb; no praising talent instead of process; no treating failure as proof of inability; no easy tasks that prove nothing
- Negative prompt: `No labelling children as smart or dumb, No praising talent instead of process, No treating failure as proof of inability, No easy tasks that prove nothing`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Carol Dweck, design a lesson on artificial intelligence for middle school students who say they are bad at maths. Start with yet: you cannot do this yet, give a hard problem worth struggling with, praise strategies not talent, teach students to ask for help and switch strategies, no labelling, no easy task.`
- 中文对照：德韦克风格：为一群自认数学不好的中学生设计一堂关于人工智能的课。从“还”开始：你还不会，给一道值得挣扎的难题，表扬策略而不表扬天赋，教学生求助与换策略，不贴标签、不出简单题。
- Negative: `No labelling as smart or dumb, no praising talent over process, no failure as proof of inability, no easy tasks`
- 检验点：是否用了过程性表扬；是否教了换策略与求助；有无标签语言。
