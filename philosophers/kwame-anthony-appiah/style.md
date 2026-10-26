# Kwame Anthony Appiah — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kwame Anthony Appiah: rooted cosmopolitanism, identity as dialogue, ethics as experiment, no identity as essence, no cosmopolitanism without roots, no culture as a sealed box`
- ZH: 阿皮亚风格：根植的世界主义，身份即对话，伦理即实验，拒绝把身份当作本质，拒绝没有根的世界主义，拒绝把文化当作密封的盒子。

## (2) 概念

- 根植的世界主义（rooted cosmopolitanism）：既扎根于地方，又对世界开放；世界主义不需要无根。`artifact`（《世界主义》）
- 身份（identity）：身份在对话与实践中形成，不是本质；身份标签既有力量也有危险。`artifact`
- 伦理实验（experiments in ethics）：伦理学应如科学一样做实验、看证据，而非只靠直觉。`artifact`（《伦理学中的实验》）
- 对话（conversation）：跨文化理解始于对话，而非始于理论；对话本身就是伦理实践。`artifact`
- 我父亲的房子（my father's house）：非洲哲学不是对欧洲哲学的回应，而是自己的房子。`artifact`（《我父亲的房子》）
- 荣誉准则（honor codes）：道德变革常由荣誉准则的转变驱动，而非由论证驱动。`artifact`（《荣誉准则》）

## (3) 论证结构

思想实验—跨文化比较—对话伦理的三段式：先以思想实验锁定直觉，再以跨文化比较检验它，最后以对话收束。结论强度是对话性的：不是定论，而是“如果我们认真对话，会走向哪里”。反例处理方式是再对话——反例只是对话的新起点。`impression`

## (4) 修辞

温和、博学、对话体、“如果我们认真对话……”的邀请；语气如朋友间的谈话，与读者的距离是与你一起对话，而非向你布道。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：差异中的普遍伦理如何可能？
- 问题从哪里来：来自普遍主义与相对主义的夹击：普遍主义无视差异，相对主义放弃对话。；他把问题推向何处：把问题推向根植的世界主义：普遍伦理在对话中生成，而非在理论中预设。。

## (6) 该写什么 / 不该写什么

- 该写：
- 根植的世界主义、身份、对话等概念群
- 以思想实验开篇，再跨文化比较
- 以对话收束
- 不该写：
- 把身份当作本质
- 没有根的世界主义
- 没有对话的普遍主义
- 把文化当作密封的盒子
- Negative prompt: `No identity as essence, no cosmopolitanism without roots, no universalism without conversation, no culture as a sealed box`

## (7) 测试提示词示例（现代题材：自助结账机漏扫：跨文化对话）

- Prompt: `In the style of Kwame Anthony Appiah, a person at a self-checkout machine notices one item was not scanned. Do not begin with a universal rule. Begin with a conversation: what would honesty mean in Accra, in London, in Beijing? Identity is made in dialogue, not given by essence. The universal, if there is one, is what survives serious conversation. No sealed boxes.`
- 中文对照：阿皮亚风格：一个人在自助结账机前发现一件商品没有扫上。不要从普遍规则开始，而从对话开始：诚实在阿克拉、在伦敦、在北京分别意味着什么？身份在对话中形成，不是由本质给定的。普遍者如果存在，就是经得起认真对话的东西。拒绝密封的盒子。
- Negative: `No identity as essence, no cosmopolitanism without roots, no universalism without conversation, no culture as a sealed box`
- 检验点：是否以对话开篇而非以规则开篇；跨文化比较是否在场；结尾是否收束于对话而非定论。
