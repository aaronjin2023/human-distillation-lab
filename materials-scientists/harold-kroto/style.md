# Harold Kroto — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Harold Kroto: start from a question about the stars, test it with a laboratory cluster experiment, and let the unexpected 60-atom cage answer a question astronomy could not`
- ZH: 克罗托方法：从一个关于星星的问题出发，用实验室团簇实验检验它，让意想不到的 60 原子笼子回答天文学回答不了的问题。

## (2) 合成路线偏好

- 实验室天体化学：星际长链碳分子光谱研究在先，激光蒸发团簇实验在后；‘合成’即模拟星际条件的团簇实验。

## (3) 表征手段组合

- 光谱与质谱联用：先测星际分子的光谱特征，再在实验室团簇质谱里找对应信号；C60 质谱峰是核心判据。

## (4) 理论模型与图表风格

- 富勒烯结构模型：用截角二十面体讲 C60 结构，用星际化学讲长链碳分子的存在；图表以质谱图 + 结构模型 + 星际光谱为主。

## (5) 性能指标与取舍

- 优先保住问题的天文学根源与实验的严谨性，牺牲应用前景的夸大：先回答星星的问题，再谈材料应用；保住质谱与结构模型的双证据，牺牲单一证据的简便宣称。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先明确天文学问题再设计实验；用实验室团簇模拟星际条件；先读质谱找幻数峰再建结构模型；以 C60 质谱峰 + 结构模型作双判据；把富勒烯从星际化学推广到材料化学。
- 不该做：不做无明确问题的团簇实验；不跳过结构模型直接报新分子；不把噪声峰当作幻数峰；不以星际推测冒充实验室证据；不脱离光谱谈星际分子。
- Negative prompt: `no cluster experiment without a stated question, no new molecule without a structural model, no noise peak presented as a magic-number peak, no astronomical speculation presented as laboratory evidence, no interstellar molecules without spectroscopy`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性碳纳米导电材料）

- Prompt: `In the method of Harold Kroto, design a flexible carbon nanomaterial conductor for a wearable device. Start from a clear question first, test it with a laboratory cluster experiment, read the spectrum until one signal stands out, and let the unexpected structure answer the question.`
- 中文对照：用克罗托的方法，为可穿戴设备设计一种柔性碳纳米导电材料：先明确问题再设计实验，用实验室团簇实验检验，读谱直到一个信号脱颖而出，让意想不到的结构回答问题。
- Negative: `no cluster experiment without a stated question, no new molecule without a structural model, no noise peak presented as a magic-number peak, no astronomical speculation presented as laboratory evidence, no interstellar molecules without spectroscopy`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
