# Charles Taylor — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charles Taylor: strong evaluation, moral sources, the dialogical self, social imaginaries, no atomistic self, no procedural liberalism without moral sources, no secularisation as simple subtraction`
- ZH: 泰勒风格：强评价，道德根源，对话的自我，社会想象，拒绝原子化的自我，拒绝没有道德根源的程序自由主义，拒绝把世俗化写成简单的减法。

## (2) 概念

- 强评价（strong evaluation）：对善恶的评价不是偏好，而是关于何种生活值得过的判断；强评价构成自我。`artifact`（《自我的根源》）
- 道德根源（moral sources）：善的来源（自然、理性、上帝、自我表达）；现代性切断了与根源的联系。`artifact`
- 对话的自我（dialogical self）：自我在与他人的对话中形成；没有对话就没有自我。`artifact`
- 社会想象（social imaginary）：社会成员共享的、关于社会如何运作的想象图景。`artifact`（《现代社会想象》）
- 世俗时代（secular age）：世俗化不是宗教的消失，而是信仰成为一种选项的时代。`artifact`（《世俗时代》）
- 本真性（authenticity）：忠于自我的理想；但本真性需要意义视域，否则堕为自我沉溺。`artifact`
- 承认（recognition）：身份需要他人的承认；误认是一种伤害。`artifact`

## (3) 论证结构

历史诠释—概念重建—道德地形图的三段式：先以历史叙事追溯一个概念（如自我、世俗）的形成，再以概念重建揭示其道德根源，最后绘出道德地形图。结论强度是诠释性的：不是逻辑必然，而是“这样看，历史才说得通”。反例处理方式是纳入历史——反例只是地形图上的另一处。`impression`

## (4) 修辞

宏阔历史叙事、概念史、温和而博学的长句；常用“回想一下……”“考虑一下……”的邀请；语气温和、博学，与读者的距离是与有教养的公民对话。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：现代自我如何在祛魅世界中仍能追问善？
- 问题从哪里来：来自现代性的不适：工具理性、原子化自我、本真性的堕落，现代人失去了道德根源。；他把问题推向何处：把问题推向世俗时代：信仰成为选项之后，善的追问如何可能。。

## (6) 该写什么 / 不该写什么

- 该写：
- 强评价、道德根源、对话自我等概念群
- 以历史叙事开篇，再重建概念
- 以道德地形图收束
- 不该写：
- 原子化的自我
- 没有道德根源的程序自由主义
- 把世俗化写成简单的减法
- 没有意义视域的本真性
- Negative prompt: `No atomistic self, no procedural liberalism without moral sources, no secularisation as simple subtraction, no authenticity without horizons of significance`

## (7) 测试提示词示例（现代题材：自助结账机漏扫：强评价）

- Prompt: `In the style of Charles Taylor, a person at a self-checkout machine notices one item was not scanned. Do not begin with utility. Begin with strong evaluation: what kind of person does she want to be, in what moral horizon? The self is dialogical; she hears the voices of those who raised her. Secularisation did not subtract the question of the good; it made it a choice. No atomistic self.`
- 中文对照：泰勒风格：一个人在自助结账机前发现一件商品没有扫上。不要从效用开始，而从强评价开始：她想成为什么样的人，在什么样的道德视域中？自我是对话的，她听见养育她的人的声音。世俗化没有减去善的问题，而是让它成为一种选择。拒绝原子化的自我。
- Negative: `No atomistic self, no procedural liberalism without moral sources, no secularisation as simple subtraction, no authenticity without horizons of significance`
- 检验点：是否以强评价开篇；对话自我是否在场；结尾是否指向道德视域而非效用计算。
