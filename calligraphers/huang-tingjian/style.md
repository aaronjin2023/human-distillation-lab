# 黄庭坚 — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Huang Tingjian: running and cursive script, tall and elongated characters, long sweeping strokes, one wave with three turns, bold verticals like spears, ink dry and forceful`
- ZH: 黄庭坚风格：行草纵长取势，长枪大戟，一波三折，竖画如戟，墨枯而力沉。

## (2) 笔法

- 用笔中锋为主，回腕取势，提按起伏大；横画“一波三折”，收笔多作波磔；竖画长而挺拔，时有“长枪大戟”之势（后人评语）。`impression` 起笔多藏锋，行笔沉着，收笔顿挫分明。`impression` 禁笔：不用轻滑浮笔，不用短促碎笔。`impression`

## (3) 结字与章法

- 结字纵长取势，字形修长，重心偏上，欹侧中求险绝；笔画伸展，字势向外张扬。`verbatim` 章法行距疏朗，字行欹侧，大小参差，行气如“长枪大戟”纵横。`verbatim` 幅式多为长卷，落款小字，钤印少。`artifact`

## (4) 墨色与节奏

- 墨色浓而不滞，枯笔多而力沉；一幅之内浓淡变化随长画伸展而起伏。`verbatim` 节奏：起笔慢、行笔快、收笔顿，纵画一气呵成，横画三折放缓。`impression` 纸多用生纸，墨色渗透见笔锋往复。`impression`

## (5) 书体与取法

- 书体以行书、草书为主；取法王羲之、怀素，晚年自成纵长一路；自称“凡书要拙多于巧”。`artifact` 演变：早年较谨严，中年纵长之势已成，晚年草书更放，笔画更长更险。`impression`

## (6) 该写什么 / 不该写什么

- 该写：纵长取势的修长字形、一波三折的横画、长枪大戟的长竖、中锋回腕的沉着笔力、疏朗欹侧的行气。
- 不该写：扁方横势的结字、轻滑浮笔、短促碎笔、整齐划一的行距、浓墨滞重的大面积平涂。
- Negative prompt: `No flat wide characters, no light floating strokes, no short broken strokes, no uniform neat grid, no heavy flat ink wash, no printed typeface`

## (7) 测试提示词示例（现代题材：“深夜便利店”行草条幅）

- Prompt: `In the style of Huang Tingjian, running-cursive calligraphy writing 'late night convenience store' in Chinese characters, tall elongated characters, long sweeping verticals, one wave with three turns, dry forceful ink, large empty space`
- 中文对照：黄庭坚风格：写一句“深夜便利店”的行草条幅，字形纵长，长竖如戟，一波三折，墨枯力沉，留白大。
- Negative: `No flat wide characters, no light floating strokes, no short broken strokes, no uniform neat grid, no heavy flat ink wash, no printed typeface`
- 检验点：笔法、结字、章法、墨色是否符合本条风格；是否出现第 6 节禁区里的写法。
