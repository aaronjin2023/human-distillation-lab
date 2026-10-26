# Eugène Delacroix — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `French Romanticism, turbulent painterly brushstrokes, hot complementary colour clashes, diagonal surging composition, dramatic movement, sensual and violent energy`
- ZH: 法国浪漫主义，汹涌的绘画性笔触，炽热补色对撞，对角线汹涌构图，戏剧性动势，感性而暴烈的能量。

## (2) 色板方向

- 主色（7 色，颜料名）：朱红、铬黄、群青、翠绿、赭石、熟褐、铅白。`verbatim`
- 主色是高饱和补色对撞：朱红 vs 翠绿、铬黄 vs 群青；整体暖热、浓烈，比大卫的克制调艳得多。`verbatim`
- 辅色：橙黄、紫罗兰、暖灰。
- 禁色：克制灰调铺满；平滑无笔触；冷灰雾调；粉彩甜腻。
- 冷暖：暖热为主，冷色（群青、翠绿）作对撞点；冷暖对比强烈，是画面的能量来源。
- 明暗 / 饱和：中明度、高饱和、高对比；亮部直接用管装纯色，不经灰调过渡。

## (3) 笔触与线条

- 笔触：绘画性、汹涌、方向多变的笔触；笔触本身就是动势，方向跟随形体与情绪走。`verbatim`
- 线条：轮廓线被笔触打散，形靠色彩块面收住；无精细勾线。
- 质感：厚薄并存：亮部颜料稍厚，暗部薄涂；表面有明显的笔触起伏。

## (4) 构图习惯

- 画幅：大幅横幅历史画为主；《自由引导人民》1830 年，260×325cm；《萨达那帕拉之死》1827 年，横幅大场面。
- 视点：平视略低，观者被卷入人群 / 床榻边；视线随对角线冲向自由女神 / 萨达那帕拉。
- 布局：对角线 + 金字塔：自由女神在金字塔顶持旗，人群沿斜坡涌上；萨达那帕拉斜卧床上，人物与马匹沿对角线倾倒。
- 裁切：人物与尸体常顶边、裁边，制造“战场就在眼前”的压迫感。

## (5) 光影与透视

- 光源：戏剧性侧光 + 烟雾光：亮在自由女神的白衣与旗帜、萨达那帕拉的白袍与金器，暗部是烟与血。
- 阴影：阴影是彩色的（蓝紫、墨绿、暗红），不用纯黑；明暗靠补色对撞不靠灰阶。
- 透视：空间被动势压缩：前景尸体巨大、远景烟雾溶化；无严格焦点透视，空间靠色彩冷暖推远近。

## (6) 该画什么 / 不该画什么

- 该画：革命人群、自由女神、东方后宫与猎狮、垂死者与金器、马匹与猛兽。`verbatim`
- 不该画：克制灰调；平滑无笔触；冷灰雾调；纪念碑式对称。
- Negative prompt: `restrained grey palette, smooth invisible brushwork, cold grey haze, symmetrical monument, pastel sweetness, photorealistic polish`

## (7) 测试提示词示例（现代题材：共享单车）

- Prompt: `In the style of Eugene Delacroix, shared bicycles parked in a neat row on a modern city street at dawn, French Romanticism, turbulent painterly brushstrokes, hot complementary colour clashes, diagonal surging composition, dramatic movement`
- 中文对照：德拉克洛瓦风格，黎明时现代城市街道上一排整齐停放的共享单车，法国浪漫主义，汹涌绘画性笔触，炽热补色对撞，对角线汹涌构图，戏剧性动势。
- Negative: 见第 (6) 节。
- 检验点：单车是否排成汹涌的对角线、色彩是否补色对撞，而不是大卫式浮雕横排；笔触是否可见而汹涌。
