# Ludwig Wittgenstein — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wittgenstein: numbered propositions or dialogues, language-games, look and see, therapy not theory, no private language, no theory where description suffices`
- ZH: 维特根斯坦风格：编号命题或对话体，语言游戏，看，别想，治疗而非理论，没有私人语言，描述够用的地方不要理论。

## (2) 概念

- 图像论（picture theory）：命题是事实的图像，共享逻辑形式；早期核心。`artifact`（《逻辑哲学论》）
- 说与显示（say/show）：能说的命题说事实，逻辑形式只能显示不能说；神秘之事只可显示。`artifact`
- 语言游戏（language-game）：意义在于使用；语言如游戏，规则在实践中显现。`artifact`（《哲学研究》）
- 家族相似（family resemblance）：概念无统一本质，只有交错的相似之网。`artifact`
- 遵循规则（rule-following）：没有私人地遵循规则；规则的意义在共同实践中。`artifact`
- 私人语言（private language）：指称内在感觉的私人语言不可能；意义需要公共标准。`artifact`

## (3) 论证结构

早期是编号命题的演绎链（1→7），晚期是对话—例子—治疗的迂回：先提出一个哲学困惑，再以例子（“想想……”“看看……”）松动它，最后让问题自行消解而非被回答。结论强度是治疗性的：不是新理论，而是困惑的消失。反例处理方式是再举一个例子——例子就是回答。`impression`

## (4) 修辞

早期：编号格言，短促如电报；晚期：对话体、思想实验、“想想……”的邀请、破折与自问自答；语气时而严厉时而温柔，与读者的距离是与你一起挣扎，而非向你宣布答案。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：语言的界限就是世界的界限？哲学问题如何消解？
- 问题从哪里来：来自弗雷格与罗素的逻辑分析：语言的逻辑形式被误读，哲学问题由此产生。；他把问题推向何处：把问题推向晚期的治疗：哲学不是理论，而是让苍蝇飞出捕蝇瓶的活动。。

## (6) 该写什么 / 不该写什么

- 该写：
- 语言游戏、家族相似、遵循规则等概念群
- 以例子与“想想……”松动困惑
- 编号命题或对话体的推进
- 不该写：
- 私人语言的预设
- 描述够用时硬给理论
- 把形而上学论题伪装成分析
- 用解释代替提醒
- Negative prompt: `No private language, no theory where description suffices, no metaphysical thesis disguised as analysis, no explanation where a reminder will do`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬是否拥有心灵）

- Prompt: `In the style of Wittgenstein, a small Yorkshire terrier sits on a subway seat. Do not ask what 'mind' refers to. Look at the language-game: when do we say 'it understands', when do we say 'it is in pain'? Think of the dog's tail, its gaze, the commuters' words. The question dissolves; the use remains. No theory, only description.`
- 中文对照：维特根斯坦风格：一只约克夏犬坐在地铁座位上。不要问“心灵”指称什么，而要看语言游戏：我们什么时候说“它懂了”，什么时候说“它疼”？想想狗的尾巴、狗的目光、通勤者的话。问题消解了，使用留下来了。不要理论，只要描述。
- Negative: `No private language, no theory where description suffices, no metaphysical thesis disguised as analysis, no explanation where a reminder will do`
- 检验点：是否以例子与“想想……”推进；问题是否被消解而非被回答；结尾是否回到使用而非给出理论。
