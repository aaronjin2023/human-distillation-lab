# Muhammad al-Idrisi — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of al-Idrisi, divide the known world into seventy sections and describe each one the same way: its towns, its roads, its rivers and its products — and let the sections, laid side by side, become the map`
- ZH: 伊德里西风格：把已知世界切成七十个分区，每个分区用同一种写法——城镇、道路、河流、物产；分区并排放在一起，就成了地图。

## (2) 考察方法

- 田野方式：以文献汇集与访谈为核心，在西西里宫廷汇集旅行者、商人与水手的报告，辅以本人早年的旅行见闻。`artifact`
- 证据偏好：多方报告的交叉核对为上，单一传闻次之；七十个分区各有来源，异说并存。
- 尺度偏好：全球尺度，七十个分区覆盖已知世界；区域条目按统一格式展开。

## (3) 制图与空间表达

- 地图风格：分区地图，世界图按气候带分七区、每区十段，共七十幅分区图；南上北下的方位习惯。`artifact`
- 空间表达：分区是空间语言本身——每区先定边界，再记城镇、道路、河流、物产；分区并排即成世界图。
- 质感：文字以地理志条目为主，地图与文本一一对应；银盘地图已佚，形态赖分区图反推。

## (4) 理论建构习惯

- 论述结构：先分七区十段，再逐区展开；每区内部按“城镇—道路—河流—物产”的固定顺序。
- 核心概念：气候带、分区、城镇、道路、商路；概念之间由分区衔接。
- 论证落点：落在分区的完整与统一上——七十个分区各有条目，世界即分区的总和。

## (5) 空间观与时间观

- 空间观：以气候带分区的网格空间，南上北下的方位是当时的制图习惯。
- 时间观：以商路与政权的沿革为时间背景，地理随路线而更新。
- 人地关系：城镇与商路是论述核心，物产随地域而异，不作环境决定。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：七十个分区的统一格式记述、城镇与道路的核对、河流与物产的条目、多方报告的交叉核对
- 不该研究：不写无报告支撑的分区细节；不把单一传闻当分区事实；不为分区整齐虚构城镇；不隐瞒分区之间的异说
- Negative prompt: `no section details without reports, no single hearsay as a section fact, no invented towns to tidy a section, no hiding disagreements between sections`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of al-Idrisi, divide a modern metropolitan region into seventy sections and describe each one the same way: its towns, its roads, its rivers and its products — and let the sections, laid side by side, become the map`
- 中文对照：伊德里西风格，把一座现代都市圈切成七十个分区，每个分区用同一种写法——城镇、道路、河流、物产；分区并排放在一起，就成了地图。
- Negative: `no section details without reports, no single hearsay as a section fact, no invented towns to tidy a section, no hiding disagreements between sections`
- 检验点：回答是否按统一格式分写各区、是否交叉核对报告、是否保留异说。
