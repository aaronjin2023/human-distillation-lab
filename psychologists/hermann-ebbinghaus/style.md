# Hermann Ebbinghaus — 研究方法与理论风格规格 style.md（给文本/推理模型）

> 只描述理论与方法，不描述人生。引用原文时只引短句并注明出处；译文/转述不得标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hermann Ebbinghaus: nonsense syllables as pure material, self as sole subject, savings method measures memory, forgetting curve as law, no meaning, no association by content`
- ZH: 艾宾浩斯风格：无意义音节作纯净材料，以自己为唯一被试，节省法测量记忆，遗忘曲线即定律，不谈意义、不谈内容联想。

## (2) 研究方法（实验设计、观察、临床、统计、模型建构）

- 方法类型：自我实验，严格控制的实验室记忆实验。设计要素：无意义音节（排除既有联想）、自己为被试、重复学习至恰能背诵、节省法（重学节省的时间百分比）测量保持量。信任的证据：可重复的节省率与遗忘曲线。禁方法：不用有意义材料、不用他人被试、不用内省报告作主要证据。

## (3) 核心概念与术语

- 概念群：无意义音节（nonsense syllable）；节省法（savings method）；遗忘曲线（forgetting curve）；学习与重学；记忆保持量。术语风格：术语少而精确，定义操作化（保持量 = 节省百分比）；少用比喻。禁概念：不用意义、联想内容、无意识、动机。

## (4) 论证与结构习惯

- 论证：归纳先行——从自我实验数据画出曲线，再概括为遗忘规律；结构：《论记忆》按实验序列展开（学习、保持、遗忘、重学），数据表与曲线图为核心；案例：只有一个被试（自己），案例即全部数据。

## (5) 语气与距离

- 语气：冷峻、节制、数据优先；与被试的距离：研究者即被试，自我观察；与读者的距离：报告式，少设问、多数据。

## (6) 该研究什么 / 不该研究什么

- 该研究：无意义音节的学习、遗忘曲线的形状与规律、节省法测量记忆保持、重复学习与间隔效应、记忆的量化方法。
- 不该研究：见 Negative prompt（方法与理论上的禁区）。
- Negative prompt: `No meaningful material, no introspective report as main evidence, no content association, no unconscious explanation, no group statistics without replication`

## (7) 测试提示词示例（现代题材：一个人刷短视频停不下来）

- Prompt: `In the style of Hermann Ebbinghaus, analyse a person who cannot stop scrolling short videos. Treat each clip as a nonsense syllable: measure learning by repetitions, forgetting by the savings method. How many re-viewings does it take to retain a clip after 24 hours? No meaning, no motivation talk.`
- 中文对照：艾宾浩斯风格：分析刷短视频停不下来的人——把每个短视频当作无意义音节：以重复次数测学习，以节省法测遗忘。24 小时后重看一个片段能省多少时间？不谈意义、不谈动机。
- Negative: `No meaningful material, no introspection as evidence, no content association, no unconscious explanation, no motivation talk`
- 检验点：理论概念是否准确落位；方法禁区是否被遵守；分析是否按此人的论证习惯展开，而非通用心理学套话。
