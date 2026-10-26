# Kim Jeong-hui — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kim Jeong-hui, archaic clerical-running script, dry-brush texture, awkward ancient character forms, strong light-dark ink contrast, sparse layout`
- ZH: 金正喜风格：秋史体：隶书取法汉碑而参以行意，笔法古拙，提按顿挫分明，枯笔与涩笔并用；结字欹侧古拙，疏密对比强烈，行距紧而字距松，题诗与画面呼应。

## (2) 笔法

- 用笔：秋史体：隶书取法汉碑而参以行意，笔法古拙，提按顿挫分明，枯笔与涩笔并用。`verbatim`
- 禁笔：不用古拙金石气、不用秀媚流滑以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：结字欹侧古拙，疏密对比强烈，行距紧而字距松，题诗与画面呼应。`verbatim`
- 章法：结字欹侧古拙，疏密对比强烈，行距紧而字距松，题诗与画面呼应。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：墨色浓淡并置，枯润对比明显，喜用渴笔取古意。`verbatim`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：隶书、行书；取法汉隶与金石，师法翁方纲一路，创秋史体。`artifact`
- 取法与演变：早年习二王；中年流放济州期间书风转古拙；晚年秋史体成熟。`impression`

## (6) 该写什么 / 不该写什么

- 该写：《岁寒图》题诗：松竹题字, 隶书与行书互参的古拙结字, 金石学取法的碑版字形；主导：隶书、行书；取法汉隶与金石，师法翁方纲一路，创秋史体；秋史体：隶书取法汉碑而参以行意，笔法古拙，提按顿挫分明，枯笔与涩笔并用；墨色浓淡并置，枯润对比明显，喜用渴笔取古意。
- 不该写：smooth pretty running script, no uniform wet ink, no rigid printed typeface, no crowded decorative layout, no seal-script stiffness。
- Negative prompt: `No smooth pretty running script, no uniform wet ink, no rigid printed typeface, no crowded decorative layout, no seal-script stiffness`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Kim Jeong-hui, archaic clerical-running script, dry-brush texture, awkward ancient character forms, strong light-dark ink contrast, sparse layout`
- 中文对照：金正喜风格：隶行相参，古拙结字，枯笔涩势，墨色浓淡对比，章法疏朗。
- Negative: `No smooth pretty running script, no uniform wet ink, no rigid printed typeface, no crowded decorative layout, no seal-script stiffness`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
