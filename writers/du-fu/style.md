# Du Fu — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Du Fu: regulated verse of沉郁顿挫, history written in the body, every image carrying war and displacement, moral weight without preaching`
- ZH: 杜甫风格：沉郁顿挫的律诗，以身写史，物象皆载战乱与流离，道德重量而不说教。

## (2) 句式与节奏

- 律诗沉郁顿挫：对仗工稳而语气顿挫，句内多转折；古体则长篇铺叙、层层递进；节奏慢、重、稳，如负重而行。`impression`

## (3) 词汇与意象

- 词汇：词域：战乱（烽火、干戈）、流离（漂泊、孤舟）、茅屋、老病、百姓、朝廷；用字精严，一字有千钧；少用李白式夸张天体词。`impression`
- 意象：茅屋、烽火、孤舟、白头、秋风、战骨；意象群的核心是“破”与“存”——国破而山河在、屋破而歌不止。`impression`
- 禁词/禁意象：不用纵逸的夸张飞举、不用轻快的游仙、不写与现实无关的纯然美景、不作空洞的豪言。

## (4) 叙事视角与结构

- 视角：第一人称见证者：我是流离中的诗人，也是百姓中的一员；视角在个人与家国之间切换，不作超然旁观。`impression`
- 结构：律诗：起承转合工稳，尾联常由景转情、由己及人；长篇叙事：由一事铺开至家国，如《北征》由归家写至天下。`impression`
- 对话：抒情诗基本无对话；叙事诗中偶见问答与独白（如《石壕吏》吏与老妇的对答）。

## (5) 语气与距离

- 语气：沉郁、悲悯、克制；与百姓同情、与朝廷忧思；不狂放、不轻佻，痛而不绝望。`impression`（学界通说：诗圣、沉郁顿挫）

## (6) 该写什么 / 不该写什么

- 该写：律诗沉郁、战乱意象、茅屋孤舟、由己及人、克制的悲悯。
- 不该写：纵逸夸张、游仙轻快、纯然美景、空洞豪言。
- Negative prompt: `No soaring hyperbole, no light-hearted transcendence, no scenery detached from human suffering, no empty bravado`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Du Fu, a man buys oden at a convenience store late at night. Regulated, heavy lines; the steam recalls war-time smoke only by restraint; the night-shift worker and the man share one weariness. End by widening from one man to all who are awake.`
- 中文对照：杜甫风格：一个人在深夜便利店买关东煮。律诗式沉郁重句，热气只克制地令人想起烽烟，夜班店员与买者同有一种疲惫。结尾由一人推及所有醒着的人。
- Negative: `soaring hyperbole, light transcendence, detached scenery, empty bravado`
- 检验点：是否沉郁顿挫而非纵逸；意象是否载着现实重量；结尾是否由己及人。
