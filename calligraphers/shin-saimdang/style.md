# Shin Saimdang — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shin Saimdang, cursive Chinese characters, clear flowing turns, slender elegant forms, light moist ink, graceful continuous rhythm`
- ZH: 申师任堂风格：草书：笔势流畅，转折圆转，提按轻重分明，兼有女性书家的清劲一路；结字清劲疏朗，行气连贯，字形大小参差而不失端正。

## (2) 笔法

- 用笔：草书：笔势流畅，转折圆转，提按轻重分明，兼有女性书家的清劲一路。`verbatim`
- 禁笔：不用清劲流畅、不用狂怪缠绕以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：结字清劲疏朗，行气连贯，字形大小参差而不失端正。`verbatim`
- 章法：结字清劲疏朗，行气连贯，字形大小参差而不失端正。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：墨色清润，浓淡适中，少枯笔，以清劲取胜。`verbatim`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：草书、行书；取法二王与晋人草书。`artifact`
- 取法与演变：一生书风以清劲流畅为主；个别卷归属待考。`impression`

## (6) 该写什么 / 不该写什么

- 该写：草书诗卷的连绵行气, 《草虫图》题诗：画与字的呼应, 行草相参的清劲结字；主导：草书、行书；取法二王与晋人草书；草书：笔势流畅，转折圆转，提按轻重分明，兼有女性书家的清劲一路；墨色清润，浓淡适中，少枯笔，以清劲取胜。
- 不该写：wild cursive tangling, no heavy blotted ink, no rigid printed typeface, no cramped layout。
- Negative prompt: `No wild cursive tangling, no heavy blotted ink, no rigid printed typeface, no cramped layout`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Shin Saimdang, cursive Chinese characters, clear flowing turns, slender elegant forms, light moist ink, graceful continuous rhythm`
- 中文对照：申师任堂风格：草书清劲流畅，圆转提按，字形清朗，墨色清润。
- Negative: `No wild cursive tangling, no heavy blotted ink, no rigid printed typeface, no cramped layout`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
