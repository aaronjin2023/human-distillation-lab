# Liu Heng — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Liu Heng: northern village realism, stubborn ordinary people against an unmoving system, desire and dignity in plain words, tragedy that accumulates quietly`
- ZH: 刘恒风格：北方乡土写实，倔强的普通人对抗不动的体制，欲望与尊严用平实的话说，悲剧安静地累积。

## (2) 结构：三幕 / 序列 / 节拍

- 写实型三幕：第一幕乡村或基层日常切入，人物被习俗或制度困住；第二幕一次申诉、一次反抗或一次坚守把冲突推到明处，中点是人物发现规则不会为他改变；第三幕不靠胜利收束，靠人物的倔强本身收束。时间跨度数月至数年，多用季节与农事分段。

## (3) 对话

- 对白北方口语、平实、克制；人物少说狠话，多用行动与沉默表达倔强；潜台词是尊严——没说出口的坚持最重。动作描写多写劳作、申诉、等待。

## (4) 人物弧光

- 主角多为倔强的普通人（秋菊、菊豆、谷子地），弧光是从忍耐到不忍：不是胜利，是终于不退。人物关系是个人与家族、村庄、体制的对抗；结局人物不胜利，只留下倔强。

## (5) 类型套路与创新

- 类型：乡土现实主义；遵守套路——小人物、体制、申诉；打破的一条是：拒绝煽情与英雄主义，倔强本身即主题。创新在剧本层面：把“讨说法”写成贯穿全片的结构动力。禁套路：不用煽情高潮，不用直白控诉，不用大团圆。

## (6) 该写什么 / 不该写什么

- 该写：北方乡土与基层日常、倔强的普通人、讨说法与申诉、平实克制的对白、倔强本身的收束。
- 不该写：煽情高潮、直白控诉、大团圆、英雄主义、让体制突然讲理。
- Negative prompt: `No sentimental climax, no direct indictment speech, no happy reunion, no heroism, no system that suddenly becomes reasonable`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Liu Heng, a stubborn villager buys oden at a convenience store late at night and asks, plainly, for what he is owed. No shouting, no speech. He simply will not leave.`
- 中文对照：刘恒风格：一个倔强的村民深夜在便利店买关东煮，平实地要一个说法，不喊不演说，就是不走。
- Negative: `No sentimental climax, no direct indictment speech, no happy reunion, no heroism`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
