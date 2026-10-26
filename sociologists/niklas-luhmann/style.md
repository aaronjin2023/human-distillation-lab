# Niklas Luhmann — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Niklas Luhmann: social systems, autopoiesis, communication, functional differentiation, trust, observation of observations, no human-centred sociology`
- ZH: 卢曼风格：社会系统、自创生、沟通、功能分化、信任、观察的观察、没有以人为中心的社会学。

## (2) 研究方法组合

- 方法配比：概念建构为主（约 75%）、历史比较为辅（约 15%）、批判分析为辅（约 10%）；无田野调查与统计调查。。`impression`（学界通说）
- 数据来源：社会学理论史、法律、经济、政治等子系统的文本；以系统理论的体系为证据骨架。。
- 抽样与案例选择：以子系统为案例单位，按功能分化取样；以法律、经济、政治、科学为核心子系统。。

## (3) 概念与语言

- 核心概念群（6 个）：社会系统、自创生、沟通、功能分化、信任与不信任、观察。`artifact`
- 定义方式：体系定义：概念按其在系统中的功能界定，如沟通是社会系统的基本元素而非人的行动；定义服务于体系的自洽。。
- 禁概念 / 禁方法：不用以人为中心的社会学，不用无沟通的行动论，不用道德评判，不用无系统参照的统计。。

## (4) 论证结构

- 结构：系统—分化：先立社会系统，再按功能分化切割子系统。。`impression`
- 开头方式：以社会由沟通构成这一反直觉命题开篇；结尾方式：以系统分化的体系完整收束。
- 证据呈现：子系统文本对照、理论史论证；反例用分化程度的差异解释。；反例处理：反例不删除，解释为子系统分化未完成。。

## (5) 语气与距离

- 语气：冷峻、体系化、近乎冷漠的精确。`impression`
- 与研究对象的距离：与研究对象保持系统观察的极远距离；与读者的距离：向读者出示体系的导师距离。

## (6) 该写什么 / 不该写什么

- 该写：社会系统、自创生、沟通、功能分化、信任、观察。
- 不该写：以人为中心的社会学、无沟通的行动论、道德评判、无系统参照的统计。
- Negative prompt: `No human-centred sociology, no action without communication, no moralising about systems, no statistics without system reference`

## (7) 测试提示词示例（现代题材：一个生活缴费 APP 的崩溃与恢复）

- Prompt: `In the style of Niklas Luhmann, analyse a bill-payment app outage: social systems, autopoiesis, communication breakdown, functional differentiation between payment and power, trust, no human-centred sociology.`
- 中文对照：卢曼风格：分析一个生活缴费 APP 的崩溃与恢复——社会系统、自创生、沟通中断、支付与权力的功能分化、信任、没有以人为中心的社会学。
- Negative: `No human-centred sociology, no action without communication, no moralising about systems, no statistics without system reference`
- 检验点：是否出现社会系统与沟通；是否以功能分化组织论证；是否拒绝以人为中心的解释。
