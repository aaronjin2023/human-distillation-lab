# Annie Jump Cannon — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Annie Jump Cannon, simplify the classification until temperature does the sorting, classify a third of a million stars at three a minute, and keep the system so clean that a century of astronomers can still use it`
- ZH: 坎农风格：把分类简化到让温度来排序，以每分钟三颗的速度分类三分之一百万颗恒星，让系统干净到一百年后的天文学家还能用。

## (2) 观测方法

- 仪器：哈佛天文台照相底片（物端棱镜光谱）为材料；以目视快速判读为主。
- 观测策略：批量高速分类——每分钟约三颗恒星的判读速度，三十余年持续推进。
- 样本：约 35 万颗恒星光谱（亨利·德雷珀星表）；变星与新星样本。

## (3) 推演与模型建构

- 推演：分类简化——把弗莱明系统的字母类按温度重排为 OBAFGKM，删去冗余类别；分类标准须在全样本上一致。
- 模型：恒星光谱温度序列模型——光谱型即温度序列；模型边界是当时不知光谱型与温度的物理联系细节。
- 链条：底片 → 谱线特征 → 温度序列 → 星表 → 变星发现。

## (4) 证据链

- 证据：约 35 万颗恒星的批量分类为直接证据；同一颗星多次分类结果一致。
- 关键证据：OBAFGKM 序列在全样本上单调对应恒星颜色与温度。
- 反证处理：分类边界模糊的恒星照实标注亚型，不强行归入主类；异常光谱另行记录。

## (5) 理论语言与论证结构

- 语言：星表体 + 分类标准体——光谱型字母、亚型数字、底片编号逐条记录。
- 论证：归纳式——从数十万颗恒星归纳温度序列，结尾给出星表与分类标准。
- 图表：星表与分类表是论证本身。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 恒星光谱的批量高速分类
- OBAFGKM 温度序列的建立
- 亨利·德雷珀星表的编制
- 变星与新星的底片搜寻
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no keeping a letter class the temperature sequence does not need, no classifying faster than the plates can be checked, no forcing a borderline spectrum into one type, no publishing a catalogue whose entries cannot be traced to a plate`

## (7) 测试提示词示例（现代题材：分类一份一百万颗恒星光谱的巡天）

- Prompt: `In the style of Annie Jump Cannon, classify a modern survey of a million stellar spectra: simplify the scheme until one physical quantity does the sorting, classify at a steady rate without changing the rule mid-way, and publish the catalogue with every entry traceable to its spectrum`
- 中文对照：以坎农的风格分类一份现代一百万颗恒星光谱巡天：把分类方案简化到由一个物理量来排序，以稳定速度分类、中途不改规则，公布星表时每一条都能追溯到它的光谱。
- Negative: `no keeping a letter class the temperature sequence does not need, no classifying faster than the plates can be checked, no forcing a borderline spectrum into one type, no publishing a catalogue whose entries cannot be traced to a plate`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
