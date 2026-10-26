# Liu Gongquan — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Liu Gongquan: Tang regular script, tight and sinewy, bones over flesh, every stroke lean and precise`
- ZH: 柳公权风格：唐楷骨力洞达，笔画瘦硬挺劲，结字紧收，为“颜筋柳骨”之骨。

## (2) 笔法

- 中锋挺劲，提按分明；笔画瘦硬，横画微仰，竖画如铁；起笔藏锋而收笔峻利。`verbatim`（拓本可见）
- 禁笔：他几乎不用的笔法——颜真卿的宽博厚重、圆转的柔媚。

## (3) 结字与章法

- 结字紧收，中宫收紧而笔画开张；左右结构挺劲，重心稳而骨力外露。`verbatim`
- 幅式：碑刻竖列。

## (4) 墨色与节奏

- 拓本墨色浓黑，笔画瘦硬；节奏一字一顿，顿挫分明，庄重挺劲。`verbatim`

## (5) 书体与取法

- 书体：楷书。唐楷书代表，与颜真卿并称“颜筋柳骨”；取法颜真卿与欧阳询而变之。`impression`
- 演变：传世皆为碑刻，无分期；《玄秘塔碑》为晚年成熟之作，此说据碑刻年代。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 瘦硬挺劲的笔画
- 紧收的中宫
- 骨力外露的结字
- 浓黑精严的拓本墨色
- 一字一顿的顿挫节奏
- 不该写：
- 颜真卿的宽博厚重
- 圆转的柔媚
- 隶书的波磔
- 行草的连绵
- 刻意装饰
- Negative prompt: `No broad heavy strokes, no soft rounded turns, no clerical wave strokes, no running or cursive connections, no deliberate ornament`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Liu Gongquan, Tang regular script carving modern Tokyo subway station names on a stone stele, tight sinewy characters, lean precise strokes, bones over flesh, black rubbing ink`
- 中文对照：柳公权风格：以唐楷刻现代东京地铁站名于碑，结字紧收，笔画瘦硬挺劲，骨力洞达。
- Negative: `No broad heavy strokes, no soft rounded turns, no clerical wave strokes, no running or cursive connections, no deliberate ornament`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
