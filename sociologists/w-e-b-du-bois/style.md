# W. E. B. Du Bois — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of W. E. B. Du Bois: the color-line, double consciousness, the veil, the Philadelphia Negro survey, history and statistics together, no colour-blind analysis`
- ZH: 杜波依斯风格：颜色线、双重意识、面纱、费城黑人社区调查、历史与统计并用、没有色盲式分析。

## (2) 研究方法组合

- 方法配比：田野调查为主（约 40%）、统计调查为辅（约 30%）、历史比较为辅（约 20%）、批判分析为辅（约 10%）；《费城黑人》为社区调查与统计并用的早期典范。。`impression`（学界通说）
- 数据来源：社区入户调查、人口统计、历史文献、黑人报刊与教会记录；以费城第七区调查为证据骨架。。
- 抽样与案例选择：以社区为调查单位，逐户入户；以种族与阶级交叉取样；以费城为核心个案。。

## (3) 概念与语言

- 核心概念群（5 个）：颜色线、双重意识、面纱、才能的十分之一、费城黑人社区调查。`artifact`
- 定义方式：历史语境定义：概念从黑人经验中提炼，如双重意识先指看自我的两种目光，后扩展为种族经验的普遍结构；定义随历史而变。。
- 禁概念 / 禁方法：不用色盲式分析，不用无视种族的分层论，不用无数据的道德评判，不用无社区根基的统计。。

## (4) 论证结构

- 结构：历史—调查—理论：先讲黑人历史，再出示社区调查，最后以颜色线统摄。。`impression`
- 开头方式：以颜色线这一历史判断开篇；结尾方式：以黑人解放的历史前景收束，而非道德呼吁。
- 证据呈现：入户统计、历史对照、文学性叙述并置；反例用阶级与种族的交叉解释。；反例处理：反例不删除，解释为种族与阶级的交叉作用。。

## (5) 语气与距离

- 语气：热烈、悲悯、史诗式的庄严。`impression`
- 与研究对象的距离：与研究对象保持同情的近距离；与读者的距离：向读者揭示面纱之后的见证距离。

## (6) 该写什么 / 不该写什么

- 该写：颜色线、双重意识、面纱、社区调查、历史与统计并用。
- 不该写：色盲式分析、无视种族的分层论、无数据的道德评判、无社区根基的统计。
- Negative prompt: `No colour-blind analysis, no ignoring race in stratification, no moralising without data, no statistics without community grounding`

## (7) 测试提示词示例（现代题材：网约车司机的接单与评分）

- Prompt: `In the style of W. E. B. Du Bois, analyse ride-hailing drivers' orders and ratings: the color-line in the platform, double consciousness before the rating screen, the veil between driver and passenger, survey and history together, no colour-blind analysis.`
- 中文对照：杜波依斯风格：分析网约车司机的接单与评分——平台上的颜色线、评分屏幕前的双重意识、司机与乘客之间的面纱、调查与历史并用、没有色盲式分析。
- Negative: `No colour-blind analysis, no ignoring race in stratification, no moralising without data, no statistics without community grounding`
- 检验点：是否出现颜色线或双重意识；是否以社区调查与历史并用组织论证；是否拒绝色盲式分析。
