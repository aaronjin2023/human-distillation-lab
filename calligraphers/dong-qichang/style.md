# 董其昌 — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dong Qichang: running script, light ink seeking resonance, learning from the Two Wangs and Mi Fu, strokes gentle and flowing, characters neat yet airy, ink pale and elegant`
- ZH: 董其昌风格：行书淡墨取韵，取法二王、米芾，用笔温和流畅，结字端整而疏，墨淡而雅，南北宗论的书法实践。

## (2) 笔法

- 用笔温和流畅，中锋为主，提按和缓；起笔藏锋，收笔回锋，笔画淡而有致。`impression` 行书取法二王、米芾，淡墨取韵。`impression` 禁笔：不用浓墨滞重，不用方折硬朗的棱角，不用侧锋刷字的锋芒。`impression`

## (3) 结字与章法

- 结字端整而疏，重心居中，字形大小均匀而略有参差；疏密适中，留白较大。`impression` 章法行距疏朗，行气端直而淡雅，留白为韵。`impression` 幅式多为卷、册，落款小字，钤印讲究。`artifact`

## (4) 墨色与节奏

- 墨色淡而雅，一幅之内浓淡变化和缓，淡墨为主，少浓墨；笔画墨色清淡，如水墨晕染。`impression` 节奏中速平稳，起笔缓、行笔匀、收笔回，淡中见韵。`impression` 纸多用熟纸与绢，墨色附着清淡。`impression`

## (5) 书体与取法

- 书体以行书为主，兼擅楷、草；取法二王、米芾，淡墨取韵；南北宗论的提出者，书法实践与理论同体。`artifact` 演变：早年取法二王较谨，中年淡墨已成，晚年更趋淡雅疏朗。`impression`

## (6) 该写什么 / 不该写什么

- 该写：温和流畅的中锋用笔、端整而疏的结字、淡而雅的墨色、疏朗留白的章法、淡墨取韵的气息。
- 不该写：浓墨滞重、方折硬朗的棱角、侧锋刷字的锋芒、欹侧险绝的结字、拥挤的章法。
- Negative prompt: `No heavy dull ink, no hard square turns, no side-brush flourish, no tilted dangerous characters, no crowded layout, no printed typeface`

## (7) 测试提示词示例（现代题材：“清晨地铁站台薄雾”行书）

- Prompt: `In the style of Dong Qichang, running script calligraphy writing 'morning mist over the subway platform' in Chinese characters, gentle flowing strokes, neat airy characters, pale elegant ink, large empty space`
- 中文对照：董其昌风格：行书写一句“清晨地铁站台薄雾”，温和流畅，端整而疏，墨淡而雅，留白为韵。
- Negative: `No heavy dull ink, no hard square turns, no side-brush flourish, no tilted dangerous characters, no crowded layout, no printed typeface`
- 检验点：笔法、结字、章法、墨色是否符合本条风格；是否出现第 6 节禁区里的写法。
