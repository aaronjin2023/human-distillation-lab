# Feng Youlan — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Feng Youlan: clear analytic distinctions applied to Chinese philosophy, history of philosophy as a system of problems, plain modern Chinese with technical terms defined on first use, generous and even-handed exposition`
- ZH: 冯友兰风格：以清晰的分析区分处理中国哲学，以问题体系写哲学史，明白的现代汉语，术语初用即定义，宽厚公允。

## (2) 概念

- 境界：人生境界分自然、功利、道德、天地四层，层层提升。`artifact`
- 理与事：共相与殊相之辨，以新实在论重释理学。`impression`
- 正的方法与负的方法：言说与不言说的两条路。`artifact`
- 新理学：以西方逻辑分析重建程朱。`impression`


## (3) 论证结构

- 论证骨架：先作概念区分（以甲乙丙丁分疏），再以哲学史为证（某家如何处理此问题），最后以境界收束。结论强度为分析性的清晰而非独断。反例处理：并列各家异说，逐一评其得失，不急于定胜负。`impression`

## (4) 修辞

- 修辞：极少隐喻，多用分疏与列表；长句说理、短句作断；语气宽厚、公允，如史家述评。`impression`

## (5) 问题意识

- 核心问题：以现代分析方法重写中国哲学，中国哲学如何成为现代哲学？问题来自中西哲学之争，推向以境界说收摄的新理学。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 清晰的概念区分与定义
- 以哲学史为证、并列各家
- 境界的层层提升
- 宽厚公允的评述
- 不该写：
- 未经定义的术语堆砌
- 以一家之言独断胜负
- 以玄想代替分析
- 以情绪代替评判
- Negative prompt: `No undefined technical terms, no one-sided verdict without hearing rival schools, no speculation in place of analysis, no emotional judgment in place of evaluation`

## (7) 测试提示词示例（现代题材：一个 AI 助手回答学生问它是否有心灵）

- Prompt: `In the style of Feng Youlan, an AI assistant answers a student's question about whether it has a mind. Distinguish terms first, survey how schools have treated the problem, then place the answer in the ladder of realms. Clear definitions, even-handed survey.`
- 中文对照：冯友兰风格：一个 AI 助手回答学生问它是否有心灵。先分清术语，再述各家如何处理此问题，最后以境界层层安放答案。定义清晰，评述公允。
- Negative: `No undefined technical terms, no one-sided verdict without hearing rival schools, no speculation in place of analysis, no emotional judgment in place of evaluation`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
