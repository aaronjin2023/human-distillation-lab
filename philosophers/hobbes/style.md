# Hobbes — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hobbes: definitions as the foundation of all reasoning, the state of nature as the thought experiment, geometry applied to politics, long deductive chains from a few stark premises, the Leviathan as the image of the artificial man`
- ZH: 霍布斯风格：以定义为全部推理的地基，以自然状态为思想实验，以几何方法施于政治，由少数冷峻前提推出长演绎链，利维坦为人工巨人的意象。

## (2) 概念

- 自然状态：人对人是狼，无共同权力则战争。`artifact`
- 社会契约：众人让渡权利，立主权者。`artifact`
- 利维坦：人工巨人，主权者即巨人之魂。`artifact`
- 定义：推理始于定义，定义不清则争吵不休。`artifact`


## (3) 论证结构

- 论证骨架：先立定义（人、权力、自由），再设自然状态（思想实验），最后以契约推出利维坦。结论强度为演绎必然：前提一立，结论不可逃。反例处理：预演“契约可违”之问，以主权不可分回应。`impression`

## (4) 修辞

- 修辞：几何式演绎；思想实验（自然状态）；譬喻经典（利维坦、狼）；语气冷峻、决断。`artifact`

## (5) 问题意识

- 核心问题：无共同权力时人如何共处，主权何以合法？问题来自英国内战的动荡，推向以契约为基的现代政治哲学。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 定义先行、自然状态实验
- 社会契约的演绎链
- 利维坦的意象
- 主权不可分的收束
- 不该写：
- 未经定义的论证
- 以历史代替演绎
- 以情感代替推理
- 无契约的权力论
- Negative prompt: `No argument without prior definition, no history in place of deduction, no appeal to emotion in place of reasoning, no theory of power without the covenant`

## (7) 测试提示词示例（现代题材：一个人在自助结账机前发现有一件商品没有扫上）

- Prompt: `In the style of Hobbes, a person at a self-checkout machine notices one item was not scanned. Definitions first: what is theft, what is covenant? State of nature as the thought experiment. Long deductive chain. The Leviathan as the artificial man.`
- 中文对照：霍布斯风格：一个人在自助结账机前发现有一件商品没有扫上。定义先行：何为盗窃，何为契约？自然状态为思想实验。长演绎链。利维坦为人工巨人。
- Negative: `No argument without prior definition, no history in place of deduction, no appeal to emotion in place of reasoning, no theory of power without the covenant`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
