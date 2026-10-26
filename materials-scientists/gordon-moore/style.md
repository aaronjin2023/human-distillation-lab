# Gordon Moore — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Gordon Moore, count the transistors and extrapolate honestly: track density against cost, revise the doubling rate when the data move, and let the fab yield prove the forecast`
- ZH: 摩尔方法：数晶体管并诚实外推——跟踪密度与成本，数据变了就修正倍增周期，让晶圆良率证明预测。

## (2) 合成路线偏好

- 硅平面工艺：氧化、光刻、扩散、金属化；控掺杂、线宽、良率；集成电路的批量制造。 `artifact`

## (3) 表征手段组合

- 电学测试：晶体管密度、良率、成本核算；缺陷密度统计；工艺窗口测量。 `artifact`

## (4) 理论模型与图表风格

- 摩尔定律：集成电路上晶体管数约每两年翻倍（1965 年初版为每年翻倍，1975 年修正为两年）；密度–成本权衡；工艺缩放的经济学。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住良率与成本的可承受性；可牺牲单器件的极致性能；缩放保住经济性，牺牲物理极限的冒进。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 晶体管密度、良率、成本三者一起报
- 外推时注明适用范围与修正历史
- 用晶圆良率验证缩放，不只看线宽
- 先看数据趋势，再做预测
- 不该做：方法上的禁区——no Moore's-law claim without density and cost data；no extrapolating a doubling rate without a revision history；no reporting linewidth without yield；no claiming scaling from a single chip。
- Negative prompt: `no Moore's-law claim without density and cost data, no extrapolating a doubling rate without a revision history, no reporting linewidth without yield, no claiming scaling from a single chip`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Gordon Moore, design a flexible integrated circuit for a wearable device: count transistors and cost together, set a scaling plan with a stated doubling horizon, and prove yield before claiming the forecast`
- 中文对照：摩尔方法，为可穿戴设备设计柔性集成电路：晶体管数与成本一起算，定出注明期限的缩放计划，用良率证明预测，确认后再谈器件。
- Negative: `no Moore's-law claim without density and cost data, no extrapolating a doubling rate without a revision history, no reporting linewidth without yield, no claiming scaling from a single chip`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
