# Xenophon — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xenophon on taxation: let the city earn before it taxes, tax the resident alien fairly, use the silver mines and the harbour, no levy that drives away the trader`
- ZH: 色诺芬式税收：先使城邦生利而后征税，公平对待外邦居民，以银矿与港口为财源，不征驱走商人之税。

## (2) 税收理念与公平—效率排序

- 理念：财政收入先于税率，城邦应先经营银矿、港口与外邦居民的贡献，再谈征税；税不可驱走商人与劳力。`artifact`
- 好税制三条标准（用其术语）：生利先于征税；公平对待外邦居民；银矿与港口为财源。
- 公平与效率冲突时：收入来源多元先于单一重税：宁愿经营矿产与港口少征，也不当重税驱走商人。

## (3) 论证方式与证据习惯

- 论证：财政算术 + 历史比较（雅典银矿与港口），以收入数字为证；实用主义，不尚空论。
- 证据：证据：银矿产量、港口关税、外邦居民人数；反例是重税导致商人他往。
- 禁忌论证：不用抽象公平原则推导税率，不用数学模型，不以道德说教代替财政算术。

## (4) 语言风格

- 句式：对话与论述体，条理清晰；词汇：收入、银矿、港口、外邦人、家政；语气：务实的管理者口吻，对纳税人是“生利共赢”的邀请。

## (5) 税制设计偏好

- 税基偏好：最信任银矿、港口与外邦居民贡献，最怀疑重征本邦农人；税率偏好：轻税、公平对待外邦人；征管偏好：经营性收入优先、关税与使用费，厌恶驱商之税。

## (6) 该写什么 / 不该写什么

- 该写：
- 生利先于征税：城邦先经营银矿与港口，再谈税率，收入多元是税制的前提。
- 外邦居民税：公平对待居留外邦人，其贡献为城邦财源，税不可歧视过重。
- 银矿与港口：矿产与海港关税为财源，税基在经营不在摊派。
- 家政之喻：治国如治家，量入为出、经营有度，财政即家政之大者。
- 不驱商之税：税率以不驱走商人与劳力为界，税源与商路同进退。
- 不该写：不写驱走商人之重税、不写歧视外邦人的苛税、不写脱离经营的空谈税率。
- Negative prompt: `No levy that drives away the trader, no discriminatory tax on resident aliens, no rate without a revenue source, no tax detached from the harbour and the mines`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计数字服务税）

- Prompt: `In the style of Xenophon on taxation, design a digital services tax for a small island state. Let the island earn from its digital harbour first, tax foreign platforms fairly, no levy that drives away the trader.`
- 中文对照：色诺芬风格：为一个假想岛国设计数字服务税。先让岛国从数字港口生利，公平对待外国平台，不征驱走商人之税。
- Negative: `no levy that drives away the trader, no discriminatory tax on foreign platforms, no rate without a revenue source`
- 检验点：经营性收入是否先于税率；外邦公平是否写明；驱商边界是否可算。
