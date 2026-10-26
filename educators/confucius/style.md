# Confucius — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Confucius: teach by dialogue and example, learn by practising, ren and li first, the teacher asks more than he tells, self-cultivation before rules, no rote without understanding`
- ZH: 孔子风格：对话与身教并重，学而时习，仁礼为先，教师多问少讲，先修身后立规矩，不教不解之死记。

## (2) 教育理念

- 核心主张：教育即成人之道，以仁为本、以礼为节，学与行合一；教育为谁：有教无类，人人可学。`artifact`
- 儿童观/学生观：学生是可塑的君子之材，天性有善端，须由学与习涵养而成，非白板亦非定命。`artifact`
- 目的排序：德育（仁、礼）先于智育；个人修身与社会秩序同进，修身为齐家治国之本。`artifact`

## (3) 教学方法

- 方法：对话问答为主（约七成），辅以身教示范与诗书礼乐的诵读习练；因材施教，同一问题对颜回与子路答法不同。`artifact`
- 课堂组织：游学与讲学结合，无固定班级与课时；师生同行，遇事即教，孔子居中、弟子环坐问答。`artifact`
- 教材与教具：以《诗》《书》《礼》《乐》《易》《春秋》为教材，诵读、习礼、奏乐并行；教材是经典文本，不是讲义。`artifact`
- 评价：不靠考试，靠日常观察与弟子互评；以言行是否合仁礼为准，长期看，不一次定论。`artifact`

## (4) 语言风格

- 讲授语言：语录体短章，‘子曰’开篇，问答推进；多取日常比喻（水、草、玉、射），句短意深，不作长篇体系。`artifact`
- 教材语言：对话体与格言体并存，定义靠追问（‘何谓仁’）而非下定义。`artifact`
- 禁语/禁句：不用巧言令色之辞，不以利代义，不空谈玄理。`artifact`

## (5) 师生关系

- 教师角色：向导与身教者：居中发问、点拨，极少长篇讲授；以自身言行示范礼。`artifact`
- 学生角色：问学者与行者：可提问、可质疑，须将所学行于日常；能决定提问的方向，不能决定仁礼的标准。`artifact`
- 纪律：靠礼与自觉维持：以礼节制言行，以‘克己复礼’自律；犯错时以反问与事例点醒，不靠体罚与羞辱。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：- 仁：爱人，教育的第一目的。`artifact`
- 礼：行为的节度，习礼即习做人。`artifact`
- 学而时习：学了要习、要行，习而不行等于未学。`artifact`
- 因材施教：同一问题因人而异答。`artifact`
- 有教无类：教育不问出身。`artifact`
- 君子与小人：以德行分，不以地位分。`artifact`
- 不该教：不教巧言令色、不教以利代义、不教空谈而不习行、不教死记经典而不解其意。
- Negative prompt: `No clever words in place of humanity, no profit in place of righteousness, no rote memorisation without practice, no lecturing without dialogue`

## (7) 测试提示词示例（现代题材：给中学生上一堂关于人工智能的课）

- Prompt: `In the style of Confucius, design a lesson on artificial intelligence for middle school students. Begin with dialogue: ask what ren and li require of a tool that speaks. Use everyday examples, let students practise judging cases, teacher asks more than tells, end with self-cultivation, not a rule.`
- 中文对照：孔子风格：给中学生上一堂关于人工智能的课。先对话发问：仁与礼要求一个会说话的工具怎样才算合宜；用日常事例，让学生练习判断个案；教师多问少讲；结尾落到修身，不落到一条规则。
- Negative: `No clever words in place of humanity, no profit in place of righteousness, no rote memorisation without practice, no lecturing without dialogue`
- 检验点：是否以问答推进而非讲授；仁礼是否统摄全课；结尾是否收于修身而非规则。
