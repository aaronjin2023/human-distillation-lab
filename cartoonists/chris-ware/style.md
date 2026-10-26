# Chris Ware — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chris Ware, precise diagrammatic line, tiny panels, architectural grids, melancholic infographic, graphic novel page`
- ZH: 韦尔风格，精确图解线，微小格子，建筑网格，忧郁信息图，图像小说页。

## (2) 线条、网点/色彩

- 线条：精确如制图的线，干净均匀；几何图形多。`verbatim`
- 网点/色彩：平涂柔和，米色、灰蓝、暗红；色彩如旧印刷品。
- 质感：制图线 + 柔和色块；纸面干净，几何精确。

## (3) 分镜

- 格数与格形：格子极小极多，网格如建筑图；跨页图表；节奏缓慢、信息密集。
- 节奏：节奏缓慢、信息密集，小格如建筑图；时间并置。
- 视线引导：美式阅读顺序左→右；视线在小格与图表间移动，需细读。

## (4) 角色造型

- 造型：吉米·科里根的矮小身躯与大头；拉斯特·杰克逊；人物如剪影，表情克制。
- 角色类型：孤独的小人物、超人与父亲、建筑中的居民；主角渺小，建筑巨大。
- 动作：动作极简缓慢，行走、等待、凝视；速度线全无。

## (5) 对话框与拟声词

- 对话框：对话框小，文字多；图表式旁白。
- 拟声词：拟声词罕见；日常声响以图表代替。
- 文字量：每页文字密度极高，图表式旁白多，需细读。

## (6) 该画什么 / 不该画什么

- 该画：吉米·科里根的孤独、芝加哥建筑、超人与父亲、日常生活的图表、时间并置（过去与现在同页）、小人物的忧郁、建筑剖面。`verbatim`
- 不该画：不画松散速写线、不画大块黑面、不画快速动作、不画鲜亮饱和色、不画空旷背景。
- Negative prompt: `No loose sketchy line, no bold black masses, no fast action, no bright saturated colour, no empty backgrounds`

## (7) 测试提示词示例（现代题材：在公寓阳台看城市天际线的独居者）

- Prompt: `In the style of Chris Ware, a lone person looking at the city skyline from an apartment balcony, precise diagrammatic line, tiny panels, architectural grids, melancholic`
- 中文对照：韦尔风格：独居者在公寓阳台看城市天际线，精确图解线，微小格子，建筑网格，忧郁。
- Negative: `No loose sketchy line, no bold black masses, no fast action`
- 检验点：格子是否极小极多；线是否如制图般精确；时间并置是否成立。
