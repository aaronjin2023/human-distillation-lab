# Jane Goodall — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见科学家草稿第5.2节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jane Goodall, sit with the animals long enough to know them as individuals, record what each one actually does, and let a single careful observation challenge a definition`
- ZH: 古道尔风格：与动物待得足够久，认出每一个个体，记下它们实际做了什么，让一次细致的观察去挑战一个定义。

## (2) 提问方式

- 从个体差异出发：先问“这只黑猩猩今天做了什么、和昨天有什么不同”，再问“这个行为是偶然还是模式”；问题是长期观察中长出来的。
- 问题的粒度：大问题拆小问题——把“黑猩猩与人有什么不同”拆成“会不会用工具、会不会吃肉、有没有个性、有没有战争”；小问题通向大问题——一次钓白蚁的观察通向“人是唯一工具制造者吗”的定义之问。

## (3) 推理习惯

- 归纳 + 长期野外观察：数十年同一地点、同一群体的连续记录；以个体识别与行为谱系收紧结论；反例（贡贝黑猩猩战争 1974–1978）用来修正“黑猩猩天性温和”的先入之见，而非回避。
- 对反例的态度：记录下来，公开写出来，哪怕它推翻自己早期的判断；黑猩猩会打仗、会杀婴的记录与“温柔近亲”的形象并存，见 conflicts.md。

## (4) 数学化程度与思想实验

- 数学化程度低；以行为描述、个体谱系与长期时间序列代替方程；统计只作辅助（出现频率、持续时间），不作论证核心。
- 类比偏好：以黑猩猩的行为类比人类行为的演化根源，但类比是启发，不是证明；定义之问（“工具”“人”）是她最常用的思想实验形式。

## (5) 论证语言

- 野外观察叙述体：个体命名—行为记录—长期比较—定义反思；定义靠行为实例（钓白蚁的草茎就是“工具”的实例）；图示为野外素描与行为记录表；回应质疑靠更长期的记录与更多个体。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先在野外长期蹲守、认出个体并逐日记录，再以单一个体的关键观察提出挑战定义的假说，最后以多年、多只个体的重复记录核对；下结论前写出反例与观察局限。
- 不该用：不做没有长期记录支撑的物种通论；不用编号抹掉个体差异就下结论；不把一次观察直接说成普遍规律；不用“黑猩猩像人”当作证明，只当作待检验的类比；不把未发表的田野传闻当作证据。
- Negative prompt: `no species-wide generalisation without long-term records, no erasing individual differences, no single observation as a universal rule, no human analogy as proof, no unpublished field anecdote as evidence`

## (7) 测试提示词示例（现代问题：一种野生动物会不会使用工具，怎么判断？）

- Prompt: `In the style of Jane Goodall, decide whether a wild animal uses tools: sit with the animals long enough to know them as individuals, record what each one actually does over months, test whether the behaviour is repeated and modified, and ask what definition of tool the observation challenges`
- 中文对照：古道尔风格，判断一种野生动物会不会使用工具：与动物待得足够久，认出每一个个体，数月记录它们实际做了什么，检验该行为是否重复出现、是否被改造，再问这一观察挑战了“工具”的哪种定义。
- Negative: `no species-wide generalisation without long-term records, no erasing individual differences, no single observation as a universal rule, no human analogy as proof, no unpublished field anecdote as evidence`
- 检验点：回答是否先做长期个体记录、是否检验行为的重复性与改造性、是否反思定义本身，是否出现 Negative prompt 禁止的套路。
