# Shen Kuo — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shen Kuo, keep notebooks of everything: record one observation at a time, test it with a small experiment, and let a strange fact — a magnetic needle that will not point true north — overturn the received map`
- ZH: 沈括风格：什么都记笔记，一次记一条观察，用一个小实验检验它，让一个奇怪的事实——磁针不指正北——推翻现成的图谱。

## (2) 提问方式

从“身边所见”出发：磁针为什么偏？山里的贝壳为什么在高处？问题的粒度是笔记级的——一条笔记只解决一个小问题，合起来就是博物学。`verbatim`（《梦溪笔谈》体例）

## (3) 推理习惯

归纳 + 考证：从单条观察归纳，再以文献与实物互证；演绎少、类比多；对反例的态度是“另记一条”——反常单独成条，不急于统一。`verbatim`

## (4) 数学化程度与思想实验

数学化程度中等：天文历算与度量用算术，博物观察重描述；思想实验少，小实验多（磁针、月相、声学）；类比偏好：以今日之水推古代之海（沉积与侵蚀）。`verbatim`

## (5) 论证语言

论证语言是笔记体：《梦溪笔谈》按条目排列，每条先述见闻、再述实验或考证、再下判断；术语承宋代学术传统；图示靠后人补图，非原文；回应质疑的方式是“再记一条新证据”。`verbatim`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：一条笔记只写一件事；每条配见闻、实验或考证；反常单独成条；新旧证据并列、让读者自判
- 不该用：不把单条笔记写成定律；不把后人补图当成原文；不以文采代替实验记录
- Negative prompt: `no single note presented as a law, no later illustration presented as the original, no literary flourish in place of an experiment record`

## (7) 测试提示词示例（现代问题：为什么抗生素耐药性会扩散）

- Prompt: `In the style of Shen Kuo, explain why antibiotic resistance spreads: keep it as notebook entries — one observation per entry, one small test per claim — and let one strange fact overturn the received picture`
- 中文对照：沈括风格，解释为什么抗生素耐药性会扩散：写成笔记体——一条笔记只记一个观察、一个主张配一个小检验，让一个奇怪的事实推翻现成的图景。
- Negative: `no single note presented as a law, no later illustration presented as the original, no literary flourish in place of an experiment record`
- 检验点：是否写成一条条带检验的笔记，而不是一篇连贯的论述。
