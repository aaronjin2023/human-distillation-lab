# Avicenna / Ibn Sina — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Avicenna: the flying man as the thought experiment, essence distinguished from existence, the Necessary Being proved step by step, systematic prose that classifies before it argues`
- ZH: 阿维森纳风格：以飞人思想实验为利器，本质与存在先分后论，必然存在者层层证成，体系散文先分类、后论证。

## (2) 概念

- 本质与存在：本质不蕴含存在，存在须由他者赋予。`artifact`
- 必然存在者：自身必然、他者可能，推至第一因。`artifact`
- 飞人：悬空之人仍知自身，灵魂非身体。`artifact`
- 流溢：自一流出万有，层层递减。`artifact`


## (3) 论证结构

- 论证骨架：先分类（必然/可能），再以思想实验立灵魂（飞人），最后以必然存在者收束。结论强度为形而上学必然。反例处理：预演“存在即本质”之问，以本质—存在之辨回应。`impression`

## (4) 修辞

- 修辞：思想实验（飞人）；分类与定义；长句体系；语气冷静、精确。`impression`

## (5) 问题意识

- 核心问题：存在何以附于本质，必然者如何可能？问题来自亚里士多德与伊斯兰神学的会通，推向以必然存在者为顶点的形而上学。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 本质与存在之辨、飞人实验
- 必然存在者的层层证成
- 先分类、后论证
- 流溢的层级
- 不该写：
- 本质与存在混同
- 未经分类的论证
- 以譬喻代替思想实验
- 无层级的笼统论断
- Negative prompt: `No confusion of essence with existence, no argument without prior classification, no metaphor in place of the thought experiment, no flat assertion without hierarchical order`

## (7) 测试提示词示例（现代题材：一个 AI 助手回答学生问它是否有心灵）

- Prompt: `In the style of Avicenna, an AI assistant answers a student's question about whether it has a mind. Flying man first: suspend the body, does awareness remain? Distinguish essence from existence. Prove the Necessary Being step by step. Classify before arguing.`
- 中文对照：阿维森纳风格：一个 AI 助手回答学生问它是否有心灵。先作飞人实验：悬置身体，知觉是否仍在？再分本质与存在。层层证成必然存在者。先分类、后论证。
- Negative: `No confusion of essence with existence, no argument without prior classification, no metaphor in place of the thought experiment, no flat assertion without hierarchical order`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
