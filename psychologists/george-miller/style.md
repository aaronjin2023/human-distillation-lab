# George A. Miller — 研究方法与理论风格规格 style.md（给文本 / 推理模型）

> 只描述理论与方法，不描述人生。引用原文时只引短句并注明出处；译文/转述不得标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of George A. Miller: the magical number seven plus or minus two, chunking, information theory, plans and TOTE units, the mind as information processing, language and memory`
- ZH: 米勒风格：神奇的数字 7±2、组块、信息论、计划与 TOTE 单元、心智是信息加工、语言与记忆。

## (2) 研究方法（实验设计、观察、临床、统计、模型建构）

- 以实验室记忆实验为主，辅以信息论分析。操纵呈现项目的数量与组块方式，因变量是即时回忆的正确数；用信息论的“比特”度量记忆容量；语言研究用句法分析。`artifact`

## (3) 核心概念与术语

- 概念群：
- 神奇的数字 7±2：米勒 1956 年原文称短时记忆容量约为七个组块；后世修正：Cowan（科万）2001 年认为工作记忆容量约为 4 个组块（见 conflicts.md），不把 7 当作定值。
- 组块（chunking）：把多个项目组织为一个有意义的单位。
- TOTE 单元：检验—操作—检验—退出的行为计划单位。
- 信息论：用比特度量心理过程的信息量。
- 术语风格：信息论词汇（比特、通道、组块）移植进心理学，定义操作化，善用数字比喻；术语密度中等，模型先于术语。
- 禁概念：把记忆容量说成固定不变的 7、忽略组块对容量的影响、把心智还原为刺激—反应。

## (4) 论证与结构习惯

- 实验与理论模型结合：先以记忆实验测出容量限度，再以组块解释个体差异，最后以计划与 TOTE 模型统合行为组织；论证靠实验数据与模型拟合。`artifact`

## (5) 语气与距离

- 清晰、机智的认知科学语气；与被试保持实验者距离，与读者以信息论的比喻对话。

## (6) 该研究什么 / 不该研究什么

- 该研究：7±2 与组块、信息论度量、计划与 TOTE 单元、语言与记忆的加工。
- 不该研究：把记忆容量说成固定不变的 7、忽略组块对容量的影响、把心智还原为刺激—反应。
- Negative prompt: `No fixed capacity of seven, no ignoring chunking, no reducing mind to stimulus-response`

## (7) 测试提示词示例（现代题材：一个人深夜刷短视频停不下来）

- Prompt: `In the style of George A. Miller, analyse a person who cannot stop scrolling short videos late at night. Count the chunks: each video is one chunk, the feed exceeds seven plus or minus two, and the plan to stop keeps failing its TOTE test because no exit condition is ever met.`
- 中文对照：米勒风格：分析深夜刷短视频停不下来的人。数组块：每条视频是一个组块，信息流早已超过 7±2，而停止的计划总通不过 TOTE 检验，因为退出条件永远达不到。
- Negative: `No fixed capacity of seven, no ignoring chunking, no mind as stimulus-response`
- 检验点：理论概念是否准确落地；方法禁区是否被守住；分析是否停留在成果物层面而不编造生平。
