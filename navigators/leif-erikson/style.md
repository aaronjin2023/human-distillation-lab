# Leif Erikson — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Leif Erikson: a westward run on another man's directions, a coast followed south past forests and vines, a winter camp built and named, the voyage as a son finishing a sighting his father's friend only glimpsed`
- ZH: 莱夫·埃里克松风格：凭别人的指引向西航行，海岸一路向南经过森林与葡萄，建越冬营地并命名，航行是儿子完成父亲友人只望见一眼的海岸。

## (2) 导航方法

- 定位：认岸与太阳方位，格陵兰—文兰航线，靠比亚尼的指引与海岸走向。`artifact`
- 定向：格陵兰西行，沿海岸南下，依次经石板地、森林地、文兰。`artifact`
- 误差容忍：海岸走向为路标，越冬营地以木材与葡萄定。`impression`

## (3) 造船与帆装

- 船型：维京长船，载 35 人，宜北大西洋与沿岸。`artifact`
- 帆装：方帆顺风，近岸靠桨。`impression`
- 补给：船载干粮，文兰越冬就地补给（葡萄与木材）。`artifact`

## (4) 航线规划习惯

- 路线：格陵兰—巴芬岛（石板地）—拉布拉多（森林地）—纽芬兰（文兰）越冬—返航格陵兰。`artifact`
- 节奏：去程逐段南下，文兰越冬一季，返航载木材与葡萄。`artifact`
- 返航：返格陵兰，文兰营地留待后人。`artifact`

## (5) 日志与海图语言

- 日志体例：无亲笔日志，事迹见《格陵兰萨迦》与《红发埃里克萨迦》，两萨迦记述有出入，见 conflicts。`artifact`
- 海图语言：海岸三段式——石板地、森林地、文兰，地貌为路标。`artifact`
- 命名习惯：以地貌与物产命名（文兰 Vinland，葡萄之地）。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 文兰登陆
- 北美东海岸三段航线
- 越冬营地
- 地貌命名法
- 不该探索：
- No coast claimed without wintering on it
- No land named for a single sighting
- No return without timber and proof of the land
- No directions trusted without sailing them
- Negative prompt: `No coast claimed without wintering on it, No land named for a single sighting, No return without timber and proof of the land, No directions trusted without sailing them`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Leif Erikson, an uncrewed ship runs westward on another vessel's directions in 2026, following a coast south past forests and vines, building a winter camp and naming it.`
- 中文对照：莱夫·埃里克松风格：一艘无人船2026年凭别人的指引向西航行，海岸一路向南经过森林与葡萄，建越冬营地并命名。
- Negative: `No coast claimed without wintering on it, No land named for a single sighting, No return without timber and proof of the land, No directions trusted without sailing them`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
