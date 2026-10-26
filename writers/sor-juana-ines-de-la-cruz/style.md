# Sor Juana Inés de la Cruz — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sor Juana Inés de la Cruz: Baroque wit, intricate sonnets and redondillas, learned allusion, paradox and self-defence, reason arguing with love`
- ZH: 索尔·胡安娜风格：巴洛克式的机智，精密的十四行诗与八音节诗，博学的典故，悖论与自辩，理性与爱情辩论。

## (2) 句式与节奏

- 格律严整，对仗工整；长句中典故密集；悖论句作收束。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：梦、迷宫、镜子、玫瑰、灵魂、理性；拉丁典故与神话意象密集。
- 意象：梦、迷宫、镜子、玫瑰、灵魂出窍；意象来自巴洛克传统。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：第一人称抒情与论辩；《答复》为书信体自辩。
- 结构：十四行诗与长诗并行；《第一梦》以灵魂夜游为结构；戏剧用迷宫式情节。
- 对话：诗中以呼告与辩论代对话；剧作对白巴洛克式华丽，独白多为哲理咏叹。

## (5) 语气与距离

- 机智、庄重；既抒情又论辩。

## (6) 该写什么 / 不该写什么

- 该写：第一梦（灵魂夜游、求知不得）、迷宫（爱情与命运的迷宫）、镜子与玫瑰（美与虚幻）、理性与爱情（终身的辩题）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No plain speech, no formlessness, no sentimental confession, no loose structure`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Sor Juana, a letter to yourself ten years from now. Baroque wit. A sonnet's discipline. Paradox and self-defence. Reason arguing with love.`
- 中文对照：索尔·胡安娜风格，一封写给十年后自己的信。巴洛克式的机智。十四行诗的格律。悖论与自辩。理性与爱情辩论。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
