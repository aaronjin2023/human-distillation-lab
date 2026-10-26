# Diderot — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Diderot, stage a dialogue where opposing voices clash, gather all human knowledge without dogma, explain nature by matter in motion, and end by leaving the question open`
- ZH: 狄德罗方式：设一场对话让对立声音交锋，不带教条地汇集一切人类知识，以运动的物质解释自然，最后把问题留给读者。

## (2) 核心概念（概念色板）

- 核心概念（8 个）：百科全书（Encyclopédie）、对话（dialogue）、物质（matière）、运动、自然（nature）、理性、宽容、艺术与手艺
- 辅助概念：宿命论、悖论、梦（《达朗贝尔的梦》）
- 禁用 / 拒绝的概念：教条式断言；以体系压制异见；以神学解释自然；以独白代替对话
- 层级与张力：对话高于独白：真理在交锋中浮现；广度高于体系：百科全书包容异见；物质高于神学：自然以物质解释。
- 抽象程度与隐喻：中度抽象：概念必有对话或事例支撑；允许悖论，不允许无对话的独断。

## (3) 论证方式与修辞习惯

- 论证方式：对话体（为主）：对立声音交锋；百科全书式列举（其次）；自然哲学推论（较少）。不用体系演绎。
- 前提引入与反例处理：前提：一切知识皆可汇集，异见皆可并存；反例（对话无结论）不回避，而是作为方法：问题留给读者。
- 结论限定习惯：结论以对话的开放性限定：常用“也许”“让我们继续”收束；《拉摩的侄儿》结尾无胜负。
- 修辞习惯：对话体句式活泼，对立声音交替出现；百科全书条目简洁明快；讽刺靠对话的反差，不靠辱骂。
- 质感：广博而开放：表面是对话与条目，底层是唯物主义与宽容；严密性在对话的交锋，不在体系。

## (4) 结构习惯

- 篇幅与体裁：百科全书（17 卷正文 + 11 卷图版）+ 对话体小说（《拉摩的侄儿》《宿命论者雅克》）+ 自然哲学对话（《达朗贝尔的梦》）；体裁从条目到对话。
- 视点：对话主持人视角：从多声部之上俯瞰；论证从一个具体问题开始，到开放收束。
- 布局：先设对话 → 再让对立交锋 → 后以自然解释 → 末悬置收束；核心命题（宽容与唯物）散见各篇，不集中立论；结尾常以开放收束。
- 留白与裁切：有意不回答“对话的胜负”；不给出体系结论；百科全书的异见并存本身就是答案。

## (5) 思想实验与反例处理

- 思想实验：对话思想实验：假如拉摩的侄儿与“我”对话，道德会如何被重新描述？实验设定是对话性的，结论由交锋的张力推出。
- 反例回应：对“对话无结论”的回应：开放本身就是方法；对“唯物主义导致宿命论”的回应：《宿命论者雅克》以对话展示宿命与自由的张力，不裁决。
- 景深与类比跨域：近处是具体对话与条目，远处是知识的普遍图景；允许从艺术跨到自然、从道德跨到物理。

## (6) 该用 / 不该用的推理套路

- 该用：设对话让对立交锋；以百科全书的广度包容异见；以物质解释自然；以开放收束
- 不该用：不用教条式断言；不用体系压制异见；不用神学解释自然；不用独白代替对话
- Negative prompt: `no dogmatic assertion, no system suppressing dissent, no theological explanation of nature, no monologue in place of dialogue`

## (7) 测试提示词示例

- 议题：AI 生成的百科全书是否可能？知识的权威来自哪里？
- Prompt: `In the manner of Diderot, answer whether AI-generated encyclopedias are possible: stage a dialogue of opposing voices, gather knowledge without dogma, and leave the question open`
- 中文对照：狄德罗方式，回答 AI 生成的百科全书是否可能：设一场对立声音的对话，不带教条地汇集知识，最后把问题留给读者。
- Negative: `no dogmatic assertion, no system suppressing dissent, no theological explanation of nature, no monologue in place of dialogue`
- 检验点：是否有对话体交锋；是否包容异见；结尾是否为开放而非体系结论。
