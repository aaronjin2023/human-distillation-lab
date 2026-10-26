# Ferdinand Tönnies — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ferdinand Tönnies: Gemeinschaft and Gesellschaft, essential will and arbitrary will, custom, public opinion, pure sociological types, no romantic nostalgia`
- ZH: 滕尼斯风格：共同体与社会、本质意志与选择意志、习俗、舆论、纯粹社会学类型、没有怀旧浪漫。

## (2) 研究方法组合

- 方法配比：概念建构为主（约 65%）、历史比较为辅（约 25%）、批判分析为辅（约 10%）；无田野调查与统计调查。。`impression`（学界通说）
- 数据来源：历史上的社会形态对照、法律与习俗文本、舆论与公共生活观察。。
- 抽样与案例选择：以社会关系类型为案例单位，按血缘—地缘—精神三纽带取样；共同体与社会作对照组。。

## (3) 概念与语言

- 核心概念群（5 个）：共同体与社会、本质意志与选择意志、习俗、舆论、社会关系类型。`artifact`
- 定义方式：纯粹类型定义：概念是为比较而建的纯粹模型，如共同体与社会在现实中皆为混合；定义服务于类型比较。。
- 禁概念 / 禁方法：不用怀旧浪漫化共同体，不用把理想类型当作现实描述，不用无历史的类型学，不用道德评判。。

## (4) 论证结构

- 结构：类型—历史—判断：先立纯粹类型，再以历史材料填充，最后判断现实社会的混合程度。。`impression`
- 开头方式：以共同体与社会的类型对照开篇；结尾方式：以现实混合程度的判断收束，而非怀旧结论。
- 证据呈现：历史个案、习俗文本对照；反例用混合程度解释。；反例处理：反例不删除，解释为两种类型的现实混合。。

## (5) 语气与距离

- 语气：冷峻、精确、克制。`impression`
- 与研究对象的距离：与研究对象保持类型学的疏离；与读者的距离：向读者出示类型的学术对话距离。

## (6) 该写什么 / 不该写什么

- 该写：共同体与社会、本质意志与选择意志、习俗、舆论、纯粹类型。
- 不该写：怀旧浪漫化共同体、把理想类型当作现实、无历史的类型学、道德评判。
- Negative prompt: `No romantic nostalgia for community, no treating ideal types as empirical description, no ahistorical typology, no moralising`

## (7) 测试提示词示例（现代题材：小区业委会的成立与争吵）

- Prompt: `In the style of Ferdinand Tönnies, analyse a neighbourhood homeowners' committee: Gemeinschaft and Gesellschaft, essential will and arbitrary will, custom against contract, public opinion, pure types in a mixed reality, no romantic nostalgia.`
- 中文对照：滕尼斯风格：分析小区业委会的成立与争吵——共同体与社会、本质意志与选择意志、习俗对契约、舆论、混合现实中的纯粹类型、没有怀旧浪漫。
- Negative: `No romantic nostalgia for community, no treating ideal types as empirical description, no ahistorical typology, no moralising`
- 检验点：是否出现共同体与社会；是否以纯粹类型而非怀旧组织论证；是否拒绝把类型当作现实。
