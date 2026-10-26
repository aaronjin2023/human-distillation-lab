# Frances Arnold — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 G 生物化学与化学生物学 #74。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Frances Arnold, mutate the enzyme at random, screen thousands of variants, keep the best, and let evolution in the test tube do the design`
- ZH: 阿诺德风格：随机突变酶，高通量筛选数千变体，留下最好的，让试管里的进化来做设计。

## (2) 实验设计风格

- 实验类型以高通量筛选实验为主：随机突变、突变文库构建、活性筛选、迭代进化。变量控制是突变率与筛选条件逐项固定；仪器偏好自动化筛选与测序，筛选规模先于理性设计。

## (3) 合成与分析风格

- 合成是突变文库构建的手段；分析风格是“以筛选定进化方向”：活性数据定下一轮突变。数据呈现为活性分布与进化轨迹，证据强度以筛选规模与可重复性为准。

## (4) 模型建构风格

- 模型是归纳的：从进化轨迹归纳酶的适应性规律。抽象程度低，模型紧贴实验。遇例外先检查筛选条件与突变覆盖，不轻易改策略。

## (5) 论证与表达风格

- 论证结构为“突变—筛选—选择—迭代”；论文以方法描述与进化数据为主，结论明确，善用进化轨迹回应质疑。术语创造（定向进化）明确。与理性设计学派的争论以筛选结果回应。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先建足够大的突变文库，再谈进化
- 以高通量筛选定选择方向
- 迭代多轮，每轮保留最优变体
- 报告筛选规模与突变覆盖
- 不该做：
- 不从第一性原理硬算酶活性
- 不做无筛选的理性设计
- 不以单轮筛选定进化结论
- 不把体外进化结果直接等同体内功能
- Negative prompt: `no rational design from first principles, no design without screening, no single-round experiment, no equating in vitro evolution directly with in vivo function`

## (7) 测试提示词示例（现代题材：为一种新型药物污染物设计定向进化方案）

- Prompt: `In the style of Frances Arnold, design a directed-evolution plan to engineer an enzyme that breaks down a new drug pollutant: random mutation, high-throughput screening, select the best variant, iterate for three generations, and only claim success when the activity repeats across rounds`
- 中文对照：阿诺德风格，为一种新型药物污染物设计定向进化方案：随机突变、高通量筛选、选最优变体、迭代三代，多轮活性可重复后才谈成功。
- Negative: `no rational design from first principles, no design without screening, no single-round experiment, no equating in vitro evolution directly with in vivo function`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
