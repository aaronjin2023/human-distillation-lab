# Giovanni Battista Palatino — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Giovanni Battista Palatino, Renaissance Roman capitals, well-proportioned upright letters, black ink on paper, dignified even layout`
- ZH: 乔瓦尼·巴蒂斯塔·帕拉蒂诺风格：鹅毛笔罗马体：笔画端正，粗细对比适中，起收笔干净，字母比例严谨；罗马大写字母比例严谨，行款端正，字距均匀。

## (2) 笔法

- 用笔：鹅毛笔罗马体：笔画端正，粗细对比适中，起收笔干净，字母比例严谨。`artifact`
- 禁笔：不用比例严谨、不用随意变形以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：罗马大写字母比例严谨，行款端正，字距均匀。`artifact`
- 章法：罗马大写字母比例严谨，行款端正，字距均匀。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：黑墨为主，印本黑白对比清晰。`artifact`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：罗马体；《新书法书》为文艺复兴罗马体字帖代表。`artifact`
- 取法与演变：16世纪中叶罗马：罗马体字帖范式。`impression`

## (6) 该写什么 / 不该写什么

- 该写：罗马大写字母形制, 《新书法书》的字母示范, 文艺复兴罗马体范式；主导：罗马体；《新书法书》为文艺复兴罗马体字帖代表；鹅毛笔罗马体：笔画端正，粗细对比适中，起收笔干净，字母比例严谨；黑墨为主，印本黑白对比清晰。
- 不该写：italic slant, no Gothic blackletter, no irregular handwriting, no printed roman typeface, no decorative border。
- Negative prompt: `No italic slant, no Gothic blackletter, no irregular handwriting, no printed roman typeface, no decorative border`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Giovanni Battista Palatino, Renaissance Roman capitals, well-proportioned upright letters, black ink on paper, dignified even layout`
- 中文对照：帕拉蒂诺风格：文艺复兴罗马体大写，比例严谨，行款端正，黑墨纸面。
- Negative: `No italic slant, no Gothic blackletter, no irregular handwriting, no printed roman typeface, no decorative border`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
