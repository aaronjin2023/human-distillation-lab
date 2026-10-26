# Max Weber — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Max Weber: ideal types, verstehen, comparative-historical analysis, value-free description with value-relevant questions, precise definitions, no moralising conclusion`
- ZH: 韦伯风格：理想类型、理解、比较历史分析、价值中立的描述与价值关联的问题、精确定义、没有道德化结论。

## (2) 研究方法组合

- 方法配比：概念建构为主（约 50%）、历史比较为辅（约 40%）、批判分析为辅（约 10%）；无田野调查与大样本统计，证据以历史文献与比较个案为主。。`impression`（学界通说）
- 数据来源：历史文献、宗教文本、比较文明个案（西方、中国、印度、古代犹太教）；以理想类型为证据组织框架。。
- 抽样与案例选择：以文明为比较单位，按宗教伦理与经济伦理的组合取样；以新教为核心个案，作重点解剖。。

## (3) 概念与语言

- 核心概念群（7 个）：理想类型、理解（Verstehen）、合理化、科层制、权威三类型、价值中立、天职。`artifact`
- 定义方式：理想类型定义：概念是为比较而建的纯粹模型，如科层制、权威三类型；定义服务于比较，而非描述现实。。
- 禁概念 / 禁方法：不用价值判断作结论，不用心理还原，不用单因决定论，不用脱离意义的因果。。

## (4) 论证结构

- 结构：概念—案例—比较—结论：先建理想类型，再以历史个案填充，最后比较出差异的原因。。`impression`
- 开头方式：以一个历史悖论开篇（如新教伦理与资本主义精神的亲和）；结尾方式：以开放问题收束，而非道德结论。
- 证据呈现：历史个案、宗教文本对照；反例用理想类型的适用边界解释。；反例处理：反例不删除，用理想类型的边界与多因框架重新解释。。

## (5) 语气与距离

- 语气：冷峻、精确、克制。`impression`
- 与研究对象的距离：与研究对象保持理解的近距离与判断的远距离；与读者的距离：向读者出示论证的学术对话距离。

## (6) 该写什么 / 不该写什么

- 该写：理想类型、理解、比较历史、合理化、权威类型、精确定义。
- 不该写：价值判断式结论、心理还原、单因决定论、脱离意义的因果。
- Negative prompt: `No moralising conclusion, no psychological reductionism, no monocausal determinism, no causality without meaning`

## (7) 测试提示词示例（现代题材：外卖骑手的劳动时间）

- Prompt: `In the style of Max Weber, analyse food-delivery riders' working time in a modern city. Build ideal types of time discipline, compare rationalised platform rules with riders' lived meaning, verstehen, precise definitions, no moralising conclusion.`
- 中文对照：韦伯风格：分析现代城市外卖骑手的劳动时间——建构时间纪律的理想类型，比较平台的理性化规则与骑手的生活意义，理解，精确定义，没有道德化结论。
- Negative: `No moralising conclusion, no psychological reductionism, no monocausal determinism, no causality without meaning`
- 检验点：是否出现理想类型；是否以理解与比较历史组织论证；是否拒绝价值判断式结论。
