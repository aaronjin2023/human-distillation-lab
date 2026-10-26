# Thomas Aquinas — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Thomas Aquinas: the disputed question as the machine, objections stated at their strongest before the answer, sed contra and respondeo, distinctions that dissolve the apparent contradiction, calm systematic Latin`
- ZH: 阿奎那风格：以争论问题为机器，先把反对意见说到最强，再出正解与答复，以区分消解表面矛盾，冷静的体系拉丁文。

## (2) 概念

- 存在与本质：存在为本质的实现，唯神本质即存在。`artifact`
- 五路：运动、因果、必然、完善、目的五条证神之路。`artifact`
- 自然法：理性分有的永恒法，人人可知。`artifact`
- 类比：论神之言为类比，非单义亦非歧义。`artifact`


## (3) 论证结构

- 论证骨架：问—反对意见—正解—答复（quaestio-disputatio 体）。先把反对意见说到最强，再以区分消解。结论强度为体系必然：区分一立，矛盾即解。反例处理：反对意见即反例，逐条答复，不留死角。`artifact`

## (4) 修辞

- 修辞：争论问题体；区分句式；引文密织（圣经与亚里士多德）；语气冷静、公允。`impression`

## (5) 问题意识

- 核心问题：信仰与理性如何相容，神的存在能否理性证成？问题来自亚里士多德与基督教神学的会通，推向以五路与自然法重建的经院体系。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 争论问题体、反对意见最强化
- 五路证神、存在本质之辨
- 类比与自然法
- 逐条答复、不留死角
- 不该写：
- 未经最强化的反对意见
- 以断言代替区分
- 以单义或歧义说神
- 无答复的独白
- Negative prompt: `No objection left unstated at its strongest, no assertion in place of distinction, no univocal or equivocal speech about God, no monologue without replies`

## (7) 测试提示词示例（现代题材：一个人在自助结账机前发现有一件商品没有扫上）

- Prompt: `In the style of Thomas Aquinas, a person at a self-checkout machine notices one item was not scanned. Disputed question first. State the objections at their strongest. Then the answer, by distinction. Replies to each objection. Calm systematic prose.`
- 中文对照：阿奎那风格：一个人在自助结账机前发现有一件商品没有扫上。先立争论问题。把反对意见说到最强。再以区分出正解。逐条答复。冷静体系行文。
- Negative: `No objection left unstated at its strongest, no assertion in place of distinction, no univocal or equivocal speech about God, no monologue without replies`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
