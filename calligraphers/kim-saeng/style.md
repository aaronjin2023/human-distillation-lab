# Kim Saeng — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kim Saeng, running-cursive Chinese characters on paper, fluid rounded turns, varied character sizes, light and dark ink, in the manner of Wang Xizhi as transmitted through later Korean stone rubbings`
- ZH: 金生风格：据后世著录与集字碑：行草流畅，提按分明，笔势圆转，取法二王一路；集字碑字形大小参差，行气连贯；原作章法已不可复原，只能从集字推断结字。

## (2) 笔法

- 用笔：据后世著录与集字碑：行草流畅，提按分明，笔势圆转，取法二王一路。`artifact`
- 禁笔：不用二王行草的流畅圆转、不用生硬的碑刻方折以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：集字碑字形大小参差，行气连贯；原作章法已不可复原，只能从集字推断结字。`artifact`
- 章法：集字碑字形大小参差，行气连贯；原作章法已不可复原，只能从集字推断结字。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：刻石传本墨色已失，只能从拓本黑白与笔画粗细推断原墨的浓淡节奏。`artifact`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：行书、草书；取法王羲之；后世称其书体为金生体，为朝鲜书法奠基者之一。`artifact`
- 取法与演变：统一新罗时期活动；生前即负盛名；死后字迹散佚，仅以集字与著录传世。`impression`

## (6) 该写什么 / 不该写什么

- 该写：二王一路的行草结字（经集字碑保存）, 后世摹刻与集字：金生体作为范式被反复临摹, 碑刻集字本身成为传世载体；主导：行书、草书；取法王羲之；后世称其书体为金生体，为朝鲜书法奠基者之一；据后世著录与集字碑：行草流畅，提按分明，笔势圆转，取法二王一路；刻石传本墨色已失，只能从拓本黑白与笔画粗细推断原墨的浓淡节奏。
- 不该写：claimed autograph manuscript, no invented complete scroll, no rigid seal-script grid, no modern printed typeface, no decorative border。
- Negative prompt: `No claimed autograph manuscript, no invented complete scroll, no rigid seal-script grid, no modern printed typeface, no decorative border`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Kim Saeng, running-cursive Chinese characters on paper, fluid rounded turns, varied character sizes, light and dark ink, in the manner of Wang Xizhi as transmitted through later Korean stone rubbings`
- 中文对照：金生风格：行草汉字，圆转流畅，字形大小参差，墨色浓淡，如二王一路经朝鲜集字碑传世的样子。
- Negative: `No claimed autograph manuscript, no invented complete scroll, no rigid seal-script grid, no modern printed typeface, no decorative border`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
