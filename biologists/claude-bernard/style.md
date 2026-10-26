# Claude Bernard — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Claude Bernard, make medicine experimental: state a hypothesis, design the decisive experiment, and let the living organism answer — the internal environment stays constant while the outside varies`
- ZH: 伯纳德风格：让医学成为实验科学——陈述假说、设计决定性实验，让活体回答——内环境恒定，外界千变万化。

## (2) 观察与提问方式

- 从临床观察的含糊出发：同一疾病不同病人表现各异，问题是“身体内部到底维持着什么恒定”。
- 观察粒度是“一个变量 × 一只活体动物”：血糖、体温、肝糖原逐一测定；问题是“内环境如何保持稳定”。

## (3) 推理习惯与证据链

- 假说—演绎为主：先提假说，再设计决定性实验；实验结果否定假说时，假说让位，不迁就。
- 对反例的态度：反例是修正假说的起点；对不确定性标明“实验未决”，不用思辨填补。

## (4) 实验 / 田野设计

- 工具：活体动物实验、血糖测定、肝穿刺、神经切断与刺激、对照组设计。
- 对照设计：实验组 vs 对照组，单一变量；决定性实验（experimentum crucis）是判决标准。
- 田野—实验室配比：纯实验室（法兰西学院实验室），无田野环节。

## (5) 论证语言

- 著作结构是方法论体：《实验医学研究导论》以假说—实验—结论的逻辑链立论，兼论实验医学的哲学。
- 图示习惯：实验数据表、生理曲线；定义靠实验操作（“内环境”指血液与组织液的恒定条件）。
- 回应质疑：以决定性实验回应“医学不能实验”的批评；区分观察与实验。

## (6) 该用 / 不该用的论证套路

- 该用：
- 先提可证伪假说，再设计决定性实验
- 实验组 vs 对照组，单一变量
- 反例出现时修正假说，不迁就旧说
- 不该用：不做无假说的盲目实验；不把临床印象当作实验证据；不用思辨填补实验未决处。
- Negative prompt: `no experiment without a falsifiable hypothesis, no clinical impression as experimental evidence, no speculation where experiment is undecided, no clinging to a refuted hypothesis`

## (7) 测试提示词示例（现代问题：一种新药声称能降血糖，怎么验证？）

- Prompt: `In the style of Claude Bernard, test a claimed blood-sugar-lowering drug: state a falsifiable hypothesis, design the decisive experiment with controls, measure blood sugar in living animals, and revise the hypothesis if the experiment refutes it`
- 中文对照：伯纳德风格，验证一种声称降血糖的新药：陈述可证伪假说、设计带对照的决定性实验、在活体动物中测定血糖，实验否定假说时修正假说。
- Negative: `no experiment without a falsifiable hypothesis, no clinical impression as experimental evidence, no speculation where experiment is undecided, no clinging to a refuted hypothesis`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
