# Gustave Flaubert — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Flaubert: le mot juste, free indirect style perfected, boredom rendered in exquisite prose, the provincial as the universal, no authorial judgement spoken aloud`
- ZH: 福楼拜风格：恰如其分的词，自由间接体臻于完美，无聊以精美的散文写出，外省即普遍，作者的判断绝不明说。

## (2) 句式与节奏

- 句式：句长：长句绵延，节奏如音乐；自由间接引语让叙述与人物内心无缝切换；短句只用在收束的冷峻处。
- 节奏：节奏：缓慢而精确——一页可写一分钟，一章可写一年；高潮不在事件，在一句的转折。

## (3) 词汇与意象

- 词汇：词汇：恰如其分的词（le mot juste）、外省的日常词、庸俗词与诗意词并置；爱用反讽的委婉语。
- 意象：意象群：外省小镇、药房与帽子、马车与窗、舞会与债务、庸俗与梦想。
- 禁词/禁意象：禁词/禁意象：不写作者的直白判断，不用廉价的抒情，不写快节奏的情节。

## (4) 叙事视角与结构

- 视角：叙事视角：第三人称，自由间接引语是核心——叙述者的声音与人物的内心互相渗透，作者绝不现身评判。
- 结构：结构：三部式（外省—巴黎—外省），以人物的幻想与现实的落差为线；开头多为一个场景，结尾以冷峻的收束。

## (5) 语气与距离

- 语气：语气：冷峻、精确而悲悯；与人物的距离是审美的距离——爱语言，也厌人物。

## (6) 该写什么 / 不该写什么

- 该写：该写：恰如其分的词、自由间接体、外省的无聊、精确的描写。
- 不该写：不该写：作者直白判断、廉价抒情、快节奏情节。
- Negative prompt: `No authorial judgement spoken aloud, no cheap lyricism, no fast-paced plot, no loose prose`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Flaubert, a woman buys oden at a convenience store late at night. Le mot juste. Free indirect style. Boredom rendered in exquisite prose. No judgement spoken aloud.`
- 中文对照：福楼拜风格，一位女子深夜在便利店买关东煮。恰如其分的词，自由间接体，无聊以精美的散文写出，判断绝不明说。
- Negative: `authorial judgement spoken aloud, cheap lyricism, fast-paced plot, loose prose`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
