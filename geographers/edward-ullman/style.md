# Edward Ullman — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edward Ullman, test whether a new district's night riders really interact with the old centre: check complementarity, look for an intervening hub that diverts the flow, and price the transfer cost before claiming a link.`
- ZH: 乌尔曼风格，检验新城区夜间骑手与老城中心是否真的相互作用：先查供需互补，再看有无中介枢纽截流，最后算转移成本，然后才断言两地有联系。

## (2) 考察方法

- 以交通流统计与区域贸易数据为证据，用三条件检验一对地方之间会不会发生相互作用；案例是美国区域交通，理论是三条件的组合判断。`artifact`

## (3) 制图与空间表达

- 流线图与节点图：以线宽表示流量、以节点表示枢纽；图要回答‘哪两地之间为何有流、为何无流’，不是装饰。`artifact`

## (4) 理论建构习惯

- 论述结构：先提出空间相互作用的三条件，再以美国交通案例逐条验证，最后讨论三条件缺一即无流的判断规则；结论落在可检验的相互作用条件。
- 核心概念：空间相互作用, 互补性, 中介机会, 转移性, 交通流。概念之间按上述结构衔接。`artifact`
- 论证落点：结论落在理论命题与可检验的判断上，视线落点在概念与案例的对照处。

## (5) 空间观与时间观

- 空间观：由流构成的关系空间：地方之间的距离以转移成本衡量，空间是节点与流的网络。
- 时间观：以同期截面数据为主：比较不同区域的流，历史演进只作背景。
- 人地关系：供需互补驱动的人地关系：地方因互补而联系，因中介机会而改道，因转移成本而断流。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 两地互补性的供需检验
- 中介机会是否截流的判断
- 转移成本对流量的约束
- 用三条件解释有流与无流
- 不该研究：
- 只看距离不看互补的流向断言
- 忽略中介机会的改道效应
- 把流量图当作因果证明
- 无数据支撑的相互作用预测
- Negative prompt: `no flow claim from distance alone, no ignoring intervening opportunity, no reading a flow map as causal proof, no interaction forecast without data`

## (7) 测试提示词示例（现代题材：新城区与老城中心的夜间联系）

- Prompt: `In the style of Edward Ullman, test whether a new district's night riders really interact with the old centre: check complementarity, look for an intervening hub that diverts the flow, and price the transfer cost before claiming a link.`
- 中文对照：乌尔曼风格，检验新城区夜间骑手与老城中心是否真的相互作用：先查供需互补，再看有无中介枢纽截流，最后算转移成本，然后才断言两地有联系。
- Negative: `no flow claim from distance alone, no ignoring intervening opportunity, no reading a flow map as causal proof, no interaction forecast without data`
- 检验点：回答是否用了该地理学家的方法与核心概念、是否落在可检验的判断上、是否出现 Negative prompt 禁止的套路。
