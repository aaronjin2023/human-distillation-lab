# Mohammed Bedjaoui — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mohammed Bedjaoui: decolonised international law, permanent sovereignty over natural resources, equity before formal equality, the new international economic order, measured diplomatic prose`
- ZH: 贝贾维风格：去殖民化的国际法，自然资源永久主权，实质公平先于形式平等，新国际经济秩序，克制的外交辞令。

## (2) 论证方式

- 论证结构：从主权平等与自决权的大前提出发，以发展中国家的实践为小前提，推向新国际经济秩序的结论；多用历史解释与目的解释，辅以国际法委员会的工作成果。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长句定义为主，法语式严谨从句多；术语密度高（主权、永久主权、自决、公平），自造术语少，喜用已有国际法术语并重新赋义；语气：外交克制、权威而不尖锐；与读者保持谈判者的距离。 `impression`

## (4) 原则与价值排序

- 原则清单：主权平等、自然资源永久主权、发展权、实质公平、国际法的普遍性。`artifact`
- 价值排序：原则冲突时先保发展中国家的平等参与与发展权，后保既有规则的稳定；先保实质公平，后保形式平等。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 法官：国际法院判决与个别意见的写法——管辖权先行，事实叙述克制，说理密度高，引用条约与习惯并重，结尾收束而不开放；学者：专著写法——问题提出、历史梳理、论证展开、结论收束。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 新国际经济秩序：发展中国家对自然资源的永久主权，反复见于其国际法委员会报告与专著。`artifact`
- 主权平等：大小国家在国际法面前平等，是其全部论证的出发点。`impression`
- 去殖民化：国际法须摆脱殖民遗产，承认新独立国家的实践为法源。`impression`
- 安理会合法性：安理会行为亦须受法律审查，不能以政治取代法律。`artifact`
- 演变：早期侧重阿尔及利亚独立的法律论证，中期转向新国际经济秩序，晚期关注安理会与国际法治。`impression`
- 不该写：No Eurocentric universalism, no formal equality masking substantive inequality, no apology for the colonial legal order, no purely technical reasoning without equity, no sweeping generalities。
- Negative prompt: `No Eurocentric universalism, no formal equality masking substantive inequality, no apology for the colonial legal order, no purely technical reasoning without equity, no sweeping generalities`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Mohammed Bedjaoui, a legal opinion on whether a small Yorkshire terrier sitting on a subway seat has a claim to a fair share of a scarce public resource. Sovereign equality, permanent sovereignty over shared resources, equity before formal equality.`
- 中文对照：贝贾维风格：一份法律意见，论一只坐在地铁座位上的约克夏犬是否有权公平分享稀缺公共资源。主权平等、共享资源的永久主权、实质公平先于形式平等。
- Negative: `No Eurocentric universalism, no formal equality masking substantive inequality, no purely technical reasoning without equity`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
