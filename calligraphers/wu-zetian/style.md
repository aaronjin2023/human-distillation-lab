# Wu Zetian — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wu Zetian: Tang running script and flying-white, bold and unrestrained, imperial scale with dry-brush breaks`
- ZH: 武则天风格：唐行书兼飞白，豪放不拘，碑版气度，枯笔间见。

## (2) 笔法

- 行书兼飞白：笔画豪放，提按分明；飞白处枯笔疾书，丝丝露白。`impression`（碑刻与著录通说）
- 禁笔：他几乎不用的笔法——纤弱秀媚、端正划一。

## (3) 结字与章法

- 结字开张，欹侧分明；章法行气豪放，行距疏朗，碑版气度。`impression`
- 幅式：碑刻竖列。

## (4) 墨色与节奏

- 拓本墨色浓黑，飞白处枯润对比；节奏豪放疾速，一气呵成处多。`impression`

## (5) 书体与取法

- 书体：行书、飞白。唐高宗时期的女皇书法；碑刻为武周时期的官方书风，取法二王而豪放。`impression`
- 演变：传世皆为碑刻，无分期；自书说存疑，见 conflicts。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 豪放不拘的行书
- 开张的结字
- 飞白枯笔
- 浓黑的拓本墨色
- 豪放疾速的节奏
- 不该写：
- 纤弱秀媚
- 端正划一
- 楷书的方折顿笔
- 缓慢从容
- 刻意装饰
- Negative prompt: `No slender delicate strokes, no uniform character size, no regular-script square turns, no slow calm rhythm, no deliberate ornament`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Wu Zetian, Tang running script and flying-white writing modern Tokyo subway station names on a stone stele, bold unrestrained characters, dry-brush breaks, imperial scale, black rubbing ink`
- 中文对照：武则天风格：以唐行书兼飞白刻现代东京地铁站名于碑，结字开张豪放，间见飞白枯笔。
- Negative: `No slender delicate strokes, no uniform character size, no regular-script square turns, no slow calm rhythm, no deliberate ornament`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
