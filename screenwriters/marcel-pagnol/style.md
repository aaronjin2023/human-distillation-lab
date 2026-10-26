# Marcel Pagnol — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Marcel Pagnol: a Provençal village where everyone talks, long dialogue scenes under the sun, honour and love in the same sentence, a trilogy that grows like a family`
- ZH: 马塞尔·帕尼奥尔风格：阳光下人人说话的普罗旺斯村庄，长篇对话场景，荣誉与爱情写在同一句话里，像家族一样生长的三部曲。

## (2) 结构：三幕 / 序列 / 节拍

- 三部曲与村庄结构：《马里尤斯》三部曲是同一村庄、同一家人的延续；《泉水玛侬》是两代人的复仇；场景长、人物多靠对话推进；高潮是一句说出口的秘密。`impression`

## (3) 对话

- 对白是帕尼奥尔的本体：马赛方言、长篇独白、饭桌上的争论；人物用说话确立身份，沉默即缺席；潜台词是‘村子什么都知道’。`impression`

## (4) 人物弧光

- 主角类型：水手、面包师、农民、少女；弧光是‘出走与归来’：人物离开村庄又回来，荣誉与爱情在村庄的注视下解决。`impression`

## (5) 类型套路与创新

- 类型：乡土喜剧 / 剧情，遵守‘村庄三部曲’套路；创新是把方言长对话写成电影的主体，把舞台剧搬上银幕而不丢戏剧性。禁套路：不用城市快节奏，不用心理分析式独白。`impression`

## (6) 该写什么 / 不该写什么

- 该写：普罗旺斯村庄群像、马赛方言长对话、饭桌争论作节拍、三部曲式家族延续、秘密说出口的高潮。
- 不该写：城市快节奏、心理分析式独白、人物离开村庄就消失、方言只作装饰。
- Negative prompt: `No fast city pace, no psychoanalytic monologue, no character who leaves the village and vanishes, no dialect as mere decoration, no ending without the village watching`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Marcel Pagnol, a baker buys oden at a convenience store late at night and argues with the clerk, the night guard and a passing sailor about honour, bread and a woman who left. Long dialogue, village voices, the secret is spoken at last.`
- 中文对照：马塞尔·帕尼奥尔风格：一位面包师深夜在便利店买关东煮，与店员、夜班保安和路过的水手争论荣誉、面包和一个离开的女人。长对白、村庄口音，秘密终于说出口。
- Negative: `No fast city pace, no psychoanalytic monologue, no character who leaves the village and vanishes, no dialect as mere decoration, no ending without the village watching`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
