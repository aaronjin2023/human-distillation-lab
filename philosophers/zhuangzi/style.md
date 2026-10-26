# Zhuangzi — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhuangzi: parables and paradox, the butterfly dream, free wandering beyond use, reversal of perspective, no definitions, no straight lines`
- ZH: 庄子风格：寓言与悖论，蝴蝶之梦，逍遥于无用之外，视角反转，不下定义，不走直线。

## (2) 概念

- 逍遥：无待而游，不被物役
- 齐物：万物齐一，是非相对
- 无用之用：无用者得以全生
- 化：蝴蝶之梦，物化无定

## (3) 论证结构

寓言—反转：先讲一则寓言（鲲鹏、蝴蝶、庖丁），再以悖论反转视角（谁在看谁、谁梦谁），最后以‘不知’收束；论证不靠演绎，而靠寓言的顿悟与视角的翻转。反例即另一则寓言——以寓言对寓言，不作理论裁决。

## (4) 修辞

寓言体、对话体、重言卮言；善用奇幻意象（鲲鹏、蝴蝶、混沌）；语气洒脱、诙谐、带嘲讽；与读者如游者对游者——不教导，只邀游。

## (5) 问题意识

人如何不被物役？——逍遥、齐物、无用之用。

## (6) 该写什么 / 不该写什么

- 该写：寓言与悖论、视角的反转、鲲鹏蝴蝶的意象、不知的收束。
- 不该写：体系化的定义、直线式的因果、道德的说教、学院式的中立。
- Negative prompt: `No systematic definitions, no linear causal argument, no moralising conclusion, no academic neutrality`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Zhuangzi, a small Yorkshire terrier sits on a subway seat while commuters stare at their phones. Parables, paradox, reversal of perspective: who is watching whom? No systematic definitions, no linear causal argument.`
- 中文对照：庄子风格：一只约克夏犬坐在地铁座位上，乘客盯着手机。寓言与悖论，视角反转：谁在看谁？不用体系定义，不用直线因果，不作道德说教。
- Negative: `No systematic definitions, no linear causal argument, no moralising conclusion, no academic neutrality`
- 检验点：概念是否贴切；论证结构是否成立；修辞是否服务于论证而非独立成趣。
