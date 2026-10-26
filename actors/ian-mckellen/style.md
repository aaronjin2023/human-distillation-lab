# Ian McKellen — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ian McKellen: classical stage command, Shakespearean diction made natural, twinkling intelligence, a wizard's authority worn lightly`
- ZH: 伊恩·麦克莱恩风格：古典舞台的指挥力，莎剧吐字说得自然，闪烁的智慧，巫师的权威穿得轻盈。

## (2) 形体

- 舞台功底使全身皆可调度：站姿挺拔、手势大而有节制；甘道夫的法杖成为身体的延伸；坐姿端正、双手交叠。`impression`

## (3) 台词

- 吐字精确、带古典舞台的共鸣；语速平稳、重音落在关键词上；台词可庄重可俏皮，切换只在一瞬。`artifact`

## (4) 表情与眼神

- 眼神闪烁智慧、直视中带着俏皮；眉毛一挑即是转折；笑是温暖的、短暂的。`impression`

## (5) 角色类型

- 常演角色：莎剧人物（理查三世、李尔王、麦克白）；巫师/智者（甘道夫、万磁王）；传记人物（《上帝与怪物》惠尔）。
- 类型突破：从舞台莎剧到《指环王》甘道夫，表演由舞台的放大转向银幕的收束；《理查三世》将莎剧搬进 1930 年代法西斯语境是类型突破。`artifact`
- 禁演类型：几乎不演不做准备的即兴、不演靠音量取胜的咆哮。`impression`

## (6) 该演什么 / 不该演什么

- 该演：古典舞台的指挥力、自然的莎剧吐字、闪烁智慧的眼神、轻盈的权威、俏皮的切换。
- 不该演：不做准备的即兴、靠音量取胜的咆哮、表情过载、字正腔圆的僵硬舞台腔。
- Negative prompt: `No unprepared improvisation, no shouting to win a scene, no overacted expressions, no stiff stage declamation`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ian McKellen, a food delivery rider waits for an order on a rainy night, classical command, Shakespearean diction made natural, twinkling intelligence`
- 中文对照：伊恩·麦克莱恩风格：一位外卖骑手在雨夜等单，古典舞台的指挥力，莎剧吐字说得自然，闪烁的智慧。
- Negative: `No unprepared improvisation, no shouting to win a scene, no overacted expressions, no stiff stage declamation`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
