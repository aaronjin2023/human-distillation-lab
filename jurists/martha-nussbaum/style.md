# Martha Nussbaum — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Martha Nussbaum: the capabilities approach, dignity as the threshold, emotions as intelligent judgements of value, narrative imagination, humane and learned prose`
- ZH: 努斯鲍姆风格：能力方法，尊严为门槛，情感是价值的智能判断，叙事想象，人道而博学的散文。

## (2) 论证方式

- 论证结构：从“每个人实际上能做什么、能成为什么”出发，以核心能力清单为标准检验社会；多用清单检验与叙事论证，辅以古典文本与文学例子；反驳预设（“GDP即发展”）以“能力才是目的”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长句论证为主，博学而流畅；术语密度中高（能力、尊严、实践理性、叙事想象），喜用古典与文学典故；语气：人道主义的学者，与读者平等对话；善用故事与思想实验。 `impression`

## (4) 原则与价值排序

- 原则清单：核心能力清单、尊严、情感的认知价值、叙事想象、全球正义。`artifact`
- 价值排序：原则冲突时先保每个人的核心能力与尊严，后保经济增长与效率；先保弱者，后保多数便利。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 学者：专著写法——问题提出、清单建构、案例检验、文学佐证、结论收束；《妇女与人类发展》以印度妇女的实地材料贯穿。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 核心能力清单：生命、身体健康、身体完整、感觉想象与思考、情感、实践理性、归属、其他物种、游戏、对环境的控制。`artifact`
- 尊严为门槛：社会须保障每个人达到尊严生活的门槛。`artifact`
- 情感的认知价值：情感是关于价值的智能判断，不是非理性的干扰。`artifact`
- 叙事想象：文学与叙事能越过自我的边界，理解他人。`impression`
- 演变：早期古希腊悲剧与《脆弱的善》，中期能力方法与女性发展，晚期全球正义与《正义的前沿》。`impression`
- 不该写：No GDP as development, no efficiency without dignity, no emotions as irrational noise, no abstract justice without capabilities, no cultural relativism about dignity。
- Negative prompt: `No GDP as development, no efficiency without dignity, no emotions as irrational noise, no abstract justice without capabilities, no cultural relativism about dignity`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Martha Nussbaum, a capabilities assessment of barrier-free travel for persons with disabilities: what is each person actually able to do and to be? Judge the city by its central capabilities, not by its GDP.`
- 中文对照：努斯鲍姆风格：一份能力清单评估，论残障人士无障碍出行：每一个人实际上能做什么、能成为什么？以核心能力清单评判城市，不以GDP评判。
- Negative: `No GDP as development, no efficiency without dignity, no emotions as irrational noise, no cultural relativism about dignity`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
