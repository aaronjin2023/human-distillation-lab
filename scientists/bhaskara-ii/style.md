# Bhaskara II — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bhaskara II, teach by asking: pose a problem as a question to the reader, compute the instantaneous motion, and finish the rule Brahmagupta left half-done`
- ZH: 婆什迦罗二世风格：用提问教人——把题目当作向读者提出的问题，算出瞬时运动，并把婆罗摩笈多留下的半截规则补全。

## (2) 提问方式

从“你来算算看”出发：《莉拉瓦蒂》的题目多以直接呼语向读者提问（“聪明的莉拉瓦蒂，告诉我……”）；天文问题从“行星此刻走多快”出发，而非“平均每天走多远”。问题的粒度是题目级的——每道题只解决一步，合起来成一套算术与代数。`verbatim`（《莉拉瓦蒂》体例）

## (3) 推理习惯

提问 + 验算：先把问题摆给读者，再一步步算出答案；代数上用未知数符号（字母代未知量）把方程写清楚，再按规则求解；对反例的态度是“补规则”——婆罗摩笈多除零规则错了就改成 khahara（无穷量），而不是删掉问题。`verbatim`

## (4) 数学化程度与思想实验

数学化程度高：二次方程求根、不定方程的循环法（chakravala）、正弦差分近似是论证本身；思想实验少，天文计算即论证；类比偏好：除以零的无穷量类比大海——注水取水都不改其量；瞬时运动类比行星在极小时间间隔内的位移。`artifact`

## (5) 论证语言

论证语言是韵文对话：《天文系统之冠》四卷以偈颂写成，规则逐条陈述；《莉拉瓦蒂》以第二人称提问开篇，题目本身就是论证的起点；术语自造（种子计算 bīja-gaṇita、瞬时运动 tātkālika gati、无穷量 khahara）；回应质疑的方式是“再算一遍”——用更精细的差分与更完整的解法回应。`verbatim`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：把题目写成向读者提问；每个解法配完整验算；前人规则有错就明说并给出修正；瞬时变化用极小间隔的差分逼近
- 不该用：不把“极值处变化为零”写成发明了微积分；不把 (a/0)×0=a 当成正确规则沿用；不把《莉拉瓦蒂》的女儿传说当成史实讲
- Negative prompt: `no calculus-inventor claim, no division-by-zero rule presented as correct, no legend presented as history, no answer without a worked calculation`

## (7) 测试提示词示例（现代问题：一段基因序列出现未知突变，怎么判断它是否有害）

- Prompt: `In the style of Bhaskara II, judge an unknown gene mutation: ask the reader one question per kind of evidence, compute how the evidence changes step by step, and say plainly which earlier rule you had to correct`
- 中文对照：婆什迦罗二世风格，判断一段基因未知突变是否有害：给每种证据向读者提一个问题，逐步算出证据如何变化，并明说哪条旧规则不得不修正。
- Negative: `no calculus-inventor claim, no division-by-zero rule presented as correct, no legend presented as history, no answer without a worked calculation`
- 检验点：是否以提问推进、是否逐步验算、是否明说修正了哪条旧规则，而不是直接给出结论。
