# Wang Xun — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Xun: running script, calm and warm, restrained emotion in a single letter, the quiet cousin of the two Wangs`
- ZH: 王珣风格：行书温润从容，一纸尺牍，情致内敛，为二王之外的东晋行书。

## (2) 笔法

- 中锋为主，提按温和；转折圆转，起收藏锋，牵丝细而不密。`verbatim`（摹本可见）
- 禁笔：他几乎不用的笔法——狂草的连绵放纵、险绝欹侧。

## (3) 结字与章法

- 结字端正而略欹，大小参差温和；章法行气平和，行距疏朗，尺牍气息浓。`verbatim`
- 幅式：卷 / 尺牍 / 册页，横卷为主，行列疏朗。

## (4) 墨色与节奏

- 墨色温润，浓淡相间极微；节奏从容平和，无疾速处。`verbatim`

## (5) 书体与取法

- 书体：行书。与王羲之、王献之为同族；《伯远帖》与《快雪时晴帖》《中秋帖》并称“三希”。`artifact`
- 演变：仅存一帖，无分期可言。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 温润从容的行书
- 端正略欹的结字
- 细而不密的牵丝
- 温润微淡的墨色
- 尺牍的平和行气
- 不该写：
- 狂草的连绵放纵
- 险绝欹侧
- 浓墨滞重
- 板滞馆阁体
- 刻意装饰
- Negative prompt: `No wild-cursive tangling, no daring slanted compositions, no heavy stagnant ink, no rigid printed typeface, no deliberate ornament`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Wang Xun, running script writing a short letter about modern Tokyo subway stations, calm warm strokes, restrained emotion, light moist ink on paper`
- 中文对照：王珣风格：以行书写一封关于现代东京地铁站的短札，笔画温润从容，情致内敛，墨色温润。
- Negative: `No wild-cursive tangling, no daring slanted compositions, no heavy stagnant ink, no rigid printed typeface, no deliberate ornament`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
