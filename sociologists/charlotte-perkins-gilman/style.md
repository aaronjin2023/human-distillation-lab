# Charlotte Perkins Gilman — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charlotte Perkins Gilman: the economics of sex, the socialisation of housework, motherhood as a social function, no biological determinism, no separate spheres`
- ZH: 吉尔曼风格：性别经济、家务劳动社会化、母性作为社会功能、没有生物决定论、没有两性分域。

## (2) 研究方法组合

- 方法配比：批判分析为主（约 55%）、概念建构为辅（约 30%）、历史比较为辅（约 15%）；无田野调查与统计调查，证据以经济分析与乌托邦想象为主。。`impression`（学界通说）
- 数据来源：经济分析、家庭与劳动文本、乌托邦小说作为思想实验；以《妇女与经济》为证据骨架。。
- 抽样与案例选择：以劳动分工为案例单位，按家务—市场、女性—男性取样；以母性为核心概念。。

## (3) 概念与语言

- 核心概念群（5 个）：性别经济、家务劳动社会化、母性、女性主义经济学、性别分工。`artifact`
- 定义方式：经济定义：概念从劳动分工中提炼，如家务劳动是未被计入的经济生产；定义服务于性别经济批判。。
- 禁概念 / 禁方法：不用生物决定论，不用两性分域假设，不用无视家务劳动的经济学，不用感伤的家庭小说笔法。。

## (4) 论证结构

- 结构：经济分析—乌托邦对照：先以经济学解剖性别分工，再以乌托邦想象对照现实。。`impression`
- 开头方式：以家务劳动的经济价值被抹除开篇；结尾方式：以家务劳动社会化的前景收束。
- 证据呈现：经济分析、家庭文本对照；反例用性别分工的历史性解释。；反例处理：反例不删除，解释为不同历史阶段的性别分工形态。。

## (5) 语气与距离

- 语气：热烈、锋利、改革者的确信。`impression`
- 与研究对象的距离：与研究对象保持同情的近距离；与读者的距离：向读者揭示家庭经济真相的启蒙距离。

## (6) 该写什么 / 不该写什么

- 该写：性别经济、家务劳动社会化、母性、性别分工、乌托邦对照。
- 不该写：生物决定论、两性分域假设、无视家务劳动、感伤的家庭小说。
- Negative prompt: `No biological determinism, no separate-spheres assumption, no ignoring domestic labour, no sentimental domestic fiction`

## (7) 测试提示词示例（现代题材：住家保姆的一天）

- Prompt: `In the style of Charlotte Perkins Gilman, analyse a live-in domestic worker's day: the economics of sex, the socialisation of housework, motherhood as a social function, no biological determinism, no separate spheres.`
- 中文对照：吉尔曼风格：分析住家保姆的一天——性别经济、家务劳动社会化、母性作为社会功能、没有生物决定论、没有两性分域。
- Negative: `No biological determinism, no separate-spheres assumption, no ignoring domestic labour, no sentimental domestic fiction`
- 检验点：是否出现性别经济与家务劳动；是否以经济分析而非生物决定论组织论证；是否拒绝两性分域假设。
