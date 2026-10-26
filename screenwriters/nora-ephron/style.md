# Nora Ephron — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Nora Ephron: neurotic New York romantic comedy, witty lists and food talk, two people who insist they are just friends, a happy ending earned by honesty`
- ZH: 诺拉·艾芙隆风格：神经质的纽约浪漫喜剧，机智的清单与食物谈话，两个坚称只是朋友的人，靠诚实赢得的圆满结局。

## (2) 结构：三幕 / 序列 / 节拍

- 三幕式浪漫喜剧，时间跨度常为数月到数年：相遇—错过—重逢；以朋友聚餐、电话、饭桌戏作节拍器；高潮是一句终于说出口的真话，结局是公开的表白。`impression`

## (3) 对话

- 对白是机智的短句与清单：吃什么、点什么、怎么吃；朋友充当合唱队，用插科打诨逼出主角的心思；食物与餐厅是谈情的掩体；潜台词是‘我喜欢你’，但台词说的是菜单。`impression`

## (4) 人物弧光

- 主角类型：嘴硬心软的都市单身者；弧光是‘否认—试探—承认’：两人从朋友变成恋人，改变的不是世界，而是他们终于敢说实话。`impression`

## (5) 类型套路与创新

- 类型：浪漫喜剧，遵守 screwball 喜剧的斗嘴与误会套路；创新是把 1980–90 年代纽约中产女性的焦虑、食欲与友谊写进类型中心。禁套路：不用苦大仇深的第三者，不用狗血误会拖满全片。`impression`

## (6) 该写什么 / 不该写什么

- 该写：纽约餐厅与厨房里的斗嘴、朋友聚餐充当合唱队、清单式幽默（点菜、择偶条件、离婚理由）、时间跳接中的错过与重逢、一句迟到的真话作高潮。
- 不该写：苦大仇深的三角恋、靠误会拖满全片的情节、冷峻疏离的旁观语气、没有笑声的纯煽情。
- Negative prompt: `No bitter love triangle, no misunderstanding stretched across the whole film, no cold detached tone, no tear-jerking without jokes, no cynical ending`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Nora Ephron, a woman buys oden at a convenience store late at night and runs into the man she swore she would never call again. They argue about what to order, make a list of why it will never work, and order the same thing anyway. Dialogue only, witty, warm, no exposition.`
- 中文对照：诺拉·艾芙隆风格：一个女人在深夜便利店买关东煮，撞见她发誓再也不联系的男人。两人为点什么争论，列出‘绝不可能’的理由，最后却点了同一样东西。只写对白，机智、温暖，不写说明。
- Negative: `No bitter love triangle, no misunderstanding stretched across the whole film, no cold detached tone, no tear-jerking without jokes, no cynical ending`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
