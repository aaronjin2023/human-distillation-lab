# Thonmi Sambhota — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Thonmi Sambhota, early Tibetan script manuscript, square upright letters derived from Indian Gupta script, straight even lines, black ink on paper`
- ZH: 吞弥·桑布扎风格：藏文书法：字母取法印度笈多体，笔画横平竖直，起收笔干净，字母结构方整；藏文字母横向排列，行款笔直，字距均匀，音节界限分明。

## (2) 笔法

- 用笔：藏文书法：字母取法印度笈多体，笔画横平竖直，起收笔干净，字母结构方整。`artifact`
- 禁笔：不用字母方整可读、不用繁复变形以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：藏文字母横向排列，行款笔直，字距均匀，音节界限分明。`artifact`
- 章法：藏文字母横向排列，行款笔直，字距均匀，音节界限分明。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：墨色均匀，抄本黑白对比清晰。`artifact`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：藏文创制；传说为藏文创造者，取法印度文字。`artifact`
- 取法与演变：传说7世纪创制藏文；文献记载晚至14世纪，创制说本身有争议。`impression`

## (6) 该写什么 / 不该写什么

- 该写：藏文字母形制, 《三十颂》的语法体系, 藏文抄本的行款；主导：藏文创制；传说为藏文创造者，取法印度文字；藏文书法：字母取法印度笈多体，笔画横平竖直，起收笔干净，字母结构方整；墨色均匀，抄本黑白对比清晰。
- 不该写：claimed autograph manuscript, no invented 7th-century scroll, no Latin letters, no printed typeface, no decorative border。
- Negative prompt: `No claimed autograph manuscript, no invented 7th-century scroll, no Latin letters, no printed typeface, no decorative border`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Thonmi Sambhota, early Tibetan script manuscript, square upright letters derived from Indian Gupta script, straight even lines, black ink on paper`
- 中文对照：吞弥·桑布扎风格：早期藏文抄本，字母方整如印度笈多体，行款笔直，黑墨纸面。
- Negative: `No claimed autograph manuscript, no invented 7th-century scroll, no Latin letters, no printed typeface, no decorative border`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
