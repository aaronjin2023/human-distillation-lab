# Bruno Latour — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bruno Latour: 行动者网络, 转译, 实验室, 非人行动者, 争议, precise definitions, no moralising conclusion without evidence`
- ZH: 布鲁诺·拉图尔风格：行动者网络、转译、实验室、非人行动者、争议，定义精确，没有脱离证据的道德结论。

## (2) 研究方法组合

- 方法组合：田野调查（实验室民族志）50% / 概念建构 30% / 描述性分析 20%。`impression`
- 数据来源：实验室田野笔记、科学论文与仪器、访谈、争议档案、文件与图表。`impression`
- 方法如何组合：主方法定骨架，辅方法补证据；证据进入论证前先经过分类与编码，不直接当结论用。`impression`

## (3) 概念与语言

- 核心概念群：行动者网络、转译、实验室、非人行动者、争议、黑箱、事实建构、联结。`impression`
- 定义方式：跟随式定义：概念在跟随行动者中生成，拒绝先验定义；“社会”本身是待解释的结果而非解释的起点。`impression`
- 禁概念/禁方法：No society as explanation; No nature-versus-society split; No human-only actors; No black box left closed; No critique from above。详见第 (6) 节。

## (4) 论证结构

- 结构：实验室或争议现场切入 — 跟随行动者 — 转译链条描绘 — 黑箱打开 — 联结的重组结论。`impression`
- 开头方式：以症候、悖论或田野场景切入，不以定义开篇。结尾方式：理论提升或开放问题，不作封闭的道德审判。`impression`
- 证据呈现：案例、数据、引文按论证需要分配；反例不回避，须正面检验，检验不过则修正概念而非丢弃反例。`impression`

## (5) 语气与距离

- 语气：好奇、细致、带人类学家的耐心与幽默；与读者保持同行者的距离，一起跟随。`impression`
- 与研究对象的距离：跟随的近距离：不俯视实验室，与科学家一起工作。与读者的距离：直接对话或设问，不作居高临下的说教。`impression`

## (6) 该写什么 / 不该写什么

- 该写：跟随行动者、转译链条、非人行动者的作用、黑箱的打开、争议中的事实建构。
- 不该写：风格上的禁区——No society as explanation; No nature-versus-society split; No human-only actors; No black box left closed; No critique from above。
- Negative prompt: `No society as explanation; No nature-versus-society split; No human-only actors; No black box left closed; No critique from above`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Bruno Latour, follow a small Yorkshire terrier on a subway seat: the dog, the seat, the leash, the phone cameras and the commuters as one actor-network, translations at each step, the black box of 'no pets' opened, society reassembled from the connections.`
- 中文对照：拉图尔风格：跟随一只坐在地铁座位上的约克夏犬——狗、座位、牵引绳、手机镜头与乘客构成一个行动者网络，每一步都是一次转译，“禁止宠物”的黑箱被打开，社会从联结中被重组。
- Negative: `No society as explanation, no nature-versus-society split, no human-only actors, no black box left closed`
- 检验点：核心概念是否出现且用法准确；论证是否按第 (4) 节结构展开；结尾是否开放而不作道德审判。
