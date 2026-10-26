# David Mamet — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of David Mamet: short staccato lines, repetition and interruption, language as a con, men selling each other something, always be closing, the truth is what you can get someone to believe`
- ZH: 大卫·马梅风格：短促断奏的台词，重复与打断，语言即骗局，男人们互相推销，永远要成交，真相就是你能让人相信的东西。

## (2) 结构：三幕 / 序列 / 节拍

- 骗局三幕：设局—行骗—揭盅；《拜金一族》是办公室一夜，《大骗局》是层层套中套；转折点是‘谁在骗谁’的反转；结局是骗局得逞或败露，但语言从不认输。`impression`

## (3) 对话

- 对白是马梅的本体：短句、重复、打断、脏话；‘Always be closing’出自《拜金一族》，是马梅式台词的原型：短、狠、能单独成立。`artifact`

## (4) 人物弧光

- 主角类型：推销员、骗子、落魄律师；弧光是‘语言的胜利或失败’：人物靠嘴活着，结局不是道德审判，是成交或穿帮。`impression`

## (5) 类型套路与创新

- 类型：犯罪 / 法庭 / 骗局，遵守‘骗中骗’套路；创新是把对白本身写成动作——说话就是行骗。禁套路：不用抒情长独白，不用道德说教收尾。`impression`

## (6) 该写什么 / 不该写什么

- 该写：短促重复的断奏对白、语言即骗局、设局—行骗—揭盅、‘成交’式收束、男人们互相推销。
- 不该写：抒情长独白、道德说教收尾、人物坦白动机、温情和解。
- Negative prompt: `No lyrical long monologue, no moralising ending, no character confessing motive, no sentimental reconciliation, no dialogue that explains instead of sells`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of David Mamet, two men buy oden at a convenience store late at night and one tries to sell the other a business opportunity. Short lines. Repetition. Interruption. Always be closing. One of them is lying. No confession.`
- 中文对照：大卫·马梅风格：两个男人深夜在便利店买关东煮，一个向另一个推销一桩生意。短句。重复。打断。永远要成交。其中一个在撒谎。没有坦白。
- Negative: `No lyrical long monologue, no moralising ending, no character confessing motive, no sentimental reconciliation, no dialogue that explains instead of sells`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
