# Paul F. Lazarsfeld — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文/转述不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paul Lazarsfeld: operationalised concepts, panel surveys, two-step flow, statistical models, no causal claim from one cross-section`
- ZH: 保罗·拉扎斯菲尔德风格：把社会学变成可测量的科学：抽样、问卷、面板、统计模型。

## (2) 研究方法组合

- 问卷调查与统计为主（约70%）、面板与追踪为辅（约20%）、定性访谈为辅（约10%）。`impression`
- 方法组合：把社会学变成可测量的科学：抽样、问卷、面板、统计模型。`impression`
- 数据来源：问卷、面板追踪数据、投票与收听率统计。`artifact`

## (3) 概念与语言

- 核心概念群：两级传播、意见领袖、面板调查、潜在结构分析、变量与指标、调查方法论。`impression`
- 定义方式：以著作中的概念辨析与操作化定义为主，概念随时期演变。`impression`
- 禁概念/禁方法：无指标的概念空谈、无抽样的概括。`impression`

## (4) 论证结构

- 结构：问题操作化—抽样与问卷—面板追踪—统计模型—谨慎的因果推断。`impression`
- 开头方式：以问题、田野场景、统计反常或概念辨析开场；结尾以理论提升、开放问题或政策含义收束。`impression`
- 证据呈现：案例、数据、图表、引文按著作分配；反例以比较与检验处理，不回避。`impression`

## (5) 语气与距离

- 语气：冷静、技术性、带方法论的自信；以操作化定义取信。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 抽样与问卷设计
- 面板追踪的变化
- 意见领袖的中介
- 潜在结构的统计模型
- 不该写：
- 无指标的概念空谈
- 用一次横断面数据谈因果
- 把相关写成因果
- Negative prompt: `No concept without indicators, no causal claim from one cross-section, no correlation as causation`

## (7) 测试提示词示例（现代题材：地铁乘客对约克夏犬反应的面板调查）

- Prompt: `In the style of Paul Lazarsfeld, design a panel survey of subway commuters' reactions to a Yorkshire terrier on a seat: operationalise civil inattention, sample by time and carriage, track the same riders over weeks, model opinion leaders, no causal claim from one cross-section.`
- 中文对照：拉扎斯菲尔德风格：为地铁乘客对座位上约克夏犬的反应设计面板调查——操作化“文明的漠视”、按时段与车厢抽样、数周追踪同一批乘客、建模意见领袖；不用一次横断面数据谈因果。
- Negative: `No concept without indicators, no causal claim from one cross-section, no correlation as causation`
- 检验点：方法组合是否对位；核心概念是否出现且定义精确；禁区写法是否未出现。
