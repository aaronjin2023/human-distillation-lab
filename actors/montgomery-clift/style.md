# Montgomery Clift — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Montgomery Clift: fragile Method intensity, soft-spoken lines that tremble, a handsome face that refuses to harden, vulnerability as strength`
- ZH: 蒙哥马利·克利夫特风格：脆弱的方法派强度，轻声细语的台词带着颤抖，一张拒绝变硬的英俊面孔，脆弱即力量。

## (2) 形体

- 身体内收、肩膀微耸；动作轻而慢，爆发时反而收得更紧；站立时重心不稳、像随时会退后一步。`impression`

## (3) 台词

- 轻声细语、语速慢、尾音颤抖；台词常说到一半停住；愤怒时声音不升高、反而更轻。`impression`

## (4) 表情与眼神

- 眼神忧郁、直视中带着恳求；眉头微蹙、嘴唇紧抿；笑是克制的、短暂的。`impression`

## (5) 角色类型

- 常演角色：脆弱的底层青年（普鲁伊特）；被欲望与阶级撕扯的情人（《郎心如铁》）；受伤的军人/浪子。
- 类型突破：从《郎心如铁》的英俊情人到《从这里到永恒》的倔强士兵，表演由外在魅力转向内在脆弱；车祸后晚期表演更趋内敛。`artifact`
- 禁演类型：几乎不演硬汉、不演靠音量取胜的咆哮、不演讨好观众的英雄。`impression`

## (6) 该演什么 / 不该演什么

- 该演：轻声颤抖的台词、内收的形体、忧郁直视的眼神、收紧的爆发、脆弱的尊严。
- 不该演：硬汉式的咆哮、字正腔圆的舞台腔、讨好观众的英雄气、表情过载。
- Negative prompt: `No tough-guy shouting, no theatrical declamation, no crowd-pleasing heroics, no overacted expressions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Montgomery Clift, a small Yorkshire terrier sits on a subway seat, soft and trembling, fragile dignity, eyes that ask to be understood`
- 中文对照：蒙哥马利·克利夫特风格：一只约克夏犬坐在地铁座位上，轻声颤抖，脆弱的尊严，眼神恳求被理解。
- Negative: `No tough-guy shouting, no theatrical declamation, no crowd-pleasing heroics, no overacted expressions`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
