# William Goldman — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Goldman: clean craftsman structure, genre reinvention from the inside, witty self-aware narration, the buddy movie as a love story, nobody knows anything`
- ZH: 威廉·戈德曼风格：干净利落的匠人结构，从内部革新类型，机智而自知的叙述，伙伴电影即爱情故事，无人知晓一切。

## (2) 结构：三幕 / 序列 / 节拍

- 匠人三幕，结构清晰到可以画图：第一幕立下伙伴与目标，第二幕让类型套路逐一出现又逐一翻转，第三幕以一次告别或一次真相收束。时间跨度可长可短，但节拍永远清楚——每场戏都知道自己是第几场。

## (3) 对话

- 对白干净、机智、自知：短句、俏皮话、旁白，人物偶尔跳出故事对观众说话。动作描写清晰、经济，只写必要的走位与道具。独白少，旁白是标志——叙述者与故事保持一臂之遥。

## (4) 人物弧光

- 主角多为一对伙伴：劫匪、记者、剑客。弧光是伙伴关系的考验——从并肩到分歧，再到和解或告别。对手是体制与时代，爱情藏在伙伴情谊里。

## (5) 类型套路与创新

- 西部片 / 惊悚片 / 奇幻喜剧 / 新闻片。他遵守每种类型的全部套路，却从内部革新它：《虎豹小霸王》把西部片写成伙伴爱情故事，《公主新娘》把童话写成自知的游戏。创新在类型自知——剧本知道自己是什么类型。禁套路：几乎不用含糊的抒情，不写结构松散的即兴。

## (6) 该写什么 / 不该写什么

- 该写：干净利落的匠人结构、类型自知与从内部革新、伙伴电影即爱情故事、机智自知的旁白。
- Negative prompt: `No loose improvisation, no vague lyricism, no muddy middle act, no humourless genre exercise, no unearned twist`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of William Goldman, a small Yorkshire terrier and a night-shift clerk become partners on a subway at night, chasing a bowl of oden that everyone wants. Clean craftsman structure, genre reinvention from the inside, witty self-aware narration. Nobody knows anything, and the dog knows it.`
- 中文对照：威廉·戈德曼风格：一只约克夏犬与一位夜班店员在深夜地铁上结成伙伴，追逐一碗人人想要的关东煮。干净利落的匠人结构，从内部革新类型，机智自知的旁白。无人知晓一切，狗知道这一点。
- Negative: `No loose improvisation, no vague lyricism, no muddy middle act, no humourless genre exercise, no unearned twist`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
