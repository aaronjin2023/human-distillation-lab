# Raden Saleh — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Romantic oil painting, dramatic diagonal composition, strong chiaroscuro, wild animals and historical drama, stormy tropical landscape, detailed anatomy`
- ZH: 浪漫主义油画，戏剧性对角线构图，强烈明暗对照，野兽与历史场面，暴风雨般的热带风景，解剖学准确的动物。

## (2) 色板方向

- 主色（7 色，颜料名）：赭石、深褐、朱红、群青、墨绿、金黄、白垩白。`verbatim` / `artifact`
- 以暖褐与金黄为主，朱红点睛，群青与墨绿画热带丛林与夜空；明暗对照强烈。`verbatim`
- 辅色：淡黄画光斑、灰色画烟尘。
- 禁色：平涂无明暗；灰暗土色大面积平涂；浮世绘式轮廓线。
- 冷暖：整体偏暖，暖褐与金黄主调，冷色只作丛林与夜空的点缀。
- 明暗 / 饱和：明暗对照强烈：光从一侧打来，暗部用深褐，亮部用金黄与白；阴影有彩色倾向。

## (3) 笔触与线条

- 笔触：学院派油画笔触，动物毛发以细笔层层叠加，丛林以阔笔扫出；动势靠笔触方向。`verbatim`
- 线条：轮廓线为油画的明暗交界线，非独立的线；动物的轮廓以明暗收住。`verbatim`
- 质感：油彩的厚薄并置——动物毛发厚涂，远景薄涂；无木刻刀味，无水墨晕染。

## (4) 构图习惯

- 画幅：横幅大画为主，《迪波内戈罗被捕》为历史大画。`artifact`
- 视点：平视 / 轻微仰视；对角线构图，动势自左下冲向右上。`verbatim`
- 布局：中心人物（迪波内戈罗）立于画面中心偏右，荷兰军官环绕，视线落在被捕者的挺立身姿上；狮子猎手一路以狮子与猎物的搏斗为中心。`verbatim`
- 裁切：搏斗场面常被裁掉边缘，画面之外仍有野兽。

## (5) 光影与透视

- 光源：单光源明暗对照，戏剧性光影；亮在被捕者与狮子的身上。
- 阴影：深褐阴影，有彩色倾向；暗部不是纯黑，是暖褐的深处。
- 透视：焦点透视与空气透视并用，远景丛林以淡色推远。

## (6) 该画什么 / 不该画什么

- 该画：迪波内戈罗被捕、狮子猎手、受伤的狮子、爪哇风景、火山、狩猎。`verbatim`
- 不该画：平涂无明暗；灰调写实；浮世绘式轮廓线；无动势的静态风景。
- Negative prompt: `flat colour without chiaroscuro, grey muted palette, ukiyo-e outlines, photorealistic detail without drama, static composition`

## (7) 测试提示词示例（现代题材：深夜拉面店）

- Prompt: `In the style of Raden Saleh, a ramen shop late at night in a modern city, Romantic oil painting, dramatic diagonal composition, strong chiaroscuro, stormy tropical sky above the shop, detailed anatomy of the people, warm ochre and gold against deep green night`
- 中文对照：拉登·萨利赫风格，深夜的拉面店，浪漫主义油画，戏剧性对角线构图，强烈明暗对照，店上方暴风雨般的热带夜空，人物解剖准确，暖赭与金黄对照深绿夜色。
- Negative: 见第 (6) 节。
- 检验点：对角线动势是否强烈、明暗对照是否戏剧性；人物与动物是否解剖准确。
