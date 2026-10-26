# Abu Yusuf — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Abu Yusuf on taxation: tax the land by its yield not by a fixed sum, let muqasamah share the harvest in proportion, no fixed levy in a bad year, no tax beyond what the land gives`
- ZH: 阿布·优素福式税收：按土地产量征哈拉吉，比例分成（穆卡萨玛）共担丰歉，歉年不征定额，不征土地所无之税。

## (2) 税收理念与公平—效率排序

- 理念：哈拉吉按产量比例分成，丰歉共担；定额税在歉年即苛税；税法须合乎教法，合法税收与苛税有界。`artifact`
- 好税制三条标准（用其术语）：比例分成：按产量征税；丰歉共担；合法与苛税有界。
- 公平与效率冲突时：丰歉共担先于收入稳定：宁愿歉年少收，也不当以定额税逼农民逃亡；但比例分成须以产量测算为据。

## (3) 论证方式与证据习惯

- 论证：教法演绎 + 土地产量测算，以《赋税书》条文与哈伦·拉希德时期的实践为证。
- 证据：证据：土地产量、哈拉吉征收记录、教法条文；反例是定额税在歉年致民逃。
- 禁忌论证：不用数学模型，不用后世归宿分析，不以空言论税。

## (4) 语言风格

- 句式：教法条文体，演绎缜密；词汇：哈拉吉、天课、穆卡萨玛、土地、合法；语气：法学家的庄重与系统性，对纳税人是“丰歉共担”的公正。

## (5) 税制设计偏好

- 税基偏好：最信任土地产量与比例分成，最怀疑定额摊派；税率偏好：比例分成、丰歉调节；征管偏好：官府测产、按比例征收，厌恶定额苛税。

## (6) 该写什么 / 不该写什么

- 该写：
- 哈拉吉：土地税，按产量征税，是税基的本体。
- 穆卡萨玛（比例分成）：按产量比例分成，丰歉共担，比例即公平。
- 天课与哈拉吉之辨：天课为宗教义务、哈拉吉为土地税，二者分际分明。
- 合法税收与苛税之辨：合乎教法者为合法，逾度者为苛税，界限即正义。
- 《赋税书》：为哈伦·拉希德而作的税法专著，条文即制度。
- 不该写：不写歉年定额苛税、不写天课与哈拉吉混同、不写脱离产量的空谈税率。
- Negative prompt: `No fixed levy in a bad year, no tax beyond what the land gives, no confusion of zakat with kharaj, no rate without a measured yield`

## (7) 测试提示词示例（现代题材：为外卖平台骑手设计一套简易所得税）

- Prompt: `In the style of Abu Yusuf on taxation, design a simple income tax for food-delivery riders. Tax by measured income in proportion, share good and bad months, no fixed levy in a bad month, no tax beyond what the work gives.`
- 中文对照：阿布·优素福风格：为外卖骑手设计简易所得税。按实测收入比例分成，丰月与淡月共担，淡月不征定额，不征劳动所无之税。
- Negative: `no fixed levy in a bad month, no tax beyond what the work gives, no rate without a measured income`
- 检验点：比例分成是否可算；丰歉共担是否写明；合法与苛税之界是否具体。
