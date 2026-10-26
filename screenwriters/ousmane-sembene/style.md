# Ousmane Sembène — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ousmane Sembène: postcolonial satire with a straight face, ordinary people against the system, Wolof and French in the same sentence, dignity as resistance`
- ZH: 塞姆班风格：一本正经的后殖民讽刺，普通人对抗制度，沃洛夫语与法语在同一句里，尊严即抵抗。

## (2) 结构：三幕 / 序列 / 节拍

- 结构多为三幕式讽刺：《黑女孩》以女佣的日常为骨架，时间跨度数月；《汇票》以一张汇票的兑现为线索，层层受阻；《发干》以阳痿为隐喻，喜剧外壳、悲剧内核。场次中等，靠日常受阻推进。

## (3) 对话

- 对白简洁、口语化，沃洛夫语与法语并存；人物用客套话与沉默交锋，潜台词是殖民与阶级。动作描写细致（家务、等待、行走），对白与动作互相拆台。旁白极少。

## (4) 人物弧光

- 主角多为普通人：女佣、失业者、商人，弧光是尊严的坚守而非胜利；人物越反抗越被制度吞掉，结尾常是沉默的抵抗。人物关系以殖民者与被殖民者的对照为主。

## (5) 类型套路与创新

- 类型：讽刺 / 社会现实主义。遵守现实主义的耐心，打破‘非洲电影必是奇观’的成见：日常即政治。创新在把一张汇票、一次阳痿写成后殖民寓言，把尊严写成抵抗。

## (6) 该写什么 / 不该写什么

- 该写：后殖民讽刺、普通人对抗制度、沃洛夫语与法语并存、日常即政治、尊严作抵抗。
- 不该写：猎奇化的异国情调、直白说教、煽情收束、类型化反转、大团圆。
- Negative prompt: `No exotic spectacle, no direct preaching, no sentimental ending, no plot-twist gimmick, no happy ending`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ousmane Sembène, a woman buys oden at a convenience store late at night in Dakar. She has worked all day in a house that is not hers. The clerk speaks French; she answers in Wolof. Dignity is resistance.`
- 中文对照：塞姆班风格：一个女人在达喀尔深夜的便利店买关东煮。她在别人家里干了一整天活。店员说法语，她用沃洛夫语回答。尊严即抵抗。
- Negative: `No exotic spectacle, no direct preaching, no sentimental ending, no plot-twist gimmick, no happy ending`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
