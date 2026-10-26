# Ibn al-Bawwab — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ibn al-Bawwab, naskh Quran manuscript, bold regular letters, straight parallel lines, black ink with restrained gold chapter headings on paper`
- ZH: 伊本·巴瓦卜风格：誊抄体：芦苇笔，笔画粗细均匀而有力，起收笔干净，字母挺拔；行距紧密而清晰，字行笔直平行，章法端正，金饰章首与经文分明。

## (2) 笔法

- 用笔：誊抄体：芦苇笔，笔画粗细均匀而有力，起收笔干净，字母挺拔。`verbatim`
- 禁笔：不用清晰可读、不用繁复装饰压过文字以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：行距紧密而清晰，字行笔直平行，章法端正，金饰章首与经文分明。`verbatim`
- 章法：行距紧密而清晰，字行笔直平行，章法端正，金饰章首与经文分明。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：黑墨为主，金饰与蓝白几何纹饰于章首与页边，墨色均匀沉稳。`verbatim`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：誊抄体；完善伊本·穆格莱比例体系，兼创雷哈尼、穆哈卡克一路。`artifact`
- 取法与演变：完善比例体系；1000–1001年抄本为其成熟期的代表。`impression`

## (6) 该写什么 / 不该写什么

- 该写：《古兰经》誊抄体整卷, 金饰章首与几何纹饰, 紧凑而清晰的行款；主导：誊抄体；完善伊本·穆格莱比例体系，兼创雷哈尼、穆哈卡克一路；誊抄体：芦苇笔，笔画粗细均匀而有力，起收笔干净，字母挺拔；黑墨为主，金饰与蓝白几何纹饰于章首与页边，墨色均匀沉稳。
- 不该写：Latin letters, no printed naskh typeface, no slanted irregular lines, no gaudy floral border, no uniform stroke width。
- Negative prompt: `No Latin letters, no printed naskh typeface, no slanted irregular lines, no gaudy floral border, no uniform stroke width`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ibn al-Bawwab, naskh Quran manuscript, bold regular letters, straight parallel lines, black ink with restrained gold chapter headings on paper`
- 中文对照：伊本·巴瓦卜风格：誊抄体《古兰经》抄本，字形挺拔规整，行款笔直，黑墨配少量金饰章首。
- Negative: `No Latin letters, no printed naskh typeface, no slanted irregular lines, no gaudy floral border, no uniform stroke width`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
