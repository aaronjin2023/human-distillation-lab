# Anton Chekhov — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chekhov: the gun on the wall, subtext over text, people talking past each other, the cherry orchard sold offstage, laughter through tears, nothing happens and everything changes`
- ZH: 契诃夫风格：墙上的枪，潜台词重于台词，各说各话，樱桃园在幕后被卖掉，笑中带泪，什么都没发生，一切都变了。

## (2) 句式与节奏

- 句式：句长：对白短促而日常，潜台词在停顿里；描写段落长句绵延，细节极具体。
- 节奏：节奏：缓慢的日常节奏——一幕可写一下午，一部可写数年；高潮不在事件，在一句的停顿。

## (3) 词汇与意象

- 词汇：词汇：日常词（茶、樱桃、火车、莫斯科）、潜台词词、未说出口的词；爱用重复与停顿。
- 意象：意象群：樱桃园、莫斯科、三姊妹的窗、海鸥、墙上的枪、茶与黄昏。
- 禁词/禁意象：禁词/禁意象：不写宏大的情节，不用直白的说教，不写廉价的感伤。

## (4) 叙事视角与结构

- 视角：叙事视角：舞台视角——人物各说各话，真相在对话的缝隙中；叙述者不现身，不裁决。
- 结构：结构：四幕剧，以日常场景为核；开头多为一个场景（归来、等待），结尾以离别或沉默收束；短篇则以一次事件为核，结尾常为一句翻转。

## (5) 语气与距离

- 语气：语气：温和、克制而悲悯；与人物的距离如医生——爱他们，也看清他们。

## (6) 该写什么 / 不该写什么

- 该写：该写：墙上的枪、潜台词、各说各话、日常中的变化。
- 不该写：不该写：宏大情节、直白说教、廉价感伤。
- Negative prompt: `No grand plot, no direct preaching, no cheap sentiment, no melodrama`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Chekhov, a woman buys oden at a convenience store late at night. Short everyday dialogue. Subtext over text. People talking past each other. Nothing happens and everything changes.`
- 中文对照：契诃夫风格，一位女子深夜在便利店买关东煮。短促的日常对话，潜台词重于台词，各说各话，什么都没发生，一切都变了。
- Negative: `grand plot, direct preaching, cheap sentiment, melodrama`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
