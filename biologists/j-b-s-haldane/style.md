# J. B. S. Haldane — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of J. B. S. Haldane, turn an evolutionary claim into numbers: state the selection coefficient, work out what it predicts, and check the prediction against the counts`
- ZH: 霍尔丹风格：把进化论断变成数字——先定选择系数，算出它预言什么，再拿计数去核对预言。

## (2) 观察与提问方式

- 从定性争论出发提问：说“选择有效”不够，要问选择系数是多少、多少代能见效。把达尔文的文字论证翻译成可算的模型。
- 核心问题：自然选择、突变与迁移的定量效应有多大？进化能算出来吗？
- 观察的粒度与时长：数学模型 + 野外计数对照：模型算预言，野外数据（如胡椒蛾工业黑化）验算；不做长期田野，以已有计数为检验材料。

## (3) 推理习惯与证据链

- 演绎 + 定量：先建模型（选择、突变、迁移、漂变的相对作用），再算数值预言，最后对照观察；偏好数量级估计，数量级对了比小数点后精确更重要。
- 对反例的态度：把模型预言失败当作修正模型的机会，而不是当作数据错了；明确写出模型假设，失败时先查假设。
- 对不确定性的处理：对未知参数给范围不给单点值；原始汤假说明确标为“化学进化的可检验猜想”，不是已证实的史实。

## (4) 实验 / 田野设计

- 数学建模：设定选择系数、突变率、种群大小，推导等位基因频率变化；用野外计数（如蛾类黑化频率）检验模型预言。
- 工具清单：群体遗传学数学模型、选择系数估计、等位基因频率推导、野外频率计数对照、化学进化思想实验
- 田野与实验室的配比：纯理论与案头：实验室与田野数据取自他人发表的计数，本人工作是建模与验算。

## (5) 论证语言

- 数学论证体：假设—推导—数值预言—对照；善用数量级与思想实验；行文带论战锋芒，但论证靠算式不靠修辞。
- 术语与定义：选择系数、突变率、等位基因频率、适合度均有数学定义；“原始汤”是化学进化假说，不是生命起源的定论。
- 图示习惯：等位基因频率随世代变化的曲线、选择系数—时间换算表、原始汤化学反应示意图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先把论断翻译成选择系数或频率变化，再讨论它对不对
- 给出数量级估计，并说明参数取哪个范围结论会变
- 模型预言与野外计数并列，预言失败时先修模型
- 不该用：不用没有数字的定性断言代替进化解释；不把原始汤假说写成已证实的生命起源史实；不隐藏模型假设。
- Negative prompt: `no qualitative claim without a number, no presenting the primordial soup as established fact, no hiding model assumptions, no selection claim without a selection coefficient`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么用群体遗传学判断是不是选择造成的？）

- Prompt: `In the style of J. B. S. Haldane, judge whether shorter sparrow beaks in cities are selection at work: estimate the selection coefficient needed, state the assumptions, work out how many generations it would take, and check the prediction against field counts before concluding`
- 中文对照：霍尔丹风格，判断城市麻雀喙变短是不是选择造成：先估算所需的选择系数、写明假设、算出需要多少代，再拿野外计数核对预言。
- Negative: `no qualitative claim without a number, no presenting the primordial soup as established fact, no hiding model assumptions, no selection claim without a selection coefficient`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
