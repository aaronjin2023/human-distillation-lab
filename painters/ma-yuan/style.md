# Ma Yuan — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ma Yuan, Southern Song landscape, one-corner composition, large axe-cut texture strokes, ink and light colour on silk, half the picture empty mist, a tiny scholar in the corner`
- ZH: 马远风格，南宋山水，马一角构图，大斧劈皴，绢本水墨淡彩，半幅空作雾水，一角小景中一二人物。

## (2) 色板方向

- 主色（颜料名）：墨色、淡赭、花青、淡石绿、朱砂（点人物）。`verbatim` / `artifact`
- 辅色：淡赭、淡花青，墨色为主，朱砂只点人物。
- 禁色：青绿重彩；满幅全景；密皴重染。
- 冷暖：墨分浓淡为主，暖色只作点染；整体清、亮、透，不沉。
- 明暗 / 饱和：靠墨的浓淡干湿，不靠明暗渐变；饱和度克制，亮在留白。

## (3) 笔触与线条

- 笔触：大斧劈皴：方硬阔笔，侧锋劈出山石的棱角与体积，比郭熙云头皴更方、更劲；树多挺拔劲松，枝干如铁。`artifact`（画史通说；《踏歌图》画面可见）
- 线条：书法性线条，中锋为主；轮廓不封闭，靠笔意收住形。
- 质感：绢 / 纸上水墨晕染 + 枯笔飞白；无油彩堆积，无工笔细线。

## (4) 构图习惯

- 画幅：马一角：景物偏于一角，余下半幅以上留白作雾水；对角线分割，实角与虚空对峙，人物极小。`verbatim`（“一角马”通说）
- 视点：平视 / 轻微俯视；无焦点透视，散点 / 平面构成。
- 布局：题款、印章是构图的一部分，位置计入画面平衡。
- 裁切：马一角，景物偏于一角，余下半幅以上留白作雾水；不画满幅。

## (5) 光影与透视

- 光源：无固定光源；亮在留白雾水，暗在大斧劈的浓墨；空间靠实角与虚空的对比，不用焦点透视。`verbatim`
- 阴影：无写实阴影；墨的浓淡即体积，淡即远、浓即近。
- 透视：无焦点透视；空间靠留白 + 墨色浓淡推远近。

## (6) 该画什么 / 不该画什么

- 该画：一角山水、大斧劈皴、寒江独钓、踏歌、梅石溪凫、半幅留白、角落小景。`verbatim`
- 不该画：全景满幅、繁密云头皴、重彩青绿、焦点透视、满幅人物、工笔细节。
- Negative prompt: `full panoramic mountains filling the picture, dense cloud texture strokes, heavy blue-green colour, linear perspective, crowded figures, meticulous gongbi detail`

## (7) 测试提示词示例（现代题材：窗台上的咖啡与雨窗）

- Prompt: `In the style of Ma Yuan, a cup of coffee on a windowsill in a modern city, one-corner composition, large axe-cut texture strokes, half the picture empty mist, rain on the window as empty water, a tiny figure in the corner`
- 中文对照：马远风格，现代城市窗台上的一杯咖啡与雨窗，马一角构图，大斧劈皴，半幅空作雾水，雨窗即空水，一角一小人。
- Negative: 见第 (6) 节。
- 检验点：大斧劈皴与一角构图二者至少其一成立；半幅留白是否作雾水、人物是否极小，而不是只换了题材。
