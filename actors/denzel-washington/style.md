# Denzel Washington — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Denzel Washington: commanding stillness with a preacher's cadence, a smile that can turn to steel, moral authority carried in the voice, a man who owns the room by standing still`
- ZH: 丹泽尔·华盛顿风格：布道者节奏的指挥性静止，微笑能转成钢铁，声音里的道德权威，一个站着不动就拥有全场的人。

## (2) 形体

- 站姿挺拔、肩膀放松；手势大而有节制，一抬手即是裁决；走路不慌不忙，压迫感来自静止。`impression`

## (3) 台词

- 音色浑厚、带布道者的节奏与停顿；语速平稳、重音落在关键词上；微笑时声音柔和，愤怒时反而压低。`impression`

## (4) 表情与眼神

- 表情克制，微笑与钢铁之间切换只在一瞬；眼神直视、不回避。`impression`

## (5) 角色类型

- 常演角色：历史领袖（马尔科姆·X）；正直的军人/警察（《光荣》特里普）；腐败的警探（《训练日》阿隆佐）。
- 类型突破：从《光荣》的逃亡奴隶到《马尔科姆·X》的历史领袖，再到《训练日》的腐败警探，表演由正直转向复杂；舞台《藩篱》是晚期高峰。`artifact`
- 禁演类型：几乎不演小丑式喜剧、不演自我贬低的角色、不演靠暴力解决问题的莽汉。`impression`

## (6) 该演什么 / 不该演什么

- 该演：指挥性的静止、布道者的节奏、微笑转钢铁的切换、浑厚的声音、直视的眼神。
- 不该演：小丑式喜剧、自我贬低的表演、靠音量取胜的咆哮、表情过载。
- Negative prompt: `No broad clowning, no self-degrading performance, no shouting to win a scene, no overacted expressions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Denzel Washington, a food delivery rider waits for an order on a rainy night, commanding stillness, a preacher's cadence, a smile that can turn to steel`
- 中文对照：丹泽尔·华盛顿风格：一位外卖骑手在雨夜等单，指挥性的静止，布道者的节奏，微笑能转成钢铁。
- Negative: `No broad clowning, no self-degrading performance, no shouting to win a scene, no overacted expressions`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
