# Sidney Poitier — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sidney Poitier: quiet dignity under pressure, stillness before the outburst, precise diction, moral clarity without preaching, a man who refuses to be diminished`
- ZH: 西德尼·波蒂埃风格：压力下的安静尊严，爆发前的静止，字正腔圆的台词，道德清晰而不说教，一个拒绝被贬低的人。

## (2) 形体

- 站姿挺拔、肩膀放松；动作幅度小而精确；愤怒时先静止三秒再行动；走路不慌不忙，压迫感来自静止而非动作。`impression`

## (3) 台词

- 音色温润、吐字清晰、带轻微加勒比口音；语速平稳、重音落在关键词上；愤怒的台词反而压低声音说。`impression`

## (4) 表情与眼神

- 表情克制，愤怒与悲伤都收在眼神里；直视对方、不回避；微笑克制而温暖。`impression`

## (5) 角色类型

- 常演角色：正直的专业人士（《炎热的夜晚》蒂布斯警探）；跨越种族界线的挑战者（《逃亡》《猜猜谁来吃晚餐》）；温和的导师/父亲形象。
- 类型突破：从《逃亡》的手铐囚犯到《炎热的夜晚》的警探，角色从被审视者变为审视者；晚年转向导演与公共角色。`artifact`
- 禁演类型：几乎不演小丑式喜剧、不演自我贬低的角色、不演靠暴力解决问题的莽汉。`impression`

## (6) 该演什么 / 不该演什么

- 该演：静止中的尊严、压低声音的愤怒、字正腔圆的台词、直视的眼神、克制的微笑。
- 不该演：夸张的肢体喜剧、自我贬低的表演、靠音量取胜的咆哮、煽情的独白。
- Negative prompt: `No broad physical comedy, no self-degrading performance, no shouting to win a scene, no sentimental monologue`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Sidney Poitier, a food delivery rider waits for an order on a rainy night, standing still and upright, quiet dignity, precise words, refusing to be diminished`
- 中文对照：西德尼·波蒂埃风格：一位外卖骑手在雨夜等单，站得笔直安静，尊严在静止中，台词字正腔圆，拒绝被贬低。
- Negative: `No broad physical comedy, no self-degrading performance, no shouting to win a scene, no sentimental monologue`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
