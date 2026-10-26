# Giotto di Bondone — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Giotto di Bondone, early Renaissance buon fresco, solid sculptural figures with real weight, muted earth colours, deep blue sky, diagonal composition, sincere human grief`
- ZH: 乔托风格，早期文艺复兴湿壁画，人物结实有分量，土色为主，深蓝天空，对角线构图，情感真挚。

## (2) 色板方向

- 主色（7 色，颜料名）：群青（天空与圣母袍）、赭石、土黄、土红、铅白、墨绿、淡粉肤色。`verbatim`
- 辅色：灰绿（山石）、暗褐（阴影）。
- 禁色：金底满铺；高饱和的后世油画色；细腻的学院式渐变。
- 冷暖：暖土色人物配冷群青天空，冷暖对峙但不刺眼。
- 明暗 / 饱和：中低对比，靠明暗塑造体积，不靠强烈明暗反差；饱和度克制，灰泥质感明显。

## (3) 笔触与线条

- 笔触：湿壁画笔触，色块平实、边缘肯定，少有拖泥带水的晕染；衣纹用几笔宽阔的明暗带出体积。`verbatim`
- 线条：轮廓线沉稳、粗细均匀，不追求书法性；人物造型靠体块而非线条。
- 质感：灰泥墙面质感，颜料渗入墙体，表面哑光、颗粒感；干壁补色处略亮。

## (4) 构图习惯

- 画幅：壁画横幅为主，斯克罗维尼礼拜堂为连续叙事组画，单幅约 200×185 厘米。`artifact`
- 视点：平视略俯，观者站在场景前方地面高度。
- 布局：对角线构图——《哀悼基督》中山坡从右上斜落至左下基督头部，视线沿山坡滑向主体；人物成群蹲伏在前景，地面占画面下半部。`verbatim`
- 裁切：人物常被画框边缘截断，营造身临其境的近景感；天使群占满天空上部。

## (5) 光影与透视

- 光源：均匀的漫射光，无单一戏剧光源；光从画面外上方来，人物受光面一致。
- 阴影：淡灰褐阴影，体积靠明暗两大面，不靠细碎过渡。
- 透视：直觉透视而非数学透视——建筑略有缩短、人物按前后重叠定远近；空间感来自人物体量与重叠，而非灭点。`artifact`（学界共识：乔托用直觉透视，马萨乔才系统化）

## (6) 该画什么 / 不该画什么

- 该画：圣经叙事群像；蹲伏、俯身、怀抱等沉重身体动作；岩石山坡、简朴建筑；天使群。
- 不该画：金底平面装饰；纤细哥特式人物；华丽繁复的图案；后世巴洛克式的戏剧光影。
- Negative prompt: `gold leaf background, thin Gothic figures, ornate decoration, Baroque dramatic spotlight, smooth academic blending, photorealistic detail`

## (7) 测试提示词示例（现代题材：深夜拉面店）

- Prompt: `In the style of Giotto di Bondone, a late-night ramen shop in a modern city, early Renaissance fresco, solid sculptural figures with real weight, a cook leaning over the counter and customers crouched on stools, muted earth colours, deep blue night sky, diagonal composition, sincere human warmth, buon fresco on plaster`
- 中文对照：乔托风格，现代城市里的一家深夜拉面店，早期文艺复兴湿壁画，人物结实沉重，厨师俯身在柜台后、食客坐在凳子上，土色为主，深蓝夜空，对角线构图，真挚的人情味。
- Negative: 见第 (6) 节。
- 检验点：人物是否像石块一样落地、有分量，而不是轻飘的插画人物；构图是否有对角线把视线引向主体；是否没有金底和巴洛克式聚光。
