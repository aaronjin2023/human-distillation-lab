# José Rizal — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of José Rizal: reformist epic, a colony seen clearly, satire that names the friar and the official, love and nation in the same sentence, a farewell that becomes a hymn`
- ZH: 黎刹风格：改良主义史诗，一个殖民地被清晰地看见，点名修士与官员的讽刺，爱与祖国在同一句里，一封告别信变成一首赞歌。

## (2) 句式与节奏

句长：以中长句为主，句法清晰、细节堆积；段落长，一段可同时完成场景、社会讽刺与人物。节奏：缓慢、史诗，靠家族与社会的并置推进；《不要碰我》以克里斯托莫的归来为框架，靠一桩桩社会场景的并置推进。`impression`

## (3) 词汇与意象

词汇：西班牙语日常词、他加禄语词与殖民官僚词汇并置；‘祖国’‘修士’‘起义’是核心词。意象群：祖国（被爱着的祖国）、修士与教堂、监狱与刑场、河流与稻田、告别信；意象是历史的零件。禁词/禁意象：不用华丽的抒情，不用抽象的哲理议论，不用冷静的旁观。`impression`/`artifact`

## (4) 叙事视角与结构

视角：第三人称全知，叙述者直接介入，边讲故事边议论；视角在人物之间滑动，同一事件在不同人物意识中呈现不同形状。结构：归来的框架 + 社会场景的并置；开头多为一个归来的场景，结尾多为告别或死亡的收束。对话：对话是讽刺的载体，人物靠言语的夸张暴露自己。`impression`

## (5) 语气与距离

语气：庄重、讽刺、带见证的热情；与人物的距离是同情的凝视；与读者的距离是直接的——请读者作见证。悲悯多于反讽，证词多于抒情。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：一个殖民地被清晰地看见；点名修士与官员的讽刺；爱与祖国在同一句里；一封告别信变成一首赞歌。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No ornate lyricism, no abstract philosophising, no cool detachment, no flat reportage, no heroic rhetoric`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of José Rizal, a letter to oneself ten years from now. A colony seen clearly. Satire that names the official and the friar. Love and nation in the same sentence. A farewell that becomes a hymn.`
- 中文对照：黎刹风格，一封写给十年后自己的信。一个殖民地被清晰地看见；点名官员与修士的讽刺；爱与祖国在同一句里；一封告别信变成一首赞歌。
- Negative: `ornate lyricism, abstract philosophising, cool detachment, flat reportage, heroic rhetoric`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
