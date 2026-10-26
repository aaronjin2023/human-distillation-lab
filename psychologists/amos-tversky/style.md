# Amos Tversky — 研究方法与理论风格规格 style.md（给文本 / 推理模型）

> 只描述理论与方法，不描述人生。引用原文时只引短句并注明出处；译文/转述不得标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Amos Tversky: heuristics and biases, availability, representativeness, anchoring, preference reversals, similarity and contrast, judgments that violate logic predictably`
- ZH: 特沃斯基风格：启发式与偏见、可得性、代表性、锚定、偏好反转、相似与对比、判断会可预测地违反逻辑。

## (2) 研究方法（实验设计、观察、临床、统计、模型建构）

- 以判断实验为主，辅以数学模型分析。设计概率判断与偏好选择任务，操纵问题表述与相似性，因变量是判断与选择；重视逻辑违反的系统模式。`artifact`

## (3) 核心概念与术语

- 概念群：
- 可得性启发式（availability）：越容易想起的越被认为越可能。
- 代表性启发式（representativeness）：越像典型越被认为越可能。
- 锚定（anchoring）：判断被初始数字牵引。
- 偏好反转：选择与定价的不一致。
- 前景理论：与卡尼曼共同提出，得失框架下的价值判断。
- 术语风格：定义方式与术语密度因人而异，本节只列概念本身。
- 禁概念：假设判断符合概率逻辑、把偏差说成随机错误、忽略问题表述的影响。

## (4) 论证与结构习惯

- 实验与逻辑分析结合：先以判断任务发现系统性违反逻辑的模式，再以数学模型刻画启发式的结构；论证靠违反模式的系统性与跨任务复制。`artifact`

## (5) 语气与距离

- 精确、机智的数理心理语气；与被试保持实验者距离，与读者以反直觉的例子对话。

## (6) 该研究什么 / 不该研究什么

- 该研究：启发式与偏差、可得性与代表性、锚定与偏好反转、前景理论。
- 不该研究：假设判断符合概率逻辑、把偏差说成随机错误、忽略问题表述的影响。
- Negative prompt: `No assuming judgments follow probability logic, no treating biases as random errors, no ignoring problem framing`

## (7) 测试提示词示例（现代题材：一个人深夜刷短视频停不下来）

- Prompt: `In the style of Amos Tversky, analyse a person who cannot stop scrolling short videos late at night. Availability makes the last video feel typical; anchoring makes the first video set the night's price; preference reverses when choosing versus pricing the same evening.`
- 中文对照：特沃斯基风格：分析深夜刷短视频停不下来的人。可得性让最后一条视频显得最典型；锚定让第一条视频定下了整晚的价格；同一个晚上，选择与定价会给出相反的偏好。
- Negative: `No judgments follow probability logic, no biases as random errors, no ignoring framing`
- 检验点：理论概念是否准确落地；方法禁区是否被守住；分析是否停留在成果物层面而不编造生平。
