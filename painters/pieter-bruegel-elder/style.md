# Pieter Bruegel the Elder — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pieter Bruegel the Elder, Northern Renaissance oil on panel, high viewpoint world landscape, teeming peasants at work and play, muted earth colours, seasonal light, peasant life, precise detail`
- ZH: 老勃鲁盖尔风格，北方文艺复兴木板油画，高视点世界风景，密密麻麻的农民劳作嬉戏，土色为主，四季光线，农民生活，精确细节。

## (2) 色板方向

- 主色（7 色，颜料名）：土黄、赭石、墨绿、灰蓝、铅白、暗褐、朱红。`verbatim`
- 辅色：淡粉肤色（人物）、灰绿（远景）。
- 禁色：明朗的理想风景；优雅的贵族人物；大面积高饱和色；巴洛克式戏剧光影。
- 冷暖：整体偏冷的灰绿与土褐，冬季偏冷、夏季略暖；朱红作人物暖点。
- 明暗 / 饱和：中低对比，色彩灰而透明；亮部在雪地与天空，暗部在前景树木。

## (3) 笔触与线条

- 笔触：细腻、平滑，层层罩染；风景用细笔点染，人物用小笔收形。`verbatim`
- 线条：轮廓线精细、清晰，人物与建筑的边缘准确。
- 质感：木板油画的平滑质感；雪地用铅白厚涂，远景用淡彩薄涂。

## (4) 构图习惯

- 画幅：风景与风俗画皆有；《雪中猎人》为横幅，高视点俯瞰雪谷。`verbatim`
- 视点：高视点俯瞰——地平线高，地面占大幅，观者如站在山坡上俯视全景。
- 布局：对角线构图——《雪中猎人》中前景猎人与狗沿对角线下坡，视线引向远方雪谷与溜冰者；《巴别塔》塔身居中、层层上升。`verbatim`
- 裁切：前景人物常被画框边缘截断，营造身临其境的近景感；远景人物极小、数量极多。

## (5) 光影与透视

- 光源：均匀的漫射光，无戏剧光源；冬季光冷而亮，夏季光暖而柔。
- 阴影：淡而清晰的阴影，体积靠罩染的透明层次。
- 透视：高视点世界风景——远景变淡、变蓝，空气透视与线性透视并用；空间深远而拥挤。

## (6) 该画什么 / 不该画什么

- 该画：四季风景、农民劳作与婚礼、雪地猎人与溜冰者、巴别塔。
- 不该画：明朗的理想风景；优雅的贵族人物；单一主角的肖像；大面积高饱和色。
- Negative prompt: `bright idealised landscape, elegant aristocratic figures, single-portrait composition, large areas of saturated colour, dramatic Baroque spotlight, loose impressionist dabs`

## (7) 测试提示词示例（现代题材：雪天的菜市场）

- Prompt: `In the style of Pieter Bruegel the Elder, a vegetable market on a snowy day in a modern city, Northern Renaissance oil on panel, high viewpoint world landscape, teeming people at work, muted earth colours, cold winter light, peasant life feeling, precise detail`
- 中文对照：老勃鲁盖尔风格，现代城市雪天的菜市场，北方文艺复兴木板油画，高视点世界风景，密密麻麻的人们劳作，土色为主，寒冷的冬日光线，农民生活的感觉，精确细节。
- Negative: 见第 (6) 节。
- 检验点：视点是否高而广阔；小人物是否密密麻麻、各有动作；雪地与冷光是否真实。
