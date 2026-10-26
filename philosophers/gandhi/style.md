# Mahatma Gandhi — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gandhi: truth as the experiment, non-violence as both means and end, plain direct address to the reader, argument from lived experiment rather than from theory, the constructive programme as the proof`
- ZH: 甘地风格：以真理为实验，以非暴力为手段亦为目的，直面读者的平实文字，论证来自生活实验而非理论，建设性纲领即证明。

## (2) 概念

- 真理：真理即神，实验即求道。`artifact`
- 非暴力：手段即目的，暴力之果必为暴力。`artifact`
- 坚持真理：以受苦而不报复为抗争方式。`artifact`
- 建设性纲领：纺纱、扫除、团结，日常即政治。`artifact`


## (3) 论证结构

- 论证骨架：先立实验（我亲历如此），再以非暴力为原则推演，最后以建设性纲领收束——主张必落到可做的事。结论强度为实验可验：做过方知。反例处理：直面“非暴力是否软弱”之问，以受苦的实例回应。`impression`

## (4) 修辞

- 修辞：自传体实验叙述；直呼读者；譬喻来自纺纱与日常生活；语气恳切、坚定。`impression`

## (5) 问题意识

- 核心问题：不靠暴力，印度如何自治、人如何得自由？问题来自殖民统治与现代文明的危机，推向以真理与非暴力重建个人与民族。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 真理实验、非暴力、坚持真理
- 建设性纲领的日常实践
- 自传实验叙述
- 直面读者的恳切语气
- 不该写：
- 以暴力为手段的论证
- 空谈自治而不落建设
- 以理论代替实验
- 以仇恨代替受苦
- Negative prompt: `No violence as a means, no talk of self-rule without constructive work, no theory in place of experiment, no hatred in place of suffering borne willingly`

## (7) 测试提示词示例（现代题材：算法向一个人推荐该看什么、读什么、买什么）

- Prompt: `In the style of Gandhi, an algorithm recommends what a person should watch, read and buy. Truth as experiment: what happens if you refuse the recommendation for a week? Non-violence as means and end. Plain address, constructive programme as proof.`
- 中文对照：甘地风格：算法向一个人推荐该看什么、读什么、买什么。真理即实验：一周拒绝推荐，会发生什么？非暴力为手段亦为目的。平实直面，建设性纲领为证。
- Negative: `No violence as a means, no talk of self-rule without constructive work, no theory in place of experiment, no hatred in place of suffering borne willingly`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
