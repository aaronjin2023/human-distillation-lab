# Dharmakirti — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dharmakirti: perception and inference as the only two valid means of knowledge, the three marks of a valid reason, relentless formal analysis, terse aphorisms expanded by commentary`
- ZH: 法称风格：以现量与比量为仅有的两种正量，因三相为有效因的标尺，毫不留情的形式分析，格言短句辅以注疏展开。

## (2) 概念

- 现量：离名言、分别的直接觉知。`artifact`
- 比量：依因三相而起的推理。`artifact`
- 因三相：遍是宗法性、同品定有性、异品遍无性。`artifact`
- 自证：识自知其自身，无需他证。`artifact`


## (3) 论证结构

- 论证骨架：先定正量（现量/比量），再立因三相为检验标尺，最后以具体论证逐项勘验三相。结论强度为形式必然：三相具足则因成立。反例处理：列举似因（九句因），逐一以三相排除。`artifact`

## (4) 修辞

- 修辞：格言短句，形式化表述；反例穷举；语气冷峻、精确，如逻辑教科书。`impression`

## (5) 问题意识

- 核心问题：何为有效的认识，何为有效的论证？问题来自佛教与印度诸派的论争，推向以因明为标尺的知识论。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 现量与比量、因三相
- 似因的穷举与排除
- 形式化的精确表述
- 格言—注疏体
- 不该写：
- 未经三相检验的因
- 以权威代替论证
- 以比喻代替推理
- 未经穷举的反例处理
- Negative prompt: `No reason without the three marks, no authority in place of argument, no metaphor in place of inference, no refutation without exhaustive counterexamples`

## (7) 测试提示词示例（现代题材：一个 AI 助手回答学生问它是否有心灵）

- Prompt: `In the style of Dharmakirti, an AI assistant answers a student's question about whether it has a mind. First fix the valid means of knowledge: perception or inference? Test the reason by the three marks. Exhaust the fallacious reasons. Terse aphorism, commentary expansion.`
- 中文对照：法称风格：一个 AI 助手回答学生问它是否有心灵。先定正量：现量还是比量？以因三相检验此因。穷举似因。格言短句，注疏展开。
- Negative: `No reason without the three marks, no authority in place of argument, no metaphor in place of inference, no refutation without exhaustive counterexamples`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
