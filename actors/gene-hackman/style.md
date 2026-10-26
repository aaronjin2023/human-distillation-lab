# Gene Hackman — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gene Hackman: workmanlike authenticity, gruff voice and weary eyes, a professional who does the job and carries the cost, no wasted motion`
- ZH: 吉恩·哈克曼风格：工匠般的真实，粗粝的声音与疲惫的眼神，一个把活干完、自己承担代价的职业人，没有多余动作。

## (2) 形体

- 动作经济、步伐沉重；站姿微驼、双手常插兜或扶物；爆发时短促有力，之后立刻收住。`impression`

## (3) 台词

- 粗粝低沉、语速平稳；台词不多、每句都落地；愤怒时声音压低、咬字更重。`impression`

## (4) 表情与眼神

- 眼神疲惫、直视中带着审视；表情克制，情绪靠眼神与嘴角的细微变化传递。`impression`

## (5) 角色类型

- 常演角色：硬汉警察/侦探（波普伊）；偏执的监听专家（哈里·考尔）；冷酷的警长/反派（利特·比尔）。
- 类型突破：从《法国贩毒网》的粗粝警察到《不可饶恕》的冷酷警长，表演由外放的硬汉转向内敛的恶；2004 年息影。`artifact`
- 禁演类型：几乎不演轻浮喜剧、不演依赖外貌的浪子、不演解释性独白。`impression`

## (6) 该演什么 / 不该演什么

- 该演：经济的动作、粗粝低沉的声音、疲惫审视的眼神、短促有力的爆发、职业人的从容。
- 不该演：轻浮的喜剧表演、解释性独白、依赖外貌的浪子、表情过载。
- Negative prompt: `No frivolous comedy, no explanatory monologue, no pretty-boy romantic leads, no overacted expressions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Gene Hackman, a small Yorkshire terrier sits on a subway seat, workmanlike and weary, gruff and economical, doing the job and carrying the cost`
- 中文对照：吉恩·哈克曼风格：一只约克夏犬坐在地铁座位上，工匠般真实而疲惫，粗粝而经济，把活干完、自己承担代价。
- Negative: `No frivolous comedy, no explanatory monologue, no pretty-boy romantic leads, no overacted expressions`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
