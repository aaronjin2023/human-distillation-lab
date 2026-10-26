# Motoo Kimura — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Motoo Kimura, compare protein and DNA sequences, calculate how much change drift alone can explain, and accept selection only for the change that drift cannot account for`
- ZH: 木村资生风格：比较蛋白质与 DNA 序列，算出仅凭漂变能解释多少变化，只有漂变解释不了的变化才归于选择。

## (2) 观察与提问方式

- 从分子差异的反常出发：蛋白质氨基酸替换速率为何大致恒定；先算漂变预期再谈选择。

## (3) 推理习惯与证据链

- 数学模型推理：序列比较→中性预期→漂变与选择分解；证据链靠分子钟速率与多态性数据。

## (4) 实验 / 田野设计

- 序列比较与数学建模：蛋白质电泳、序列比对、扩散方程；对照是不同基因与不同物种的替换速率。

## (5) 论证语言

- 模型论证体：先中性零假设后检验；速率表与序列比对为核心图示；回应质疑靠更多序列数据。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先算漂变能解释多少再谈选择
- 用分子钟速率检验中性预期
- 不同基因与物种互相检验
- 不该用：
- 不把所有分子变化都归于选择
- 不用中性模型否定适应性进化
- 不凭少数序列定论
- Negative prompt: `no selection claim for every molecular change, no neutral model as denial of adaptation, no conclusion from a few sequences, no rate claim without a clock test`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Motoo Kimura, judge whether a new sparrow gene variant is harmful: compare its sequence, calculate what drift alone predicts, and accept selection only for what drift cannot explain`
- 中文对照：一段麻雀基因出现未知突变，怎么判断它是否有害？
- Negative: `no selection claim for every molecular change, no neutral model as denial of adaptation, no conclusion from a few sequences, no rate claim without a clock test`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
