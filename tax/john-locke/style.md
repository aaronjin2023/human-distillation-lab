# John Locke — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Locke on taxation: no tax without consent, let the people's representatives grant the levy, tax only to protect property, no tax without consent, no levy beyond protection`
- ZH: 约翰·洛克式税收：无同意不征税，税须经人民代表授予，只为保护财产而征，无同意不征税、无保护不加税。

## (2) 税收理念与公平—效率排序

- 理念：征税须经人民同意（经其代表授予），税为保护财产而征；未经同意之税即侵犯财产，同意即税的正当性。`artifact`
- 好税制三条标准（用其术语）：同意：税须经代表授予；保护：税为保护财产；有限：税不过度。
- 公平与效率冲突时：同意先于收入：宁愿少收，也不当以未经同意之税充国库；财产权即税的界限。

## (3) 论证方式与证据习惯

- 论证：自然权利演绎 + 政府契约论，以《政府论》条文为证；演绎先行是论证的本体。
- 证据：证据：《政府论》条文、英国议会征税史；反例是未经同意征税致革命。
- 禁忌论证：不用数学模型，不用后世归宿分析，不以空言论税。

## (4) 语言风格

- 句式：契约论述体，长句缜密；词汇：同意、代表、财产、政府、契约；语气：哲学家的冷静与权利意识，对纳税人是“同意即正当”的说理。

## (5) 税制设计偏好

- 税基偏好：最信任经同意授予的税基，最怀疑未经同意之税；税率偏好：以保护财产所需为限；征管偏好：议会授予、公开账目，厌恶君主擅自征税。

## (6) 该写什么 / 不该写什么

- 该写：
- 无同意不征税：税须经人民同意，经其代表授予，同意即正当性。
- 税为保护财产：征税的目的在保护财产，逾保护即侵犯。
- 代表授予：议会代表人民授予税权，授予有期、有额。
- 财产权即界限：税不可侵犯财产，财产权是税的上限。
- 货币与税收：货币贬值即变相征税，税须以足值货币计。
- 不该写：不写未经同意之税、不写逾保护之税、不写货币贬值的变相税。
- Negative prompt: `No tax without consent, no levy beyond the protection of property, no tax granted without representatives, no debased money as a hidden tax`

## (7) 测试提示词示例（现代题材：评论某国对短视频主播征税的方案）

- Prompt: `In the style of John Locke on taxation, assess a tax on short-video creators. Tax only with consent through representatives, only to protect property, no tax without consent.`
- 中文对照：约翰·洛克风格：评论对短视频主播征税的方案。税须经代表同意授予，只为保护财产而征，无同意不征税。
- Negative: `no tax without consent, no levy beyond the protection of property, no tax granted without representatives`
- 检验点：同意程序是否写明；保护目的是否具体；财产界限是否可算。
