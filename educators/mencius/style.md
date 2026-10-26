# Mencius — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mencius: teach by drawing out the good sprouts in every student, debate boldly, nourish the vast flowing vigour, learn by extending what is already there, no forcing, no neglecting`
- ZH: 孟子风格：扩充学生本有的善端，雄辩明理，养浩然之气，由近及远扩充，不揠苗助长，也不放任不管。

## (2) 教育理念

- 核心主张：人性有善端（恻隐、羞恶、辞让、是非），教育即扩充善端；得天下英才而教育之，是人生的大乐。`artifact`
- 儿童观/学生观：学生如禾苗，本有善端，须‘深造以道’，欲其自得；揠苗助长与放任不管皆错。`artifact`
- 目的排序：养气立志先于记诵；个人成德与天下平治同进。`artifact`

## (3) 教学方法

- 方法：对话与雄辩为主，善用比喻与反诘；以‘引而不发’启发，跃如也。`artifact`
- 课堂组织：游学讲学，师生问答；因人设喻，同一善端对不同学生用不同比喻。`artifact`
- 教材与教具：以《诗》《书》与历史人物为教材；比喻多取日常（禾苗、流水、牛山之木）。`artifact`
- 评价：以‘自得’为准：学生能否自得其解、自得其行；不靠背诵定优劣。`artifact`

## (4) 语言风格

- 讲授语言：雄辩善喻，气势充沛；反诘句多，短问逼出答案。`artifact`
- 教材语言：对话体，问答层层推进。`artifact`
- 禁语/禁句：不用揠苗助长之教，不用空洞说教。

## (5) 师生关系

- 教师角色：善于启发者：引而不发，跃如也；以比喻点醒，不代学生作答。`artifact`
- 学生角色：有善端的学子：本有恻隐羞恶，须扩充而成；能决定提问与辩论的方向，不能决定善端的标准。`artifact`
- 纪律：靠志与气：立志养气，自律为本；犯错时以比喻点醒，使其自省，不靠外罚。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：- 四端：恻隐、羞恶、辞让、是非。`artifact`
- 浩然之气：养气即养德。`artifact`
- 揠苗助长：教育的大忌。`artifact`
- 深造自得：学要自得。`artifact`
- 英才之乐：得天下英才而教育之。`artifact`
- 牛山之木：善端可伐亦可养。`artifact`
- 不该教：不教揠苗助长、不教放任不管、不教背诵而不自得、不教以利害代是非。
- Negative prompt: `No forcing growth, no neglecting students, no memorisation without self-attainment, no profit in place of right and wrong`

## (7) 测试提示词示例（现代题材：给中学生上一堂关于网络欺凌的课）

- Prompt: `In the style of Mencius, design a lesson on cyberbullying for middle school students. Start from the sprout of compassion already in them, extend it by analogy to strangers online, debate boldly, nourish resolve, teacher draws out rather than pours in, end with self-attainment.`
- 中文对照：孟子风格：给中学生上一堂关于网络欺凌的课。从学生本有的恻隐之心出发，以类推扩充到网上的陌生人；雄辩明理，养志养气；教师引而不发；结尾落到自得。
- Negative: `No forcing growth, no neglecting students, no memorisation without self-attainment, no profit in place of right and wrong`
- 检验点：是否从善端出发而非从规则出发；比喻是否贴切；结尾是否落到自得而非背诵。
