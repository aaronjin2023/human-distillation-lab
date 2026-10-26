# Hassan Massoudy — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hassan Massoudy, modern Arabic calligraphy writing a line of poetry, gestural reed-pen strokes, black and coloured ink, letters stretched and dancing, large empty space`
- ZH: 哈桑·马苏迪风格：芦苇笔与宽笔并用，笔势如手势，提按起伏大，墨色干湿对比强烈；字母解构重组，字形欹侧，行款自由，留白大胆，诗句与字形互文。

## (2) 笔法

- 用笔：芦苇笔与宽笔并用，笔势如手势，提按起伏大，墨色干湿对比强烈。`verbatim`
- 禁笔：不用手势与诗意、不用印刷体的均匀以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：字母解构重组，字形欹侧，行款自由，留白大胆，诗句与字形互文。`verbatim`
- 章法：字母解构重组，字形欹侧，行款自由，留白大胆，诗句与字形互文。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：黑墨为主，间用彩墨，干湿枯润并置，笔触如舞。`verbatim`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：现代阿拉伯书法；取法传统苏鲁斯与誊抄，融现代抽象表现。`artifact`
- 取法与演变：生于伊拉克，居巴黎；已发表著作与展览作品为蒸馏范围。`impression`

## (6) 该写什么 / 不该写什么

- 该写：诗句书法：字母随诗意变形, 手势书法：笔势如身体动作, 彩墨与黑墨并置；主导：现代阿拉伯书法；取法传统苏鲁斯与誊抄，融现代抽象表现；芦苇笔与宽笔并用，笔势如手势，提按起伏大，墨色干湿对比强烈；黑墨为主，间用彩墨，干湿枯润并置，笔触如舞。
- 不该写：Latin letters, no printed naskh typeface, no uniform stroke width, no tidy grid layout, no decorative floral border。
- Negative prompt: `No Latin letters, no printed naskh typeface, no uniform stroke width, no tidy grid layout, no decorative floral border`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Hassan Massoudy, modern Arabic calligraphy writing a line of poetry, gestural reed-pen strokes, black and coloured ink, letters stretched and dancing, large empty space`
- 中文对照：哈桑·马苏迪风格：现代阿拉伯书法写一行诗，手势笔触，黑彩墨并置，字母拉伸起舞，大幅留白。
- Negative: `No Latin letters, no printed naskh typeface, no uniform stroke width, no tidy grid layout, no decorative floral border`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
