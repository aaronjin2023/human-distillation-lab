# Émile Durkheim — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Émile Durkheim: social facts as things, collective conscience, mechanical and organic solidarity, anomie, the sacred and the profane, statistics with comparison`
- ZH: 涂尔干风格：社会事实即物、集体意识、机械团结与有机团结、失范、神圣与世俗、有比较的统计。

## (2) 研究方法组合

- 方法配比：统计调查为主（约 45%）、概念建构为辅（约 35%）、历史比较为辅（约 20%）；《自杀论》以官方自杀统计为核心证据。。`impression`（学界通说）
- 数据来源：官方自杀统计、宗教与图腾民族志、法律与职业规范文本；以比较统计表为证据骨架。。
- 抽样与案例选择：以社会类型为比较单位（天主教/新教国家、已婚/未婚、战时/平时），按整合与调节程度取样；以自杀率为因变量。。

## (3) 概念与语言

- 核心概念群（6 个）：社会事实、集体意识、机械团结与有机团结、失范、神圣与世俗、社会整合。`artifact`
- 定义方式：操作化定义：概念须以外在、可观察的指标界定，如社会事实以外在性与约束性定义；定义服务于统计比较。。
- 禁概念 / 禁方法：不用心理还原，不用个人动机解释社会事实，不用无比较的个案，不用道德评判作结论。。

## (4) 论证结构

- 结构：定义—分类—统计比较—理论：先界定社会事实，再分类，最后以统计比较验证理论。。`impression`
- 开头方式：以一个统计反常开篇（如新教国家自杀率高于天主教国家）；结尾方式：以社会整合程度的理论提升收束。
- 证据呈现：比较统计表、民族志对照；反例用整合与调节的二维差异解释。；反例处理：反例不删除，用整合—调节二维框架重新解释。。

## (5) 语气与距离

- 语气：冷峻、科学、立法式的确信。`impression`
- 与研究对象的距离：与研究对象保持科学疏离；与读者的距离：向读者出示证据的科学报告距离。

## (6) 该写什么 / 不该写什么

- 该写：社会事实、集体意识、机械团结与有机团结、失范、神圣与世俗、比较统计。
- 不该写：心理还原、个人动机解释、无比较的个案、道德评判作结论。
- Negative prompt: `No psychological reductionism, no individualist explanation of social facts, no moralising conclusion, no statistics without comparison`

## (7) 测试提示词示例（现代题材：深夜便利店里的排队）

- Prompt: `In the style of Émile Durkheim, analyse late-night queues at a convenience store: social facts as things, collective conscience in the queue, mechanical solidarity among strangers, anomie when the queue breaks, statistics with comparison.`
- 中文对照：涂尔干风格：分析深夜便利店里的排队——社会事实即物、排队中的集体意识、陌生人之间的机械团结、队伍散乱时的失范、有比较的统计。
- Negative: `No psychological reductionism, no individualist explanation of social facts, no moralising conclusion, no statistics without comparison`
- 检验点：是否出现社会事实与集体意识；是否以比较统计而非个人动机组织论证；是否拒绝心理还原。
