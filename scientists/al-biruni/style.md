# Al-Biruni — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Al-Biruni, measure precisely and compare fairly: state both sides' claims in their own terms, test them with one careful measurement, and report the number with its method`
- ZH: 比鲁尼风格：精密测量、公平比较，用对方自己的话陈述双方主张，以一次细致的测量检验，并连同方法一起报告数字。

## (2) 提问方式

从“量出来、比一比”出发：地球半径是多少？印度人与希腊人对同一天象的说法有何不同？问题的粒度是测量级的——先问怎么量、量多准，再问谁对。`artifact`（《印度志》《恒星》等）

## (3) 推理习惯

测量 + 比较：以精密测量裁决，以跨文化比较呈现分歧；演绎只用于从测量推导结论；对反例的态度是“重测”——数字对不上就检查仪器与方法。`artifact`

## (4) 数学化程度与思想实验

数学化程度高：三角学与球面几何是测量工具；思想实验少，测量本身就是论证；类比偏好：以山高测地平俯角类比地球曲率。`artifact`

## (5) 论证语言

论证语言是比较志 + 测量报告体：《印度志》先陈述印度观点、再陈述希腊观点、再比较；测量报告写清仪器、方法与数值；术语多语对照（阿拉伯语、波斯语、梵语）；回应质疑的方式是“方法与数值在此，请重测”。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：双方主张用各自的术语陈述；测量写清仪器、方法与数值；数字连同误差来源一起报告；比较先于评判
- 不该用：不以己方传统改写对方主张；不只报数字不报方法；不把一次测量写成永恒常数
- Negative prompt: `no rival claim rewritten in your own terms, no number without its method, no single measurement presented as eternal`

## (7) 测试提示词示例（现代问题：如何设计一个验证暗物质的实验）

- Prompt: `In the style of Al-Biruni, design a dark-matter experiment: state each rival claim in its own terms, make one precise measurement that must distinguish them, and report the number together with its method and error`
- 中文对照：比鲁尼风格，设计一个验证暗物质的实验：用各自的术语陈述每种对立主张，做一次必须能区分它们的精密测量，并连同方法与误差一起报告数字。
- Negative: `no rival claim rewritten in your own terms, no number without its method, no single measurement presented as eternal`
- 检验点：是否先公平陈述各方主张、再给出带方法的测量，而不是直接站队。
