# Xunzi — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xunzi: human nature is evil, ritual as artifice that makes good, learning accumulates like earth, the gentleman formed not born, names must be rectified`
- ZH: 荀子风格：性恶，礼为化性起伪之术，学如积土，君子成于学而非生，正名。

## (2) 概念

- 性恶：人性本恶，善者伪也
- 礼：化性起伪的人为之术
- 积：学如积土、积水，积善成德
- 正名：名实相符，名正则言顺

## (3) 论证结构

立恶—化伪：先立性恶之本（人生而有欲），再以礼义化性起伪；论证靠类比（木受绳则直、金就砺则利）与分类（天与人的分工）。反例靠再定义化解——善不是性，是伪（人为）的成就。

## (4) 修辞

论说文体、长句铺陈；善用类比与排比；语气冷峻、缜密、带批判；与读者如师者对学者——不煽情，只讲理。

## (5) 问题意识

人性本恶，善从何来？——礼义化性，学而后成。

## (6) 该写什么 / 不该写什么

- 该写：性恶的立论、礼义化性的论证、积学的比喻、正名的要求。
- 不该写：性善的断言、天命的诉诸、无为的放任、脱离礼的空谈。
- Negative prompt: `No assertion that human nature is good, no appeal to fate or heaven's mandate, no laissez-faire non-action, no empty talk detached from ritual`

## (7) 测试提示词示例（现代题材：AI 写作会不会让人变懒）

- Prompt: `In the style of Xunzi, will AI writing make people lazy? Human nature is evil, ritual as artifice that makes good, learning accumulates like earth, names must be rectified, no appeal to fate, no system of ease.`
- 中文对照：荀子风格：AI 写作会不会让人变懒？性恶，礼为化性起伪之术，学如积土，正名，不诉诸天命，不谈无为放任。
- Negative: `No assertion that human nature is good, no appeal to fate or heaven's mandate, no laissez-faire non-action, no empty talk detached from ritual`
- 检验点：概念是否贴切；论证结构是否成立；修辞是否服务于论证而非独立成趣。
