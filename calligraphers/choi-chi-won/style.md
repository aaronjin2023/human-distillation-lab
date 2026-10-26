# Choi Chi-won — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Choi Chi-won, running-script stele inscription characters, firm central-brush strokes, even spacing, dignified碑-style layout, black ink on stone rubbing texture`
- ZH: 崔致远风格：碑铭行书：中锋为主，提按清晰，笔画劲健，兼有唐人碑版的方整与行书的流动；碑额与碑文分行，字距均匀，行气端正，碑式章法重对称与满格。

## (2) 笔法

- 用笔：碑铭行书：中锋为主，提按清晰，笔画劲健，兼有唐人碑版的方整与行书的流动。`artifact`
- 禁笔：不用碑铭的端正可读、不用狂草的连绵难辨以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：碑额与碑文分行，字距均匀，行气端正，碑式章法重对称与满格。`artifact`
- 章法：碑额与碑文分行，字距均匀，行气端正，碑式章法重对称与满格。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：刻本墨色已失；拓本黑白对比强烈，笔画以刻工转译为准，不可等同墨迹。`artifact`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：行书、楷书碑铭；取法唐代碑版书法，在唐朝考中进士后归国。`artifact`
- 取法与演变：唐朝留学得名；归国后碑铭为主要传世书迹；卒年不详。`impression`

## (6) 该写什么 / 不该写什么

- 该写：禅师碑铭：碑文行书, 文集《桂苑笔耕集》所载文字, 唐风碑版的朝鲜化；主导：行书、楷书碑铭；取法唐代碑版书法，在唐朝考中进士后归国；碑铭行书：中锋为主，提按清晰，笔画劲健，兼有唐人碑版的方整与行书的流动；刻本墨色已失；拓本黑白对比强烈，笔画以刻工转译为准，不可等同墨迹。
- 不该写：wild cursive tangling, no tiny cramped columns, no dry-brush abstraction, no printed typeface, no invented autograph scroll。
- Negative prompt: `No wild cursive tangling, no tiny cramped columns, no dry-brush abstraction, no printed typeface, no invented autograph scroll`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Choi Chi-won, running-script stele inscription characters, firm central-brush strokes, even spacing, dignified碑-style layout, black ink on stone rubbing texture`
- 中文对照：崔致远风格：行书碑铭字，笔力劲健，字距均匀，碑式章法端正，如拓本黑白。
- Negative: `No wild cursive tangling, no tiny cramped columns, no dry-brush abstraction, no printed typeface, no invented autograph scroll`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
