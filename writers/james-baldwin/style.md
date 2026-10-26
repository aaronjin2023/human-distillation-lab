# James Baldwin — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Baldwin: long, musical, biblical sentences, fierce moral clarity, intimate second-person address, love and terror held together, the personal as the political, no evasion`
- ZH: 詹姆斯·鲍德温风格：漫长而富音乐性的圣经式长句，锋利的道德清晰度，亲密的第二人称呼告，爱与恐惧并置，个人即政治，绝不回避。

## (2) 句式与节奏

- 句式：句长以长句为主：从句层层嵌套，逗号与分号绵延，间以短促的断言句如钟声敲下；排比与反复是基本节奏。
- 节奏：节奏如布道与爵士：长句铺陈、短句收束，段落由低语渐至高潮再回落；散文的节奏比小说更急，书信体段落常一气呵成。

## (3) 词汇与意象

- 词汇：词汇：圣经语言（罪、救赎、火、水）与日常口语并置，爱、恐惧、羞耻、自由等大词反复出现但从不空洞；爱用第二人称 you，把读者拉进被告席与忏悔室。
- 意象：意象群：火与审判（《下一次将是烈火》的火）、山与教会（《向苍天呼吁》的山）、房间与封闭空间（《乔瓦尼的房间》的房间）、镜子与面孔、水与洗礼。
- 禁词/禁意象：禁词/禁意象：不写含糊其辞的中间立场，不用学术黑话代替道德判断，不写廉价的乐观与和解。

## (4) 叙事视角与结构

- 视角：叙事视角：小说多为第一人称或贴近人物的第三人称限知；散文多为第一人称书信体，直接对你说话；视角即审判席，叙述者既是证人也是被告。
- 结构：结构：小说常以一个场景切入，再以闪回展开一生；散文常以一封信或一次对话起笔，层层推进到普遍命题；结尾多为一句断言而非情节收束。

## (5) 语气与距离

- 语气：语气：热烈、严厉而亲密，既像布道又像情书；与人物的距离极近（爱他们、审判他们），与读者的距离为零——直接对话、毫不留情。

## (6) 该写什么 / 不该写什么

- 该写：该写：种族与性向的交叉压迫、爱作为道德实践、教会的虚伪与真诚、美国梦的代价、个人良知的拷问。
- 不该写：不该写：含糊的中间立场、学术化的冷漠分析、把人物写成议题的传声筒、廉价乐观的结局。
- Negative prompt: `No evasive neutrality, no academic jargon, no cheap optimism, no characters as mouthpieces, no sentimental reconciliation`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of James Baldwin, a small Yorkshire terrier sits on a subway seat while commuters look away. Long musical sentences. A direct address to the reader: what are you afraid to see? Love and terror held together. No evasion.`
- 中文对照：詹姆斯·鲍德温风格，一只小约克夏犬坐在地铁座位上，通勤者纷纷移开视线。漫长而富音乐性的长句，直接对读者发问：你害怕看见什么？爱与恐惧并置，绝不回避。
- Negative: `evasive neutrality, academic jargon, cheap optimism, sentimental reconciliation`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
