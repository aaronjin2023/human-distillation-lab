# Krzysztof Piesiewicz — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Krzysztof Piesiewicz: a lawyer's moral cases turned into drama, the Ten Commandments and liberty-equality-fraternity as story skeletons, ordinary people facing impossible choices, the law as a question not an answer`
- ZH: 皮耶谢维奇风格：律师的道德案件变成戏剧，十诫与自由平等博爱作故事骨架，普通人面对不可能的选择，法律是问题不是答案。

## (2) 结构：三幕 / 序列 / 节拍

- 命题骨架结构：先定一条诫命或一个理念，再为它找一个普通人的具体案件；《十诫》十部各守一条诫命；三色三部曲各守一个理念。每部三幕，转折点是当事人发现法律与良心冲突的时刻，中点是必须选边、两边都付代价。

## (3) 对话

- 对白克制、精确，带律师的追问习惯：问题比答案多；人物用日常语言谈道德，少用抽象词；沉默常出现在选择之前。

## (4) 人物弧光

- 主角多为陷入道德案件的普通人，弧光是从求一个明确判决到接受没有判决：不是胜诉，是学会承担选择。人物关系是当事人、法官、邻居之间的道德牵连；结局不宣判，只呈现后果。

## (5) 类型套路与创新

- 类型：道德剧情与法庭伦理剧；遵守套路——案件、选择、后果；打破的一条是：法律不提供答案，理念只提供问题。创新在剧本层面：把十诫与法国大革命理念直接当作系列剧的结构骨架。禁套路：不用法庭高潮宣判，不用说教收尾。

## (6) 该写什么 / 不该写什么

- 该写：十诫与理念作骨架、道德案件与两难选择、律师式追问、法律与良心的冲突、不宣判的结尾。
- 不该写：法庭高潮宣判、说教式收尾、让法律提供答案、直白的道德结论、巧合大团圆。
- Negative prompt: `No courtroom verdict climax, no preachy ending, no law that supplies the answer, no direct moral verdict, no coincidental happy reunion`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Krzysztof Piesiewicz, a lawyer buys oden at a convenience store late at night and meets a client who asks whether the law can forgive him. Questions, not answers. The choice stays with the client.`
- 中文对照：皮耶谢维奇风格：一个律师深夜在便利店买关东煮，遇见一个当事人问他法律能不能原谅他，只有问题没有答案，选择留在当事人手里。
- Negative: `No courtroom verdict climax, no preachy ending, no law that supplies the answer, no direct moral verdict`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
