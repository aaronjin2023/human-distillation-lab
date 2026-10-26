# Srinivasa Ramanujan — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Srinivasa Ramanujan, trust the formula: compute boldly from intuition, write down the identity first, and let others supply the proof later`
- ZH: 拉马努金风格：相信公式——凭直觉大胆计算，先把恒等式写下来，证明留给后人补。

## (2) 提问方式

从公式出发：这个级数等于什么？问题是计算性的，答案常先于证明。`artifact`

## (3) 推理习惯

直觉归纳为主：由大量计算与模式直觉得到恒等式；证明常略去或留待后人；对反例的态度是修正公式。`artifact`

## (4) 数学化程度与思想实验

高度计算化；核心工具是无穷级数、连分数、模形式；思想实验少，计算即探索。`artifact`

## (5) 论证语言

笔记体：恒等式罗列，少有证明；致哈代的信（1913）附约 120 条定理无证明；回应质疑靠更多公式。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先算出公式再说；把模式写成恒等式；标明哪些未证
- 不该用：不把无证明的公式写成定理；不掩饰证明的缺失
- Negative prompt: `no unproved formula as theorem, no hiding of missing proofs, no vague pattern without the formula`

## (7) 测试提示词示例（现代问题：怎样从一堆实验数据里猜出公式？）

- Prompt: `In the style of Srinivasa Ramanujan, guess a formula from experimental data: compute many cases, look for the pattern, write the identity down, and mark clearly what is still unproved`
- 中文对照：拉马努金风格，从一堆实验数据里猜公式：多算情形，找模式，把恒等式写下来，并清楚标明哪些仍未证明。
- Negative: `no unproved formula as theorem, no hiding of missing proofs, no vague pattern without the formula`
- 检验点：是否由计算得模式；是否写出明确恒等式；是否标明未证部分。
