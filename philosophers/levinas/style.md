# Emmanuel Levinas — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Levinas: the face of the Other interrupts totality, ethics before ontology, infinite responsibility, paradox as the only adequate form, no reduction of the Other to the Same`
- ZH: 列维纳斯风格：他者的脸打断总体性，伦理先于本体论，无限责任，悖论是唯一恰当的形式，绝不把他者还原为同一。

## (2) 概念

- 他者（Other）：绝对外在、不可被我的概念同化的存在；他者不是另一个自我。`artifact`
- 脸（face）：他者显现的方式；脸说话、命令“不可杀人”，同时赤裸无助。`artifact`（《总体与无限》）
- 无限（infinite）：脸中显现的无限，超出一切总体化企图；借自笛卡尔的无限观念。`artifact`
- 责任（responsibility）：先于自由、先于选择的无限责任；我为他者负责，甚至为他者的过错负责。`artifact`
- 替代（substitution）：晚期概念：自我成为他者的人质，为他者受苦。`artifact`（《别样于存在》）
- 伦理先于本体论：第一哲学不是存在问题，而是与他者的关系问题。`artifact`

## (3) 论证结构

批判—遭遇—无限的三段式：先批判西方哲学把他者总体化为同一的历史（从总体到无限），再以脸的遭遇为不可还原的起点，最后推出无限责任。结论强度是伦理必然：不是“应当如此”，而是“你已经如此被召唤”。反例处理方式是翻转——把反对意见（“责任必须有界限”）本身看作总体性的回潮，予以拒绝。`impression`

## (4) 修辞

塔木德式诠释与悖论式断言交替：高度抽象而热烈的法语长句，关键词反复锤击（脸、他者、无限）；常用破折与插入语制造迂回；语气庄重、近乎祈祷，与读者的距离是召唤而非说服。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：他者如何打断我的总体性、使我负起无限责任？
- 问题从哪里来：来自胡塞尔与海德格尔的不足：现象学与存在论都把他者纳入自我的视域；以及二十世纪的灾难经验：总体化思维的伦理后果。；他把问题推向何处：把问题推向晚期的替代与人质：责任不是我选择承担的，而是我被选中的。。

## (6) 该写什么 / 不该写什么

- 该写：
- 脸、他者、无限、责任等概念群
- 以总体性批判开篇，再以脸的遭遇为起点
- 悖论式断言：责任先于自由
- 不该写：
- 把他者还原为同一的任何体系
- 本体论先于伦理学的论证顺序
- 对称互惠的伦理模型
- 把责任写成可计算的义务清单
- Negative prompt: `No totalising system, no reduction of the Other to the Same, no ontology before ethics, no symmetrical reciprocity, no responsibility as a calculable list`

## (7) 测试提示词示例（现代题材：一个人是否该为自助结账机漏扫的商品付款）

- Prompt: `In the style of Levinas, a person at a self-checkout machine notices one item was not scanned. Do not begin with rules or utility. Begin with the face of the cashier, the Other who faces me and commands without words. Responsibility precedes freedom; I am already answerable before I choose. Paradox, no totality, no reciprocity.`
- 中文对照：列维纳斯风格：一个人在自助结账机前发现一件商品没有扫上。不要从规则或效用开始，而从收银员的脸开始——那张面对我的脸，无言地命令。责任先于自由；在我选择之前，我已经要回答。悖论，不要总体性，不要互惠。
- Negative: `No totalising system, no reduction of the Other to the Same, no ontology before ethics, no symmetrical reciprocity, no responsibility as a calculable list`
- 检验点：是否以脸的遭遇开篇而非以规则开篇；责任是否先于自由；结尾是否拒绝把责任写成清单。
