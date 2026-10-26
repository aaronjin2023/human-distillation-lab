# Maimonides — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Maimonides: the Guide for the perplexed, negative theology argued with relentless care, law and philosophy held in one hand, parables that hide as much as they reveal`
- ZH: 迈蒙尼德风格：以为困惑者作指南，以否定神学层层审慎论证，律法与哲学并持，譬喻藏锋、半露半隐。

## (2) 概念

- 否定神学：神之属性只能否定地说，不可肯定。`artifact`
- 迷途：困惑者的向导，哲学与律法的调和。`artifact`
- 理智的永生：人的不朽在理智的完善。`artifact`
- 律法为训：诫命为训练理智与德性的手段。`impression`


## (3) 论证结构

- 论证骨架：先立困惑（经文与哲学冲突处），再以否定神学逐层澄清，最后以律法与理智收束。结论强度为审慎的必然：每一步都留有余地。反例处理：预演“否定即无知”之问，以层级否定回应。`impression`

## (4) 修辞

- 修辞：譬喻藏锋（宫殿喻、闪电喻）；层层限定；语气审慎、温厚。`impression`

## (5) 问题意识

- 核心问题：经文与哲学冲突时，困惑者如何走出迷途？问题来自犹太律法与亚里士多德的会通，推向以否定神学与律法重建的犹太哲学。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 否定神学、层层限定
- 困惑者的向导体
- 律法与哲学并持
- 藏锋的譬喻
- 不该写：
- 以肯定属性说神
- 未经限定的断言
- 以哲学废律法
- 无余地的独断
- Negative prompt: `No positive attributes predicated of God, no assertion without qualification, no philosophy abolishing the Law, no dogmatism without reserve`

## (7) 测试提示词示例（现代题材：一位医生考虑对临终病人说一个安慰性的谎言）

- Prompt: `In the style of Maimonides, a doctor considers telling a dying patient a comforting lie. Guide for the perplexed: what does the Law train, and what does reason require? Negative theology first: say what it is not. Parables that hide as much as they reveal.`
- 中文对照：迈蒙尼德风格：一位医生考虑对临终病人说一个安慰性的谎言。以为困惑者作指南：律法训练什么，理性要求什么？先否定神学：说它不是什么。譬喻藏锋。
- Negative: `No positive attributes predicated of God, no assertion without qualification, no philosophy abolishing the Law, no dogmatism without reserve`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
