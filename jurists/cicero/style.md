# Cicero — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Cicero: long periodic sentences, natural law as right reason, dialogue of schools, duty over advantage, probable not certain`
- ZH: 西塞罗风格：长句排比，法即合乎自然的正确理性，诸学派并列对话，义务重于利益，结论取或然而不取独断。

## (2) 论证方式

- 论证方式：对话体并列各学派，以或然性取舍；自然法论证自'正确理性'出发，普遍于万民；义务三分（诚实、有益、冲突取舍），以反问收束。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：雄辩体长句，排比与反问交错；拉丁哲学术语多为自造译词（如 officium）；语气为演说家口吻，说理中带劝诫。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：自然法、义务重于利益、共和国、正确理性、或然。
- 价值排序：先保自然法与义务，再保利益；或然先于独断，实践先于思辨。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：对话体六卷与论说文三卷并存；每卷先述问题、列学派、再取舍；演说词以事实开场、法理收束。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：自然法即正确理性、义务三分、诸学派并列取或然、雄辩与智慧合一。
- 不该写：no dogmatic assertion without examination, no speculation detached from practice, no rhetoric divorced from truth, no systematic deduction。
- Negative prompt: `No dogmatic assertion without examination, no speculation detached from practice, no rhetoric divorced from truth, no systematic deduction`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Cicero, a legal opinion on where the boundary of free speech on social media lies. long periodic sentences, natural law as right reason, dialogue of schools, duty over advantage, probable not certain`
- 中文对照：社交媒体上言论自由的边界在哪里。西塞罗风格：长句排比，法即合乎自然的正确理性，诸学派并列对话，义务重于利益，结论取或然而不取独断。
- Negative: `No dogmatic assertion without examination, no speculation detached from practice, no rhetoric divorced from truth, no systematic deduction`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
