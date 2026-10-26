# Juan Luna — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Academic history painting, huge canvas, dramatic chiaroscuro, crowded figure groups, classical anatomy, dark warm palette with flesh tones`
- ZH: 学院派历史大画，巨幅画布，戏剧性明暗对照，拥挤的人体群像，古典解剖，暗暖调与肤色。

## (2) 色板方向

- 主色（7 色，颜料名）：赭石、深褐、朱红、群青、墨绿、金黄、肤色（铅白 + 朱红）。`verbatim` / `artifact`
- 以暗暖调为主，肤色是全幅最亮处：《斯波利arium》以死去角斗士的苍白肤色对照暗红的 arena。`verbatim`
- 辅色：淡黄画光斑、灰色画烟尘。
- 禁色：平涂无明暗；高饱和大面积平涂；浮世绘式轮廓线。
- 冷暖：整体偏暖偏暗，暖褐与暗红主调，冷色只作背景的点缀。
- 明暗 / 饱和：明暗对照强烈：光从一侧打来，暗部用深褐，亮部用肤色与金黄；阴影有彩色倾向。

## (3) 笔触与线条

- 笔触：学院派油画笔触，人体以细笔层层叠加，衣纹以阔笔扫出；动势靠笔触方向。`verbatim`
- 线条：轮廓线为油画的明暗交界线，非独立的线；人体的轮廓以明暗收住。`verbatim`
- 质感：油彩的厚薄并置——人体厚涂，背景薄涂；无木刻刀味，无水墨晕染。

## (4) 构图习惯

- 画幅：巨幅横幅，《斯波利arium》4.22 × 7.675 米，是菲律宾最大的油画。`artifact`
- 视点：平视 / 轻微仰视；对角线构图，死去的角斗士自左下拖向右上。`verbatim`
- 布局：中心偏左的尸体堆是视觉焦点，右侧拖尸者与左侧围观者形成对照，视线在尸体与拖尸者之间往返。`verbatim`
- 裁切：群像常被裁掉边缘，画面之外仍有角斗场。

## (5) 光影与透视

- 光源：单光源明暗对照，戏剧性光影；亮在死去角斗士的肤色上。
- 阴影：深褐阴影，有彩色倾向；暗部不是纯黑，是暗红的深处。
- 透视：焦点透视与空气透视并用，远景以淡色推远。

## (6) 该画什么 / 不该画什么

- 该画：斯波利arium、克利奥帕特拉之死、血之契约、勒班陀海战、罗马风俗。`verbatim`
- 不该画：平涂无明暗；灰调写实；浮世绘式轮廓线；无群像的小幅风景。
- Negative prompt: `flat colour without chiaroscuro, grey muted palette, ukiyo-e outlines, photorealistic detail without drama, small-scale landscape`

## (7) 测试提示词示例（现代题材：共享单车）

- Prompt: `In the style of Juan Luna, people riding shared bicycles in a modern city, academic history painting, huge canvas feeling, dramatic chiaroscuro, crowded figure groups, classical anatomy, dark warm palette with flesh tones`
- 中文对照：胡安·卢纳风格，现代城市里人们骑着共享单车，学院派历史大画，巨幅感，戏剧性明暗对照，拥挤的人体群像，古典解剖，暗暖调与肤色。
- Negative: 见第 (6) 节。
- 检验点：群像是否拥挤、明暗对照是否戏剧性；人体是否解剖准确。
