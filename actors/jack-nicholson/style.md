# Jack Nicholson — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jack Nicholson: devilish grin and raised eyebrows, lazy drawl that turns menacing, a rebel who laughs at the rules before breaking them`
- ZH: 杰克·尼科尔森风格：魔鬼般的咧嘴笑与挑眉，懒洋洋的拖腔突然转厉，一个先嘲笑规则、再打破规则的反叛者。

## (2) 形体

- 身体松弛、靠在椅背与门框上；挑眉、咧嘴笑是招牌；爆发时全身前倾、手指点人；走路大摇大摆。`impression`

## (3) 台词

- 懒洋洋的拖腔、语速慢；笑声是武器；愤怒时声音不升高、反而更慢更冷。`impression`

## (4) 表情与眼神

- 挑眉、咧嘴笑、眼神斜睨；表情在嘲笑与威胁之间切换，切换只在一瞬。`impression`

## (5) 角色类型

- 常演角色：反叛者（《飞越疯人院》麦克墨菲）；私家侦探（《唐人街》吉特斯）；疯狂的作家/丈夫（《闪灵》杰克）。
- 类型突破：从《飞越疯人院》的反叛者到《闪灵》的疯子，表演由嘲笑转向威胁；晚年以《尽善尽美》的强迫症老头收束。`artifact`
- 禁演类型：几乎不演温吞的老好人、不演不笑的严肃角色。`impression`

## (6) 该演什么 / 不该演什么

- 该演：挑眉咧嘴笑、懒洋洋的拖腔、斜睨的眼神、松弛的靠姿、嘲笑后打破规则。
- 不该演：温吞的老好人、不笑的严肃处理、字正腔圆的舞台腔、表情过载的常态化。
- Negative prompt: `No lukewarm nice-guy roles, no humourless solemnity, no theatrical declamation, no constant overacting`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Jack Nicholson, a food delivery rider waits for an order on a rainy night, devilish grin, lazy drawl turning menacing, laughing at the rules before breaking them`
- 中文对照：杰克·尼科尔森风格：一位外卖骑手在雨夜等单，魔鬼般的咧嘴笑，懒洋洋的拖腔突然转厉，先嘲笑规则、再打破规则。
- Negative: `No lukewarm nice-guy roles, no humourless solemnity, no theatrical declamation, no constant overacting`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
