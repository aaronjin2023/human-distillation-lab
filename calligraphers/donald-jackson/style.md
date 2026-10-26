# Donald Jackson — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Donald Jackson, Saint John's Bible manuscript page, clear calligraphic letters, straight even lines, black ink with gold illumination on vellum`
- ZH: 唐纳德·杰克逊风格：鹅毛笔与宽头笔并用：笔画清晰有力，起收笔干净，字母结构严谨而富表现力；圣经抄本：行款笔直，字距均匀，彩绘插图与文字呼应，页边留白规整。

## (2) 笔法

- 用笔：鹅毛笔与宽头笔并用：笔画清晰有力，起收笔干净，字母结构严谨而富表现力。`verbatim`
- 禁笔：不用手抄的庄重、不用印刷体的冷漠以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：圣经抄本：行款笔直，字距均匀，彩绘插图与文字呼应，页边留白规整。`verbatim`
- 章法：圣经抄本：行款笔直，字距均匀，彩绘插图与文字呼应，页边留白规整。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：黑墨为主，金饰与彩绘并用，墨色均匀润泽。`verbatim`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：现代西方书法；王室抄写员出身，《圣约翰圣经》艺术总监。`artifact`
- 取法与演变：20世纪末至21世纪初：《圣约翰圣经》为当代手抄圣经的代表。`impression`

## (6) 该写什么 / 不该写什么

- 该写：《圣约翰圣经》的抄本页, 彩绘插图与文字的呼应, 王室文书的端正行款；主导：现代西方书法；王室抄写员出身，《圣约翰圣经》艺术总监；鹅毛笔与宽头笔并用：笔画清晰有力，起收笔干净，字母结构严谨而富表现力；黑墨为主，金饰与彩绘并用，墨色均匀润泽。
- 不该写：printed typeface, no irregular handwriting, no Gothic blackletter, no gaudy illumination covering the text, no uniform stroke width。
- Negative prompt: `No printed typeface, no irregular handwriting, no Gothic blackletter, no gaudy illumination covering the text, no uniform stroke width`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Donald Jackson, Saint John's Bible manuscript page, clear calligraphic letters, straight even lines, black ink with gold illumination on vellum`
- 中文对照：唐纳德·杰克逊风格：《圣约翰圣经》抄本页，字母清晰有力，行款笔直，黑墨配金饰彩绘，羊皮纸。
- Negative: `No printed typeface, no irregular handwriting, no Gothic blackletter, no gaudy illumination covering the text, no uniform stroke width`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
