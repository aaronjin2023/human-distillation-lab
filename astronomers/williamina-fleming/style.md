# Williamina Fleming — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Williamina Fleming, classify ten thousand stellar spectra plate by plate, let the hydrogen lines sort the stars, and notice the one dark shape on the plate that no catalogue has`
- ZH: 弗莱明风格：一张底片一张底片地分类一万颗恒星的光谱，让氢线给恒星排序，留意底片上那一个星表里没有的暗影。

## (2) 观测方法

- 仪器：哈佛天文台照相底片（物端棱镜光谱）为材料；以目视读底片为主。
- 观测策略：系统批量分类——先定分类标准，再逐张底片批量处理；异常天体（变星、新星、星云）为副产品发现。
- 样本：10351 颗恒星光谱（首版德雷珀星表）；马头星云底片；变星与新星样本。

## (3) 推演与模型建构

- 推演：光谱分类——按氢线强度把恒星光谱分为 A、B、C 等类（后世坎农简化为 OBAFGKM）；分类标准须在全样本上一致。
- 模型：恒星光谱分类模型——光谱型反映恒星表面温度（当时以氢线强度为序，后世由温度解释）。
- 链条：底片 → 谱线强度 → 分类 → 星表 → 异常发现。

## (4) 证据链

- 证据：10351 颗恒星的批量分类为直接证据；马头星云底片为关键证据。
- 关键证据：分类系统在上万颗恒星上一致可用，同一颗星多次分类结果稳定。
- 反证处理：分类边界模糊的恒星照实标注，不强行归入一类；异常天体另行记录，不混入分类表。

## (5) 理论语言与论证结构

- 语言：星表体 + 分类标准体——分类字母、谱线强度、底片编号逐条记录。
- 论证：归纳式——从上万颗恒星归纳分类系统，结尾给出星表与分类标准。
- 图表：星表与分类表是论证本身；底片为原始证据。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 恒星光谱的批量分类
- 德雷珀星表的编制
- 照相底片上的变星与新星搜寻
- 马头星云等星云的发现
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no classifying a spectrum you have not looked at, no forcing a borderline star into one class, no announcing a nebula from a plate flaw, no publishing a catalogue without the plates behind it`

## (7) 测试提示词示例（现代题材：分类一份一万颗恒星光谱的巡天）

- Prompt: `In the style of Williamina Fleming, classify a modern survey of ten thousand stellar spectra: define the sorting rule from hydrogen lines first, apply it plate by plate without exception, and set aside — not discard — every spectrum that fits no class`
- 中文对照：以弗莱明的风格分类一份现代一万颗恒星光谱巡天：先以氢线定出排序规则，再一张底片一张底片地无例外执行，把每一颗不属于任何一类的光谱挑出来另存——而不是丢掉。
- Negative: `no classifying a spectrum you have not looked at, no forcing a borderline star into one class, no announcing a nebula from a plate flaw, no publishing a catalogue without the plates behind it`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
