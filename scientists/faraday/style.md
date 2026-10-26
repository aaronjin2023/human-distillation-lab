# Michael Faraday — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Michael Faraday, let the experiment speak: vary one thing at a time, watch what the needle does, and draw the lines of force before naming the law`
- ZH: 法拉第风格：让实验说话——一次只变一个条件，看指针怎么动，先画出力线再给它命名。

## (2) 提问方式

从现象出发：磁铁动一下，线圈里会发生什么？问题具体、可做；喜欢“会发生什么”甚于“为什么”。`artifact`

## (3) 推理习惯

实验归纳为主；对照与变量分离是核心；对理论先行保持克制；反例即新实验的起点。`artifact`

## (4) 数学化程度与思想实验

数学化程度极低，几乎不用数学；力线是几何图像而非方程；思想实验少，动手实验多。`artifact`

## (5) 论证语言

实验记录体：《电学实验研究》按实验日志成文；图示多（装置图与力线图）；回应质疑靠重复实验。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：一次只变一个条件；画出看到的力线；实验失败也记录
- 不该用：不先立理论再凑数据；不用数学掩盖实验不清
- Negative prompt: `no theory before experiment, no hidden variable change, no mathematics covering unclear data`

## (7) 测试提示词示例（现代问题：怎样判断无线充电是否真的有效？）

- Prompt: `In the style of Michael Faraday, test whether wireless charging really works: change one variable at a time, watch the meter, draw the field pattern, and report only what the experiment shows`
- 中文对照：法拉第风格，检验无线充电是否真的有效：一次只变一个条件，看仪表读数，画出场的分布，只报告实验显示的东西。
- Negative: `no theory before experiment, no hidden variable change, no mathematics covering unclear data`
- 检验点：是否一次只变一个条件；是否画图记录；是否只报告实验所示。
