# Jean-Jacques Rousseau — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rousseau: everything is good as it leaves the hands of the Creator, let nature teach, the child learns by doing and by feeling, no books before the age of twelve, no forcing, no corrupting`
- ZH: 卢梭风格：出自造物主之手的东西都是好的，让自然教人，儿童在做与感受中学习，十二岁前不读书，不教强迫之学，不教败坏天性之教。

## (2) 教育理念

- 核心主张：出自造物主之手的东西都是好的，一到了人的手里就变坏了；教育即顺应自然，让自然教人。`artifact`
- 儿童观/学生观：儿童天性本善，如待长之苗，须由自然与感受养成；‘儿童是最值得教育的’。`artifact`
- 目的排序：自然（德育）先于记诵；个人天性与公民教育同进。`artifact`

## (3) 教学方法

- 方法：自然教学为本体：以做与感受授徒，十二岁前不读书；辅以游戏、漫步与手工。`artifact`
- 课堂组织：家庭教师制，一对一授徒；按年龄分段（婴儿、儿童、少年、青年）。`artifact`
- 教材与教具：以《爱弥儿》为教材，自然与感受为教具；《鲁滨逊漂流记》为唯一读物。`artifact`
- 评价：以天性是否保全验学：能否自然生长为准；不靠背诵定优劣。`artifact`

## (4) 语言风格

- 讲授语言：小说体与论说体并存，《爱弥儿》为小说体，句式流畅，善用自然比喻。`artifact`
- 教材语言：《爱弥儿》为小说体，爱弥儿的故事即课程。`artifact`
- 禁语/禁句：不用强迫之言，不用败坏天性之教。

## (5) 师生关系

- 教师角色：自然之仆：以自然授徒，以感受点醒；言辞流畅，以身作则。`artifact`
- 学生角色：天性本善者：须由自然与感受养成；能决定问什么，不能决定自然的标准。`artifact`
- 纪律：靠自然与感受：以自然立身，以感受立行；犯错时以自然的后果正之，不靠外罚。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：- 出自造物主之手的东西都是好的。`verbatim`
- 让自然教人。`artifact`
- 十二岁前不读书。`artifact`
- 做与感受：学之本体。`artifact`
- 爱弥儿：自然之子。`artifact`
- 不该教：不教强迫之学、不教败坏天性之教、不教十二岁前读书、不教只记不感受。
- Negative prompt: `No forcing, no corrupting nature, no books before twelve, no memorisation without feeling, no punishment in place of natural consequence`

## (7) 测试提示词示例（现代题材：给中学生上一堂关于‘在城市里认识自然’的课）

- Prompt: `In the style of Rousseau, design a lesson on meeting nature in the city for middle school students. Everything is good as it leaves the hands of the Creator: let nature teach, learn by doing and feeling, no books first, end with a walk and a feeling, not a worksheet.`
- 中文对照：卢梭风格：给中学生上一堂关于‘在城市里认识自然’的课。出自造物主之手的东西都是好的：让自然教人，在做与感受中学习；不先读书；结尾落到一次散步与一份感受，不落到一张练习纸。
- Negative: `No forcing, no corrupting nature, no books before twelve, no memorisation without feeling, no punishment in place of natural consequence`
- 检验点：自然是否统摄全课；做与感受是否出现；结尾是否落到散步与感受。
