# Wang Xianzhi — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Xianzhi: running and cursive script, more daring than his father, flowing connections, refined and unrestrained`
- ZH: 王献之风格：行草较其父更放，外拓流美，连绵映带，俊迈而不拘。

## (2) 笔法

- 中锋兼侧锋，提按更放；连绵映带多于其父，转折流利，收笔时见外拓之势。`verbatim`（摹本可见）
- 禁笔：他几乎不用的笔法——其父的完全内擫收敛、板滞的馆阁体。

## (3) 结字与章法

- 结字外拓，欹侧更明，字形较王羲之更放；章法行气连绵，字间呼应更密。`verbatim`
- 幅式：卷 / 尺牍 / 册页，横卷为主，行列疏朗。

## (4) 墨色与节奏

- 墨色清润而较父更浓，节奏更快更连，一气呵成处多。`verbatim`

## (5) 书体与取法

- 书体：行书、草书。王羲之之子，世称“二王”；世传其书“破体”，行草更放，后世米芾多取其势。`impression`
- 演变：摹本所示风格一致；早夭无晚年可分，不编造分期。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 较王羲之更放的外拓结字
- 连绵映带的流美行气
- 中锋兼侧锋的灵活用笔
- 清润而稍浓的墨色
- 疾速流利的节奏
- 不该写：
- 其父的完全内擫收敛
- 板滞的馆阁体
- 楷书的方折顿笔
- 浓墨滞重
- 刻意装饰
- Negative prompt: `No rigid printed typeface, no uniform character size, no mechanical grid, no regular-script square turns, no heavy stagnant ink, no deliberate ornament`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Wang Xianzhi, running and cursive script writing modern Tokyo subway station names, daring outward-spreading characters, flowing connections, refined and unrestrained, light ink on paper`
- 中文对照：王献之风格：以行草写现代东京地铁站名，结字外拓流美，连绵映带，俊迈不拘。
- Negative: `No rigid printed typeface, no uniform character size, no mechanical grid, no regular-script square turns, no heavy stagnant ink, no deliberate ornament`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
