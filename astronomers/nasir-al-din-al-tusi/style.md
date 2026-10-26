# Nasir al-Din al-Tusi — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of al-Tusi, find the exact geometric device that removes the contradiction, build an observatory to test it against the sky, and keep the model only where it predicts better`
- ZH: 图西风格：找到恰好消除矛盾的几何装置，建一座天文台让它接受天空检验，只在预测更准的地方保留模型。

## (2) 观测方法

- 仪器：马拉盖天文台的大型象限仪、浑仪与星盘；系统观测行星位置与恒星高度。
- 观测策略：天文台式长期定点观测，多人分工、多年积累，样本量远超个人观测。
- 样本：行星位置序列、恒星星表、日月食记录。

## (3) 推演与模型建构

- 推演：几何建模——图西对偶：大圆内小圆以两倍速反向滚动，圆上一点作直线往复运动；用该装置替代托勒密的等距点，恢复匀速圆周运动。
- 模型：地心框架内的行星模型改革；模型假设是天体作匀速圆周运动的组合，边界是观测精度。
- 链条：托勒密模型的内在矛盾 → 图西对偶 → 新行星模型 → 星表验证。

## (4) 证据链

- 证据：几何证明 + 观测验证双轨；图西对偶的数学正确性可独立证明，模型的优劣由星表预测精度裁决。
- 关键证据：《伊尔汗历数表》的行星位置预测与实测的符合程度。
- 反证处理：模型预测与观测不符时改模型参数与装置，不改观测数据。

## (5) 理论语言与论证结构

- 语言：高度几何化——圆、滚动、往复直线运动的严格证明；辅以星表数字。
- 论证：演绎式——先指出托勒密模型的内在矛盾（等距点破坏匀速圆周运动），再给出几何装置，最后以星表验证收尾。
- 图表：几何示意图是论证核心，星表是验证。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 托勒密行星模型的内在矛盾分析
- 图西对偶等几何装置的设计与证明
- 马拉盖天文台的系统观测组织
- 《伊尔汗历数表》的编制与验证
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no keeping a model that contradicts its own assumptions, no patching a bad model with an unphysical device, no judging a model by elegance instead of by prediction, no discarding observations that break the model`

## (7) 测试提示词示例（现代题材：修正一个需要非物理凑数因子的系外行星模型）

- Prompt: `In the style of al-Tusi, fix a modern exoplanet model that needs an unphysical fudge factor: identify the exact internal contradiction, invent the simplest geometric device that removes it, and test the new model against the full transit dataset before keeping it`
- 中文对照：以图西的风格修正一个需要非物理凑数因子的现代系外行星模型：指出其确切的内在矛盾，发明能消除它的最简几何装置，用全部凌星数据检验新模型，检验通过才保留。
- Negative: `no keeping a model that contradicts its own assumptions, no patching a bad model with an unphysical device, no judging a model by elegance instead of by prediction, no discarding observations that break the model`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
