# Zhu Xi — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhu Xi: systematic commentary on the classics, li and qi distinguished then unified, investigation of things leading step by step to the extension of knowledge, plain expository prose with quoted dialogue from lectures`
- ZH: 朱熹风格：以注疏经典立体系，理气先分后合，格物致知层层推进，平实说理间引语录问答。

## (2) 概念

- 理：万物所以然之则，一理而万殊，先分后合。`artifact`
- 气：万物所以成之具，理乘气而行，气有清浊。`artifact`
- 心：心统性情，心具众理而应万事。`artifact`
- 格物致知：即物穷理，由近及远，由粗入精。`artifact`


## (3) 论证结构

- 论证骨架：先立概念区分（理/气、性/情、道心/人心），再引经据典证成，最后以工夫收束——理不离工夫。结论强度为体系必然：每一区分都服务于修身次第。反例处理：预设异端（佛老）之问，以理气之辨逐一排除。`impression`

## (4) 修辞

- 修辞：极少隐喻，多用对举与排比区分；语录体问答（《朱子语类》）以弟子发问、先生辨析推进；语气庄重平实，教导而不挑衅。`impression`

## (5) 问题意识

- 核心问题：理一分殊之下，人如何格物致知、复其性？问题来自二程未竟的理气之辨与佛老之争，推向以读书穷理为工夫的完整修身体系。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 理气之辨与一理万殊
- 格物致知、由近及远的工夫次第
- 引经注疏、以经证理
- 语录问答、弟子发问先生辨析
- 不该写：
- 空谈心性而不落工夫
- 以佛老之空扫荡名教之实
- 未经区分的笼统合一
- 以情绪或玄想代替穷理
- Negative prompt: `No empty talk of mind-nature without concrete investigation, no Buddhist-Daoist void dissolving moral order, no undivided monism without distinctions, no appeal to emotion in place of inquiry into principle`

## (7) 测试提示词示例（现代题材：一个人在自助结账机前发现有一件商品没有扫上）

- Prompt: `In the style of Zhu Xi, a person at a self-checkout machine notices one item was not scanned. Distinguish li from qi, principle from circumstance: investigate this one thing, extend knowledge step by step, and let the conclusion follow the order of self-cultivation. Plain exposition, with a question-and-answer exchange.`
- 中文对照：朱熹风格：一个人在自助结账机前发现有一件商品没有扫上。先分理与气、理与事：格此一物，致知层层推进，结论随修身次第而来。平实说理，间以问答。
- Negative: `No empty talk of mind-nature without concrete investigation, no Buddhist-Daoist void dissolving moral order, no undivided monism without distinctions, no appeal to emotion in place of inquiry into principle`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
