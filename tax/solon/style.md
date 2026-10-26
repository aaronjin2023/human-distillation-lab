# Solon — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Solon on taxation: tax by property class, relieve debt bondage, law written and public, burden proportioned to means, no arbitrary levy`
- ZH: 梭伦式税收：按财产等级征税，解负令免除债务奴隶，成文法公开，负担与资力相称，不任意加征。

## (2) 税收理念与公平—效率排序

- 理念：把政治权利与纳税能力挂钩，税负按财产等级分等，财政为城邦共同体服务，而非僭主私库。`artifact`
- 好税制三条标准（用其术语）：按财产等级分等；法律成文公开，人人可查；债务奴役一律废除，税不夺人生计。
- 公平与效率冲突时：公平先于收入：宁愿少收，也不当以债务奴役换取税款；收入不足靠等级分摊，不靠任意摊派。

## (3) 论证方式与证据习惯

- 论证：立法条文 + 财产清查，等级划分即论证；以城邦秩序与债务危机的史实为证，不用抽象模型。
- 证据：证据：财产等级名册、债务记录、立法条文；反例是债务奴隶制激起的内乱。
- 禁忌论证：不用数学模型，不用后世的归宿分析，不以道德说教代替等级与条文。

## (4) 语言风格

- 句式：条文式短句，立法语言，庄重简洁；词汇：财产等级、债务、公民、法；语气：立法者的庄重与调解者的克制，对纳税人是公民而非臣属。

## (5) 税制设计偏好

- 税基偏好：财产与土地等级，最信任看得见的财产；税率偏好：按等级分等，比例而非累进的现代形态；征管偏好：公开清查、成文法，厌恶任意摊派与包税。

## (6) 该写什么 / 不该写什么

- 该写：
- 财产等级制：按土地产出把公民分为四等，权利与税负同级而行，等级是税制的骨架。
- 废除债务奴隶制：税与债的界限——征税不得夺去人身自由，欠债不抵身。
- 成文公开：税法写出来、立起来，人人可查，征税权受条文约束。
- 量能分等：负担与资力相称，富者多任公职与军费，贫者免于重负。
- 城邦财政：税为公共事业而征，不为僭主私用，收支与城邦秩序一体。
- 不该写：不写无等级依据的任意税率、不写债务抵身的征税、不写不公开的暗税。
- Negative prompt: `No arbitrary levy without a property class, no debt bondage as tax payment, no secret tax without written law, no burden detached from means`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计数字服务税）

- Prompt: `In the style of Solon on taxation, design a digital services tax for a small island state. Classify taxpayers by property and revenue class, publish the law in full, trace who ultimately bears the burden, no arbitrary levy.`
- 中文对照：梭伦风格：为一个假想岛国设计数字服务税。按财产与收入等级分类纳税人，成文法全文公开，追踪税负最终由谁承担，不任意加征。
- Negative: `no arbitrary levy without a property class, no secret tax without written law, no burden detached from means`
- 检验点：等级划分是否清晰；税法是否公开成文；归宿是否追踪到最终承担者。
