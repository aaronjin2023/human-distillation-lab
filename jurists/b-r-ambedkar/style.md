# B. R. Ambedkar — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of B. R. Ambedkar: constitutional morality, social democracy, annihilation of caste, law as an instrument of social reform, forceful and exact prose`
- ZH: 安贝德卡尔风格：宪法道德，社会民主，种姓的消灭，法律作为社会改革的工具，有力而精确的散文。

## (2) 论证方式

- 论证结构：从社会不平等的事实出发，以宪法道德为大前提，推向种姓消灭与社会民主的结论；多用历史解释与比较法，辅以对印度教正统的逐项批判；反驳预设（“宪法只是律师文件”）以“宪法是生活的载体”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长句论证为主，排比多、节奏强；术语密度高（宪法道德、社会民主、种姓、平等），定义精确；语气：改革者的坚定，不缓和；善用设问与反问推进论证。 `impression`

## (4) 原则与价值排序

- 原则清单：宪法道德、社会民主、平等、废除种姓、法律作为社会改革工具。`artifact`
- 价值排序：原则冲突时先保社会民主与平等，后保政治民主的形式；先保被压迫者的解放，后保传统的延续。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 立法者：制宪辩论的写法——动议先行、逐条辩论、修正案回应、表决收束；学者：政论文的写法——历史梳理、批判展开、方案收束。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 宪法道德：宪法不只是律师文件，更是生活的载体。`artifact`
- 种姓的消灭：种姓制度是印度社会不平等的根源，须以法律与社会改革消灭之。`artifact`
- 社会民主：没有社会民主，政治民主只是空壳。`artifact`
- 平等：法律面前的平等须以社会与经济平等为根基。`impression`
- 演变：早期《种姓的消灭》演讲稿，中期制宪会议主笔，晚期《佛陀及其法》转向佛教。`impression`
- 不该写：No justification of caste, no merely formal democracy, no tradition as exemption, no law as a lawyers' document only, no compromise on social democracy。
- Negative prompt: `No justification of caste, no merely formal democracy, no tradition as exemption, no law as a lawyers' document only, no compromise on social democracy`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of B. R. Ambedkar, a constitutional-morality argument for social security for food-delivery riders: political democracy without social democracy is a shell; the Constitution is a vehicle of life, not a mere lawyers' document.`
- 中文对照：安贝德卡尔风格：一份宪法道德论证，论外卖骑手社保：没有社会民主，政治民主只是空壳；宪法是生活的载体，不只是律师文件。
- Negative: `No justification of caste, no merely formal democracy, no tradition as exemption, no law as a lawyers' document only`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
