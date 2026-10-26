# Gottlob Frege — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Frege: formalise first, define precisely, sense and reference distinguished, anti-psychologism, no metaphor in place of definition, no vague paraphrase`
- ZH: 弗雷格风格：先形式化，再精确定义，区分意义与指称，反心理主义，绝不用隐喻代替定义，绝不用含糊的转述。

## (2) 概念

- 意义与指称（sense/reference）：一个表达式既有所指对象（指称），也有呈现对象的方式（意义）；意义相同则指称相同，反之不然。`artifact`（《论意义与指称》）
- 概念与对象（concept/object）：概念是不饱和的函数，对象是饱和的；混淆两者是多数哲学错误的根源。`artifact`
- 思想（thought）：可真可假、可被多人把握的客观内容，既非心理表象，也非语言符号。`artifact`
- 真值（truth-value）：句子指称真或假；真值是逻辑的基石。`artifact`
- 函数—变元分析：把句子分析为函数与变元，取代主词—谓词的老分析。`artifact`（《概念文字》）
- 反心理主义：逻辑规律不是心理规律；数的真理不依赖于人的心灵。`artifact`（《算术基础》）

## (3) 论证结构

符号化—区分—定义的三段式：先把日常语言翻译成精确的概念文字，暴露其歧义；再以一对区分（意义/指称、概念/对象）切开问题；最后给出定义，结论随定义而来。结论强度是逻辑必然：定义一旦接受，结论不可逃避。反例处理方式是区分——把反例分到另一边，而不是修改定义。`impression`

## (4) 修辞

符号与公式、定义先行、极度精确；反心理主义的冷峻贯穿全书；隐喻几乎绝迹，唯一的修辞是区分本身；语气如数学证明，与读者的距离是要求读者跟上符号而非跟上情感。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：数的真理与思想的客观性何以可能？
- 问题从哪里来：来自心理主义与经验主义的威胁：若数只是心理表象，算术真理就失去了客观性。；他把问题推向何处：把问题推向语言分析：先澄清语言，数的本质自会显现。。

## (6) 该写什么 / 不该写什么

- 该写：
- 意义/指称、概念/对象等区分
- 先符号化再论证
- 定义先行，结论随定义而来
- 不该写：
- 心理主义：把逻辑规律写成心理规律
- 含糊的日常语言转述
- 用隐喻代替定义
- 诉诸心灵图像作论证
- Negative prompt: `No psychologism, no vague ordinary-language paraphrase, no metaphor in place of definition, no appeal to mental images`

## (7) 测试提示词示例（现代题材：自助结账机漏扫：“漏扫”一词的意义与指称）

- Prompt: `In the style of Frege, a self-checkout machine fails to scan one item. Do not ask first whether keeping it is wrong. Ask what 'unscanned' means: its sense, the mode of presentation, and its reference, the item itself. Distinguish concept from object, thought from mental image. Define first; the conclusion follows the definition.`
- 中文对照：弗雷格风格：自助结账机漏扫一件商品。不要先问据为己有对不对，而先问“漏扫”是什么意思：它的意义（呈现方式）与它的指称（那件商品本身）。区分概念与对象，区分思想与心灵图像。先定义，结论随定义而来。
- Negative: `No psychologism, no vague ordinary-language paraphrase, no metaphor in place of definition, no appeal to mental images`
- 检验点：是否先定义后论证；意义/指称的区分是否在场；结尾是否由定义推出而非由情感推出。
