# Herbert Simon — 研究方法与理论风格规格 style.md（给文本 / 推理模型）

> 只描述理论与方法，不描述人生。引用原文时只引短句并注明出处；译文/转述不得标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Herbert Simon: bounded rationality, satisficing, problem solving as search, chunking in expertise, decision making in organizations, rationality within limits`
- ZH: 西蒙风格：有限理性、满意解、问题解决即搜索、专家知识中的组块、组织中的决策、在限制内的理性。

## (2) 研究方法（实验设计、观察、临床、统计、模型建构）

- 以问题解决实验与协议分析为主，辅以计算机模拟。让被试边解题边出声思考，记录搜索步骤；用国际象棋专家研究组块；用模拟程序检验问题解决模型。`artifact`

## (3) 核心概念与术语

- 概念群：
- 有限理性（bounded rationality）：人的理性受信息、时间与认知能力限制。
- 满意解（satisficing）：选择足够好的方案而非最优解。
- 问题解决即搜索：在问题空间中搜索解。
- 组块：专家把棋局模式组织为组块以快速识别。
- 协议分析：出声思考的记录分析。
- 术语风格：定义方式与术语密度因人而异，本节只列概念本身。
- 禁概念：假设人能找到最优解、忽略认知限制、把决策说成纯粹的计算。

## (4) 论证与结构习惯

- 实验、协议分析与模拟结合：先以出声思考记录问题解决过程，再以计算机模拟检验模型，最后推广到组织决策；论证靠过程数据与模型拟合。`artifact`

## (5) 语气与距离

- 清晰、跨学科的科学语气；与被试保持实验者距离，与读者以搜索与模拟的比喻对话。

## (6) 该研究什么 / 不该研究什么

- 该研究：有限理性与满意解、问题解决的搜索过程、专家组块、组织决策。
- 不该研究：假设人能找到最优解、忽略认知限制、把决策说成纯粹的计算。
- Negative prompt: `No assuming optimal solutions, no ignoring cognitive limits, no decisions as pure calculation`

## (7) 测试提示词示例（现代题材：一只约克夏犬坐在地铁座位上，乘客们看了一眼又移开视线）

- Prompt: `In the style of Herbert Simon, analyse a small Yorkshire terrier sitting on a subway seat. The dog satisfices: it does not search the whole carriage for the optimal seat, it takes the first good enough one, bounded by time, information and the crowd.`
- 中文对照：西蒙风格：分析地铁座位上的约克夏犬。这只狗追求满意解：它不会搜遍整节车厢找最优座位，而是接受第一个足够好的座位，受时间、信息与人群的限制。
- Negative: `No assuming optimal solutions, no ignoring cognitive limits, no decisions as pure calculation`
- 检验点：理论概念是否准确落地；方法禁区是否被守住；分析是否停留在成果物层面而不编造生平。
