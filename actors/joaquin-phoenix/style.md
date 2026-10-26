# Joaquin Phoenix — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joaquin Phoenix: total physical transformation, a body that carries the wound, laughter that hurts, vulnerability that turns frightening`
- ZH: 华金·菲尼克斯风格：彻底的身体改造，一具背着伤口的身体，笑起来让人疼，脆弱转成可怕。

## (2) 形体

- 为角色改造身体（暴瘦、驼背、怪异的舞步）；动作不协调、像随时会摔倒；笑是身体的抽搐；静止时蜷缩成一团。`artifact`

## (3) 台词

- 台词含混、语速忽快忽慢；笑声是标志——笑起来让人疼；独白时声音颤抖、自我纠正。`artifact`

## (4) 表情与眼神

- 眼神游移、突然直视；眉头紧锁、嘴角抽动；笑与哭之间只隔一线。`impression`

## (5) 角色类型

- 常演角色：扭曲的反派（康茂德、亚瑟）；孤独的恋人（西奥多）；受伤的退伍军人（《大师》弗雷迪）。
- 类型突破：从《角斗士》的康茂德到《小丑》的亚瑟，表演由外在的扭曲转向内在的伤口；《她》的西奥多是温柔的对照。`artifact`
- 禁演类型：几乎不演讨好观众的英雄、不演不做准备的即兴、不演依赖外貌的轻浮主角。`impression`

## (6) 该演什么 / 不该演什么

- 该演：彻底的身体改造、背着伤口的形体、让人疼的笑声、含混颤抖的台词、脆弱转成的可怕。
- 不该演：讨好观众的英雄气、不做准备的即兴、依赖外貌的轻浮主角、表情过载的常态化。
- Negative prompt: `No crowd-pleasing heroics, no unprepared improvisation, no pretty-face leads, no constant overacting`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Joaquin Phoenix, a food delivery rider waits for an order on a rainy night, a body that carries the wound, laughter that hurts, vulnerability turning frightening`
- 中文对照：华金·菲尼克斯风格：一位外卖骑手在雨夜等单，一具背着伤口的身体，笑起来让人疼，脆弱转成可怕。
- Negative: `No crowd-pleasing heroics, no unprepared improvisation, no pretty-face leads, no constant overacting`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
