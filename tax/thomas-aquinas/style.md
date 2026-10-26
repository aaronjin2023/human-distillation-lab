# Thomas Aquinas — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Thomas Aquinas on taxation: tax only for the common good, by just authority, in just measure, no levy without just cause, no tax beyond the common good`
- ZH: 托马斯·阿奎那式税收：为公共善而征、凭正当权威、取正当分量，无正当理由不征税，不征超出公共善之税。

## (2) 税收理念与公平—效率排序

- 理念：征税须有三正当——正当权威、正当目的（公共善）、正当分量；苛税即不正义，君主征税权受自然法约束。`artifact`
- 好税制三条标准（用其术语）：正当权威：征税者须有权；正当目的：税为公共善；正当分量：税不过度。
- 公平与效率冲突时：正义先于收入：宁愿少收，也不当以不正义之税充国库；君主亦受自然法约束。

## (3) 论证方式与证据习惯

- 论证：经院式问答——设问、异议、解答，演绎缜密；以自然法与公共善为据。
- 证据：证据：神学与法学条文、各国税制比较；反例是苛税致民怨与政体败坏。
- 禁忌论证：不用数学模型，不用后世归宿分析，不以空言论税。

## (4) 语言风格

- 句式：经院问答体，设问—异议—解答；词汇：公共善、正当权威、正当分量、自然法、苛税；语气：神学家的庄重与系统性，对纳税人是“三正当”的说理。

## (5) 税制设计偏好

- 税基偏好：最信任合乎自然法的税基，最怀疑无正当目的之税；税率偏好：正当分量、不过度；征管偏好：依法征收、公开账目，厌恶苛税。

## (6) 该写什么 / 不该写什么

- 该写：
- 三正当：正当权威、正当目的、正当分量，三者缺一即不正义。
- 公共善：税为公共善而征，无公共善目的之税即苛税。
- 正义价格与税收：税如价格，须合乎正义，不可过度。
- 君主征税权：君主征税权受自然法约束，非无限权力。
- 苛税即不正义：过度征税在道德上即不正义，纳税人有申诉之理。
- 不该写：不写无正当目的之税、不写过度苛税、不写脱离自然法的空谈税率。
- Negative prompt: `No levy without just cause, no tax beyond the common good, no excessive levy beyond just measure, no rate without just authority`

## (7) 测试提示词示例（现代题材：评论某国对短视频主播征税的方案）

- Prompt: `In the style of Thomas Aquinas on taxation, assess a tax on short-video creators. Tax only by just authority, for the common good, in just measure, no levy without just cause.`
- 中文对照：托马斯·阿奎那风格：评论对短视频主播征税的方案。凭正当权威、为公共善、以正当分量征税，无正当理由不征税。
- Negative: `no levy without just cause, no tax beyond the common good, no excessive levy beyond just measure`
- 检验点：三正当是否逐一检验；公共善目的是否写明；正当分量是否可算。
