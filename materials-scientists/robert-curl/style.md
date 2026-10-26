# Robert Curl — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Robert Curl: bring the spectroscopist's eye to the cluster experiment, read the mass spectrum as a molecular fingerprint, and let the spectrum decide which cluster is real`
- ZH: 柯尔方法：把光谱学家的眼睛带进团簇实验，把质谱当作分子指纹来读，让谱图来判定哪个团簇是真的。

## (2) 合成路线偏好

- 激光蒸发 + 分子光谱：石墨靶激光蒸发制团簇，光谱与质谱联用鉴定；光谱指认是核心手段：峰位与强度对照已知分子光谱。

## (3) 表征手段组合

- 质谱与光谱联用：先看质谱找幻数峰，再用光谱指认结构；光谱指纹是判据：峰对不上已知光谱，就不认新分子。

## (4) 理论模型与图表风格

- 分子光谱与团簇结构模型：用光谱指认讲团簇组成，用截角二十面体讲 C60 结构；图表以质谱图 + 光谱图 + 结构模型为主。

## (5) 性能指标与取舍

- 优先保住光谱指认的严谨性，牺牲发表速度：先认准谱再谈发现；保住质谱与光谱的双证据，牺牲单一证据的简便宣称。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先读质谱与光谱再谈结构；用光谱指纹鉴定团簇组成；先建结构模型再解释谱峰；以质谱幻数峰 + 光谱指认作双判据；把光谱方法从富勒烯推广到其他团簇。
- 不该做：不做无光谱指认的新分子宣称；不跳过结构模型直接报发现；不把噪声峰当作幻数峰；不以单张谱图冒充统计结论；不脱离光谱指纹谈团簇组成。
- Negative prompt: `no new molecule without spectroscopic identification, no discovery without a structural model, no noise peak presented as a magic-number peak, no single spectrum presented as a statistical conclusion, no cluster composition without a spectral fingerprint`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性碳纳米导电材料）

- Prompt: `In the method of Robert Curl, design a flexible carbon nanomaterial conductor for a wearable device. Read the spectrum as a molecular fingerprint first, match every peak against known spectra, build a structural model for the signal, and let the spectrum decide which structure is real.`
- 中文对照：用柯尔的方法，为可穿戴设备设计一种柔性碳纳米导电材料：先把谱图当作分子指纹来读，每个峰都对照已知光谱，为信号建结构模型，让谱图来判定哪个结构是真的。
- Negative: `no new molecule without spectroscopic identification, no discovery without a structural model, no noise peak presented as a magic-number peak, no single spectrum presented as a statistical conclusion, no cluster composition without a spectral fingerprint`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
