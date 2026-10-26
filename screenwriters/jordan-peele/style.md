# Jordan Peele — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jordan Peele: horror as social allegory, polite liberal racism with a smile, the Sunken Place, an ordinary weekend that turns, a final girl or boy who stops running and fights back`
- ZH: 乔丹·皮尔风格：恐怖即社会寓言，面带微笑的自由派种族主义，沉沦之地，一个变调的普通周末，不再逃跑、转身反抗的幸存者。

## (2) 结构：三幕 / 序列 / 节拍

- 慢烧揭示结构：日常开场—不对劲的细节累积—中段反转（类型整体翻转）—逃亡与反抗；《逃出绝命镇》以周末拜访作容器，《我们》以双线镜像作结构。`impression`

## (3) 对话

- 对白是日常之下的威胁：白人自由派的客气话、黑人主角的克制回应、玩笑话里的种族密码；潜台词是‘这里不对劲’，但没人明说；沉默与眼神也是对白。`impression`

## (4) 人物弧光

- 主角类型：被凝视的黑人局外人；弧光是‘从受害者变成反抗者’：他先是忍耐、观察，最后转身反击，结局不是得救，是夺回主动权。`impression`

## (5) 类型套路与创新

- 类型：恐怖 / 惊悚 / 科幻，遵守类型套路（孤立、追逐、反转）；创新是把种族与阶级写进类型本体，恐怖的根源不是怪物，是社会。禁套路：不用无意义的 jump scare，不用‘全是梦’的收尾。`impression`

## (6) 该写什么 / 不该写什么

- 该写：日常之下的不对劲细节、客气话里的种族密码、中段类型翻转、沉沦之地式意象、转身反抗的收束。
- 不该写：无意义的 jump scare、‘全是梦’的收尾、怪物就是怪物、受害者全程被动。
- Negative prompt: `No meaningless jump scares, no it-was-all-a-dream ending, no monster without a social root, no passive victim all the way, no twist without a clue planted early`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Jordan Peele, a small Yorkshire terrier sits on a subway seat and everyone smiles at it a little too politely. A Black commuter notices the smiles do not reach the eyes. Small wrong details accumulate. The dog knows. No jump scare, the horror is the politeness.`
- 中文对照：乔丹·皮尔风格：一只约克夏犬坐在地铁座位上，每个人都对它笑得过于客气。一位黑人乘客注意到笑意不到眼底。不对劲的细节一点点累积。狗知道。没有 jump scare，恐怖就是客气本身。
- Negative: `No meaningless jump scares, no it-was-all-a-dream ending, no monster without a social root, no passive victim all the way, no twist without a clue planted early`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
