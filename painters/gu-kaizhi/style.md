# Gu Kaizhi — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gu Kaizhi, Eastern Jin figure painting on silk, spring-silkworm-thread lines, slender elegant figures, flat mineral colour, narrative handscroll unfolding right to left`
- ZH: 顾恺之风格，东晋人物画，绢本，春蚕吐丝般细劲连绵的线条，人物修长秀美，平涂矿物色，叙事手卷自右向左展开。

## (2) 色板方向

- 主色（颜料名）：墨色、朱砂、赭石、花青、石绿、石青、藤黄。`verbatim` / `artifact`
- 辅色：淡赭染肤、淡花青衬底，衣纹以朱砂、石绿分段平涂，色不盖线。
- 禁色：水墨晕染大面积留白；浓墨皴染；写意泼墨。
- 冷暖：墨分浓淡为主，暖色只作点染；整体清、亮、透，不沉。
- 明暗 / 饱和：靠墨的浓淡干湿，不靠明暗渐变；饱和度克制，亮在留白。

## (3) 笔触与线条

- 笔触：线条为“春蚕吐丝”：细劲、连绵、均匀而有弹性，中锋行笔，起止藏锋，衣纹如高古游丝；面部以淡墨细线勾五官，点睛传神。`verbatim`（摹本画面可见）
- 线条：书法性线条，中锋为主；轮廓不封闭，靠笔意收住形。
- 质感：绢 / 纸上水墨晕染 + 枯笔飞白；无油彩堆积，无工笔细线。

## (4) 构图习惯

- 画幅：横向手卷叙事：右起左收，分段场景以山水树石隔开；人物成组作弧形 / 对峙安排，视线与姿态引导观者逐段读图；人物占幅不大，留白即水天。`verbatim`
- 视点：平视 / 轻微俯视；无焦点透视，散点 / 平面构成。
- 布局：题款、印章是构图的一部分，位置计入画面平衡。
- 裁切：横向手卷，场景随卷展开、逐段读图；人物成组不顶边，树石隔景，留白即水天。

## (5) 光影与透视

- 光源：无固定光源、无明暗体积；亮暗靠线与平涂色的疏密，空间靠上下叠置与隔景，不用焦点透视。`verbatim`
- 阴影：无写实阴影；墨的浓淡即体积，淡即远、浓即近。
- 透视：无焦点透视；空间靠留白 + 墨色浓淡推远近。

## (6) 该画什么 / 不该画什么

- 该画：宫廷人物、神话叙事、长卷分段故事、修长人物、淡彩平涂、题文与画面并置。`verbatim`
- 不该画：写实明暗、焦点透视、厚涂堆积、满幅山水、浓艳大面积平涂、现代透视建筑。
- Negative prompt: `photorealistic shading, linear perspective, thick impasto, crowded full landscape, heavy saturated colour filling the whole scroll, modern architecture`

## (7) 测试提示词示例（现代题材：便利店夜景）

- Prompt: `In the style of Gu Kaizhi, a small convenience store at night in a modern city, slender elegant figures in a narrative handscroll, spring-silkworm-thread lines on silk, flat mineral colour, scenes unfolding right to left, sparse trees dividing the scenes`
- 中文对照：顾恺之风格，现代城市里一家便利店的夜景，人物修长秀美，叙事手卷自右向左展开，春蚕吐丝细线，绢本平涂矿物色，树石隔景分段。
- Negative: 见第 (6) 节。
- 检验点：春蚕吐丝的线与人物神态（传神）二者至少其一成立；人物是否修长秀美、顾盼生姿，而不是只换了题材。
