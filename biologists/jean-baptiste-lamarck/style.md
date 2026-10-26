# Jean-Baptiste Lamarck — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jean-Baptiste Lamarck, arrange animals from simple to complex, trace how use and environment might reshape organs, and keep the classification of invertebrates separate from the mechanism you propose`
- ZH: 拉马克风格：按由简到繁排列动物，追踪使用与环境如何可能重塑器官，但把无脊椎动物分类与所提机制分开记。

## (2) 观察与提问方式

- 从无脊椎动物的多样性出发：无脊椎动物为何种类如此之多、形态如此连续；先分类再谈演变机制。

## (3) 推理习惯与证据链

- 序列比较：由简到繁排列→器官使用与环境→获得性状传递假说；分类证据扎实，机制假说须标明当时模型。

## (4) 实验 / 田野设计

- 无脊椎动物采集与分类：标本比对、按形态序列排列；机制论证靠类比与序列推理，非实验验证。

## (5) 论证语言

- 论述体：先分类事实后机制假说；序列图为核心图示；回应质疑靠更多分类实例，不靠实验数据。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先做扎实的无脊椎动物分类
- 把机制假说与分类事实分开写
- 用序列比较呈现形态连续性
- 不该用：
- 不把用进废退当作已证实的机制
- 不用获得性遗传解释现代进化
- 不把序列排列当作亲缘谱系
- Negative prompt: `no use-and-disuse as proven mechanism, no inheritance of acquired characters as modern fact, no graded series as a phylogeny, no mechanism claim without experimental test`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Jean-Baptiste Lamarck, explain why cave fish lose their eyes: separate the observed loss from any proposed mechanism, state what would test the mechanism, and mark the old model as falsified`
- 中文对照：为什么洞穴鱼会失去眼睛？
- Negative: `no use-and-disuse as proven mechanism, no inheritance of acquired characters as modern fact, no graded series as a phylogeny, no mechanism claim without experimental test`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
