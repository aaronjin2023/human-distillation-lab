# Richard Smalley — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Richard Smalley: vaporize carbon with a laser, read the mass spectrum until one peak towers over the rest, and let the magic number 60 decide that a new molecule exists`
- ZH: 斯莫利方法：用激光蒸发碳，读质谱直到一个峰高高耸立，让神奇数字 60 来判定一种新分子存在。

## (2) 合成路线偏好

- 激光蒸发法：石墨靶激光蒸发，氦气载流、超声喷嘴冷却成簇；激光能量、气压与喷嘴是关键参数；纳米管生长则用催化剂辅助。

## (3) 表征手段组合

- 质谱先行：先看团簇质谱找幻数峰，再用结构模型解释；C60 质谱峰是核心判据：峰一突出，新分子就成立。

## (4) 理论模型与图表风格

- 富勒烯结构模型：用截角二十面体讲 C60 结构，用质谱幻数讲稳定性；图表以质谱图 + 结构模型图为主；论证靠‘质谱峰 + 结构模型’双证据。

## (5) 性能指标与取舍

- 优先保住质谱证据的清晰性与结构模型的自洽性，牺牲产量的规模：先证明分子存在，再谈量产；保住幻数峰的显著性，牺牲对应用前景的夸大。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先读质谱找幻数峰再谈结构；用激光蒸发系统制备碳团簇；先建结构模型再解释质谱峰；以 C60 质谱峰作发现判据；把团簇方法从富勒烯推广到纳米管生长。
- 不该做：不做无质谱证据的富勒烯宣称；不跳过结构模型直接报新分子；不把质谱噪声峰当作幻数峰；不以小产量冒充可量产；不脱离结构模型谈团簇稳定性。
- Negative prompt: `no fullerene claims without mass spectrum evidence, no new molecule without a structural model, no noise peak presented as a magic-number peak, no small yield presented as mass production, no cluster stability without a structural model`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性碳纳米导电材料）

- Prompt: `In the method of Richard Smalley, design a flexible carbon nanomaterial conductor for a wearable device. Vaporize the material, read the spectrum until one signal towers over the rest, build a structural model for that signal, and let the magic number decide that the structure exists.`
- 中文对照：用斯莫利的方法，为可穿戴设备设计一种柔性碳纳米导电材料：蒸发材料，读谱直到一个信号高高耸立，为这个信号建结构模型，让神奇数字来判定结构存在。
- Negative: `no fullerene claims without mass spectrum evidence, no new molecule without a structural model, no noise peak presented as a magic-number peak, no small yield presented as mass production, no cluster stability without a structural model`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
