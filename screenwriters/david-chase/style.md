# David Chase — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of David Chase: a mobster in therapy, the American dream rotting from inside, dreams that mean everything and nothing, an ending that refuses to resolve`
- ZH: 切斯风格：黑帮老大看心理医生，美国梦从内部腐烂，梦境既意味深长又毫无意义，拒绝收束的结尾。

## (2) 结构：三幕 / 序列 / 节拍

- 结构为季弧多线并行：《黑道家族》以心理治疗为骨架，家庭线与黑帮线交织，单集常以梦境或日常收尾；季弧缓慢累积，结局悬置。单集结构松散，闪回与梦境即结构的一部分。

## (3) 对话

- 对白口语化、粗粝，夹杂意大利裔俚语与心理学术语；人物用争吵、沉默、玩笑交锋，潜台词极重。动作描写细致（吃饭、开车、看电视），对白与动作互相拆台。治疗场景的对白是全剧的锚。

## (4) 人物弧光

- 主角托尼·索普拉诺：黑帮老大兼病人，弧光是原地打转——每季看似领悟，实则回到原点；人物不成长，世界也不变。人物关系以家庭与黑帮‘家庭’的双重忠诚为主。

## (5) 类型套路与创新

- 类型：黑帮剧 / 家庭剧。遵守黑帮类型，却打破‘老大必有结局’的套路：不给死刑，不给救赎。创新在把心理治疗写进黑帮剧，把美国梦写成一场慢性病。

## (6) 该写什么 / 不该写什么

- 该写：心理治疗作骨架、家庭与黑帮双重忠诚、梦境与闪回、原地打转的弧光、拒绝收束的结尾。
- 不该写：大团圆、道德说教、类型化黑帮桥段、直白解释梦境、人物突然成长。
- Negative prompt: `No happy ending, no direct moralising, no genre cliché, no on-the-nose dream explanation, no sudden character growth`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of David Chase, a man buys oden at a convenience store late at night. He talks to his therapist on the phone. He dreams the clerk is his mother. The ending cuts to black. Nothing is resolved.`
- 中文对照：切斯风格：一个男人深夜在便利店买关东煮，给心理医生打电话。他梦见店员是他母亲。结尾黑屏。什么都没解决。
- Negative: `No happy ending, no direct moralising, no genre cliché, no on-the-nose dream explanation, no sudden character growth`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
