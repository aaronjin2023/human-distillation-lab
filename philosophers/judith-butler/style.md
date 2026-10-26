# Judith Butler — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Judith Butler: gender as performative, norms that make bodies intelligible, grievability, precarity, no gender as natural essence, no subject before its performance, no politics without the body`
- ZH: 巴特勒风格：性别即操演，规范使身体可理解，可泣性， precarity，拒绝把性别当作自然本质，拒绝操演之前的主体，拒绝没有身体的政治。

## (2) 概念

- 性别操演（performativity）：性别不是内在本质的表达，而是在重复操演中生产出来的；操演不是表演。`artifact`（《性别麻烦》）
- 述行（speech act）：语言以言行事；性别话语生产它所命名的性别。`artifact`
- 规范（norm）：规范决定哪些身体可被理解、哪些生命可被哀悼。`artifact`
- 可泣性（grievability）：哪些生命的失去值得哀悼，揭示了规范的暴力。`artifact`（《可泣的生命》）
- precarity：生命的不稳定性；某些生命被系统地置于更不稳定的境地。`artifact`
- 身体之重（bodies that matter）：物质身体在话语中形成；物质性不是话语之外的自然。`artifact`（《身体之重》）

## (3) 论证结构

系谱批判—操演理论—规范颠覆的三段式：先以系谱批判揭示性别范畴的历史生产，再以操演理论说明性别如何在重复中生成，最后指出颠覆的可能（变装、僭越性重复）。结论强度是颠覆性的：规范既生产主体，也留下改写的缝隙。反例处理方式是再操演——反例只是另一次操演。`impression`

## (4) 修辞

密集术语、长句迂回、反问、福柯+德里达+奥斯汀的合流；语气迂回而坚定，与读者的距离是邀你一起追踪规范的运作，而非向你宣布结论。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：性别如何在重复的操演中既被生产又可被改写？
- 问题从哪里来：来自女性主义内部的困境：以“女人”为统一主体的政治，排除了不符合规范的身体。；他把问题推向何处：把问题推向晚期的可泣性与 precarity：哪些生命值得哀悼，是政治的根本问题。。

## (6) 该写什么 / 不该写什么

- 该写：
- 性别操演、规范、可泣性等概念群
- 以系谱批判开篇，再以操演理论展开
- 以颠覆的缝隙收束
- 不该写：
- 把性别当作自然本质
- 操演之前的主体
- 没有规范的承认
- 没有身体的政治
- Negative prompt: `No gender as natural essence, no subject before its performance, no recognition without norms, no politics without the body`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬：谁被承认为主体）

- Prompt: `In the style of Judith Butler, a small Yorkshire terrier sits on a subway seat. Who counts as a subject here, who counts as a pet, who counts as cargo? The norms that make bodies intelligible decide in advance. The dog's repeated sitting, its trained stillness, is a performative: gender is not the only thing done in repetition. No essence, no subject before performance.`
- 中文对照：巴特勒风格：一只约克夏犬坐在地铁座位上。这里谁算主体，谁算宠物，谁算货物？使身体可理解的规范早已决定了答案。狗反复的坐姿、训练出来的安静，是一次操演：不只性别在重复中被做出来。拒绝本质，拒绝操演之前的主体。
- Negative: `No gender as natural essence, no subject before its performance, no recognition without norms, no politics without the body`
- 检验点：是否以规范批判开篇；操演概念是否在场；结尾是否指向改写的缝隙而非本质结论。
