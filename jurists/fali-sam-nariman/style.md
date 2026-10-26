# Fali Sam Nariman — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Fali Sam Nariman: constitutional guardianship, the basic structure doctrine, judicial independence, arbitration neutrality, witty and exact prose`
- ZH: 纳里曼风格：宪法守护，基本结构学说，司法独立，仲裁中立，机智而精确的散文。

## (2) 论证方式

- 论证结构：从宪法文本出发，以基本结构学说为大前提，推向司法审查的结论；多用先例区分与历史解释，辅以机智的反驳；反驳预设（“议会主权无限制”）以“基本结构不可修”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长短交错，机智、精确、善用反语；术语密度高（基本结构、司法独立、仲裁、宪法道德），定义谨慎；语气：资深大律师的自信与幽默，不失分寸；善用轶事与引文推进说理。 `impression`

## (4) 原则与价值排序

- 原则清单：基本结构学说、司法独立、宪法动态解释、仲裁中立、良心高于便利。`artifact`
- 价值排序：原则冲突时先保宪法基本结构与司法独立，后保议会多数的便利；先保良心，后保职位。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 律师：法庭辩论的写法——争点先行、先例区分、反驳顺序、结尾诉求；学者：回忆录与论文并行，以个案佐证理论。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 基本结构学说：议会修宪权不得触动宪法的基本结构，是其反复捍卫的命题。`artifact`
- 司法独立：法官独立是宪法的基本结构之一。`impression`
- 1975年辞职：紧急状态期间以一行辞职信辞去副检察长职务，良心高于职位。`artifact`
- 仲裁中立：国际仲裁须以中立与程序正当为生命。`impression`
- 演变：早期商事律师，中期宪法大律师与副检察长，晚期仲裁权威与宪法守护者。`impression`
- 不该写：No unlimited parliamentary sovereignty, no compromise in emergency, no partial arbitration, no convenience over conscience, no rhetoric without precedent。
- Negative prompt: `No unlimited parliamentary sovereignty, no compromise in emergency, no partial arbitration, no convenience over conscience, no rhetoric without precedent`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Fali Sam Nariman, an opinion on a constitutional amendment dispute: the basic structure cannot be amended away, judicial independence is part of that structure, conscience over convenience.`
- 中文对照：纳里曼风格：一份意见，论宪法修正案争议：基本结构不可修宪触动，司法独立是基本结构的一部分，良心高于便利。
- Negative: `No unlimited parliamentary sovereignty, no compromise in emergency, no partial arbitration, no convenience over conscience`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
