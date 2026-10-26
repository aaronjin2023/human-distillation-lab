# Miguel de Cervantes — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Cervantes: dialogue between dreamer and realist, irony that loves its target, stories within stories, the novel questioning itself, laughter with tears`
- ZH: 塞万提斯风格：梦想家与现实主义者的对话，爱着对象的反讽，故事套故事，小说自我质疑，笑中带泪。

## (2) 句式与节奏

- 句式：句长：长短交错——堂吉诃德的长篇大论（骑士小说腔）对照桑丘的短促谚语；对话是基本单位，叙述常被对话打断。
- 节奏：节奏：出游—受挫—对话—再出游的循环；每一循环都是一次希望的升起与破灭，节奏如潮汐。

## (3) 词汇与意象

- 词汇：词汇：骑士小说的华丽辞藻与农民谚语并置；瘦马、破甲、风车、客栈；爱用谚语，桑丘的谚语即是民间智慧的词库。
- 意象：意象群：风车与巨人、瘦马罗西南特、客栈与城堡、胡子与头盔、书与疯癫、路与归家。
- 禁词/禁意象：禁词/禁意象：不写单一的讽刺，不用现代心理学术语，不写廉价的英雄颂歌。

## (4) 叙事视角与结构

- 视角：叙事视角：多层叙述——作者、译者、阿拉伯史家西德·哈迈德·贝嫩黑利、手稿发现者，叙述的可靠性层层存疑；视角即是主题。
- 结构：结构：上下两部（1605、1615），第二部的人物读过第一部——小说自我指涉的先驱；插叙故事套住主线，故事套故事。

## (5) 语气与距离

- 语气：语气：温和而锋利的反讽，笑中带泪；爱堂吉诃德，也笑他；与读者的距离如旅伴，边走边议论。

## (6) 该写什么 / 不该写什么

- 该写：该写：对话、故事套故事、谚语、风车、小说的自我质疑。
- 不该写：不该写：单一讽刺、现代心理分析、廉价英雄颂歌。
- Negative prompt: `No one-sided satire, no modern psychological jargon, no cheap heroic praise`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Cervantes, a man buys oden at a convenience store late at night, convinced the steamer is a castle kitchen. Long speeches answered by short proverbs. Stories within stories. Laughter with tears.`
- 中文对照：塞万提斯风格，一人深夜在便利店买关东煮，坚信蒸锅是城堡的厨房。长篇大论对照短促谚语，故事套故事，笑中带泪。
- Negative: `one-sided satire, modern psychological jargon, cheap heroic praise`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
