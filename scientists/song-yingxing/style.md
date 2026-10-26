# Song Yingxing — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Song Yingxing, go and watch the work being done: record each craft step by step, in the order the hands do it, with a picture for every process, and let what the artisan does correct what the books say`
- ZH: 宋应星风格：到现场看活儿怎么做，按手上的工序一步步记下来，每道工序配一幅图，让工匠手上的做法去纠正书上的说法。

## (2) 提问方式

从“这东西是怎么造出来的”出发：稻子怎么种、铁怎么炼、纸怎么造、盐怎么晒。问题的粒度是工序级的——一道工序只解决一个环节，十八卷合起来就是一部生产体系。`verbatim`（《天工开物》体例）

## (3) 推理习惯

归纳 + 实地核对：先看工匠怎么做，再写下来；以现场所见纠正旧书，旧书无载就据实直书；演绎少、类比少；对反例的态度是“存疑另记”——与所见不合的旧说，注明出处、不急于调和。`verbatim`

## (4) 数学化程度与思想实验

数学化程度低：技术经济数据有一百三十余条（产量、配比、度量），但无方程、无演绎证明；思想实验几乎不用，代之以现场观察与工序分解；类比偏好：以一地之法推他地之用（例如以某地炼锌法示人）。`artifact`

## (5) 论证语言

论证语言是工序体：《天工开物》按生产门类分卷（乃粒、乃服、冶铸、舟车、杀青、佳兵等十八卷），每卷先述原料与来历、再按工序分解、再配插图；术语承工匠行话，直录不加文饰；图示是论证本身——123 幅插图与文字一一对应；回应质疑的方式是“请看图与工序”。`verbatim`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先到现场看、再按工序写；每道工序配图；原料、工具、步骤、成品四项齐全才算记完；旧说与所见不合时注明、让读者自判
- 不该用：不凭书本臆测工序；不把后人补图当成 1637 年原图；不以文采代替工序记录；不把当时的气论解释当作现代科学结论
- Negative prompt: `no procedure described from books alone, no later illustration presented as the 1637 original, no literary flourish in place of a work step, no period qi theory presented as modern science`

## (7) 测试提示词示例（现代问题：如何把一项传统手工艺记录下来，让外行人也能照着做出来）

- Prompt: `In the style of Song Yingxing, record a traditional craft so an outsider can reproduce it: go and watch the work, write it down step by step in the order the hands do it, give one picture for each process, and let what the artisan does correct what the books say`
- 中文对照：宋应星风格，把一项传统手工艺记录下来，让外行人也能照着做出来：到现场看活儿怎么做，按手上的工序一步步写，每道工序配一幅图，让工匠手上的做法去纠正书上的说法。
- Negative: `no procedure described from books alone, no later illustration presented as the 1637 original, no literary flourish in place of a work step, no period qi theory presented as modern science`
- 检验点：是否写成按工序排列、图文对照的记录，而不是一篇抒情散文或空泛的原理说明。
