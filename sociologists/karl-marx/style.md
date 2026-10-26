# Karl Marx — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Karl Marx: historical materialism, modes of production, alienation, surplus value, class struggle, the critique of political economy, no moralising without material analysis`
- ZH: 马克思风格：历史唯物主义、生产方式、异化、剩余价值、阶级斗争、政治经济学批判、没有物质分析就没有道德评判。

## (2) 研究方法组合

- 方法配比：批判分析为主（约 50%）、历史比较为辅（约 30%）、概念建构为辅（约 20%）；统计材料多取自官方报告与工厂视察记录（《资本论》以英国蓝皮书为重要来源）。。`impression`（学界通说）
- 数据来源：政治经济学文献、官方统计报告（蓝皮书）、工厂视察记录、历史上的生产方式对照。。
- 抽样与案例选择：以生产方式为案例单位，按原始—奴隶—封建—资本主义取样；以英国为资本主义典型个案，作重点解剖。。

## (3) 概念与语言

- 核心概念群（6 个）：历史唯物主义、生产方式、异化、剩余价值、阶级斗争、商品拜物教。`artifact`
- 定义方式：历史语境定义：概念从生产关系中提炼，如商品、价值、异化皆随生产方式而变；定义服务于历史分期。。
- 禁概念 / 禁方法：不用唯心史观，不用脱离物质生产的道德评判，不用无历史的普遍人性论，不用心理还原。。

## (4) 论证结构

- 结构：批判—重构：先批判既有政治经济学范畴，再以生产方式重构历史；开头多为对流行观念的颠倒，结尾多为历史趋势的判断。。`impression`
- 开头方式：以流行观念的颠倒开篇（如商品之谜）；结尾方式：以历史趋势判断收束，而非道德呼吁。
- 证据呈现：官方统计、工厂记录、历史对照；反例用生产方式差异解释。；反例处理：反例不删除，解释为不同生产方式或过渡形态的表现。。

## (5) 语气与距离

- 语气：热烈、批判、反讽。`impression`
- 与研究对象的距离：与被批判对象保持审判距离，与工人阶级保持同情距离；与读者的距离：直接对话、号召读者看穿表象。

## (6) 该写什么 / 不该写什么

- 该写：生产方式、剩余价值、异化、阶级斗争、商品拜物教、历史分期。
- 不该写：唯心史观、脱离物质的道德评判、无历史的普遍人性论、心理还原。
- Negative prompt: `No moralising without material analysis, no idealist explanation of history, no ahistorical universalism, no psychological reductionism`

## (7) 测试提示词示例（现代题材：外卖骑手的劳动时间）

- Prompt: `In the style of Karl Marx, analyse food-delivery riders' working time: the mode of production of platform labour, surplus value in algorithmic piece-rates, alienation, class struggle without moralising, historical materialism.`
- 中文对照：马克思风格：分析外卖骑手的劳动时间——平台劳动的生产方式、算法计件中的剩余价值、异化、阶级斗争、历史唯物主义，不作脱离物质的道德评判。
- Negative: `No moralising without material analysis, no idealist explanation of history, no ahistorical universalism, no psychological reductionism`
- 检验点：是否出现生产方式与剩余价值；是否以物质分析而非道德评判收束；是否拒绝唯心史观。
