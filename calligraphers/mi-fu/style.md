# 米芾 — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mi Fu: running script, brush-written with side brush, eight sides of the brush tip, characters tilted dangerously yet balanced, strokes fast and sweeping, ink wet and lively`
- ZH: 米芾风格：行书刷字，八面出锋，欹侧险绝，行笔迅疾，墨润而活。

## (2) 笔法

- 用笔以“刷字”为本：侧锋取势，八面出锋，笔锋翻转多变；起笔多露锋，行笔迅疾，收笔带出锋芒。`impression` 笔法善用中侧锋转换，一笔之中见提按翻转。`impression` 禁笔：不用迟缓描红式的中锋描摹，不用端正板滞的馆阁楷。`impression`

## (3) 结字与章法

- 结字欹侧险绝，重心欹斜而能稳住，字形大小参差极大；字与字之间牵丝映带，呼应紧密。`verbatim` 章法行距忽疏忽密，行气欹侧起伏，如“风樯阵马”（后人评语）。`impression` 幅式多为长卷与信札，落款小字，钤印一二方。`artifact`

## (4) 墨色与节奏

- 墨色润而不滞，浓淡变化随行笔速度起伏；湿笔处墨色饱满，干笔处见飞白。`verbatim` 节奏极快：起笔迅疾，行笔连绵，收笔带势，一气呵成；慢处只在字势转折。`impression` 纸多用蜀素等绢与熟纸，墨色附着见锋。`impression`

## (5) 书体与取法

- 书体以行书为主；集古字，取法二王、颜真卿、褚遂良、沈传师，自称“集古字”。`artifact` 演变：早年临古较谨，中年刷字之势成形，晚年行书更沉着，欹侧中见稳。`impression`

## (6) 该写什么 / 不该写什么

- 该写：刷字、八面出锋的侧锋笔法、欹侧险绝而能稳住的结字、字大小极悬殊的参差、牵丝映带的紧密呼应、湿润活泼的墨色。
- 不该写：端正板滞的馆阁楷、迟缓的描红式中锋、整齐划一的行距、枯涩滞重的墨色、断笔的楷书结字。
- Negative prompt: `No upright stiff official script, no slow tracing strokes, no uniform neat grid, no dry dull ink, no disconnected regular-script characters, no printed typeface`

## (7) 测试提示词示例（现代题材：“约克夏犬坐在地铁座位上”行书）

- Prompt: `In the style of Mi Fu, running script calligraphy writing 'a Yorkshire terrier sitting on a subway seat' in Chinese characters on silk, brush-written side-brush strokes, tilted dangerous characters, fast sweeping rhythm, wet lively ink`
- 中文对照：米芾风格：写一句“约克夏犬坐在地铁座位上”，刷字八面出锋，欹侧险绝，行笔迅疾，墨润而活。
- Negative: `No upright stiff official script, no slow tracing strokes, no uniform neat grid, no dry dull ink, no disconnected regular-script characters, no printed typeface`
- 检验点：笔法、结字、章法、墨色是否符合本条风格；是否出现第 6 节禁区里的写法。
