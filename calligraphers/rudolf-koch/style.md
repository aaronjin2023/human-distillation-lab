# Rudolf Koch — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rudolf Koch, German modern calligraphy, bold broad-nib letters, strong black-and-white contrast, black ink on paper, carved-letter feeling`
- ZH: 鲁道夫·科赫风格：宽头笔与刻刀并用：笔画粗壮有力，起收笔果断，字母结构如刀刻；字母粗壮端正，行款有力，字距紧凑，黑白对比强烈。

## (2) 笔法

- 用笔：宽头笔与刻刀并用：笔画粗壮有力，起收笔果断，字母结构如刀刻。`artifact`
- 禁笔：不用粗壮有力、不用纤弱秀媚以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：字母粗壮端正，行款有力，字距紧凑，黑白对比强烈。`artifact`
- 章法：字母粗壮端正，行款有力，字距紧凑，黑白对比强烈。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：黑墨为主，印本黑白对比强烈。`artifact`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：现代书法与字体设计；德意志工艺联盟一路，科赫体为代表。`artifact`
- 取法与演变：20世纪初德国：现代书法与字体设计并行。`impression`

## (6) 该写什么 / 不该写什么

- 该写：科赫体字母形制, 《书写之书》的示范, 宽头笔大字；主导：现代书法与字体设计；德意志工艺联盟一路，科赫体为代表；宽头笔与刻刀并用：笔画粗壮有力，起收笔果断，字母结构如刀刻；黑墨为主，印本黑白对比强烈。
- 不该写：thin delicate strokes, no pointed-pen flourishing, no irregular handwriting, no decorative border, no uniform stroke width。
- Negative prompt: `No thin delicate strokes, no pointed-pen flourishing, no irregular handwriting, no decorative border, no uniform stroke width`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Rudolf Koch, German modern calligraphy, bold broad-nib letters, strong black-and-white contrast, black ink on paper, carved-letter feeling`
- 中文对照：科赫风格：德国现代书法，宽头笔字母粗壮有力，黑白对比强烈，如刀刻。
- Negative: `No thin delicate strokes, no pointed-pen flourishing, no irregular handwriting, no decorative border, no uniform stroke width`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
