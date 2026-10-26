# David Simon — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of David Simon: the system is the protagonist, institutions rot people slowly, no heroes, only corners and codes, journalism as drama`
- ZH: 西蒙风格：制度才是主角，机构慢慢腐蚀人，没有英雄，只有街角与规则，新闻即戏剧。

## (2) 结构：三幕 / 序列 / 节拍

- 结构为季弧多线并行、群像交织：《火线》每季一个机构（毒品、港口、政治、学校、媒体），五季拼成一座城市；单集多线并行，时间跨度一季，闪回极少，靠制度逻辑推进。

## (3) 对话

- 对白写实、密集，夹杂街头俚语、警局黑话与体制术语；人物用行话交锋，潜台词即生存规则。动作描写克制，对白密度高，场景提示少。独白不用，靠群像说话。

## (4) 人物弧光

- 主角是群像：警察、毒贩、教师、记者，弧光是制度的循环而非个人成长；人物越努力越被系统吞掉，结尾常是换人重演。人物关系以机构与街角的对照为主。

## (5) 类型套路与创新

- 类型：社会现实主义剧集。遵守纪实风格，打破‘破案必有真相’的套路：案子破不了，系统照常运转。创新在把新闻调查的方法写进剧本结构，每季即一篇长篇报道。

## (6) 该写什么 / 不该写什么

- 该写：制度作主角、群像多线并行、街头俚语与体制黑话、每季一个机构、循环而非成长的弧光。
- 不该写：个人英雄主义、煽情收束、直白说教、类型化破案桥段、全知旁白。
- Negative prompt: `No lone hero, no sentimental ending, no direct preaching, no procedural cliché, no omniscient narration`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of David Simon, a corner store clerk sells oden late at night while a detective watches from a car. Two systems pass each other and never meet. No case is solved. The city keeps going.`
- 中文对照：西蒙风格：一个街角店员深夜卖关东煮，侦探在车里看着。两个系统擦肩而过，永不相交。案子没破。城市照常运转。
- Negative: `No lone hero, no sentimental ending, no direct preaching, no procedural cliché, no omniscient narration`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
