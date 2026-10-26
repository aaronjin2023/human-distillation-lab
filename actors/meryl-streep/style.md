# Meryl Streep — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Meryl Streep: total accent and voice transformation, precise emotional calibration, intelligence in every glance, a character actress who disappears into the role`
- ZH: 梅丽尔·斯特里普风格：彻底的口音与声音改造，精确的情绪刻度，眼神里的智慧，一个消失进角色里的性格演员。

## (2) 形体

- 为角色改造形体与姿态（苏菲的蜷缩、撒切尔的挺直）；手势精确、每一下都有出处；动作随口音与身份切换。`artifact`

## (3) 台词

- 口音改造是核心：波兰口音、英国口音、丹麦口音皆可切换；音色随角色变，语速与停顿精确。`artifact`

## (4) 表情与眼神

- 表情精确到刻度：悲伤、愤怒、讥诮皆可微调；眼神智慧而直视；哭与笑都收着演。`impression`

## (5) 角色类型

- 常演角色：受困的母亲/妻子（乔安娜、苏菲）；历史人物（撒切尔、朱莉娅·查尔德）；喜剧与反派（《穿普拉达的女王》米兰达）。
- 类型突破：从《克莱默夫妇》的离婚母亲到《铁娘子》的撒切尔，表演由情感的精确转向历史人物的再造；晚年喜剧角色是类型突破。`artifact`
- 禁演类型：几乎不演不做口音准备的角色、不演依赖外貌的轻浮主角。`impression`

## (6) 该演什么 / 不该演什么

- 该演：口音与声音的改造、精确的情绪刻度、智慧直视的眼神、为角色改造的形体、收着演的哭与笑。
- 不该演：不做准备的即兴、依赖外貌的轻浮主角、表情过载、靠音量取胜的咆哮。
- Negative prompt: `No unprepared improvisation, no pretty-face leads, no overacted expressions, no shouting to win a scene`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Meryl Streep, a woman buys oden at a convenience store late at night, total accent transformation, precise emotional calibration, intelligence in every glance`
- 中文对照：梅丽尔·斯特里普风格：一位女士深夜在便利店买关东煮，彻底的口音改造，精确的情绪刻度，眼神里的智慧。
- Negative: `No unprepared improvisation, no pretty-face leads, no overacted expressions, no shouting to win a scene`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
