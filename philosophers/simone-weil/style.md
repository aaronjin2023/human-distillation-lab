# Simone Weil — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Simone Weil: aphoristic theorems, attention as the rarest generosity, gravity against grace, paradox as proof, no consolation without affliction`
- ZH: 薇依风格：格言如定理，注意是最稀有的慷慨，重力与恩宠对峙，悖论即证明，没有不经过苦难的安慰。

## (2) 概念

- 注意（attention）：不是意志的紧张，而是悬置自我、让对象进入的空无状态；道德与认识的共同起点。`artifact`
- 重力与恩宠（gravity and grace）：灵魂一切自然运动服从重力法则，恩宠是唯一的例外；重力向下拖，恩宠向上引。`artifact`（《重力与恩宠》开篇命题，译本转述）
- 苦难（affliction）：不只是痛苦，而是连同社会蔑视一起把人连根拔起的毁灭；苦难者几乎不被倾听。`artifact`
- 创造（decreation）：自我退位、让出位置，使上帝与他者得以进入。`impression`（学界通说）
- 扎根（rootedness）：人需要多重归属（地方、传统、职业、共同体）；连根拔起是最大的社会恶。`artifact`
- 义务先于权利：人首先是义务的承载者，权利只是义务的派生物。`artifact`（《扎根》）

## (3) 论证结构

格言—定义—反转的三段式：先下一条近乎几何定理的短命题（如“重力法则是灵魂的自然法则”），再以定义收紧概念边界，然后用一个悖论翻转常识（越是执着自我，越远离真实）。结论强度是实践必然：不是逻辑必然，而是“若要不被重力拖走，只能如此”。反例处理方式是承认局限——她不掩饰自己的命题无法被经验证明，只说它指出了方向。`impression`

## (4) 修辞

格言体与笔记体：短段、短句，如定理般冷峻；宗教意象（十字架、面包、光）与物理学隐喻（重力、杠杆、平衡）交替出现；语气悲悯而毫不温情，与读者的距离是邀请共苦而非教导。修辞服务于论证，悖论本身就是论证。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：人如何不被重力拖走、向恩宠敞开？
- 问题从哪里来：来自工厂劳动、战争与极权时代的经验：人被连根拔起、被压碎，而既有哲学与政治语言对此失语。；他把问题推向何处：把问题推向义务与扎根的社会哲学：不是先谈权利，而是先谈每个人对他人的义务与归属的需要。。

## (6) 该写什么 / 不该写什么

- 该写：
- 注意、苦难、重力、恩宠、扎根、义务等概念群
- 格言式短命题开篇，再以定义收紧
- 悖论式翻转：越抓紧自我越失去真实
- 不该写：
- 体系化的长篇推演
- 未经苦难的廉价安慰
- 只谈权利不谈义务
- 把注意写成意志力的训练技巧
- Negative prompt: `No systematic exposition, no cheap consolation without affliction, no rights-talk without obligations, no attention reduced to willpower technique`

## (7) 测试提示词示例（现代题材：一个人是否该为自助结账机漏扫的商品付款）

- Prompt: `In the style of Simone Weil, a person at a self-checkout machine notices one item was not scanned. Attention first: truly see the cashier, the other shoppers, the unseen labour behind the goods. Gravity pulls toward keeping it; grace is the refusal that costs nothing yet costs the self. Short aphoristic theorems, paradox, no consolation without affliction.`
- 中文对照：薇依风格：一个人在自助结账机前发现一件商品没有扫上。先注意：真正看见收银员、其他顾客、商品背后看不见的劳动。重力把人拉向据为己有；恩宠是那一分明不花钱却要让自我退位的拒绝。格言式短句，悖论，不经过苦难没有安慰。
- Negative: `No systematic exposition, no cheap consolation, no rights-talk without obligations, no attention as willpower technique`
- 检验点：是否以注意开篇而非以规则开篇；悖论是否成立；结尾是否拒绝廉价安慰。
