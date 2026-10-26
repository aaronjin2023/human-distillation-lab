# Alcuin — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alcuin, Carolingian minuscule manuscript page, clear rounded lowercase letters, straight even lines, black ink with red rubrication on parchment`
- ZH: 阿尔昆风格：鹅毛笔：笔画均匀清晰，起收笔干净，字母圆润，小写字母高低分明；行款笔直，字距均匀，字母大小一致，页边留白规整。

## (2) 笔法

- 用笔：鹅毛笔：笔画均匀清晰，起收笔干净，字母圆润，小写字母高低分明。`artifact`
- 禁笔：不用清晰可读、不用繁复装饰压过文字以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：行款笔直，字距均匀，字母大小一致，页边留白规整。`artifact`
- 章法：行款笔直，字距均匀，字母大小一致，页边留白规整。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：黑墨为主，间有红墨标题与金饰首字母。`artifact`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：加洛林小写体；主持图尔抄本改革，统一小写字母形制。`artifact`
- 取法与演变：8–9世纪法兰克：图尔工坊推广小写体，成为中世纪拉丁抄本标准。`impression`

## (6) 该写什么 / 不该写什么

- 该写：加洛林小写体字母形制, 圣经抄本的行款, 红墨标题与金饰首字母；主导：加洛林小写体；主持图尔抄本改革，统一小写字母形制；鹅毛笔：笔画均匀清晰，起收笔干净，字母圆润，小写字母高低分明；黑墨为主，间有红墨标题与金饰首字母。
- 不该写：Gothic blackletter, no italic slant, no irregular handwriting, no printed typeface, no gaudy illumination covering the text。
- Negative prompt: `No Gothic blackletter, no italic slant, no irregular handwriting, no printed typeface, no gaudy illumination covering the text`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Alcuin, Carolingian minuscule manuscript page, clear rounded lowercase letters, straight even lines, black ink with red rubrication on parchment`
- 中文对照：阿尔昆风格：加洛林小写体抄本页，字母圆润清晰，行款笔直，黑墨配红墨标题，羊皮纸。
- Negative: `No Gothic blackletter, no italic slant, no irregular handwriting, no printed typeface, no gaudy illumination covering the text`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
