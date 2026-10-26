# James S. Coleman — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文/转述不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Coleman: national survey evidence, social capital, rational-choice foundations, no school-only explanation`
- ZH: 詹姆斯·科尔曼风格：以全国教育调查为底：学校差异小于家庭与同伴差异。

## (2) 研究方法组合

- 大规模调查与统计为主（约70%）、概念建构为辅（约20%）、比较为辅（约10%）。`impression`
- 方法组合：以全国教育调查为底：学校差异小于家庭与同伴差异。`impression`
- 数据来源：全国教育调查、学校与学生数据、问卷。`artifact`

## (3) 概念与语言

- 核心概念群：社会资本、理性选择、教育机会平等、 Coleman 报告、社会理论基础、信任与规范。`impression`
- 定义方式：以著作中的概念辨析与操作化定义为主，概念随时期演变。`impression`
- 禁概念/禁方法：只谈学校投入不谈家庭与社会资本、把相关写成因果。`impression`

## (4) 论证结构

- 结构：全国数据—学校与家庭的分解—社会资本概念—政策含义。`impression`
- 开头方式：以问题、田野场景、统计反常或概念辨析开场；结尾以理论提升、开放问题或政策含义收束。`impression`
- 证据呈现：案例、数据、图表、引文按著作分配；反例以比较与检验处理，不回避。`impression`

## (5) 语气与距离

- 语气：冷静、技术性、带政策的争议感；以大规模数据挑战常识。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 教育机会的全国测量
- 社会资本的定义与测量
- 家庭与同伴的影响
- 理性选择的微观基础
- 不该写：
- 只谈学校经费不谈社会资本
- 用横断面数据谈教育因果
- 无全国数据的教育断言
- Negative prompt: `No school-only explanation, no causal claim from cross-sectional data, no education claim without national data`

## (7) 测试提示词示例（现代题材：地铁沿线补习班的成绩）

- Prompt: `In the style of James Coleman, analyse a subway cram school's results: national-style survey first, decompose school, family and peer effects, measure social capital in parents' networks, no school-only explanation without data.`
- 中文对照：科尔曼风格：分析地铁沿线补习班的成绩——先做全国式调查，分解学校、家庭与同伴效应，测量家长网络里的社会资本；不写没有数据的唯学校论。
- Negative: `No school-only explanation, no causal claim from cross-sectional data, no education claim without national data`
- 检验点：方法组合是否对位；核心概念是否出现且定义精确；禁区写法是否未出现。
