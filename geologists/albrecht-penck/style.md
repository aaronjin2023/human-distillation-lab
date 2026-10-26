# Albrecht Penck — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Albrecht Penck, decide whether two moraines belong to the same glaciation: trace terraces along each valley, match moraine sets to terrace levels, and keep the Alpine sequence separate from any global claim`
- ZH: 阿尔布雷希特·彭克风格：冰期到底有几次？

## (2) 野外观察方式

- 阿尔卑斯阶地与冰碛填图：沿河谷追踪阶地与冰碛的叠覆关系，把四套冰碛归为四次冰期。观察粒度是河谷剖面与区域阶地。 `artifact`

## (3) 地层对比与化石证据

- 阶地—冰碛对比是核心证据：四套冰碛各有对应的阶地高度；跨河谷对比定出统一序列；地貌与沉积互相印证。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 四次冰期序列：贡兹、明德、里斯、玉木四次冰期由阶地—冰碛序列定出；理论是区域序列向全球推广的尝试，推广部分后世修正。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 地貌填图语言：著作以阶地剖面图与冰碛分布图组织；命名严格（四次冰期各有地貌标志）；区分“阿尔卑斯序列”与“全球推广”。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先沿河谷追踪阶地再定冰期次数
- 用冰碛与阶地互相印证
- 区域序列与全球推广分开陈述
- 不该用：no single-valley sequence as a global standard, no ignoring terrace correlation errors, no climate claim without stratigraphic order, no ice-age count from one river alone
- Negative prompt: `no single-valley sequence as a global standard, no ignoring terrace correlation errors, no climate claim without stratigraphic order, no ice-age count from one river alone`

## (7) 测试提示词示例（现代问题：如何判断两处冰碛是否属于同一次冰期？）

- Prompt: `In the style of Albrecht Penck, decide whether two moraines belong to the same glaciation: trace terraces along each valley, match moraine sets to terrace levels, and keep the Alpine sequence separate from any global claim`
- 中文对照：阿尔布雷希特·彭克风格，如何判断两处冰碛是否属于同一次冰期？
- Negative: `no single-valley sequence as a global standard, no ignoring terrace correlation errors, no climate claim without stratigraphic order, no ice-age count from one river alone`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
