# Ibn Muqla — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ibn Muqla, proportional Arabic calligraphy, reed pen, alif height measured in rhombic dots, geometric letter proportions, black ink on paper, no illumination`
- ZH: 伊本·穆格莱风格：按后世著录：以芦苇笔斜切笔尖，菱形墨点为度量单位，alif高以点数计；比例体系：字母高以alif为准，圆以alif高为直径；行距与字距按点数比例定。

## (2) 笔法

- 用笔：按后世著录：以芦苇笔斜切笔尖，菱形墨点为度量单位，alif高以点数计。`artifact`
- 禁笔：不用几何比例、不用随意的自由书写以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：比例体系：字母高以alif为准，圆以alif高为直径；行距与字距按点数比例定。`artifact`
- 章法：比例体系：字母高以alif为准，圆以alif高为直径；行距与字距按点数比例定。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：无真迹可考墨色；体系本身重比例与几何，不重墨色变化。`artifact`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：誊抄体（naskh）、苏鲁斯体（thuluth）等六体；创立al-khatt al-mansub（比例书法）。`artifact`
- 取法与演变：10世纪初在巴格达确立比例体系；其法经伊本·巴瓦卜完善后传世。`impression`

## (6) 该写什么 / 不该写什么

- 该写：比例体系：菱形点、alif、圆, 六体：库法、苏鲁斯、誊抄、穆哈卡克、雷哈尼、陶基, 后世伊本·巴瓦卜对体系的完善；主导：誊抄体（naskh）、苏鲁斯体（thuluth）等六体；创立al-khatt al-mansub（比例书法）；按后世著录：以芦苇笔斜切笔尖，菱形墨点为度量单位，alif高以点数计；无真迹可考墨色；体系本身重比例与几何，不重墨色变化。
- 不该写：claimed autograph manuscript, no invented Quran page, no Latin letters, no printed naskh typeface, no uniform stroke width, no decorative floral border。
- Negative prompt: `No claimed autograph manuscript, no invented Quran page, no Latin letters, no printed naskh typeface, no uniform stroke width, no decorative floral border`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ibn Muqla, proportional Arabic calligraphy, reed pen, alif height measured in rhombic dots, geometric letter proportions, black ink on paper, no illumination`
- 中文对照：伊本·穆格莱风格：比例阿拉伯书法，芦苇笔，alif高以菱形点计，字母按几何比例，黑墨纸面。
- Negative: `No claimed autograph manuscript, no invented Quran page, no Latin letters, no printed naskh typeface, no uniform stroke width, no decorative floral border`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
