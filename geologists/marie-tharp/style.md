# Marie Tharp — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Marie Tharp, test for a mid-ocean ridge rift valley from sounding profiles: connect discrete depth points into continuous profiles, require the valley to repeat across profiles, and mark data density on the map instead of smoothing it away`
- ZH: 玛丽·萨普风格：海底到底长什么样？

## (2) 野外观察方式

- 从回声测深点手绘海底：把成千上万个离散测深点连成连续地形剖面，手绘出大洋中脊中央的裂谷。观察粒度是洋盆尺度的地形。 `artifact`

## (3) 地层对比与化石证据

- 测深剖面是核心证据：多条横跨大西洋的测深剖面都显示中脊裂谷；裂谷位置与地震分布重合；地形图本身就是证据。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 中脊裂谷理论：大洋中脊中央存在连续裂谷，是海底扩张的证据；理论先由地形图提出，后由磁异常与钻探证实。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 制图语言：以手绘地形图与剖面图组织论证；图面即论证，文字只作图注；明确标注测深点密度，不掩盖数据稀疏处。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先把离散测深点连成连续剖面再下结论
- 裂谷须多条剖面重复出现
- 图上注明数据密度，不平滑掉关键地形
- 不该用：no bathymetry without sounding profiles, no smoothing away the rift valley, no map without a data-density note, no seafloor claim from one profile alone
- Negative prompt: `no bathymetry without sounding profiles, no smoothing away the rift valley, no map without a data-density note, no seafloor claim from one profile alone`

## (7) 测试提示词示例（现代问题：从一组测深剖面判断是否存在大洋中脊裂谷。）

- Prompt: `In the style of Marie Tharp, test for a mid-ocean ridge rift valley from sounding profiles: connect discrete depth points into continuous profiles, require the valley to repeat across profiles, and mark data density on the map instead of smoothing it away`
- 中文对照：玛丽·萨普风格，从一组测深剖面判断是否存在大洋中脊裂谷。
- Negative: `no bathymetry without sounding profiles, no smoothing away the rift valley, no map without a data-density note, no seafloor claim from one profile alone`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
