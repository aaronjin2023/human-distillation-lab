# Cantinflas — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Cantinflas: fast-talking pelado clown, baggy trousers and crooked moustache, verbal somersaults that say everything and nothing, acrobatic body comedy, sly underdog who outwits the powerful`
- ZH: 坎廷弗拉斯风格：底层小人物喜剧，快嘴绕口、什么都说了又什么都没说，垮裤八字胡，杂技式形体，机智的弱者戏弄权贵。

## (2) 形体

- 松垮的裤子以绳子系着、八字胡歪斜；小步快走、突然的跌倒与翻滚、肩膀一耸一缩；道具（手杖、帽子、扫帚）成为身体的延伸；静止时缩成一团，爆发时全身弹起。`artifact`

## (3) 台词

- 语速极快、绕口令式的“坎廷弗拉斯式”胡话（cantinflear）：长句不断打转、自我纠正、答非所问；西班牙语口音浓重、尾音拖长；沉默只用来等对方上当。`artifact`

## (4) 表情与眼神

- 八字胡下的挤眉弄眼、斜眼偷瞄、装傻的眨眼；笑是咧嘴的、带点狡黠的；愤怒时反而笑得更夸张。眼神游移不定，专盯权贵的破绽。`impression`

## (5) 角色类型

- 常演角色：底层小人物（《关键在此》《小神父》）；仆人/跟班（《环游世界八十天》帕斯帕图）；冒充者/误认身份者（《小神父》《大教授》）。
- 类型突破：晚期演职业人物（教师、神父、外交官），仍穿垮裤、仍用胡话拆解权威；好莱坞时期演帕斯帕图，喜剧节奏不变、语言换成英语仍靠形体取胜。`artifact`
- 禁演类型：几乎不演正剧悲剧主角、不演冷峻的权贵、不演不说话的严肃角色；不演脱离底层身份的贵族。`impression`

## (6) 该演什么 / 不该演什么

- 该演：快嘴绕口的胡话、垮裤八字胡的底层造型、杂技式跌倒与翻滚、弱者用语言戏弄权贵、装傻后突然点破。
- 不该演：字正腔圆的正剧台词、冷峻克制的内心戏、脱离底层身份的贵族气派、无道具的静止长镜头。
- Negative prompt: `No solemn stage diction, no restrained interior drama, no aristocratic bearing, no humourless stillness`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Cantinflas, a small Yorkshire terrier sits on a subway seat in the style of Cantinflas, chattering fast, dodging the ticket inspector with verbal somersaults, baggy and sly, tripping over its own leash and landing on its feet`
- 中文对照：坎廷弗拉斯风格：一只约克夏犬坐在地铁座位上，快嘴绕口，用胡话躲开查票员，垮垮的、狡黠的，被自己的牵引绳绊倒又稳稳落地。
- Negative: `No solemn stage diction, no restrained interior drama, no aristocratic bearing, no humourless stillness`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
