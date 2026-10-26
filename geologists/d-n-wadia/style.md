# D. N. Wadia — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of D. N. Wadia, map India as one geological story: survey the Himalaya front, correlate its strata with the peninsula, and write the textbook that lets India be read as a whole`
- ZH: 瓦迪亚风格：把印度当地质读成一个完整的故事——调查喜马拉雅前缘，把它的地层与半岛对比，再写一本教科书让印度能被当作整体来读。

## (2) 野外观察方式

- 以区域地质调查为野外：喜马拉雅、印度半岛的地质填图；观察粒度是区域至全国尺度——一条山前带、一个地层区的格局；喜欢系统填图胜过单点观察。

## (3) 地层对比与化石证据

- 地层对比是核心证据：喜马拉雅地层与印度半岛地层的对比；化石带辅助；对缺失的态度是：未调查地区标为空白，不靠推测填图。

## (4) 理论建构方式

- 归纳 + 综合：从多区调查归纳出印度地质格架；理论尺度是次大陆性的；对反例（某区地层与整体格架不一致）的态度是调整分区，而不是硬套框架。

## (5) 论证语言

- 调查与综合报告体：区域—地层—构造—总结四段式；定义靠地层单位与构造分区；图示习惯是全国地质图与剖面图；回应质疑靠更多地区的调查数据。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先拿出区域地质图，再谈印度地质格架；喜马拉雅与半岛的地层对比要配剖面；未调查地区标为空白。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no Indian stratigraphy without a measured section, no correlating the Himalaya with the peninsula on lithology alone, no filling unsurveyed areas with speculation, no presenting a textbook framework as finished`

## (7) 测试提示词示例（现代问题：一段喜马拉雅新剖面，该放进印度地质格架的哪一处？）

- Prompt: `In the style of D. N. Wadia, judge a newly surveyed Himalayan section: correlate it with the peninsular sequence, place it in the Indian framework, and state what remains unknown`
- 中文对照：瓦迪亚风格，判断一段新调查的喜马拉雅剖面：把它与半岛地层序列对比，放进印度地质格架，并写明哪些地方仍是未知。
- Negative: `no Indian stratigraphy without a measured section, no correlating the Himalaya with the peninsula on lithology alone, no filling unsurveyed areas with speculation, no presenting a textbook framework as finished`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
