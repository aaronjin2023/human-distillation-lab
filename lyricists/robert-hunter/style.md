# Robert Hunter — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Hunter: American folk-myth lyrics, river and road imagery, plain words with a storyteller's riddle, chorus as a Zen-like refrain`
- ZH: 罗伯特·亨特风格：美国民间神话般的歌词，河流与公路的意象，平实的字句带着说书人的谜语，副歌即一句禅意的叠句。

## (2) 意象

- 意象群：(1)河流与公路——河、路、卡车，行走即命运；(2)民间神话——圣徒、魔鬼、黄金，神话落到日常；(3)灰与光——灰发、阳光、涟漪，微光即希望。意象密度中等偏高，每句一两个意象，明喻与暗喻交错，用典中等（民间传说、圣经轻触即止）。禁意象：直白的煽情、都市的冷硬意象。

## (3) 韵律

- 押韵：句尾押韵工整，韵脚多为柔和的尾音；常以叠句与重复制造民谣感；换韵处即叙事转折处。音节与字数：每句字数中等，长短句交错，贴合 Grateful Dead 旋律的呼吸；重音即口语重音。

## (4) 句式与口语密度

- 句式：中句为主，长短交错；多用第一人称叙事与第二人称劝慰交错，设问偶见，排比常用。口语密度中等：民谣口语打底，神话书面语点睛；叙事体多，对话体少。

## (5) 情感弧线

- 情感弧线：起——一个画面进场（河、路）；转——神话与日常交错，谜语浮现；合——副歌收在禅意的叠句上，温和而不煽情。情感强度克制而深沉，与听众保持说书人的距离；结尾常收束在一个意象上。

## (6) 该写什么 / 不该写什么

- 该写：河流与公路意象、民间神话意象、说书人的谜语句式、禅意的叠句副歌、平实的叙事。
- 不该写：直白的煽情、都市的冷硬意象、解释性的议论、生硬的押韵。
- Negative prompt: `No blunt sentimentality, no cold urban imagery, no explanatory commentary, no forced rhyme, no grand slogans`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Robert Hunter, lyrics about a man buying oden at a convenience store late at night. River and road imagery, storyteller's riddle, chorus as a Zen-like refrain. No sentimentality.`
- 中文对照：罗伯特·亨特风格：美国民间神话般的歌词，河流与公路的意象，平实的字句带着说书人的谜语，副歌即一句禅意的叠句。以“一个人在深夜便利店买关东煮”为题写歌词，见英文提示词。
- Negative: `No blunt sentimentality, no cold urban imagery, no explanatory commentary, no forced rhyme, no grand slogans`
- 检验点：意象与韵律是否成立；句式与口语密度是否对；情感弧线是否按第 (5) 节走；禁区里的写法是否出现。
