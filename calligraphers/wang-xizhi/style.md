# Wang Xizhi — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Xizhi: running script, elegant and fluid, varied character sizes, natural rhythm, light ink, graceful turns, no rigid grid`
- ZH: 王羲之风格：行书飘逸流畅，字字大小参差，节奏天然，墨色清润，转折优雅，不落板滞。

## (2) 笔法

- 中锋为主，提按分明，转折圆转兼方；起笔逆入藏锋，收笔回锋；牵丝映带自然，绝无刻意连绵。`verbatim`（摹本可见）
- 禁笔：他几乎不用的笔法——板滞的馆阁体、狂怪的缠绕连绵。

## (3) 结字与章法

- 结字欹正相生，大小参差，疏密相间；章法行气自然，字与字呼应而不粘连，行距疏朗。`verbatim`
- 幅式：卷 / 尺牍 / 册页，横卷为主，行列疏朗。

## (4) 墨色与节奏

- 墨色清润淡雅，浓淡相间而不滞；节奏快慢相生，疾徐有度，如行云流水。`verbatim`

## (5) 书体与取法

- 书体：行书、草书。师卫夫人，取法钟繇而变之；行书至此大成，后世称“书圣”，赵孟頫、董其昌皆取法二王。`impression`
- 演变：摹本所示风格一致；晚年行书更趋从容，草书更趋简淡——此说据摹本与著录，不作定论。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 行书飘逸流畅的牵丝映带
- 大小参差、疏密相间的结字
- 欹正相生、自然的行气
- 清润淡雅、浓淡相间的墨色
- 圆转兼方的优雅转折
- 不该写：
- 板滞的馆阁体
- 狂怪的缠绕连绵
- 均匀划一的字形
- 浓墨滞重的笔意
- 刻意的装饰
- Negative prompt: `No rigid printed typeface, no uniform character size, no mechanical grid, no wild tangled cursive, no heavy stagnant ink, no deliberate ornament`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Wang Xizhi, running script calligraphy writing modern Tokyo subway station names on rice paper, elegant fluid strokes, varied character sizes, natural rhythm, light ink, graceful turns, one seal at the lower left`
- 中文对照：王羲之风格：以行书写现代东京地铁站名于宣纸，笔画飘逸流畅，字字大小参差，节奏天然，墨色清润，左下角一印。
- Negative: `No rigid printed typeface, no uniform character size, no mechanical grid, no wild tangled cursive, no heavy stagnant ink, no deliberate ornament`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
