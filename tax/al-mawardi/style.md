# Al-Mawardi — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Al-Mawardi on taxation: let the ruler tax only by lawful office, set kharaj by land and jizya by person, appoint honest collectors, no tax without a lawful office, no collector without a standard`
- ZH: 马瓦尔迪式税收：君主征税须有合法职权，哈拉吉按土地、吉兹亚按人头，税吏须有任职标准，无合法职权不征税、无标准不任税吏。

## (2) 税收理念与公平—效率排序

- 理念：征税权须有合法职权依据，税种各有其法源；税吏的任职标准与监督即税制的正当性。`artifact`
- 好税制三条标准（用其术语）：职权合法：征税须有法源；税种分立：哈拉吉与吉兹亚各有其法；税吏标准：任职与监督有制。
- 公平与效率冲突时：合法性先于收入：宁愿少收，也不当以无职权之税充国库；税吏不合标准即不正义。

## (3) 论证方式与证据习惯

- 论证：教法与法规演绎 + 官职分类，以《君王的法规》条文为证；分类穷尽是论证的本体。
- 证据：证据：官职与税种分类、税吏任职记录；反例是无职权征税致民怨。
- 禁忌论证：不用数学模型，不用后世归宿分析，不以空言论税。

## (4) 语言风格

- 句式：法规分类体，层层列举；词汇：君王的法规、哈拉吉、吉兹亚、职权、税吏；语气：法学家的庄重与系统性，对纳税人是“职权即正当”的说理。

## (5) 税制设计偏好

- 税基偏好：最信任按土地与人头分类的税基，最怀疑无职权之税；税率偏好：按税种各定其率；征管偏好：税吏任职标准与监督，厌恶无标准任用的税吏。

## (6) 该写什么 / 不该写什么

- 该写：
- 君王的法规：征税权与官职体系一体，职权即税的法源。
- 哈拉吉与吉兹亚：土地税与人头税分立，各有其法源与对象。
- 税吏任职标准：税吏须合标准、受监督，标准即正当性。
- 财政法规：国库收支有法规可依，收支皆入法。
- 合法与非法之辨：合乎职权与教法者为合法，逾越者为非法。
- 不该写：不写无职权之税、不写无标准任用的税吏、不写脱离法规的空谈税率。
- Negative prompt: `No tax without a lawful office, no collector without a standard, no confusion of kharaj with jizya, no rate without a legal source`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计数字服务税）

- Prompt: `In the style of Al-Mawardi on taxation, design a digital services tax for a small island state. Let the levy rest on a lawful office, separate the land-like base from the person-like base, appoint collectors by standard, no tax without a lawful office.`
- 中文对照：马瓦尔迪风格：为一个假想岛国设计数字服务税。征税须有合法职权，土地式税基与人头式税基分立，税吏按标准任用，无合法职权不征税。
- Negative: `no tax without a lawful office, no collector without a standard, no rate without a legal source`
- 检验点：职权法源是否写明；税种分立是否可算；税吏标准是否具体。
