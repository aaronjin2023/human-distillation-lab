# Suleiman the Magnificent — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Suleiman the Magnificent on taxation: write the kanunname so every tax has a written rate, let the timar hold land for service, tax the land and the head by the book, no levy outside the kanunname`
- ZH: 苏莱曼式税收：卡努纳玛成文，每税皆有书面税率，蒂玛尔以地养兵，按册征土地税与人头税，无一税在法典之外。

## (2) 税收理念与公平—效率排序

- 理念：税以卡努纳玛成文法为据，每税皆有书面税率；蒂玛尔制以土地养兵，税与军役一体；成文即正义。`artifact`
- 好税制三条标准（用其术语）：成文：每税皆有书面税率；蒂玛尔：以地养兵；按册：土地与人头皆入册。
- 公平与效率冲突时：成文与统一先于旧制：宁愿以卡努纳玛统一各省税制，也不当放任地方任意加征；但成文须以清册为据。

## (3) 论证方式与证据习惯

- 论证：卡努纳玛条文 + 土地清册，数字即论证；以帝国疆域的急需为证。
- 证据：证据：卡努纳玛条文、土地清册、蒂玛尔记录；反例是地方任意加征致民怨。
- 禁忌论证：不用抽象公平原则推导税率，不用后世归宿模型，不以空言论税。

## (4) 语言风格

- 句式：法典条文体，短句缜密；词汇：卡努纳玛、蒂玛尔、土地税、人头税、成文；语气：立法君主的庄重与统一，对纳税人是“成文即确定”的承诺。

## (5) 税制设计偏好

- 税基偏好：最信任土地清册与蒂玛尔，最怀疑地方任意加征；税率偏好：卡努纳玛书面税率、固定；征管偏好：按册征收、蒂玛尔领主代征，厌恶法典外加征。

## (6) 该写什么 / 不该写什么

- 该写：
- 奥斯曼卡努纳玛：税以成文法典为据，每税皆有书面税率。
- 土地税与人头税：按册征土地税与人头税，清册即税基。
- 蒂玛尔制：以土地养兵，税与军役一体，领主代征有制。
- 成文即正义：税率写出来才算数，法典之外无税。
- 统一各省税制：卡努纳玛统一帝国各省税制，统一即秩序。
- 不该写：不写法典外加征、不写无清册的空谈税率、不写脱离蒂玛尔的税制。
- Negative prompt: `No levy outside the kanunname, no tax without a written rate, no land outside the register, no arbitrary increase beyond the book`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计数字服务税）

- Prompt: `In the style of Suleiman the Magnificent on taxation, design a digital services tax for a small island state. Write the kanunname so every levy has a written rate, let the register hold every platform, no levy outside the book.`
- 中文对照：苏莱曼风格：为一个假想岛国设计数字服务税。卡努纳玛成文，每税皆有书面税率，清册登记每一个平台，无一税在法典之外。
- Negative: `no levy outside the book, no tax without a written rate, no platform outside the register`
- 检验点：成文税率是否写明；清册是否完整；法典外加征是否被拒绝。
