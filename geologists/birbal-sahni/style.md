# Birbal Sahni — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Birbal Sahni, read Gondwana in a fossil leaf: collect plant fossils from the Indian Gondwana beds, compare their venation and cuticle with living plants, and let the flora date the beds`
- ZH: 萨尼风格：在一片化石叶里读冈瓦纳——从印度冈瓦纳地层里采集植物化石，比对叶脉与角质层与现生植物，再让植物群给地层定年。

## (2) 野外观察方式

- 以化石采集与显微观察为野外：印度冈瓦纳地层的植物化石；观察粒度是标本尺度——一片叶的叶脉、一块茎的解剖；喜欢成批标本的系统比较胜过单个精美标本。

## (3) 地层对比与化石证据

- 植物化石对比是核心证据：叶脉、角质层与生殖结构的形态；与现生植物对照；地层对比上，植物群组合用于冈瓦纳地层的对比与定年；对缺失的态度是：保存差的标本不定种，只写到属或形态类型。

## (4) 理论建构方式

- 归纳 + 对照：从植物群组合归纳出冈瓦纳植物群的特征；五柱木目的建立是分类学工作；理论尺度是植物群与地层；对反例（某标本不合已知类群）的态度是新立类型，而不是硬塞进旧类。

## (5) 论证语言

- 古植物论证体：标本—形态—对比—地层四段式；定义严格（叶脉类型、角质层特征）；图示习惯是化石照片与显微绘图；回应质疑靠更多标本与更完整的形态描述。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先写清标本的保存状况与产地层位，再谈分类；叶脉与角质层要一起看，不只看外形；保存差的标本不定种，只写到能确定的级别。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no species named from a poorly preserved specimen, no classifying by leaf outline alone, no dating a bed from a single fossil leaf, no forcing an odd specimen into a known genus`

## (7) 测试提示词示例（现代问题：一块新的冈瓦纳植物化石，能给地层定年吗？）

- Prompt: `In the style of Birbal Sahni, judge a new Gondwana plant fossil: describe its venation and cuticle, compare it with living and fossil relatives, and decide what it can and cannot tell about the bed it came from`
- 中文对照：萨尼风格，判断一块新的冈瓦纳植物化石：描述它的叶脉与角质层，与现生及化石亲缘类群比对，再判定它能告诉我们什么、不能告诉我们什么。
- Negative: `no species named from a poorly preserved specimen, no classifying by leaf outline alone, no dating a bed from a single fossil leaf, no forcing an odd specimen into a known genus`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
