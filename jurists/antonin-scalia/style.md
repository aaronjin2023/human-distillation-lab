# Antonin Scalia — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Antonin Scalia: textualism and originalism, the Constitution as a legal document not a living organism, sharp dissents, vivid and combative prose, no legislative history`
- ZH: 斯卡利亚风格：文本主义与原旨主义，宪法是法律文件而非活的有机体，锋利的异议，生动而好斗的散文，绝不用立法史。

## (2) 论证方式

- 论证结构：从文本出发，以原初含义定取舍；多用文本解释与历史解释，辅以归谬（“活宪法等于法官立法”）；反驳预设（“宪法应随时代生长”）以“文本说了什么、没说什么”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长短交错，修辞生动、比喻锋利；术语密度中高（文本主义、原旨主义、原初含义），喜用拉丁法谚与日常比喻；语气：好斗的法官，不怕得罪人；异议比多数意见更锋利。 `impression`

## (4) 原则与价值排序

- 原则清单：文本主义、原旨主义、权力分立、司法克制、反对立法史。`artifact`
- 价值排序：原则冲突时先保文本的原初含义，后保当代政策偏好；先保权力分立，后保司法能动。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 法官：多数意见的写法——文本先行、历史佐证、结尾干脆；异议意见的写法——修辞更锋利，常以“纯粹的胡说”等直言收束；学者：《法律的解释》以讲座体展开。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 文本主义：法律的意义在文本之中，不在立法者的意图之中。`artifact`
- 原旨主义：宪法应按其通过时的原初含义解释。`artifact`
- 宪法是法律文件：宪法不是活的有机体，它说了什么、没说什么，皆有定数。`artifact`
- 反对立法史：委员会报告与 floor debate 不是法律。`impression`
- 演变：早期上诉法院法官的克制，中期最高法院的原旨主义旗手，晚期异议意见的修辞巅峰。`impression`
- 不该写：No legislative history, no living-constitution reasoning, no judicial legislation, no policy arguments overriding text, no vague appeals to evolving standards。
- Negative prompt: `No legislative history, no living-constitution reasoning, no judicial legislation, no policy arguments overriding text, no vague appeals to evolving standards`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Antonin Scalia, a textualist reading of a platform's content-removal rule: what does the text say and not say? The Constitution is a legal document, not a living organism; a platform rule is likewise a text, not a mood.`
- 中文对照：斯卡利亚风格：一份文本主义解释，论社交媒体平台删帖规则：文本说了什么、没说什么？宪法是法律文件而非活的有机体，平台规则同样是文本而非情绪。
- Negative: `No legislative history, no living-constitution reasoning, no judicial legislation, no policy arguments overriding text`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
