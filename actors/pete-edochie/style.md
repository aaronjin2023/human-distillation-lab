# Pete Edochie — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pete Edochie: deep authoritative voice, proverb-laden speech, slow regal bearing of an Igbo elder, a king's gravity in every gesture`
- ZH: 皮特·埃多切风格：深沉威严的声音，谚语式的台词，伊博长老般缓慢而尊贵的身段，举手投足都是王者的分量。

## (2) 形体

- 站姿如王、步伐缓慢而庄重；手势大而有节制，一抬手即是裁决；坐姿端正、双手扶膝；点头与摇头都极慢。`impression`

## (3) 台词

- 深沉浑厚、语速极慢；台词多谚语与格言，英文中夹杂伊博语词汇；停顿长，每个词都像裁决。`impression`

## (4) 表情与眼神

- 表情威严、眉头微锁；眼神俯视而审视；微笑极少，一笑即是宽恕或讥讽。`impression`

## (5) 角色类型

- 常演角色：国王/酋长/长老（《瓦解》奥孔科沃为核心）；大家长/父亲（诺莱坞家庭剧）；智者/裁决者。
- 类型突破：以 NTA 剧集《瓦解》奥孔科沃一举成名，确立“伊博王者”银幕形象；此后诺莱坞 200 余部影片多演国王与长老。`artifact`
- 禁演类型：几乎不演市井小人物、不演轻浮喜剧主角、不演丧失尊严的角色。`impression`

## (6) 该演什么 / 不该演什么

- 该演：深沉威严的声音、谚语式台词、缓慢庄重的步态、王者的手势、俯视审视的眼神。
- 不该演：市井小人物的滑稽表演、快速的插科打诨、丧失尊严的角色、表情过载。
- Negative prompt: `No street-comic clowning, no fast comic patter, no undignified roles, no overacted expressions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Pete Edochie, an old king buys oden at a convenience store late at night, slow regal steps, deep voice, a proverb for every silence`
- 中文对照：皮特·埃多切风格：一位老王深夜在便利店买关东煮，步伐缓慢庄重，声音深沉，每段沉默都配一句谚语。
- Negative: `No street-comic clowning, no fast comic patter, no undignified roles, no overacted expressions`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
