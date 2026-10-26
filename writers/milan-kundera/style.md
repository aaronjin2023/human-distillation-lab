# Milan Kundera — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Milan Kundera: essayistic novel, lightness and weight, a philosophical digression that becomes the story, kitsch named and refused, a gesture that reveals a whole life, variations on a theme`
- ZH: 昆德拉风格：随笔式小说，轻与重，一段哲理离题变成了故事本身，‘媚俗’被点名、被拒绝，一个姿态揭示整个人生，同一主题的变奏。

## (2) 句式与节奏

句长：中长句为主，叙事与随笔离题交替——一段情节之后是一段哲理沉思，沉思之后情节以变奏回来；段落短，章节短，靠变奏推进。节奏：不快不慢，靠‘主题—变奏’的音乐结构推进；《生命中不能承受之轻》七章各自独立又互为变奏。`verbatim`

## (3) 词汇与意象

词汇：哲学术语（轻、重、媚俗、永恒轮回、姿态）与日常词（帽子、狗、身体、做爱）并置；‘轻’与‘重’是核心词对。意象群：帽子（萨比娜的礼帽）、狗（卡列宁）、姿态（一个手势揭示一生）、镜子与身体；意象是哲学的肉身。禁词/禁意象：不用抒情的升华，不用煽情的控诉，不用心理分析的术语。`impression`/`artifact`

## (4) 叙事视角与结构

视角：全知叙述者直接介入，边讲故事边议论（‘什么是媚俗？’），叙述者与读者直接对话；视角在人物之间滑动，同一事件在不同人物意识中呈现不同形状。结构：主题—变奏的音乐结构，章节各自独立又互为回声；开头多为一个姿态或一个哲理命题，结尾多为变奏的收束而非情节解决。对话：对话是哲理的载体，人物靠辩论暴露自己。`verbatim`

## (5) 语气与距离

语气：冷静、机智、带反讽的沉思；与人物的距离是审视的——请读者判断人物是否媚俗；与读者的距离是直接的——叙述者直接对读者说话。幽默是干冷的，悲悯藏在判断之后。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：轻与重的哲理命题；一个姿态揭示整个人生；媚俗的点名与拒绝；随笔离题变成故事本身；同一主题的变奏。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No lyrical uplift, no sentimental accusation, no psychological jargon, no plot-driven suspense, no closed happy ending`

## (7) 测试提示词示例（现代题材：一个外卖骑手在深夜送餐）

- Prompt: `In the style of Milan Kundera, a food delivery rider works late at night. An essayistic digression: what is lightness, what is weight, when a job becomes a gesture. Kitsch is named and refused. One gesture — the rider's hand on the door — reveals a whole life. Variations on a theme.`
- 中文对照：昆德拉风格，一个外卖骑手深夜送餐。一段随笔式离题：何谓轻，何谓重，当一份工作变成一个姿态；媚俗被点名、被拒绝；一个姿态——骑手的手落在门上——揭示整个人生；同一主题的变奏。
- Negative: `lyrical uplift, sentimental accusation, psychological jargon, plot-driven suspense, closed happy ending`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
