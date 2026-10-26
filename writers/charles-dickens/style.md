# Charles Dickens — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dickens: crowded London, caricature that tells the truth, dialogue as theatre, coincidence and revelation, sentiment and satire in one chapter, the city as character`
- ZH: 狄更斯风格：拥挤的伦敦，漫画式的人物却说真话，对话即戏剧，巧合与揭示，感伤与讽刺同章，城市即人物。

## (2) 句式与节奏

- 句式：句长：长短交错——描写段落长句绵延，对话短促如戏；排比与重复密集；短句常为一句的收束。
- 节奏：节奏：连载的节奏——每章一悬念，每节一高潮；场景切换快，人物出场如登台。

## (3) 词汇与意象

- 词汇：词汇：伦敦的街道与雾、职业与绰号、身体喜剧词；爱用夸张的形容词与绰号。
- 意象：意象群：伦敦的雾、泰晤士河、监狱与法庭、孤儿与遗嘱、雾都的街道、双城的断头台。
- 禁词/禁意象：禁词/禁意象：不写冷静的克制，不用小世界的精确，不写反讽的疏离。

## (4) 叙事视角与结构

- 视角：叙事视角：全知而热情的叙述者，时而直接对读者说话；第一人称（《远大前程》）则为回忆的口吻。
- 结构：结构：连载结构，多线并行，巧合与揭示为枢纽；开头多为一个场景或一句断言，结尾以和解或揭示收束。

## (5) 语气与距离

- 语气：语气：热情、感伤而讽刺；与人物的距离如导演——爱他们，也让他们受苦。

## (6) 该写什么 / 不该写什么

- 该写：该写：拥挤的伦敦、漫画人物、对话戏剧、巧合与揭示。
- 不该写：不该写：冷静克制、小世界精确、反讽疏离。
- Negative prompt: `No cold restraint, no small-world precision, no ironic detachment, no minimalism`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Dickens, a small Yorkshire terrier sits on a subway seat among a crowd of Londoners. Crowded dialogue. Caricature that tells the truth. The city as character.`
- 中文对照：狄更斯风格，一只小约克夏犬坐在地铁座位上，与一群伦敦人同行。拥挤的对话，漫画式的人物却说真话，城市即人物。
- Negative: `cold restraint, small-world precision, ironic detachment, minimalism`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
