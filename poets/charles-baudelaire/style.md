# Charles Baudelaire — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charles Baudelaire: spleen and ideal in one breath, the city as abyss and altar, perfume and carrion side by side, alexandrine held tight then broken by a sudden image, beauty extracted from evil`
- ZH: 波德莱尔风格：忧郁与理想同在一呼一吸间，城市既是深渊又是祭坛，香水与腐尸并置，亚历山大体绷紧后被一个骤然意象打断，从恶中提炼美。

## (2) 意象

- 城市（巴黎：深渊、群氓、橱窗）
- 腐尸与美（《腐尸》：美在腐烂中）
- 香水、酒、鸦片（感官的升天与沉沦）
- 深渊与天空（spleen 与 idéal 的两极）
- 猫、海、钟（静默的凝视者）
- 禁意象：田园牧歌式的纯净自然
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 亚历山大体（十二音节）为主，讲究对仗与跨行；散文诗《巴黎的忧郁》则以散文的呼吸写诗的密度，短段相接、戛然而止；句式长短交错，感叹与反问密集。

## (4) 语言密度与词汇

- 词汇：感官词极密（香、酒、丝绸、腐肉），抽象大词（无限、深渊、永恒）与具体秽物并置；善造矛盾修饰（恶之花）；禁词：温情脉脉的安慰语、直白的道德说教。

## (5) 结构习惯

- 《恶之花》以组诗结构推进：忧郁—理想—巴黎图景—酒—恶之花—死，六辑如六幕；单篇多以场景切入、意象并置、末节翻转（volta 在结尾而非中段）；散文诗以一事一顿悟。

## (6) 该写什么 / 不该写什么

- 该写：
- 城市深渊与理想的对照
- 香水、腐尸、酒的感官并置
- 从恶中提炼美的翻转结尾
- 对读者的直接挑衅与共谋
- 不该写：
- 田园牧歌的纯净慰藉
- 直白的道德说教
- 无感官支撑的抽象议论
- 温情的团圆收束
- Negative prompt: `No pastoral consolation, no direct moral preaching, no abstract discourse without a sensual image, no sentimental happy ending, no wholesome uplift`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Charles Baudelaire, a small Yorkshire terrier sits on a subway seat at night. Alexandrine tension, the subway as abyss and altar, perfume of strangers and iron smell, the dog as a small idol, beauty extracted from the crowd's spleen, a sudden closing reversal.`
- 中文对照：波德莱尔风格：一只约克夏犬深夜坐在地铁座位上。亚历山大体的张力，地铁既是深渊又是祭坛，陌生人的香水味与铁锈味，狗是一尊小小的偶像，从人群的忧郁中提炼美，结尾骤然翻转。
- Negative: `No pastoral consolation, no moral preaching, no sentimental ending, no wholesome uplift`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
