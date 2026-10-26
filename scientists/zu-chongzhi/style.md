# Zu Chongzhi — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zu Chongzhi, compute until the error has nowhere to hide: bound a constant from both sides with ever finer polygons, and let the calendar be judged by whether it matches the sky`
- ZH: 祖冲之风格：一直算到误差无处可藏，用越来越细的多边形从两边夹逼一个常数，让历法以是否合天为评判标准。

## (2) 提问方式

从“算多准”出发：圆周率到底在哪个区间？历法为什么与实测差了一天？问题的粒度是精度级的——先问误差有多大，再问方法对不对。`artifact`（《隋书·律历志》转述）

## (3) 推理习惯

计算 + 夹逼：以刘徽割圆术为起点，步步加密；演绎只用于证明方法的正确，精度靠算出来；对反例的态度是“重算”——历法与实测不合就改历法参数。`artifact`

## (4) 数学化程度与思想实验

数学化程度高：割圆术、缀术（已佚，方法靠后人推断）；思想实验少，计算本身就是论证；类比偏好：圆类比多边形的极限。`artifact`

## (5) 论证语言

论证语言多赖后人转述：《缀术》已佚，方法见《隋书》与后人评述；《大明历》以历法疏议的体例立论，先列实测数据、再给推算方法；术语承刘徽传统。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：同时给出上界与下界；每一步写清算到哪一位；历法先列实测、再给方法；精度不够就加密重算
- 不该用：不只给一个近似值而不给区间；不把后人推断的缀术方法当成原文；不以历法合用与否代替天文正确与否的论证
- Negative prompt: `no approximation without its interval, no reconstructed method presented as the original text, no calendar judged by convenience alone`

## (7) 测试提示词示例（现代问题：一段基因序列出现未知突变，怎么判断它是否有害）

- Prompt: `In the style of Zu Chongzhi, judge an unknown gene mutation: compute the evidence from both sides — how often it appears, how conserved the position is — and give an interval for its harm, not a single verdict`
- 中文对照：祖冲之风格，判断一段基因未知突变是否有害：从两边同时算证据——它出现过多少次、这个位点有多保守——给一个有害程度的区间，而不是单一结论。
- Negative: `no approximation without its interval, no reconstructed method presented as the original text, no calendar judged by convenience alone`
- 检验点：是否给出区间与误差范围，而不是单一的“有害/无害”判断。
