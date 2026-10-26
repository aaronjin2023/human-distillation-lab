# Yaqut al-Musta'simi — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yaqut al-Musta'simi, naskh Quran manuscript, rounded full letterforms, slanted reed-pen cut, even spacing, black ink with restrained gold on paper`
- ZH: 雅库特·穆斯塔阿绥米风格：誊抄体：斜切芦苇笔取势，笔画圆润而有力，提按分明，首创斜切笔尖之法（后世著录）；字形圆润饱满，行距匀称，章法端正，字母比例承伊本·巴瓦卜而更趋圆融。

## (2) 笔法

- 用笔：誊抄体：斜切芦苇笔取势，笔画圆润而有力，提按分明，首创斜切笔尖之法（后世著录）。`verbatim`
- 禁笔：不用圆润饱满、不用尖刻生硬以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：字形圆润饱满，行距匀称，章法端正，字母比例承伊本·巴瓦卜而更趋圆融。`verbatim`
- 章法：字形圆润饱满，行距匀称，章法端正，字母比例承伊本·巴瓦卜而更趋圆融。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：墨色均匀而润泽，黑墨为主，间有金饰。`verbatim`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：誊抄体；系统化比例度量，完善六体规范。`artifact`
- 取法与演变：13世纪巴格达宫廷抄写；蒙古攻陷巴格达后仍坚持抄写（后世著录）。`impression`

## (6) 该写什么 / 不该写什么

- 该写：《古兰经》誊抄体抄本, 圆润饱满的字母形态, 斜切笔尖带来的笔画变化；主导：誊抄体；系统化比例度量，完善六体规范；誊抄体：斜切芦苇笔取势，笔画圆润而有力，提按分明，首创斜切笔尖之法（后世著录）；墨色均匀而润泽，黑墨为主，间有金饰。
- 不该写：Latin letters, no printed naskh typeface, no jagged irregular strokes, no gaudy floral border, no uniform stroke width。
- Negative prompt: `No Latin letters, no printed naskh typeface, no jagged irregular strokes, no gaudy floral border, no uniform stroke width`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Yaqut al-Musta'simi, naskh Quran manuscript, rounded full letterforms, slanted reed-pen cut, even spacing, black ink with restrained gold on paper`
- 中文对照：雅库特风格：誊抄体《古兰经》抄本，字母圆润饱满，斜切笔尖，行距匀称，黑墨配金饰。
- Negative: `No Latin letters, no printed naskh typeface, no jagged irregular strokes, no gaudy floral border, no uniform stroke width`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
