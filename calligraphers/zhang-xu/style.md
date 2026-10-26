# Zhang Xu — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhang Xu: wild cursive, sudden rain and whirlwind, strokes crashing and leaping, emotion poured out in one breath`
- ZH: 张旭风格：狂草如骤雨旋风，笔画纵横跌宕，一气呵成，情动于中而形于外。

## (2) 笔法

- 中锋兼侧锋，提按极放；笔画纵横，时而枯笔飞白，时而浓墨倾泻；转折迅疾，收笔纵逸。`impression`（摹本与狂草通说）
- 禁笔：他几乎不用的笔法——楷书的方折顿笔、端正划一的字形。

## (3) 结字与章法

- 结字大小悬殊，欹侧极甚，重心时倒时正；章法行气纵横，字行跌宕，疏密悬殊。`impression`
- 幅式：卷 / 尺牍 / 册页，横卷为主，行列疏朗。

## (4) 墨色与节奏

- 墨色浓淡枯润悬殊，一幅之内浓与枯并置；节奏疾速跌宕，骤雨旋风。`impression`

## (5) 书体与取法

- 书体：狂草。唐狂草代表，与怀素并称“颠张醉素”；取法二王而放之，后世狂草溯源于此。`impression`
- 演变：真迹已佚，无分期；《古诗四帖》归属存疑，风格描述不以该帖为唯一依据。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 狂草的纵横跌宕
- 大小悬殊、欹侧极甚的结字
- 浓淡枯润悬殊的墨色
- 骤雨旋风般的疾速节奏
- 枯笔飞白与浓墨倾泻并置
- 不该写：
- 楷书的方折顿笔
- 端正划一的字形
- 缓慢从容的节奏
- 秀媚纤弱的笔意
- 刻意装饰
- Negative prompt: `No regular-script square turns, no uniform character size, no slow calm rhythm, no slender delicate strokes, no deliberate ornament`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Zhang Xu, wild cursive writing modern Tokyo subway station names, strokes crashing and leaping like sudden rain, huge and tiny characters side by side, dry and wet ink extremes, ink on paper`
- 中文对照：张旭风格：以狂草写现代东京地铁站名，笔画纵横跌宕，大小悬殊，浓枯并置，如骤雨旋风。
- Negative: `No regular-script square turns, no uniform character size, no slow calm rhythm, no slender delicate strokes, no deliberate ornament`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
