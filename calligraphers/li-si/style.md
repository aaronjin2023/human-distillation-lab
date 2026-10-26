# Li Si — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Si: small seal script, perfectly even strokes, symmetrical structure, solemn and uniform, carved in stone`
- ZH: 李斯风格：小篆线条匀净、结构对称、庄重划一，如刻石般端穆。

## (2) 笔法

- 线条圆匀如铁线，起收皆藏锋，粗细全幅一致，无提按起伏；转折处圆转不停顿，笔画如屈铁盘丝。`verbatim`（拓本可见）
- 禁笔：他几乎不用的笔法——行草的连绵牵丝、提按起伏与飞白。

## (3) 结字与章法

- 结字左右对称、上下匀称，字形修长，笔画间距均匀；章法行列整齐，字字独立不连带，碑面如棋盘。`verbatim`
- 幅式：碑刻竖列。

## (4) 墨色与节奏

- 墨色即拓本墨色：浓黑均匀，无干湿浓淡变化；节奏极慢极稳，一字一顿，无连绵之气。石刻线条无飞白。`artifact`

## (5) 书体与取法

- 书体：小篆。秦统一文字后以小篆为标准书体；取法籀文而简化匀整。李斯书为后世篆书之祖，唐李阳冰、清邓石如皆溯源于此。`impression`
- 演变：传世者皆为刻石，无从分早中晚期；风格上以《泰山刻石》残字最古朴，《峄山刻石》宋摹刻本线条更光洁——二者差异属摹刻层，非作者演变。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 小篆圆匀线条，粗细全幅一致
- 左右对称、上下匀称的修长结字
- 行列整齐、字字独立的碑刻章法
- 浓黑均匀的拓本墨色
- 圆转不停顿的转折
- 不该写：
- 行草的连绵牵丝
- 提按起伏与飞白
- 欹侧取势与大小参差
- 隶书的波磔
- 秀媚活泼的笔意
- Negative prompt: `No running or cursive connections, no varying stroke width, no dry-brush flying white, no slanted or irregular character sizes, no clerical-script wave strokes, no lively or playful brushwork`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Li Si, small seal script calligraphy carving the names of modern Tokyo subway stations on a stone stele, perfectly even rounded strokes, symmetrical tall characters, solemn uniform columns, black rubbing ink`
- 中文对照：李斯风格：以小篆刻现代东京地铁站名于石碑，线条圆匀等粗，结字对称修长，行列整齐庄重，拓本浓墨。
- Negative: `No running or cursive connections, no varying stroke width, no dry-brush flying white, no slanted or irregular character sizes, no clerical-script wave strokes, no lively or playful brushwork`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
