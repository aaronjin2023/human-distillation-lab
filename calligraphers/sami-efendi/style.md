# Sami Efendi — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sami Efendi, Ottoman thuluth calligraphy, refined rounded letters, even spacing, black ink with restrained gold on paper`
- ZH: 萨米·埃芬迪风格：苏鲁斯体：笔画精致圆润，粗细过渡自然，承拉基姆而更趋精致；章法端正，字母呼应自然，疏密适中。

## (2) 笔法

- 用笔：苏鲁斯体：笔画精致圆润，粗细过渡自然，承拉基姆而更趋精致。`verbatim`
- 禁笔：不用精致圆润、不用粗率以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：章法端正，字母呼应自然，疏密适中。`verbatim`
- 章法：章法端正，字母呼应自然，疏密适中。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：黑墨均匀润泽，金饰点缀。`verbatim`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：苏鲁斯体、誊抄体；奥斯曼晚期代表书法家。`artifact`
- 取法与演变：19世纪至20世纪初：奥斯曼书法晚期代表。`impression`

## (6) 该写什么 / 不该写什么

- 该写：希利亚, 苏鲁斯体书法集, 晚期奥斯曼书法范式；主导：苏鲁斯体、誊抄体；奥斯曼晚期代表书法家；苏鲁斯体：笔画精致圆润，粗细过渡自然，承拉基姆而更趋精致；黑墨均匀润泽，金饰点缀。
- 不该写：Latin letters, no printed naskh typeface, no rough irregular strokes, no gaudy floral border, no cramped layout。
- Negative prompt: `No Latin letters, no printed naskh typeface, no rough irregular strokes, no gaudy floral border, no cramped layout`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Sami Efendi, Ottoman thuluth calligraphy, refined rounded letters, even spacing, black ink with restrained gold on paper`
- 中文对照：萨米·埃芬迪风格：奥斯曼苏鲁斯体，精致圆润，章法端正，黑墨配金。
- Negative: `No Latin letters, no printed naskh typeface, no rough irregular strokes, no gaudy floral border, no cramped layout`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
