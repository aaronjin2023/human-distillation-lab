# Huang Doudou — 舞蹈风格规格 style.md（给视频模型）

> 只描述舞蹈，不描述人生。引用演出录像时注明作品名。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Huang Doudou: Chinese dance with drunken swagger, drum beats in the feet, terracotta warriors standing still then bursting, night deep and lyrical, proud, sharp, no ballet line`
- ZH: 黄豆豆风格：中国舞带醉意与豪气，脚下踩着鼓点，秦俑先静止再爆发，夜深沉而抒情，骄傲、锋利，没有芭蕾线条。

## (2) 动作语汇

- 核心动作：醉鼓：舞者如醉酒般摇摆、旋转，脚下踩鼓点；秦俑：身体如兵马俑般静止、挺立，再突然爆发；夜深沉：京剧《夜深沉》的音乐驱动，动作抒情而锋利；鼓点：脚下动作卡在鼓点上，鼓点即心跳。`impression`
- 动作来源：动作从中国古典舞与民间舞里来，也从鼓点与秦俑的意象里来：先有鼓点与秦俑的形态，再有舞台化的整理。`impression`（中国舞蹈史通说）
- 身体部位偏好：以全身的摇摆与静止为主导，尤其躯干的摇摆与腿脚的鼓点；手臂张开、挥舞，作醉态手势；关节活动方式是摇摆、静止、爆发。

## (3) 身体线条与空间调度

- 身体线条：身体线条曲而硬：醉态的摇摆把线条打碎，秦俑的挺立把线条拉直；重心忽高忽低，腾空与贴地快速切换；对称与不对称快速交替。
- 空间调度：舞台满台使用，队形是鼓点的聚散；独舞占中心，群舞作鼓点的合唱；进出场如醉汉漫步，舞者摇摆走入。
- 视点：观众看正面全景为主，视线落点在摇摆与静止上；近景特写只在面部表情处停留，豪气靠摇摆传达。

## (4) 节奏与音乐关系

- 节奏：节奏多变：摇摆与静止交替，速度忽慢忽快；停顿在秦俑的静止处出现，随即被爆发打断。
- 与音乐的关系：音乐关系密切：鼓点与《夜深沉》是动作的骨架；动作跟音乐走，脚下卡在鼓点上。
- 速度感：速度感是多变的：时而缓慢、时而爆发，速度随摇摆与静止的切换而切换；慢只在静止处出现。

## (5) 情绪表达

- 情绪：情绪：骄傲、豪气、抒情；情绪靠摇摆的醉态与静止的挺立传达，不靠面部表情；豪气本身就是情绪。`impression`

## (6) 该编什么 / 不该编什么

- 该编：醉鼓摇摆、秦俑静止与爆发、鼓点驱动、夜深沉抒情、独舞的豪气、群舞的鼓点合唱。
- 不该编：不编芭蕾式足尖与轻盈跳跃、不编缓慢抒情的长线条独舞、不编无鼓点的抽象动作、不编冷峻克制的极简风格、不编煽情的悲情结尾。
- Negative prompt: `No ballet pointe work, no slow lyrical adagio, no drum-less abstract movement, no cold minimalist restraint, no sentimental tragic ending`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Huang Doudou, a person buys oden at a convenience store late at night, drunken swagger, drum beats in the feet, terracotta warriors standing still then bursting, night deep and lyrical, proud and sharp, no ballet line`
- 中文对照：黄豆豆风格：一个人在深夜便利店买关东煮，醉意与豪气，脚下踩着鼓点，秦俑先静止再爆发，夜深沉而抒情，骄傲、锋利，没有芭蕾线条。
- Negative: `No ballet pointe work, no slow lyrical adagio, no drum-less abstract movement, no cold minimalist restraint, no sentimental tragic ending`
- 检验点：摇摆是否如醉酒般真实而非表演；静止是否能镇住舞台；鼓点是否踩在脚下而非背景。
