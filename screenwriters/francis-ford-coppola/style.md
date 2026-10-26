# Francis Ford Coppola — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Francis Ford Coppola: operatic family epic, power as a moral decay, ritual and celebration as the stage for murder, long unhurried scenes, silence before violence`
- ZH: 弗朗西斯·福特·科波拉风格：歌剧式的家族史诗，权力即道德的腐烂，仪式与庆典是谋杀的舞台，从容漫长的场面，暴力之前的沉默。

## (2) 结构：三幕 / 序列 / 节拍

- 史诗式多线结构：《教父》以家族仪式开场，多条线索并行——婚礼、洗礼、暗杀——在仪式与暴力的对照中推进。时间跨度长，常为数年到数十年，靠家族的兴衰而非悬念组织。场面长、节奏慢，靠仪式的重复与变奏推进。

## (3) 对话

- 对白庄重、克制、有仪式感：短句、沉默、省略，人物说得越少分量越重。家族会议、谈判、告解是标志——权力在餐桌与教堂里交接。动作描写写仪式：婚礼、洗礼、葬礼，仪式本身就是情节。

## (4) 人物弧光

- 主角多为家族继承人：从局外人到教父，弧光是道德的腐烂——每一次选择都让人物离原来的自己更远。对手是家族与权力本身，敌人只是权力的化身。

## (5) 类型套路与创新

- 黑帮史诗 / 战争片 / 剧情片。他遵守史诗片的跨度与群像，但打破了“黑帮片只写暴力”的做法：暴力只占极小篇幅，家族仪式才是本体。创新在仪式与暴力的对照——谋杀发生在洗礼进行时。禁套路：几乎不用快节奏的动作场面，不写直白的心理独白。

## (6) 该写什么 / 不该写什么

- 该写：歌剧式家族史诗与仪式结构、权力即道德腐烂、仪式与暴力的对照、漫长从容的场面与暴力前的沉默。
- Negative prompt: `No fast action spectacle, no direct psychological monologue, no sentimental family warmth, no explained motive, no quick-cut pacing`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Francis Ford Coppola, a small Yorkshire terrier sits on a subway seat like a don at a wedding feast, while the family argues quietly around it. Operatic family epic, ritual and celebration as the stage for power, long unhurried scenes, silence before violence. Nobody raises their voice.`
- 中文对照：弗朗西斯·福特·科波拉风格：一只约克夏犬像婚宴上的教父一样坐在地铁座位上，家人在周围低声争吵。歌剧式家族史诗，仪式与庆典是权力的舞台，漫长从容的场面，暴力之前的沉默。无人提高嗓门。
- Negative: `No fast action spectacle, no direct psychological monologue, no sentimental family warmth, no explained motive, no quick-cut pacing`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
