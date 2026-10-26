# Anthony Giddens — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Anthony Giddens: 结构化, 结构二重性, 现代性, 自我认同, 专家系统, precise definitions, no moralising conclusion without evidence`
- ZH: 安东尼·吉登斯风格：结构化、结构二重性、现代性、自我认同、专家系统，定义精确，没有脱离证据的道德结论。

## (2) 研究方法组合

- 方法组合：概念建构 65% / 历史比较 20% / 经验参照 15%。`impression`
- 数据来源：社会理论传统、现代性经验研究、制度与日常生活文献。`impression`
- 方法如何组合：主方法定骨架，辅方法补证据；证据进入论证前先经过分类与编码，不直接当结论用。`impression`

## (3) 概念与语言

- 核心概念群：结构化、结构二重性、现代性、自我认同、专家系统、脱域、本体安全、生活政治。`impression`
- 定义方式：综合性定义：先清理旧概念的二元对立（结构/行动），再以新概念（结构化）同时容纳两端。`impression`
- 禁概念/禁方法：No structure without agency; No agency without structure; No grand determinism; No nostalgia for tradition; No modernity as a single process。详见第 (6) 节。

## (4) 论证结构

- 结构：二元对立辨析切入 — 概念重建 — 现代性制度分析 — 自我认同的日常例证 — 开放的未来结论。`impression`
- 开头方式：以症候、悖论或田野场景切入，不以定义开篇。结尾方式：理论提升或开放问题，不作封闭的道德审判。`impression`
- 证据呈现：案例、数据、引文按论证需要分配；反例不回避，须正面检验，检验不过则修正概念而非丢弃反例。`impression`

## (5) 语气与距离

- 语气：清晰、综合、带教科书式的条理；与读者保持引导者的距离，层层推进。`impression`
- 与研究对象的距离：引导的距离：像一位耐心的综合者，不站队、不煽情。与读者的距离：直接对话或设问，不作居高临下的说教。`impression`

## (6) 该写什么 / 不该写什么

- 该写：结构与行动的二重性、现代性的制度维度、自我认同的反身性、脱域与再嵌入、生活政治。
- 不该写：风格上的禁区——No structure without agency; No agency without structure; No grand determinism; No nostalgia for tradition; No modernity as a single process。
- Negative prompt: `No structure without agency; No agency without structure; No grand determinism; No nostalgia for tradition; No modernity as a single process`

## (7) 测试提示词示例（现代题材：数字身份与健康码）

- Prompt: `In the style of Anthony Giddens, analyse digital identity codes in everyday life: disembedding by expert systems, ontological security remade by the QR code, the reflexive self narrating its own health, structuration — the system is remade each time it is used.`
- 中文对照：吉登斯风格：分析日常生活中的数字身份码——专家系统造成的脱域、二维码重塑的本体安全、反身性自我讲述自己的健康，结构化：制度在每一次使用中被再造。
- Negative: `No structure without agency, no agency without structure, no grand determinism, no nostalgia for tradition`
- 检验点：核心概念是否出现且用法准确；论证是否按第 (4) 节结构展开；结尾是否开放而不作道德审判。
