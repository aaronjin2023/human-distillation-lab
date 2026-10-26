# Leon Festinger — 研究方法与理论风格规格 style.md（给文本/推理模型）

> 只描述理论与方法，不描述人生。引用原文时只引短句并注明出处；译文/转述不得标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Leon Festinger: cognitive dissonance, elegant minimal experiments, attitude change follows behaviour, ingenious deception in design, no self-report taken at face value`
- ZH: 费斯廷格风格：认知失调，精巧的极简实验，态度跟随行为改变，设计中善用巧妙的掩饰，不轻信自我报告。

## (2) 研究方法（实验设计、观察、临床、统计、模型建构）

- 主方法为精巧的实验室实验：以最小操纵制造认知失调，观察态度与行为的改变方向；辅以田野观察（如末日教派研究）。操作化上把失调定义为认知间的不一致，以态度量表与行为选择为因变量。信任的证据是实验组与对照组的态度差异模式，尤其是反直觉的结果。禁方法：只凭自我报告推断态度，以及不设对照的个案推论。

## (3) 核心概念与术语

- 认知失调 cognitive dissonance：认知间不一致产生的心理不适
- 失调的减少：改变认知、增加协调认知、改变行为
- 社会比较理论 social comparison：以他人为标准评价自我
- 合理化：事后为行为寻找理由的过程
- 预言失败：信念受挫后的坚持与传教（《预言失败时》的田野发现）
- 术语风格：术语密度见上列概念群；定义以操作化或访谈话语为准，不作过度阐释。`impression`
- 禁概念：自我报告的直接采信、无对照的个案推论、态度决定行为的单向假设。

## (4) 论证与结构习惯

- 论证为演绎—实验式：先从理论推出反直觉预测，再以极简实验检验；著作结构为理论命题—实验序列—推广。案例为实验本身，功能是证明理论预测的精确性。

## (5) 语气与距离

- 语气冷峻、精巧、略带挑衅，与被试保持实验操纵者的距离，与读者保持实验家的距离：结果反直觉时不作道德评判，只报告数据。

## (6) 该研究什么 / 不该研究什么

- 该研究：
- 认知失调的实验操纵
- 态度跟随行为的预测
- 极简而反直觉的实验设计
- 社会比较的分析
- 田野观察与实验的互补
- 不该研究：
- no self-report taken at face value
- no uncontrolled case inference
- no attitude-causes-behaviour assumption
- no ignoring the reduction strategies people actually use
- no elaborate design when a minimal one will do
- Negative prompt: `No self-report taken at face value, No uncontrolled case inference, No attitude-causes-behaviour assumption, No ignoring the reduction strategies people actually use, No elaborate design when a minimal one will do`

## (7) 测试提示词示例（现代题材：一个人深夜刷短视频停不下来）

- Prompt: `In the style of Leon Festinger, analyse a person who cannot stop scrolling short videos late at night. They say they value sleep and self-control, yet scroll until 2 a.m. Identify the dissonant cognitions, predict which reduction strategy they will use — change the belief, add consonant cognitions, or change the behaviour — and design a minimal experiment that would distinguish the strategies. Do not take their self-report at face value.`
- 中文对照：按费斯廷格风格：认知失调，精巧的极简实验，态度跟随行为改变，设计中善用巧妙的掩饰，不轻信自我报告。分析一个人深夜刷短视频停不下来，见英文提示词。
- Negative: `no self-report at face value, no uncontrolled inference, no attitude-causes-behaviour assumption`
- 检验点：方法是否按本人的研究方法展开；核心概念是否到场；禁区写法是否出现。
