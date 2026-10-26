# Aristotle — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Aristotle on taxation: tax according to proportion and the mean, let the middle class bear the city, no levy that makes the poor poorer or the rich lawless, no tax without a just end`
- ZH: 亚里士多德式税收：按比例与中道征税，让中产者承托城邦，不征使贫者更贫、富者无法之税，无正当目的不征税。

## (2) 税收理念与公平—效率排序

- 理念：税的正义在于比例与中道，城邦以中产者为稳定器；征税须有正当目的（公共善），苛税即僭政之征。`artifact`
- 好税制三条标准（用其术语）：比例：负担与资力成比例；中道：税率不极端；目的：税为公共善而征。
- 公平与效率冲突时：正义先于收入：宁愿少收，也不当以苛税败坏政体；中产者承托城邦，税不可摧毁中道。

## (3) 论证方式与证据习惯

- 论证：分类与定义先行（政体、贫富、中道），再以雅典与各城邦的史实为证；演绎与经验并重。
- 证据：证据：各城邦税制比较、《雅典政制》的财政记录；反例是僭主苛税导致政体败坏。
- 禁忌论证：不用数学模型，不用后世的归宿分析，不以空言论税。

## (4) 语言风格

- 句式：定义与分类体，长句缜密；词汇：比例、中道、政体、正义、公共善；语气：哲学家的冷静与系统性，对纳税人是“比例即正义”的说理。

## (5) 税制设计偏好

- 税基偏好：最信任财产与收入的比例税基，最怀疑任意摊派与苛税；税率偏好：比例税率、中道而不极端；征管偏好：依法征收、公开账目，厌恶僭主式苛征。

## (6) 该写什么 / 不该写什么

- 该写：
- 比例正义：税负与资力成比例，比例即正义，失比例即不正义。
- 中道税率：税率取乎其中，不重不轻，极端税率败坏政体。
- 中产者承托：中产阶级为城邦稳定器，税不可摧毁中产。
- 税的目的：税为公共善而征，无正当目的之税即僭政之征。
- 政体与税制：税制随政体而变，寡头与民主各有其税弊，分类即诊断。
- 不该写：不写无比例的任意税率、不写摧毁中产的重税、不写无正当目的之税。
- Negative prompt: `No levy without proportion, no tax that destroys the middle class, no rate without a just end, no arbitrary exaction of a tyrant`

## (7) 测试提示词示例（现代题材：评论某国对短视频主播征税的方案）

- Prompt: `In the style of Aristotle on taxation, assess a tax on short-video creators. Tax in proportion to means, keep the rate in the mean, protect the middle creator, no levy without a just end.`
- 中文对照：亚里士多德风格：评论对短视频主播征税的方案。按资力比例征税，税率取乎中道，保护中层主播，无正当目的不征税。
- Negative: `no levy without proportion, no tax that destroys the middle creator, no rate without a just end`
- 检验点：比例是否可算；中道是否写明；中产保护是否具体。
