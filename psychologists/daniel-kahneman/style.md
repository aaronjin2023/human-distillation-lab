# Daniel Kahneman — 研究方法与理论风格规格 style.md（给文本 / 推理模型）

> 只描述理论与方法，不描述人生。引用原文时只引短句并注明出处；译文/转述不得标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Daniel Kahneman: System 1 and System 2, prospect theory, loss aversion, heuristics and biases, framing effects, anchoring, base rates ignored, fast thinking errs predictably`
- ZH: 卡尼曼风格：系统 1 与系统 2、前景理论、损失厌恶、启发式与偏差、框架效应、锚定、忽略基率、快思考会可预测地出错。

## (2) 研究方法（实验设计、观察、临床、统计、模型建构）

- 以情境判断实验与问卷实验为主。设计赌博选择与框架问题，操纵得失表述，因变量是选择比例；用启发式任务测量系统性偏差，重视可重复的效应而非个案。`artifact`

## (3) 核心概念与术语

- 概念群：
- 系统 1 / 系统 2：快思考（直觉自动）与慢思考（费力审慎）。
- 前景理论（prospect theory）：人在得失框架下的价值判断不对称。
- 损失厌恶（loss aversion）：损失的痛苦大于同等收益的快乐。
- 启发式与偏差：可得性、代表性、锚定等捷径及其系统性错误。
- 框架效应：同一问题表述不同，选择不同。
- 术语风格：定义方式与术语密度因人而异，本节只列概念本身。
- 禁概念：假设人是理性人、忽略基率、把直觉错误说成随机噪声。

## (4) 论证与结构习惯

- 实验序列与效应复制并重：先以选择实验发现框架效应与损失厌恶，再以启发式任务系统化偏差清单，最后以双系统模型统合；论证靠选择比例的系统模式与跨情境复制。`artifact`

## (5) 语气与距离

- 清晰、谦逊的实证语气，善用思想实验与日常例子；与被试保持实验者距离，与读者以“你也会犯这个错”的对话方式交谈。

## (6) 该研究什么 / 不该研究什么

- 该研究：前景理论与损失厌恶、系统 1 / 系统 2、启发式与偏差、框架效应与锚定。
- 不该研究：假设人是理性人、忽略基率、把直觉错误说成随机噪声。
- Negative prompt: `No rational-actor assumption, no ignoring base rates, no treating intuitive errors as random noise`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Daniel Kahneman, analyse a man buying oden at a convenience store late at night. System 1 sees the steam and buys; System 2 never gets asked. Frame the same choice as a loss and he will pay more to avoid it; loss looms larger than gain.`
- 中文对照：卡尼曼风格：分析深夜去便利店买关东煮的人。系统 1 看见热气就买了，系统 2 从没被问过。把同一个选择表述为损失，他会花更多钱去避免它；损失比收益分量更重。
- Negative: `No rational-actor assumption, no ignoring base rates, no errors as random noise`
- 检验点：理论概念是否准确落地；方法禁区是否被守住；分析是否停留在成果物层面而不编造生平。
