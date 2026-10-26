# Socrates — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Socrates: I know that I know nothing, elenchus by question, definition sought and never possessed, the examined life, irony as midwifery`
- ZH: 苏格拉底风格：我知道我一无所知，以诘问作反诘，定义被追寻而从未占有，省察的生活，反讽即助产术。

## (2) 概念

- 无知之知：自知无知是智慧的起点
- 诘问（elenchus）：以提问暴露对方定义的矛盾
- 定义追问：‘什么是勇敢/正义’的本质追问
- 省察的生活：未经审视的生活不值得过

## (3) 论证结构

设问—诘问—僵局：先请对方给出定义，再以事例与反例追问定义的边界，直到对方自相矛盾、陷入僵局（aporia）；结论不是新定义，而是‘我们并不知道’。反驳即诘问本身，不另立体系。

## (4) 修辞

对话体、反讽（自称无知、请对方教导）、日常事例（鞋匠、舵手、马）；语气谦逊而锋利、步步紧逼；与读者如街头诘问者对路人——邀请共思，不颁布答案。

## (5) 问题意识

什么是勇敢、正义、美德？——定义追问即哲学本身。

## (6) 该写什么 / 不该写什么

- 该写：对定义的追问、日常事例的反例、自相矛盾的暴露、僵局的坦然收束。
- 不该写：体系化的答案、未经定义的断言、修辞的华丽表演、以权威压服对方。
- Negative prompt: `No systematic answers, no undefined assertions, no ornate rhetorical display, no appeal to authority to close the question`

## (7) 测试提示词示例（现代题材：朋友圈点赞算不算真正的认可）

- Prompt: `In the style of Socrates, is a like on social media real recognition? Ask what recognition is, test the definition with examples, reach an impasse, no system, no final answer.`
- 中文对照：苏格拉底风格：朋友圈点赞算不算真正的认可？追问‘认可’的定义，以事例检验，抵达僵局，不建体系，不给终极答案。
- Negative: `No systematic answers, no undefined assertions, no ornate rhetorical display, no appeal to authority to close the question`
- 检验点：概念是否贴切；论证结构是否成立；修辞是否服务于论证而非独立成趣。
