# Cai Yong — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Cai Yong: Han clerical script, flat wide characters, crisp wave strokes, solemn stele rhythm, with flying-white dry brush`
- ZH: 蔡邕风格：汉隶扁阔、波磔分明、碑版庄重，兼飞白枯笔。

## (2) 笔法

- 隶书波磔：横画蚕头燕尾，一波三折；捺画舒展上挑。飞白则笔锋半枯，丝丝露白，见于后世著录。`artifact`
- 禁笔：他几乎不用的笔法——小篆的圆转匀线、楷书的方折顿笔。

## (3) 结字与章法

- 结字扁阔取势，横向舒展，重心平稳；左右结构开张，笔画疏朗不拥挤。`verbatim`（拓本可见）
- 幅式：碑刻竖列。

## (4) 墨色与节奏

- 碑刻拓本墨色浓黑，笔画厚实；飞白处枯润相间，节奏一波一顿，庄重缓慢。`artifact`

## (5) 书体与取法

- 书体：隶书、飞白。东汉隶书成熟期的代表；《熹平石经》为官方刊经，体式即汉隶正宗。后世钟繇楷法亦受汉隶影响。`impression`
- 演变：传世皆为碑刻，无早中晚期墨迹可分；飞白之说见后世著录，其发明权亦有争议，见 conflicts。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 汉隶扁阔结字，横向舒展
- 蚕头燕尾的波磔，一波三折
- 笔画疏朗、重心平稳的碑版章法
- 飞白枯笔，丝丝露白
- 浓黑厚实的拓本墨色
- 不该写：
- 小篆的圆转匀线
- 楷书的方折顿笔
- 行草的连绵欹侧
- 纤弱秀媚的笔意
- 浓艳的装饰
- Negative prompt: `No seal-script rounded curves, no regular-script square turns, no running or cursive connections, no slender delicate strokes, no ornate decoration`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Cai Yong, Han clerical script carving modern Tokyo subway station names on a stone stele, flat wide characters, crisp wave strokes, solemn spacing, black rubbing ink, a touch of flying-white dry brush`
- 中文对照：蔡邕风格：以汉隶刻现代东京地铁站名于碑，结字扁阔，波磔分明，行列庄重，拓本浓墨，间见飞白枯笔。
- Negative: `No seal-script rounded curves, no regular-script square turns, no running or cursive connections, no slender delicate strokes, no ornate decoration`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
