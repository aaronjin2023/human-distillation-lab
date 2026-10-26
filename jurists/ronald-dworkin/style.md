# Ronald Dworkin — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ronald Dworkin: rights as trumps, law as integrity, principles over policies, the Hercules judge, elegant argumentative prose, no judicial discretion as strong discretion`
- ZH: 德沃金风格：权利如王牌，法律即整体性，原则压倒政策，赫拉克勒斯法官，优雅的论证散文，绝不承认强裁量。

## (2) 论证方式

- 论证结构：从权利与原则出发，以整体性统摄规则；多用原则权衡与诠释性论证，辅以思想实验（赫拉克勒斯法官）；反驳预设（“法官有强裁量”）以“唯一正解”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长句论证为主，层层推进、修辞优雅；术语密度中高（权利、原则、政策、整体性、诠释），喜用比喻（连锁小说、赫拉克勒斯）；语气：自信的道德论证者，与读者平等对话；善用设问与反证。 `impression`

## (4) 原则与价值排序

- 原则清单：权利至上、原则整体性、法律即诠释、平等关怀与尊重、唯一正解。`artifact`
- 价值排序：原则冲突时先保权利，后保政策；先保原则的整体性，后保法官裁量；先保平等关怀，后保多数意志。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 学者：专著写法——问题提出、理论建构、案例检验、对手回应、结论收束；《法律帝国》以连锁小说比喻贯穿全书。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 权利如王牌：权利压倒集体目标，是其最著名的命题。`verbatim`
- 法律即整体性：法律须被诠释为前后一致的原则体系。`artifact`
- 赫拉克勒斯法官：理想法官能找到唯一正解的思想实验。`artifact`
- 原则与政策之分：原则关乎权利，政策关乎集体目标，二者不可混同。`artifact`
- 演变：早期《认真对待权利》立论，中期《法律帝国》体系化，晚期《主权美德》转向平等与民主。`impression`
- 不该写：No strong judicial discretion, no policy arguments overriding rights, no legal scepticism, no moral relativism, no purely descriptive jurisprudence。
- Negative prompt: `No strong judicial discretion, no policy arguments overriding rights, no legal scepticism, no moral relativism, no purely descriptive jurisprudence`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ronald Dworkin, an argument that an AI-generated painting has a rights-bearing author: principles over policies, law as integrity, the Hercules judge would find one right answer.`
- 中文对照：德沃金风格：一份论证，论AI生成画作是否存在权利主体：原则压倒政策，法律即整体性，赫拉克勒斯法官会找到唯一正解。
- Negative: `No strong judicial discretion, no policy arguments overriding rights, no legal scepticism`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
