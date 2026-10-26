# Billy Wilder — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Billy Wilder: perfect clockwork structure, cynical comedy with a cold heart, a voiceover that confesses too late, a twist that reframes everything, dialogue sharp enough to cut`
- ZH: 比利·怀尔德风格：钟表般精确的结构，冷心的愤世喜剧，迟到的忏悔旁白，一个翻转全部的转折，锋利到能割伤人的对白。

## (2) 结构：三幕 / 序列 / 节拍

- 结构即本体：三幕严丝合缝，每场只完成一件事，伏笔在第一幕埋下、第三幕回收。黑色电影多用倒叙与旁白开场（尸体先出现，故事再倒回去）；喜剧则以身份错位开场、追逐收束。时间跨度可长可短，但节拍永远准时——转折点落在该落的位置。

## (3) 对话

- 对白锋利、经济、机智：短句为主，双关与反讽密集，一句台词常常同时完成笑点与伏笔。旁白多为事后忏悔的口吻，人物在讲故事时才明白自己做了什么。动作描写极简，只写必要的走位与道具。

## (4) 人物弧光

- 主角多为聪明而贪心的小人物：保险推销员、编剧、乐手。弧光是堕落或觉醒——从占小便宜一步步走向无法回头，或在最后一刻悬崖勒马。对手是欲望本身，金钱、名声、爱情都是诱饵。

## (5) 类型套路与创新

- 黑色电影 / 讽刺喜剧 / 爱情喜剧。他遵守类型的全部套路，却在结尾处翻转它：喜剧以冷峻收束，黑色电影以一句玩笑收尾。创新在结构的精确——剧本像钟表，每颗齿轮都有用。禁套路：几乎不用煽情的救赎，不写直白的道德演讲。

## (6) 该写什么 / 不该写什么

- 该写：钟表般精确的三幕结构与伏笔回收、倒叙旁白：尸体先出现，故事再倒回去、锋利机智的对白，笑点与伏笔同一句、小人物的贪心与堕落。
- Negative prompt: `No sentimental redemption, no on-the-nose moral speech, no loose unstructured scenes, no unearned happy ending, no soft nostalgia`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Billy Wilder, a small Yorkshire terrier sits on a subway seat, and a voiceover confesses: it all started with a bowl of oden. Perfect clockwork structure, a twist in the last scene that reframes everything, dialogue sharp enough to cut. No sentimental redemption.`
- 中文对照：比利·怀尔德风格：一只约克夏犬坐在地铁座位上，旁白忏悔道：一切始于一碗关东煮。钟表般精确的结构，最后一场翻转全部，对白锋利到能割伤人。没有煽情的救赎。
- Negative: `No sentimental redemption, no on-the-nose moral speech, no loose unstructured scenes, no unearned happy ending, no soft nostalgia`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
