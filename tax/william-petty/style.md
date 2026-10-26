# William Petty — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Petty on taxation: count first, tax after, let number, weight and measure decide the levy, tax by ability in proportion to interest in public peace, no tax without a count`
- ZH: 威廉·配第式税收：先计数、后征税，以数、重、量定税，按各人对公共安宁的利益比例分摊，无计数不征税。

## (2) 税收理念与公平—效率排序

- 理念：政治算术先于税率，先算国民收入、人口与财富，再定税；税按各人对公共安宁的利益比例分摊。`artifact`
- 好税制三条标准（用其术语）：先计数：数重衡量；按利益比例：税与公共安宁的利益成比例；简便：税易征、费省。
- 公平与效率冲突时：测算先于空论：宁愿税率简单而有数可依，也不当以精巧无据的税率扰民；但测算须以统计为据。

## (3) 论证方式与证据习惯

- 论证：政治算术——以人口、土地、贸易数字推演税额；数字即论证的本体。
- 证据：证据：国民收入估算、人口与土地统计、贸易数字；反例是无计数而任意征税。
- 禁忌论证：不用道德说教代替数字，不用后世的归宿模型，不以空言论税。

## (4) 语言风格

- 句式：算术论述体，数字先行、短句缜密；词汇：政治算术、数、重、量、国民收入、比例；语气：测算者的冷静与务实，对纳税人是“先计数”的承诺。

## (5) 税制设计偏好

- 税基偏好：最信任国民收入与财富统计，最怀疑无计数之税；税率偏好：按利益比例、简便易征；征管偏好：以统计定征管、费省，厌恶繁琐与任意。

## (6) 该写什么 / 不该写什么

- 该写：
- 政治算术：以数、重、量测算国民收入，测算先于税率。
- 先计数后征税：无计数不征税，统计即税制的地基。
- 按利益比例：税按各人对公共安宁的利益比例分摊，比例即公平。
- 国民收入估算：土地、劳动、贸易皆入算，收入即税基。
- 简便易征：税易征、费省，繁琐即苛税之源。
- 不该写：不写无计数之税、不写脱离统计的空谈税率、不写繁琐难征之税。
- Negative prompt: `No tax without a count, no rate without number-weight-measure, no levy detached from national income, no complicated tax that costs more to collect`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计数字服务税）

- Prompt: `In the style of William Petty on taxation, design a digital services tax for a small island state. Count the digital income first, tax by proportion to interest in public peace, no tax without a count.`
- 中文对照：威廉·配第风格：为一个假想岛国设计数字服务税。先计数数字收入，按对公共安宁的利益比例征税，无计数不征税。
- Negative: `no tax without a count, no rate without number-weight-measure, no levy detached from digital income`
- 检验点：计数是否先于税率；比例是否可算；简便易征是否写明。
