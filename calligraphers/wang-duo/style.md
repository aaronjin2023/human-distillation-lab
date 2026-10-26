# 王铎 — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Duo: running and cursive script, swelling ink, learning from the Two Wangs, Mi Fu, Zhang Xu and Huaisu, strokes continuous and surging, characters large and tilted, ink thick then dry in waves`
- ZH: 王铎风格：行草涨墨，取法二王、米芾、张旭、怀素，笔画连绵涌动，字大欹侧，墨由浓转枯如涨潮。

## (2) 笔法

- 用笔连绵涌动，中锋与侧锋交替，提按幅度大；起笔多露锋，行笔迅疾，收笔带势。`impression` 草书取法张旭、怀素，行书取法二王、米芾，涨墨一路。`impression` 禁笔：不用断笔的楷书结字，不用端正板滞的馆阁楷，不用迟缓的描红。`impression`

## (3) 结字与章法

- 结字大而欹侧，重心欹斜，字形大小参差极大；字与字牵丝连绵，行气起伏如涨潮。`impression` 章法行距忽疏忽密，行气纵横，留白随势而变；大字轴尤见涨墨之势。`impression` 幅式多为轴、卷，落款小字。`artifact`

## (4) 墨色与节奏

- 墨色涨墨：一幅之内墨由浓转枯再转浓，如涨潮起伏，是其最稳定的标志。`impression` 节奏极快而顿挫分明：起笔迅疾，行笔连绵，收笔带势。`impression` 纸多用生纸，墨色渗透见涨墨。`impression`

## (5) 书体与取法

- 书体以行书、草书为主；取法二王、米芾、张旭、怀素，晚明涨墨一路；与倪元璐、黄道周、张瑞图并称晚明四家而最善涨墨。`artifact` 演变：早年取法二王较谨，中年涨墨已成，晚年更趋纵横。`impression`

## (6) 该写什么 / 不该写什么

- 该写：连绵涌动的草书笔意、大而欹侧的结字、涨墨的墨色起伏、迅疾放逸的节奏、取法二王、米芾、张旭、怀素的集古一路。
- 不该写：断笔的楷书结字、端正板滞的馆阁楷、迟缓的描红、均匀温润的墨色、整齐划一的行距。
- Negative prompt: `No disconnected regular-script characters, no stiff official script, no slow tracing strokes, no even warm ink, no uniform neat grid, no printed typeface`

## (7) 测试提示词示例（现代题材：“清晨地铁站台薄雾”行草）

- Prompt: `In the style of Wang Duo, running-cursive calligraphy writing 'morning mist over the subway platform' in Chinese characters, continuous surging strokes, large tilted characters, swelling ink thick then dry in waves`
- 中文对照：王铎风格：行草写一句“清晨地铁站台薄雾”，连绵涌动，字大欹侧，涨墨如潮。
- Negative: `No disconnected regular-script characters, no stiff official script, no slow tracing strokes, no even warm ink, no uniform neat grid, no printed typeface`
- 检验点：笔法、结字、章法、墨色是否符合本条风格；是否出现第 6 节禁区里的写法。
