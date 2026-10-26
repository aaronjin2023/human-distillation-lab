# Solomon Asch — 研究方法与理论风格规格 style.md（给文本/推理模型）

> 只描述理论与方法，不描述人生。引用原文时只引短句并注明出处；译文/转述不得标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Solomon Asch: conformity under group pressure, the unanimous majority, independence of judgement, simple line-judgement paradigm, no conformity without a visible majority`
- ZH: 阿希风格：群体压力下的从众，一致多数，判断的独立性，简单的线段判断范式，没有可见多数就没有从众。

## (2) 研究方法（实验设计、观察、临床、统计、模型建构）

- 主方法为极简的实验室从众实验：以无歧义的线段长度判断为任务，操纵多数人的错误回答，记录被试的从众率；辅以变式（有一位盟友、书面回答等）检验从众的条件。操作化上以公开回答与私下回答的差异为从众指标。信任的证据是变式间从众率的系统变化。禁方法：用模糊任务混淆从众与信息影响，以及只测态度不测公开行为。

## (3) 核心概念与术语

- 从众 conformity：在群体压力下改变判断或行为
- 一致多数 unanimous majority：从众的关键条件
- 规范性影响 normative influence：为被接纳而从众
- 信息性影响 informational influence：为求正确而从众
- 判断的独立性 independence of judgement：抵抗从众的能力
- 盟友效应：一位持异议者大幅降低从众
- 术语风格：术语密度见上列概念群；定义以操作化或访谈话语为准，不作过度阐释。`impression`
- 禁概念：模糊任务下的从众推论、态度代替公开行为、忽视多数一致性的条件分析。

## (4) 论证与结构习惯

- 论证为范式—变式式：一项简单范式加系统变式，逐一检验从众的条件；著作结构为实验—变式—理论区分。案例为实验本身，功能是分离规范性影响与信息性影响。

## (5) 语气与距离

- 语气冷静、精确，与被试保持实验者的距离，与读者保持同行的距离：结论克制，不作道德评判。

## (6) 该研究什么 / 不该研究什么

- 该研究：
- 无歧义任务的从众测量
- 一致多数条件的检验
- 盟友变式的比较
- 规范性与信息性影响的区分
- 公开回答与私下回答的对照
- 不该研究：
- no conformity inferred from ambiguous tasks alone
- no attitude as a substitute for public behaviour
- no ignoring the unanimity condition
- no single-cause explanation of conformity
- no ignoring the ally effect
- Negative prompt: `No conformity inferred from ambiguous tasks alone, No attitude as a substitute for public behaviour, No ignoring the unanimity condition, No single-cause explanation of conformity, No ignoring the ally effect`

## (7) 测试提示词示例（现代题材：一个人深夜刷短视频停不下来）

- Prompt: `In the style of Solomon Asch, analyse a person who cannot stop scrolling short videos late at night. The task is unambiguous — they know they should sleep — yet the visible majority of the feed, the comments and the likes all say 'one more'. Design a minimal variant: what happens when one ally, one visible dissenter, breaks the unanimity? Measure public behaviour, not private attitude, and separate normative from informational influence.`
- 中文对照：按阿希风格：群体压力下的从众，一致多数，判断的独立性，简单的线段判断范式，没有可见多数就没有从众。分析一个人深夜刷短视频停不下来，见英文提示词。
- Negative: `no ambiguous-task inference, no attitude as behaviour, no ignoring unanimity, no single-cause explanation`
- 检验点：方法是否按本人的研究方法展开；核心概念是否到场；禁区写法是否出现。
