# Inoue Yuichi — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Inoue Yuichi, a single huge kanji for 'night' written with a broom brush on large Japanese paper, explosive ink, dry and wet contrast, the character filling the whole sheet, one seal`
- ZH: 井上有一风格：自制帚笔大幅运笔，全身发力，墨胶调和，枯润飞白并存，笔触如泼如扫；单字独占整幅，字形撑满纸面，欹侧夸张，重心偏向一侧而以大势收住。

## (2) 笔法

- 用笔：自制帚笔大幅运笔，全身发力，墨胶调和，枯润飞白并存，笔触如泼如扫。`verbatim`
- 禁笔：不用以一字撑满全幅、不用多字章法的装饰性平衡以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：单字独占整幅，字形撑满纸面，欹侧夸张，重心偏向一侧而以大势收住。`verbatim`
- 章法：单字独占整幅，字形撑满纸面，欹侧夸张，重心偏向一侧而以大势收住。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：浓墨为主，干湿并置，胶墨滞涩生涩质；留白即纸面本身，不另作背景。`verbatim`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：汉字一字书；取法传统书道后反其道而行之，1950年代末起专攻单字。`artifact`
- 取法与演变：早期习传统书道；1955–1956年转向无形抽象表现；1950年代末起单字实验，终身反复。`impression`

## (6) 该写什么 / 不该写什么

- 该写：单字反复书写：爱、愚、贫、花、鸟、风、梦, 同一字多稿变体，字形每次不同, 多字诗文与经文抄写（次要）；主导：汉字一字书；取法传统书道后反其道而行之，1950年代末起专攻单字；自制帚笔大幅运笔，全身发力，墨胶调和，枯润飞白并存，笔触如泼如扫；浓墨为主，干湿并置，胶墨滞涩生涩质；留白即纸面本身，不另作背景。
- 不该写：small regular script, no tidy multi-character column layout, no smooth uniform ink, no delicate fine lines, no printed typeface, no decorative border。
- Negative prompt: `No small regular script, no tidy multi-character column layout, no smooth uniform ink, no delicate fine lines, no printed typeface, no decorative border`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Inoue Yuichi, a single huge kanji for 'night' written with a broom brush on large Japanese paper, explosive ink, dry and wet contrast, the character filling the whole sheet, one seal`
- 中文对照：井上有一风格：以帚笔在大幅和纸上写一个巨大的“夜”字，墨色浓烈枯润对比，一字撑满全幅，一方印章。
- Negative: `No small regular script, no tidy multi-character column layout, no smooth uniform ink, no delicate fine lines, no printed typeface, no decorative border`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
