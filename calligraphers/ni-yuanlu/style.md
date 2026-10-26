# 倪元璐 — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ni Yuanlu: running and cursive script, precipitous and angular, learning from Yan Zhenqing and Mi Fu, strokes square and sharp, characters tilted and abrupt, ink dry and forceful`
- ZH: 倪元璐风格：行草险绝方折，取法颜真卿、米芾，笔画方折锐利，结字欹侧突兀，墨枯而力沉。

## (2) 笔法

- 用笔方折锐利，中锋与侧锋交替，提按顿挫分明；起笔多露锋，收笔多作方折，不尚圆转。`impression` 笔法取法颜真卿、米芾，险绝而有骨。`impression` 禁笔：不用圆转流畅的中锋，不用温润秀媚的线条，不用连绵缠绕的狂草。`impression`

## (3) 结字与章法

- 结字欹侧突兀，重心欹斜，字形大小参差大，笔画伸展而棱角分明。`impression` 章法行距忽疏忽密，行气欹侧起伏，如崖壁突兀。`impression` 幅式多为卷、轴，落款小字。`artifact`

## (4) 墨色与节奏

- 墨色枯而力沉，一幅之内浓淡变化随方折起伏；枯笔多而力透纸背。`impression` 节奏顿挫分明：起笔突兀，行笔时快时顿，收笔方折。`impression` 纸多用生纸，墨色渗透见棱角。`impression`

## (5) 书体与取法

- 书体以行书、草书为主；取法颜真卿、米芾，晚明险绝一路；与王铎、黄道周、张瑞图并称晚明四家。`artifact` 演变：早年取法颜真卿较谨，中年险绝已成，晚年更趋方折。`impression`

## (6) 该写什么 / 不该写什么

- 该写：方折锐利的笔画、欹侧突兀的结字、枯而力沉的墨色、大小悬殊的参差、取法颜真卿、米芾的险绝气息。
- 不该写：圆转流畅的中锋、温润秀媚的线条、连绵缠绕的狂草、端正板滞的馆阁楷、均匀温润的墨色。
- Negative prompt: `No smooth rounded centre-brush, no soft elegant lines, no tangled wild cursive, no stiff official script, no even warm ink, no printed typeface`

## (7) 测试提示词示例（现代题材：“窗台上的一杯外卖咖啡”行草）

- Prompt: `In the style of Ni Yuanlu, running-cursive calligraphy writing 'a takeaway coffee on the windowsill' in Chinese characters, hard angular strokes, tilted abrupt characters, dry forceful ink`
- 中文对照：倪元璐风格：行草写一句“窗台上的一杯外卖咖啡”，方折锐利，结字欹侧突兀，墨枯力沉。
- Negative: `No smooth rounded centre-brush, no soft elegant lines, no tangled wild cursive, no stiff official script, no even warm ink, no printed typeface`
- 检验点：笔法、结字、章法、墨色是否符合本条风格；是否出现第 6 节禁区里的写法。
