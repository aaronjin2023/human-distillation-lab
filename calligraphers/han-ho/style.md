# Han Ho — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Han Ho, running-cursive Korean-Chinese characters, tall slender forms, crisp turns, generous line spacing, clear moist ink on paper`
- ZH: 韩濩风格：石峰体：行草并用，笔势挺拔，转折爽利，中锋与侧锋交替，劲健而不狂怪；结字疏朗，行距宽绰，字形修长，行气一贯而下。

## (2) 笔法

- 用笔：石峰体：行草并用，笔势挺拔，转折爽利，中锋与侧锋交替，劲健而不狂怪。`artifact`
- 禁笔：不用挺拔简健、不用缠绕繁复以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：结字疏朗，行距宽绰，字形修长，行气一贯而下。`artifact`
- 章法：结字疏朗，行距宽绰，字形修长，行气一贯而下。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：墨色清润，浓淡适中，枯笔少见，以挺拔取胜。`artifact`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：行书、草书；号石峰，取法二王与宋人，成朝鲜代表性书体之一。`artifact`
- 取法与演变：中期确立石峰体；晚期笔势更趋简健。`impression`

## (6) 该写什么 / 不该写什么

- 该写：石峰体行草诗卷, 明使求书的朝鲜行书范式（后世著录）, 诗文书卷的连续行气；主导：行书、草书；号石峰，取法二王与宋人，成朝鲜代表性书体之一；石峰体：行草并用，笔势挺拔，转折爽利，中锋与侧锋交替，劲健而不狂怪；墨色清润，浓淡适中，枯笔少见，以挺拔取胜。
- 不该写：wild cursive tangling, no heavy wet ink blots, no cramped layout, no printed typeface, no seal-script grid。
- Negative prompt: `No wild cursive tangling, no heavy wet ink blots, no cramped layout, no printed typeface, no seal-script grid`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Han Ho, running-cursive Korean-Chinese characters, tall slender forms, crisp turns, generous line spacing, clear moist ink on paper`
- 中文对照：韩濩风格：行草汉字，字形修长挺拔，转折爽利，行距宽绰，墨色清润。
- Negative: `No wild cursive tangling, no heavy wet ink blots, no cramped layout, no printed typeface, no seal-script grid`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
