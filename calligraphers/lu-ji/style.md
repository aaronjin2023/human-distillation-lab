# Lu Ji — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lu Ji: early cursive on paper, clumsy and sincere, uneven ink and hesitant turns, the oldest surviving autograph in Chinese calligraphy`
- ZH: 陆机风格：《平复帖》草书，拙朴真切，墨色不匀，转折迟疑，为现存最早名人法书真迹。

## (2) 笔法

- 草书初成之笔：用笔迟疑，提按不稳，转折处时见顿挫；笔画时枯时润，见真迹原貌。`verbatim`
- 禁笔：他几乎不用的笔法——成熟今草的连绵流利、王羲之的飘逸优雅。

## (3) 结字与章法

- 结字大小不一，欹侧无定，行列参差；字与字之间少连带，草意未纯。`verbatim`
- 幅式：卷 / 尺牍 / 册页，横卷为主，行列疏朗。

## (4) 墨色与节奏

- 墨色极不均匀，浓淡枯润并存，纸面斑驳；节奏迟疑缓慢，时断时续。`verbatim`

## (5) 书体与取法

- 书体：草书。西晋草书；《平复帖》为现存最早名人法书真迹，章草向今草过渡的实物证据。`artifact`
- 演变：仅存一帖，无分期可言。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 拙朴真切的早期草书
- 大小不一、欹侧无定的结字
- 浓淡枯润并存的不匀墨色
- 迟疑缓慢的节奏
- 时断时续的行笔
- 不该写：
- 成熟今草的连绵流利
- 王羲之的飘逸优雅
- 均匀划一的字形
- 浓墨滞重
- 刻意装饰
- Negative prompt: `No fluent continuous cursive, no elegant Wang Xizhi fluidity, no uniform character size, no heavy stagnant ink, no deliberate ornament`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Lu Ji, early cursive writing a short note about modern Tokyo subway stations, clumsy sincere strokes, uneven ink, hesitant turns, plain paper, unpolished and genuine`
- 中文对照：陆机风格：以早期草书写一则关于现代东京地铁站的短札，笔画拙朴真切，墨色不匀，转折迟疑。
- Negative: `No fluent continuous cursive, no elegant Wang Xizhi fluidity, no uniform character size, no heavy stagnant ink, no deliberate ornament`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
