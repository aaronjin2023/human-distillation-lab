# 徐渭 — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xu Wei: wild cursive, learning from Mi Fu and Huaisu, strokes drenching and splashing, characters tilted and broken, ink wet and splashing, rhythm urgent and unrestrained like blue-green vines`
- ZH: 徐渭风格：草书狂放淋漓，取法米芾、怀素，笔画纵横倾欹，墨湿而泼，节奏急促放逸，如青藤盘结。

## (2) 笔法

- 用笔纵横倾欹，中锋与侧锋交替，提按幅度极大；起笔多露锋，行笔迅疾，收笔带势如藤蔓。`impression` 草书取法米芾、怀素，淋漓而力沉，时有“青藤”之势（后人评语）。`impression` 禁笔：不用断笔的楷书结字，不用端正板滞的馆阁楷，不用迟缓的描红。`impression`

## (3) 结字与章法

- 结字倾欹破体，重心欹斜，字形大小参差极大；字与字牵丝连绵，行气起伏如藤蔓盘结。`impression` 章法行距忽疏忽密，留白随势而变。`impression` 幅式多为卷、轴，落款小字。`artifact`

## (4) 墨色与节奏

- 墨色湿而泼，一幅之内浓淡干湿变化极大；湿笔处墨色淋漓，干笔处见飞白。`impression` 节奏极快而顿挫分明：起笔迅疾，行笔连绵，收笔带势。`impression` 纸多用生纸，墨色渗透见力。`impression`

## (5) 书体与取法

- 书体以草书为主，兼擅行书；取法米芾、怀素，晚明狂草一路；其画亦以青藤著称，书画同法。`artifact` 演变：早年取法米芾较谨，中年淋漓已成，晚年更趋狂放。`impression`

## (6) 该写什么 / 不该写什么

- 该写：纵横倾欹的草书笔意、破体的欹侧结字、湿而泼的墨色、急促放逸的节奏、青藤盘结的行气。
- 不该写：断笔的楷书结字、端正板滞的馆阁楷、迟缓的描红、枯涩滞重的墨色、整齐划一的行距。
- Negative prompt: `No disconnected regular-script characters, no stiff official script, no slow tracing strokes, no dry dull ink, no uniform neat grid, no printed typeface`

## (7) 测试提示词示例（现代题材：“窗台上的一杯外卖咖啡”草书）

- Prompt: `In the style of Xu Wei, wild cursive calligraphy writing 'a takeaway coffee on the windowsill' in Chinese characters, drenching splashing strokes, tilted broken characters, wet ink, urgent unrestrained rhythm`
- 中文对照：徐渭风格：草书写一句“窗台上的一杯外卖咖啡”，纵横倾欹，墨湿而泼，节奏急促放逸。
- Negative: `No disconnected regular-script characters, no stiff official script, no slow tracing strokes, no dry dull ink, no uniform neat grid, no printed typeface`
- 检验点：笔法、结字、章法、墨色是否符合本条风格；是否出现第 6 节禁区里的写法。
