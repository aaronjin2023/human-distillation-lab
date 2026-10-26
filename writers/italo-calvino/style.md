# Italo Calvino — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Italo Calvino: lightness and exactitude, cities that are invisible, a reader addressed directly, stories that branch and fold, fable logic with mathematical clarity`
- ZH: 卡尔维诺风格：轻盈与精确，看不见的城市，直接对读者说话，分支又折叠的故事，寓言的逻辑、数学的清晰。

## (2) 句式与节奏

句长：以中短句为主，句法清晰、少从句嵌套；段落短，章节短，靠分支与折叠推进；《看不见的城市》以短篇的并置构成，节奏是‘一城—一议—下一城’的轻快切换。节奏：轻快、精确，不拖泥带水；《如果在冬夜，一个旅人》十个开头的故事各自中断，节奏靠‘开始—中断—再开始’的循环驱动。`verbatim`

## (3) 词汇与意象

词汇：意大利语日常词与哲理词（轻、精确、可见、不可见）并置；‘轻’（leggerezza）是核心词。意象群：城市（看不见的城市）、树（树上的男爵）、旅人（冬夜的旅人）、棋盘与地图、镜子；意象是寓言的零件，靠组合获得意义。禁词/禁意象：不用沉重的抒情，不用冗长的心理分析，不用直白的道德评判。`impression`/`artifact`

## (4) 叙事视角与结构

视角：第二人称（《如果在冬夜，一个旅人》直接称呼‘你’）、第三人称的寓言叙述、马可·波罗与忽必烈的对话体；视角切换是结构本身。结构：并置与分支（《看不见的城市》五十五座城市的并置）、中断与再开始（《冬夜》十个开头）、寓言的三段式；开头多为一个轻盈的设定（‘你即将开始读……’），结尾多为开放的收束。对话：对话是哲理的载体，马可·波罗与忽必烈的对话即全书。`verbatim`

## (5) 语气与距离

语气：轻盈、机智、带沉思的愉悦；与人物的距离是游戏式的——请读者一起玩结构游戏；与读者的距离是直接的——‘你’就是主角。幽默是清澈的，悲悯藏在轻盈之后。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：看不见的城市；直接对读者说话；分支又折叠的故事；寓言的逻辑、数学的清晰；轻盈与精确。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No heavy lyricism, no long psychological analysis, no direct moralising, no flat reportage, no plot-driven suspense`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Italo Calvino, a man buys oden at a convenience store late at night. You are about to begin reading this story. The store is a city, invisible. Lightness and exactitude. The story branches — one branch is the steam, one branch is the clerk, one branch is you. Fable logic with mathematical clarity.`
- 中文对照：卡尔维诺风格，一个人在深夜便利店买关东煮。你即将开始读这个故事；便利店是一座城市，看不见的；轻盈与精确；故事分支——一枝是蒸汽，一枝是店员，一枝是你；寓言的逻辑、数学的清晰。
- Negative: `heavy lyricism, long psychological analysis, direct moralising, flat reportage, plot-driven suspense`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
