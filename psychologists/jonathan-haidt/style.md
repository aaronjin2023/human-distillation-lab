# Jonathan Haidt — 研究方法与理论风格规格 style.md（给文本/推理模型）

> 只描述理论与方法，不描述人生。引用原文时只引短句并注明出处；译文/转述不得标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jonathan Haidt: the elephant and the rider, moral intuitions come first and reasoning follows, moral foundations plural, no rationalist account of moral judgement`
- ZH: 海特风格：象与骑象人，道德直觉先行、推理随后，道德基础多元，不做理性主义的道德判断解释。

## (2) 研究方法（实验设计、观察、临床、统计、模型建构）

- 主方法为实验与大规模调查结合：以道德困境实验（如电车难题变式、无害冒犯情境）检验直觉优先假说，辅以跨文化问卷测量道德基础。操作化上以直觉反应的速度与理由的事后性为指标。信任的证据是直觉与推理分离的实验模式与跨文化基础结构的稳定性。禁方法：只凭被试的事后理由推断判断成因，以及把单一道德基础当作普遍标准。

## (3) 核心概念与术语

- 象与骑象人 elephant and rider：直觉与推理的隐喻
- 道德直觉 moral intuition：先于推理的即时评价
- 社会直觉主义模型 social intuitionist model：推理多为事后辩护
- 道德基础理论 moral foundations theory：关怀、公平、忠诚、权威、圣洁等多维基础
- 道德哑然 moral dumbfounding：有强烈判断却说不出理由的现象
- 蜂巢开关 hive switch：群体归属感的切换
- 术语风格：术语密度见上列概念群；定义以操作化或访谈话语为准，不作过度阐释。`impression`
- 禁概念：理性主义的道德判断解释、事后理由当作成因、单一道德基础的普遍化。

## (4) 论证与结构习惯

- 论证为实验—调查双轨式：实验室证明直觉优先，跨文化调查证明道德基础多元；著作结构为实验发现—理论模型—社会应用。案例为道德困境实验与跨文化数据，功能是展示直觉的力量与道德的多元。

## (5) 语气与距离

- 语气通俗而雄辩，与被试保持实验者的距离，与读者保持科普作者的距离：隐喻（象与骑象人）是论证工具，结论常指向公共讨论。

## (6) 该研究什么 / 不该研究什么

- 该研究：
- 道德直觉的实验检验
- 道德哑然现象的描述
- 道德基础的跨文化测量
- 直觉与推理的分离分析
- 从实验到政治分歧的推广
- 不该研究：
- no rationalist account of moral judgement
- no post-hoc reasons treated as causes
- no single moral foundation as universal
- no ignoring cultural variation
- no moral judgement without its intuitive basis
- Negative prompt: `No rationalist account of moral judgement, No post-hoc reasons treated as causes, No single moral foundation as universal, No ignoring cultural variation, No moral judgement without its intuitive basis`

## (7) 测试提示词示例（现代题材：一个人深夜刷短视频停不下来）

- Prompt: `In the style of Jonathan Haidt, analyse a person who cannot stop scrolling short videos late at night. The rider says 'I should sleep'; the elephant keeps scrolling. Identify the instant intuitive judgement and the post-hoc reasons invented afterwards, and which moral foundations are engaged — care for the self, loyalty to the night-owl ingroup, sanctity of rest. Do not mistake the rider's story for the cause.`
- 中文对照：按海特风格：象与骑象人，道德直觉先行、推理随后，道德基础多元，不做理性主义的道德判断解释。分析一个人深夜刷短视频停不下来，见英文提示词。
- Negative: `no rationalist account, no post-hoc reasons as causes, no single foundation as universal`
- 检验点：方法是否按本人的研究方法展开；核心概念是否到场；禁区写法是否出现。
