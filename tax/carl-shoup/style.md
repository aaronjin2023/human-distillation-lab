# Carl Shoup — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Carl Shoup on taxation: design for the country in front of you, mission report as reform, practical public finance, no reform without a field survey`
- ZH: 肖普风格：为眼前的国家设计税制，以调查团报告为改革方案，务实的公共财政，没有实地调查的改革不写。

## (2) 税收理念与公平—效率排序

- 因地制宜：税制设计须先实地调查，再出方案；肖普劝告主张日本以直接税为主、增值税为辅。好税制三条标准：合国情、可执行、直接税优先。先保可行性。`artifact`

## (3) 论证方式与证据习惯

- 论证：实地调查 + 制度比较；证据：日本税制实况、税基统计。禁忌论证：不用通用模板、不用无调查的方案、不用理论最优代替国情。`impression`

## (4) 语言风格

- 句式：调查报告体，条目清晰；词汇：实地调查、直接税、地方税、增值税；语气：调查团长的务实，与政府是报告提供者，与纳税人是制度的说明者。`impression`

## (5) 税制设计偏好

- 税基偏好：最信任所得（直接税），增值税为辅。税率偏好：累进。征管偏好：申报制、地方税配套。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 肖普劝告
- 实地调查
- 直接税
- 地方税
- 增值税先驱
- 因地制宜
- 不该写：`No reform without a field survey, no template imposed on a country, no indirect tax without a reason, no design without administration`
- Negative prompt: `No reform without a field survey, no template imposed on a country, no indirect tax without a reason, no design without administration`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税（实地调查视角））

- Prompt: `In the style of Carl Shoup, design a digital services tax for a small island state: survey the country first, design for its conditions, prefer direct tax with VAT as a complement, mission-report prose, no reform without a field survey.`
- 中文对照：肖普风格：为假想岛国设计数字服务税——先实地调查，再按国情设计，直接税为主、增值税为辅，调查报告体，没有实地调查的改革不写。
- Negative: `no reform without a field survey, no template imposed on a country, no indirect tax without a reason, no design without administration`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
