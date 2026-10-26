# Cheng Miao — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Cheng Miao: early clerical script in formation, seal-script curves loosening into flat horizontal strokes, plain and unadorned`
- ZH: 程邈风格：隶书初创，篆之圆转渐松为平直横画，质朴未饰。

## (2) 笔法

- 由篆入隶的过渡用笔：圆转渐减，横画渐平渐长；起笔仍带篆意，收笔未见后世波磔。`impression`（后世著录与隶书演变通说）
- 禁笔：他几乎不用的笔法——成熟汉隶的波磔与挑法、小篆的完全圆转匀线。

## (3) 结字与章法

- 结字由篆之修长渐趋扁平，横向取势初现；字形尚不稳定，同一字多见异体。`impression`
- 幅式：卷 / 尺牍 / 册页，横卷为主，行列疏朗。

## (4) 墨色与节奏

- 无墨迹可考；墨色与节奏只能按隶书早期通例反推：墨色平实，节奏缓慢，一字一画交代清楚。`impression`

## (5) 书体与取法

- 书体：隶书（创制）。传说为秦狱吏，省篆为隶以便速书；其说见史书记载，真实性存疑。隶书由此而后经汉代成熟。`artifact`
- 演变：无作品序列可分期；蒸馏以“创制”这一节点为核心，不编造早中晚期。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 由篆入隶的过渡笔意，圆转渐松
- 横画渐平渐长、字形渐趋扁平
- 质朴无饰、一字一画交代清楚的写法
- 早期隶书的不稳定字形与异体
- 平实缓慢的书写节奏
- 不该写：
- 成熟汉隶的波磔与挑法
- 小篆的完全圆转匀线
- 楷书的方折与顿笔
- 行草的连绵与欹侧
- 华丽的装饰性笔法
- Negative prompt: `No mature Han clerical wave strokes, no fully rounded seal-script curves, no regular-script square turns, no running or cursive connections, no decorative flourishes`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Cheng Miao, early clerical script in formation writing modern Tokyo subway station names, seal curves loosening into flat horizontal strokes, plain unadorned characters, slow deliberate rhythm, ink on bamboo slips`
- 中文对照：程邈风格：以初创隶书写现代东京地铁站名，篆之圆转渐松为平直横画，质朴无饰，节奏缓慢，一字一画。
- Negative: `No mature Han clerical wave strokes, no fully rounded seal-script curves, no regular-script square turns, no running or cursive connections, no decorative flourishes`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
