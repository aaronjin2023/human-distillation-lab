# Tatar Tonga — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tatar Tonga, early Mongolian script manuscript, tall vertical connected letters in Uyghur style, flowing strokes, black ink on paper`
- ZH: 塔塔统阿风格：回鹘式蒙古文：字母竖写连绵，笔画流畅，起收笔尖锐，字形修长；竖行书写，字母上下连写，行距均匀，字形修长。

## (2) 笔法

- 用笔：回鹘式蒙古文：字母竖写连绵，笔画流畅，起收笔尖锐，字形修长。`artifact`
- 禁笔：不用竖写连绵、不用横写孤立以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：竖行书写，字母上下连写，行距均匀，字形修长。`artifact`
- 章法：竖行书写，字母上下连写，行距均匀，字形修长。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：墨色均匀，抄本黑白对比清晰。`artifact`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：蒙古文创制；以回鹘文改制蒙古文。`artifact`
- 取法与演变：13世纪初创制蒙古文；后世蒙古文书法以此为源。`impression`

## (6) 该写什么 / 不该写什么

- 该写：回鹘式蒙古文字母形制, 竖写连绵的行款, 蒙古文抄本范式；主导：蒙古文创制；以回鹘文改制蒙古文；回鹘式蒙古文：字母竖写连绵，笔画流畅，起收笔尖锐，字形修长；墨色均匀，抄本黑白对比清晰。
- 不该写：claimed autograph manuscript, no invented 13th-century scroll, no Latin letters, no printed typeface, no horizontal layout。
- Negative prompt: `No claimed autograph manuscript, no invented 13th-century scroll, no Latin letters, no printed typeface, no horizontal layout`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Tatar Tonga, early Mongolian script manuscript, tall vertical connected letters in Uyghur style, flowing strokes, black ink on paper`
- 中文对照：塔塔统阿风格：早期蒙古文抄本，回鹘式竖写连绵，字形修长，黑墨纸面。
- Negative: `No claimed autograph manuscript, no invented 13th-century scroll, no Latin letters, no printed typeface, no horizontal layout`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
