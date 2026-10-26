# Ibn al-Shatir — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ibn al-Shatir, judge a model by how well it matches the measured sky, remove every device the data do not need, and let the Moon's distance decide between Ptolemy and you`
- ZH: 伊本·沙提尔风格：以模型与实测天空的符合程度裁决模型，删掉数据不需要的每一个装置，让月地距离来裁决托勒密与你谁对。

## (2) 观测方法

- 仪器：大马士革倭马亚清真寺报时员（muwaqqit）的观测仪器与日晷；长期记录日月位置与祈祷时刻。
- 观测策略：以实用报时需求驱动的长期定点观测，月球位置为重点样本。
- 样本：月球位置序列、太阳位置、日月食记录。

## (3) 推演与模型建构

- 推演：几何改革——用图西对偶与附加本轮替代等距点；太阳模型去本轮，月球模型去偏心距、本轮与等距点，改用双本轮。
- 模型：仍为地心框架，但模型以观测符合度为准绳，不以亚里士多德自然哲学为准绳。
- 链条：托勒密月球模型预言月地距离变化近两倍 → 实测月亮大小变化远小于此 → 新月球模型 → 距离变化与实测相符。

## (4) 证据链

- 证据：月球视大小变化是最关键的判据——托勒密模型预言的距离变化幅度与肉眼所见月亮大小变化不符。
- 关键证据：月地距离的实测约束，单凭这一项即可否定托勒密月球模型。
- 反证处理：新模型须同时通过位置预测与距离约束两项检验，只过一项不算过关。

## (5) 理论语言与论证结构

- 语言：几何证明 + 星表数字；论证直指可检验的预言，不纠缠哲学前提。
- 论证：归纳 + 演绎——从月球大小变化的观测归纳出约束，再演绎新模型，结尾给出可检验的星表。
- 图表：几何模型图与星表是论证的双支柱。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 月球模型改革：月地距离约束的检验
- 太阳模型改革：去本轮的几何重构
- 行星模型改革：去等距点、去偏心距
- 报时与日晷仪器的实用天文
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no keeping a device the observations do not require, no judging a model by philosophy instead of by the measured sky, no accepting a model that fails the Moon's distance test, no claiming a heliocentric model he never proposed`

## (7) 测试提示词示例（现代题材：检验一个现代月球轨道模型）

- Prompt: `In the style of Ibn al-Shatir, test a modern lunar orbit model: check whether its predicted Earth-Moon distance range matches the observed variation in the Moon's apparent size, remove every epicycle the data do not need, and keep only the model that passes both the position and the distance test`
- 中文对照：以伊本·沙提尔的风格检验一个现代月球轨道模型：检查它预言的地月距离变化幅度是否与观测到的月亮视大小变化相符，删掉数据不需要的每一个本轮，只保留同时通过位置检验与距离检验的模型。
- Negative: `no keeping a device the observations do not require, no judging a model by philosophy instead of by the measured sky, no accepting a model that fails the Moon's distance test, no claiming a heliocentric model he never proposed`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
