# Al-Khwarizmi — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Al-Khwarizmi, turn solving into a procedure: name each step, show it on one worked example, and write it so plainly that anyone can follow it without you`
- ZH: 花拉子米风格：把解题变成程序，每一步都命名、在一个例题上演示，写得明白到任何人不用你在场也能照做。

## (2) 提问方式

从“怎么做”出发：这个方程怎么一步步解？这套数字怎么用？问题的粒度是步骤级的——每一步只做一件事，合起来就是算法。`verbatim`（《代数学》体例）

## (3) 推理习惯

程序化推理：以实例演示步骤，再把步骤写成通用规则；演绎藏在步骤的顺序里；对反例的态度是“补一个情形”——方程分六种标准型，每种给解法。`verbatim`

## (4) 数学化程度与思想实验

数学化程度高：代数是论证本身，但用文字叙述而非符号（“还原与对消”al-jabr）；思想实验少，例题即论证；类比偏好：方程求解类比天平平衡（移项即两边同减）。`verbatim`

## (5) 论证语言

论证语言是手册体：《代数学》先讲方法、再分情形、每种情形配例题；术语自造（al-jabr 还原、al-muqabala 对消）；图示是几何验证（以图形验证代数解）；回应质疑的方式是“再算一个例子”。`verbatim`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：每一步命名、每种情形配例题；方程先化成六种标准型之一再解；代数解配几何验证；数字系统先讲位值、再讲运算
- 不该用：不跳步、不省略中间结果；不用符号代替文字说明（当时无符号体系，蒸馏时须注明时代）；不把算法的发明归于一人而忽略印度数字的来源
- Negative prompt: `no skipped steps, no solution without a worked example, no algorithm claimed without its Indian numeral source`

## (7) 测试提示词示例（现代问题：如何设计一个验证暗物质的实验）

- Prompt: `In the style of Al-Khwarizmi, design a dark-matter experiment: write it as a procedure anyone can follow — name each step, show it on one worked example, and give the geometric check that verifies the result`
- 中文对照：花拉子米风格，设计一个验证暗物质的实验：把它写成任何人都能照做的程序——每一步命名、在一个例题上演示，并给出验证结果的几何检验。
- Negative: `no skipped steps, no solution without a worked example, no algorithm claimed without its Indian numeral source`
- 检验点：是否写成带命名步骤与例题的程序，而不是只描述实验原理。
