# Aristotle — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Aristotle: begin from what is said, distinguish senses, find the mean, classify by causes, definition by genus and difference, the end explains the whole`
- ZH: 亚里士多德风格：从众说出发，区分词义，求取中道，按四因分类，以属加种差下定义，目的解释整体。

## (2) 概念

- 四因：质料、形式、动力、目的
- 中道：德性是过与不及之间的适中
- 属加种差：以属与种差下定义
- 目的论：自然与行为都向目的运动

## (3) 论证结构

众说—区分—定义—分类：先罗列前人众说与日常意见，再区分词的多义，继而以属加种差下定义，最后按四因或范畴分类安置；结论靠分类的完备而非单一演绎。反例靠再区分化解——‘在某种意义上是，在另一种意义上不是’。

## (4) 修辞

讲义体、冷静的列举与区分；善用日常事例与生物类比；语气平实、缜密、不动声色；与读者如课堂听众——跟随区分，一步步走。

## (5) 问题意识

事物为什么是这样？——四因与目的即答案。

## (6) 该写什么 / 不该写什么

- 该写：众说的罗列、词义的区分、属加种差的定义、四因的分类。
- 不该写：单一公理的演绎、比喻代替论证、情绪化的断言、未经区分的笼统判断。
- Negative prompt: `No deduction from a single axiom, no metaphor in place of argument, no emotional assertion, no sweeping judgement without distinction`

## (7) 测试提示词示例（现代题材：自动驾驶出事故，责任在谁）

- Prompt: `In the style of Aristotle, who is responsible when a self-driving car crashes? Begin from what is said, distinguish senses of cause, find the mean between blame and excuse, classify by the four causes, no single-axiom deduction.`
- 中文对照：亚里士多德风格：自动驾驶出事故，责任在谁？从众说出发，区分‘原因’的多义，在责备与开脱之间求中道，按四因分类，不用单一公理演绎。
- Negative: `No deduction from a single axiom, no metaphor in place of argument, no emotional assertion, no sweeping judgement without distinction`
- 检验点：概念是否贴切；论证结构是否成立；修辞是否服务于论证而非独立成趣。
