# Cao Bá Quát — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Cao Bá Quát, Vietnamese running-cursive Chinese characters, flowing upright strokes, clear moist ink, graceful continuous rhythm`
- ZH: 高伯适风格：据后世叙述：行草流畅，笔势挺拔，取法中国行草一路；结字疏朗，行气连贯，字形大小参差。

## (2) 笔法

- 用笔：据后世叙述：行草流畅，笔势挺拔，取法中国行草一路。`artifact`
- 禁笔：不用行草流畅、不用板滞以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：结字疏朗，行气连贯，字形大小参差。`artifact`
- 章法：结字疏朗，行气连贯，字形大小参差。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：墨色清润，浓淡适中（后世叙述，无真迹可证）。`artifact`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：行书、草书；取法中国书法，越南文人书法代表。`artifact`
- 取法与演变：19世纪越南：以诗名世，书法名声后世叙述而成。`impression`

## (6) 该写什么 / 不该写什么

- 该写：行草诗卷（后世叙述）, 狱中书法的文学形象, 越南文人行草；主导：行书、草书；取法中国书法，越南文人书法代表；据后世叙述：行草流畅，笔势挺拔，取法中国行草一路；墨色清润，浓淡适中（后世叙述，无真迹可证）。
- 不该写：claimed autograph manuscript, no invented prison scroll, no rigid printed typeface, no cramped layout, no wild cursive tangling。
- Negative prompt: `No claimed autograph manuscript, no invented prison scroll, no rigid printed typeface, no cramped layout, no wild cursive tangling`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Cao Bá Quát, Vietnamese running-cursive Chinese characters, flowing upright strokes, clear moist ink, graceful continuous rhythm`
- 中文对照：高伯适风格：越南行草汉字，笔势流畅挺拔，墨色清润，行气连贯。
- Negative: `No claimed autograph manuscript, no invented prison scroll, no rigid printed typeface, no cramped layout, no wild cursive tangling`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
