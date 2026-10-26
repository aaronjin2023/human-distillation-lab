# Jane Austen — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jane Austen: free indirect discourse, irony at a polite distance, dialogue as character, three or four families in a country village, the marriage plot as moral judgement`
- ZH: 简·奥斯汀风格：自由间接引语，礼貌距离下的反讽，对话即人物，乡间三四个家庭，婚恋情节即道德判断。

## (2) 句式与节奏

- 句式：句长：中长句为主，句式工整而克制；自由间接引语让叙述与人物内心无缝切换；短句只用在反讽的收束处。
- 节奏：节奏：舞会与散步的节奏——场景缓慢展开，对话层层推进；高潮不在事件，在一句对话的转折。

## (3) 词汇与意象

- 词汇：词汇：礼貌用语（propriety）、财产与收入、舞会与拜访、性格词（sensible、silly）；爱用反讽的委婉语。
- 意象：意象群：乡间别墅、舞会、散步、书信、马车、财产与继承、雨与感冒。
- 禁词/禁意象：禁词/禁意象：不写直白的抒情，不用宏大的历史背景，不写脱离对话的议论。

## (4) 叙事视角与结构

- 视角：叙事视角：第三人称限知，自由间接引语是核心——叙述者的声音与人物的内心互相渗透，读者须分辨谁在说话。
- 结构：结构：三幕式（误会—危机—和解），以婚恋为线索；开头多为一句断言或一个场景，结尾以婚姻收束但反讽犹存。

## (5) 语气与距离

- 语气：语气：温和、机智而锋利；与人物的距离是礼貌的反讽距离——爱他们，也笑他们。

## (6) 该写什么 / 不该写什么

- 该写：该写：自由间接引语、对话、舞会与拜访、财产与婚恋、礼貌的反讽。
- 不该写：不该写：直白抒情、宏大历史背景、脱离对话的议论。
- Negative prompt: `No direct lyricism, no grand historical backdrop, no off-dialogue moralising, no sentimental excess`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Jane Austen, a woman buys oden at a convenience store late at night. Free indirect discourse. Polite irony. Dialogue as character. A small social world in one shop.`
- 中文对照：简·奥斯汀风格，一位女子深夜在便利店买关东煮。自由间接引语，礼貌的反讽，对话即人物，一家小店即一个小社会。
- Negative: `direct lyricism, grand historical backdrop, off-dialogue moralising, sentimental excess`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
