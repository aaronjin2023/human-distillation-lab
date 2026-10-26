# 苏轼 — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Su Shi: running script, plump and unhurried, flat brush and side-brush strokes, candid flaws kept, ink thick then dry, large characters leaning at ease`
- ZH: 苏轼风格：行书丰腴从容，扁笔侧锋，败笔不掩，墨由浓转枯，字大欹侧自如。

## (2) 笔法

- 用笔以侧锋、扁笔为主，中锋辅之；起笔多露锋，收笔略顿，不避“败笔”；提按幅度大，笔画圆厚，如“石压蛤蟆”之态（后人评语）。`impression` 笔锋多用羊毫，笔肚饱满，行笔沉着不疾。`impression` 禁笔：不用瘦硬挺拔的瘦金式线条，不用纤细轻滑的游丝。`impression`

## (3) 结字与章法

- 结字扁方，横势取势，重心偏低而稳；字与字大小参差，行距疏朗，行气自然欹侧。`verbatim` 章法不求整齐，字行时有欹斜，靠字形大小与墨色浓淡调节节奏。`verbatim` 幅式多为长卷与信札，落款小字，钤印一二方，位置偏下。`artifact`

## (4) 墨色与节奏

- 墨色由浓入枯，一幅之内浓淡干湿变化大，《寒食帖》后半枯笔尤多，是情绪与书写速度的直接痕迹。`verbatim` 节奏：起笔从容，中段渐快，末段枯涩放缓；一字之中顿挫分明，不连绵缠绕。`verbatim` 纸多用熟纸与笺纸，墨色晕染克制。`impression`

## (5) 书体与取法

- 书体以行书为主，兼擅楷、草；取法颜真卿、李邕、杨凝式，晚年自称“我书意造本无法”。`artifact` 演变：早年取法二王与颜真卿较谨严，黄州以后放逸丰腴，晚年更趋老辣枯淡。`impression`

## (6) 该写什么 / 不该写什么

- 该写：行书扁方结字、字形大小参差、侧锋扁笔、圆厚笔画、浓墨转枯笔的墨色变化、疏朗行距、自然欹侧的行气、败笔不掩、率意天成的气息。
- 不该写：瘦硬挺拔的瘦金式线条、纤细轻滑的游丝、整齐划一的馆阁式行距、连绵缠绕的狂草、浓艳重彩、装饰性描金。
- Negative prompt: `No thin hard slender-gold strokes, no fine silky threads, no uniform neat grid, no tangled wild cursive, no decorative gold or heavy colour, no printed typeface`

## (7) 测试提示词示例（现代题材：地铁站名行书）

- Prompt: `In the style of Su Shi, running script calligraphy writing modern Tokyo subway station names on rice paper, plump flat-brush strokes, candid dry-brush flaws, varied character sizes, unhurried rhythm, one small colophon at the lower left`
- 中文对照：苏轼风格：用地铁站名写一幅行书，扁笔圆厚，败笔不掩，字大小参差，节奏从容，左下小字落款。
- Negative: `No thin hard slender-gold strokes, no fine silky threads, no uniform neat grid, no tangled wild cursive, no decorative gold or heavy colour, no printed typeface`
- 检验点：笔法、结字、章法、墨色是否符合本条风格；是否出现第 6 节禁区里的写法。
