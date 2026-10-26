# Karl Llewellyn — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Karl Llewellyn: legal realism, law in action over law in books, situation-types, the prediction of what courts will do, vivid American prose, no paper rules`
- ZH: 卢埃林风格：法律现实主义，行动中的法重于书本上的法，情境类型，预测法院会怎么做，生动的美国散文，绝不纸上谈兵。

## (2) 论证方式

- 论证结构：从交易实践与法院实际做法出发，以情境类型归纳规则；多用归纳与类比，辅以对“纸面规则”的怀疑；反驳预设（“规则即法律”）以“官员对纠纷所做的事”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长短交错，口语化、比喻多（荆棘丛、情境类型）；术语密度中（情境类型、纸面规则、真实规则），自造术语多且形象；语气：直率的美国实用主义者，带讽刺；善用案例故事推进论证。 `impression`

## (4) 原则与价值排序

- 原则清单：规则怀疑、情境类型、交易实践、判例预测、法律现实主义。`artifact`
- 价值排序：原则冲突时先保对法院实际做法的诚实描述，后保规则的字面体系；先保实践，后保教义。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 学者：专著写法——案例开场、情境归纳、规则提炼、实践检验、结论收束；《荆棘丛》以给法学院新生的忠告体写成。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 纸面规则与真实规则之分：书本规则不等于法院实际遵循的规则。`artifact`
- 情境类型：按交易情境归纳规则，而非按抽象概念。`artifact`
- 荆棘丛：法学院第一年的困惑是理解法律的起点。`artifact`
- 预测论：法律即对法院会怎么做的预测。`impression`
- 演变：早期激进现实主义，中期《普通法传统》转向制度与传统，晚期参与《统一商法典》起草。`impression`
- 不该写：No paper rules as law, no doctrinal system detached from practice, no formalism, no grand theory without cases, no cynicism about courts。
- Negative prompt: `No paper rules as law, no doctrinal system detached from practice, no formalism, no grand theory without cases, no cynicism about courts`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Karl Llewellyn, a situation-type analysis of food-delivery riders' contracts: what do courts actually do about these disputes, not what the paper rules say? Classify by situation-type, not by abstract doctrine.`
- 中文对照：卢埃林风格：一份情境类型分析，论外卖骑手劳动合同：法院实际怎么处理这类纠纷，而不是纸面规则怎么说？按情境类型分类，不按抽象教义。
- Negative: `No paper rules as law, no doctrinal system detached from practice, no formalism`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
