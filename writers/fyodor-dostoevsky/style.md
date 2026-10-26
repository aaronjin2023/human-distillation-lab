# Fyodor Dostoevsky — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dostoevsky: polyphony, ideas in combat, the underground man, confession as interrogation, fever and ecstasy, no idea without a body`
- ZH: 陀思妥耶夫斯基风格：复调，思想的搏斗，地下室人，忏悔即审问，热病与狂喜，没有无肉身的思想。

## (2) 句式与节奏

- 句式：句长：长短交错——独白长句如热病，对话短促如审问；排比与反问密集；短句常为一句的收束。
- 节奏：节奏：热病的节奏——平静、突起、狂喜、崩溃；场景多为密室对话，一夜可写一章。

## (3) 词汇与意象

- 词汇：词汇：罪、罚、信仰、自由、苦难、地下室；爱用强烈的道德词与身体词。
- 意象：意象群：地下室、密室、斧头与血、十字架与圣像、彼得堡的雾与黄昏、大宗教法官。
- 禁词/禁意象：禁词/禁意象：不写冷静的克制，不用小世界的精确，不写温和的和解。

## (4) 叙事视角与结构

- 视角：叙事视角：复调——多声部并存，无一权威；叙述者时而现身、时而退后；人物的思想即是情节。
- 结构：结构：多线并行，密室对话为核；开头多为一个场景（犯罪、归来、审问），结尾以审判或忏悔收束。

## (5) 语气与距离

- 语气：语气：炽热、严厉而悲悯；与人物的距离极近（爱他们、审判他们），与读者的距离为零——直接质问。

## (6) 该写什么 / 不该写什么

- 该写：该写：复调、思想的搏斗、地下室人、忏悔即审问。
- 不该写：不该写：冷静克制、小世界精确、温和和解。
- Negative prompt: `No cold restraint, no small-world precision, no gentle reconciliation, no single authoritative voice`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Dostoevsky, a man buys oden at a convenience store late at night, and the purchase becomes an interrogation. Polyphony. Ideas in combat. Confession as interrogation. No single voice.`
- 中文对照：陀思妥耶夫斯基风格，一人深夜在便利店买关东煮，一次购物变成一场审问。复调，思想的搏斗，忏悔即审问，没有单一声音。
- Negative: `cold restraint, small-world precision, gentle reconciliation, single authoritative voice`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
