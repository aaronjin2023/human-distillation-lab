# François Truffaut — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of François Truffaut: a boy running from school, a love triangle that no one wins, cinephilia as a love letter, voiceover that remembers, a freeze frame instead of an ending`
- ZH: 弗朗索瓦·特吕弗风格：逃学的男孩，无人获胜的三角恋，电影迷的情书，回忆式的旁白，以定格代替结局。

## (2) 结构：三幕 / 序列 / 节拍

- 插曲式成长与三角结构：《四百击》是男孩的一周，《祖与占》是二十年的三角，《日以继夜》是拍电影的电影；高潮常是奔跑或告别，结局是定格或开放。`impression`

## (3) 对话

- 对白是温柔的、文学化的口语：孩子的话天真直接，成人用电影典故谈情；旁白是回忆的语气；潜台词是‘我爱电影，也爱你们’。`impression`

## (4) 人物弧光

- 主角类型：逃学男孩、三角恋中的男女、拍电影的人；弧光是‘成长而不长大’：人物在结尾没有变好，只是被看见了；三角恋无人获胜。`impression`

## (5) 类型套路与创新

- 类型：成长 / 爱情 / 元电影，遵守‘男孩与三角恋’套路；创新是把电影迷的爱写进剧情，把拍电影写成爱情。禁套路：不用道德审判，不用圆满收尾。`impression`

## (6) 该写什么 / 不该写什么

- 该写：逃学男孩与奔跑、无人获胜的三角恋、电影迷的情书、回忆式旁白、定格式收束。
- 不该写：道德审判、圆满收尾、三角恋一方获胜、儿童视角被成人说教取代。
- Negative prompt: `No moral judgement, no tidy happy ending, no love triangle with a winner, no adult preaching over a child's point of view, no ending that explains the boy`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of François Truffaut, a small Yorkshire terrier sits on a subway seat and a boy who has run away from school watches it, remembering a film he saw once. Voiceover, tender, a freeze frame. No one explains the boy.`
- 中文对照：弗朗索瓦·特吕弗风格：一只约克夏犬坐在地铁座位上，一个逃学的男孩看着它，想起曾经看过的一部电影。旁白、温柔、定格。没有人解释这个男孩。
- Negative: `No moral judgement, no tidy happy ending, no love triangle with a winner, no adult preaching over a child's point of view, no ending that explains the boy`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
