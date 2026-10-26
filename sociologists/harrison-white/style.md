# Harrison C. White — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文/转述不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Harrison White: networks and mathematical models, identity and control, markets from networks, no attribute tables instead of networks`
- ZH: 哈里森·怀特风格：以数学模型写结构：市场不是供求曲线，是网络中的位置。

## (2) 研究方法组合

- 数学建模与网络分析为主（约60%）、概念建构为辅（约25%）、案例为辅（约15%）。`impression`
- 方法组合：以数学模型写结构：市场不是供求曲线，是网络中的位置。`impression`
- 数据来源：网络数据、市场与组织案例、数学模型。`artifact`

## (3) 概念与语言

- 核心概念群：认同与控制、网络与市场、结构等价、范畴与网络、身份的故事、社会结构的数学模型。`impression`
- 定义方式：以著作中的概念辨析与操作化定义为主，概念随时期演变。`impression`
- 禁概念/禁方法：属性社会学、把市场写成供求曲线、把认同写成固定本质。`impression`

## (4) 论证结构

- 结构：属性社会学的批判—网络模型—市场与认同的机制—结构的涌现。`impression`
- 开头方式：以问题、田野场景、统计反常或概念辨析开场；结尾以理论提升、开放问题或政策含义收束。`impression`
- 证据呈现：案例、数据、图表、引文按著作分配；反例以比较与检验处理，不回避。`impression`

## (5) 语气与距离

- 语气：抽象、冷峻、带数学的精确；以模型反驳属性社会学。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 网络中的结构位置
- 市场作为网络的产物
- 认同的建构与控制
- 结构等价的模型
- 不该写：
- 用属性交叉表代替网络
- 把市场写成抽象供求
- 把认同写成固定属性
- Negative prompt: `No attribute tables instead of networks, no market as abstract supply and demand, no identity as fixed attribute`

## (7) 测试提示词示例（现代题材：地铁车厢的座位市场网络）

- Prompt: `In the style of Harrison White, model a subway carriage as a network: identities emerge from ties and stories, not from attributes; map structural equivalence among commuters, show how a market for seats forms, no attribute table without a network.`
- 中文对照：怀特风格：把一节地铁车厢建模为网络——认同从关系与故事中涌现，而非属性；绘制乘客间的结构等价，揭示座位市场如何形成；不写没有网络的属性交叉表。
- Negative: `No attribute tables instead of networks, no market as abstract supply and demand, no identity as fixed attribute`
- 检验点：方法组合是否对位；核心概念是否出现且定义精确；禁区写法是否未出现。
