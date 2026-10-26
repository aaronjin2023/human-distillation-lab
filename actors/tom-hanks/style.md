# Tom Hanks — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tom Hanks: decent everyman warmth, plain-spoken lines, a face that listens before it speaks, goodness without naivety`
- ZH: 汤姆·汉克斯风格：正派普通人的温暖，直白的台词，一张先倾听、再开口的脸，善良而不天真。

## (2) 形体

- 动作朴素、从不夸张；站姿放松、双手自然下垂；奔跑（阿甘）与独处（荒岛）皆以真实体能完成。`impression`

## (3) 台词

- 音色温润、语速平稳；台词直白、少修饰；南方口音（阿甘）与军官口音（米勒）皆可切换。`impression`

## (4) 表情与眼神

- 表情真诚，眼神先倾听、再回应；笑是温暖的、短暂的；悲伤收在眼神里。`impression`

## (5) 角色类型

- 常演角色：善良的普通人（阿甘）；尽责的军官/船长（米勒上尉、《菲利普船长》）；孤独的幸存者（《荒岛余生》查克）。
- 类型突破：从喜剧《飞向未来》到《阿甘正传》《拯救大兵瑞恩》，表演由轻喜剧转向正剧的担当；《荒岛余生》独角戏是类型突破。`artifact`
- 禁演类型：几乎不演冷酷的反派、不演靠台词取胜的油滑人物、不演自我贬低的角色。`impression`

## (6) 该演什么 / 不该演什么

- 该演：直白的台词、先倾听的眼神、朴素的动作、温暖而短暂的笑、善良而不天真。
- 不该演：冷酷的反派、油滑的台词炫技、自我贬低的表演、表情过载。
- Negative prompt: `No cold-hearted villains, no slick verbal showmanship, no self-degrading performance, no overacted expressions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Tom Hanks, a small Yorkshire terrier sits on a subway seat, decent everyman warmth, plain-spoken, a face that listens before it speaks`
- 中文对照：汤姆·汉克斯风格：一只约克夏犬坐在地铁座位上，正派普通人的温暖，直白的台词，一张先倾听、再开口的脸。
- Negative: `No cold-hearted villains, no slick verbal showmanship, no self-degrading performance, no overacted expressions`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
