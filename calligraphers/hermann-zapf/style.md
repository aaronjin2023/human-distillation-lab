# Hermann Zapf — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hermann Zapf, Palatino calligraphy, elegant broad-nib letters, graceful thick-thin contrast, black ink on paper, Renaissance humanist feeling`
- ZH: 赫尔曼·察普夫风格：宽头笔与尖笔并用：帕拉丁诺取法文艺复兴书法，笔画优雅，粗细过渡自然；字母比例优雅，行款端正，字距均匀，留白适中。

## (2) 笔法

- 用笔：宽头笔与尖笔并用：帕拉丁诺取法文艺复兴书法，笔画优雅，粗细过渡自然。`artifact`
- 禁笔：不用优雅比例、不用粗率以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：字母比例优雅，行款端正，字距均匀，留白适中。`artifact`
- 章法：字母比例优雅，行款端正，字距均匀，留白适中。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：黑墨为主，印本黑白对比清晰。`artifact`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：字体设计与书法；帕拉丁诺与奥普蒂玛为20世纪代表字体。`artifact`
- 取法与演变：20世纪中叶：帕拉丁诺（1948）与奥普蒂玛（1952–1955）相继问世。`impression`

## (6) 该写什么 / 不该写什么

- 该写：帕拉丁诺体字母形制, 奥普蒂玛体字母形制, 手写体字帖示范；主导：字体设计与书法；帕拉丁诺与奥普蒂玛为20世纪代表字体；宽头笔与尖笔并用：帕拉丁诺取法文艺复兴书法，笔画优雅，粗细过渡自然；黑墨为主，印本黑白对比清晰。
- 不该写：crude geometric sans, no irregular handwriting, no Gothic blackletter, no decorative border, no uniform stroke width。
- Negative prompt: `No crude geometric sans, no irregular handwriting, no Gothic blackletter, no decorative border, no uniform stroke width`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Hermann Zapf, Palatino calligraphy, elegant broad-nib letters, graceful thick-thin contrast, black ink on paper, Renaissance humanist feeling`
- 中文对照：察普夫风格：帕拉丁诺体书法，宽头笔字母优雅，粗细过渡自然，黑墨纸面。
- Negative: `No crude geometric sans, no irregular handwriting, no Gothic blackletter, no decorative border, no uniform stroke width`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
