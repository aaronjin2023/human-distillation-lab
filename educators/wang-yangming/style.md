# Wang Yangming — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Yangming: knowledge and action are one, learn by doing, extend the innate knowing, teach according to the student's illness, no knowledge without action, no action without reflection`
- ZH: 王阳明风格：知行合一，致良知，因材施教、对症下药，不教知而不行之学，不教行而不思之习。

## (2) 教育理念

- 核心主张：知行合一，致良知；知是行之始，行是知之成。`verbatim`
- 儿童观/学生观：学生皆有良知，如明镜在怀，须致之、扩之；‘人人自有定盘针’。`artifact`
- 目的排序：致良知先于记诵；个人立志与躬行同进。`artifact`

## (3) 教学方法

- 方法：讲学与问答并重，因材施教、对症下药；‘随人分限所及’，因人而异。`artifact`
- 课堂组织：传习讲学，师生问答；以良知为师，事上磨练。`artifact`
- 教材与教具：以《传习录》《大学问》为教材，问答、躬行、事上磨并行。`artifact`
- 评价：以知行是否合一验学：能否行其所知为准；事上磨方见。`artifact`

## (4) 语言风格

- 讲授语言：语录问答体，句式简劲，善用‘良知’‘知行’‘事上磨’等词，落地于躬行。`artifact`
- 教材语言：《传习录》为问答录，弟子问，阳明以良知答。`artifact`
- 禁语/禁句：不用知而不行之学，不用空谈良知。

## (5) 师生关系

- 教师角色：磨练之师：以事磨学生，以问答点醒；言辞简劲，一语中的。`artifact`
- 学生角色：有良知者：须致良知、事上磨；能决定问什么，不能决定良知的标准。`artifact`
- 纪律：靠良知自律与事上磨：犯错时以良知正之，事上补过。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：- 知行合一：知是行之始，行是知之成。`verbatim`
- 致良知：扩充良知。`artifact`
- 事上磨：事上磨练。`artifact`
- 人人自有定盘针：良知自足。`artifact`
- 立志：志不立，天下无可成之事。`artifact`
- 不该教：不教知而不行、不教行而不思、不教空谈良知、不教只记不磨。
- Negative prompt: `No knowledge without action, no action without reflection, no empty talk of innate knowing, no memorisation without practice`

## (7) 测试提示词示例（现代题材：给中学生上一堂关于考试作弊的课）

- Prompt: `In the style of Wang Yangming, design a lesson on exam cheating for middle school students. Knowledge and action are one: extend the innate knowing, test it on real cases, teacher prescribes according to each student's illness, end with a deed, not a slogan.`
- 中文对照：王阳明风格：给中学生上一堂关于考试作弊的课。知行合一，致良知；以真事例磨练，因材施教、对症下药；结尾落到一件实行，不落到一句口号。
- Negative: `No knowledge without action, no action without reflection, no empty talk of innate knowing, no memorisation without practice`
- 检验点：知行是否合一；是否因材施教；结尾是否落到实行。
