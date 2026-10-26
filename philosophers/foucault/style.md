# Michel Foucault — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Foucault: archive, rupture, genealogy; power produces truth and subjects; no continuous progress, no sovereign subject, no moralising without analysis`
- ZH: 福柯风格：档案、断裂、系谱；权力生产真理与主体；没有连续的进步叙事，没有主权主体，没有脱离分析的道德谴责。

## (2) 概念

- 权力（power）：不是被占有的东西，而是无处不在的关系网络；权力生产而非仅仅压制。`artifact`
- 知识/权力（power/knowledge）：真理话语与权力机制相互生产，没有脱离权力的真理。`artifact`
- 规训（discipline）：通过监视、检查、规范化塑造身体的技术；全景敞视是其模型。`artifact`（《规训与惩罚》）
- 治理术（governmentality）：治理人口与自我的技术集合；从主权到规训再到治理。`artifact`
- 考古学（archaeology）：描述话语形成的规则与断裂，而非追溯起源。`artifact`
- 系谱学（genealogy）：追问概念与制度的偶然出身，以历史反驳本质。`artifact`
- 主体化（subjectivation）：人如何被权力塑造成主体，又如何反抗成为另一种主体。`artifact`

## (3) 论证结构

档案—断裂—系谱的三段式：先铺陈档案（疯人院、监狱、性话语的历史材料），再指出断裂（古典时代与现代的断裂，而非连续进步），最后以系谱收束（今天的“真理”只是历史偶然的沉淀）。结论强度是历史反讽：不是“应当如何”，而是“原来可以不是这样”。反例处理方式是反转——把反对意见的证据变成系谱的新材料。`impression`

## (4) 修辞

档案式列举、长句铺陈、反转常识的冷峻挑衅；常用“不是……而是……”句式翻转读者预期；语气冷静而危险，与读者的距离是邀你共谋怀疑而非接受结论。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：权力如何生产真理与主体？
- 问题从哪里来：来自对人道主义进步叙事的不满：疯癫史、监狱史、性史都显示，所谓进步往往是权力技术的精致化。；他把问题推向何处：把问题推向晚期的自我技术与生存美学：人如何在权力中反抗、塑造自我。。

## (6) 该写什么 / 不该写什么

- 该写：
- 档案材料、断裂、系谱等方法概念
- 以历史断裂反驳连续进步
- “不是……而是……”的翻转句式
- 不该写：
- 连续进步的历史叙事
- 以主权主体为论证起点
- 脱离分析的道德谴责
- 普遍人性作为论证前提
- Negative prompt: `No continuous progress narrative, no sovereign subject as starting point, no moralising denunciation without analysis, no universal human nature as premise`

## (7) 测试提示词示例（现代题材：自助结账机漏扫与自我监视）

- Prompt: `In the style of Foucault, a self-checkout machine that never scans one item. Do not ask whether keeping it is wrong. Ask what archive produces this scene: the camera above, the recorded voice saying 'unexpected item', the customer who watches herself being watched. Discipline without a guard, power that produces the honest subject. Rupture, not progress.`
- 中文对照：福柯风格：一台自助结账机总有一件商品扫不上。不要问据为己有对不对，而问是什么档案生产了这个场景：头顶的摄像头、那句“请将商品放回”的录音、那个监视着自己被监视的顾客。没有看守的规训，生产出诚实主体的权力。断裂，不是进步。
- Negative: `No continuous progress narrative, no sovereign subject as starting point, no moralising denunciation without analysis, no universal human nature as premise`
- 检验点：是否以档案与场景开篇而非以道德判断开篇；断裂是否出现；结尾是否指向“原来可以不是这样”。
