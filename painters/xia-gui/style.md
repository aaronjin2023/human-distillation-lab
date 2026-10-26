# Xia Gui — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xia Gui, Southern Song landscape, half-side composition, split brush and ink wash, misty streams and distant peaks, dramatic diagonals, ink on paper, vast emptiness`
- ZH: 夏圭风格，南宋山水，夏半边构图，破笔水墨，溪山清远，斜角取势，纸本水墨，空阔苍茫。

## (2) 色板方向

- 主色（颜料名）：墨色、淡赭、花青、淡石绿。`verbatim` / `artifact`
- 辅色：淡赭、淡花青，墨色为主，几乎无色，以水墨为主。
- 禁色：青绿重彩；满幅全景；工笔细描。
- 冷暖：墨分浓淡为主，暖色只作点染；整体清、亮、透，不沉。
- 明暗 / 饱和：靠墨的浓淡干湿，不靠明暗渐变；饱和度克制，亮在留白。

## (3) 笔触与线条

- 笔触：破笔 / 劈笔：以破笔、散锋写山石树木，笔触苍劲简率；水墨晕染层次极细，雾气以淡墨层层推出。`artifact`（画史通说；《溪山清远图》画面可见）
- 线条：书法性线条，中锋为主；轮廓不封闭，靠笔意收住形。
- 质感：绢 / 纸上水墨晕染 + 枯笔飞白；无油彩堆积，无工笔细线。

## (4) 构图习惯

- 画幅：夏半边：景物偏于半边，余下半幅留白作水天；斜角取势，实与虚沿对角线交错，画面动势比马远更放逸。`verbatim`
- 视点：平视 / 轻微俯视；无焦点透视，散点 / 平面构成。
- 布局：题款、印章是构图的一部分，位置计入画面平衡。
- 裁切：夏半边，景物偏于半边，余下半幅留白作水天；不画满幅。

## (5) 光影与透视

- 光源：无固定光源；亮在留白水天，暗在破笔浓墨；空间靠墨色由浓到淡、由实到虚推远。`verbatim`
- 阴影：无写实阴影；墨的浓淡即体积，淡即远、浓即近。
- 透视：无焦点透视；空间靠留白 + 墨色浓淡推远近。

## (6) 该画什么 / 不该画什么

- 该画：半边山水、溪山清远、雨中归舟、山水十二景式长卷、破笔水墨、斜角构图。`verbatim`
- 不该画：全景满幅、工整一角、重彩青绿、焦点透视、满幅人物、工笔细节。
- Negative prompt: `full panoramic mountains, neat one-corner symmetry, heavy blue-green colour, linear perspective, crowded figures, meticulous gongbi detail`

## (7) 测试提示词示例（现代题材：深夜拉面店的蒸汽）

- Prompt: `In the style of Xia Gui, a late-night ramen shop in a modern city, half-side composition, split brush and ink wash, steam as mist, dramatic diagonals, vast emptiness, ink on paper`
- 中文对照：夏圭风格，现代城市一家深夜拉面店的蒸汽，夏半边构图，破笔水墨，蒸汽如雾，斜角取势，空阔苍茫，纸本水墨。
- Negative: 见第 (6) 节。
- 检验点：破笔水墨与半边构图二者至少其一成立；画面是否空阔苍茫、斜角取势，而不是只换了题材。
