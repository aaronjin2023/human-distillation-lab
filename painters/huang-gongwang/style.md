# Huang Gongwang — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Huang Gongwang, Yuan literati landscape, dry brush and hemp-fibre texture strokes, long披麻皴, ink on paper, layered mountains in level distance, reclusion in the Fuchun mountains`
- ZH: 黄公望风格，元四家文人画，干笔披麻皴，长披麻皴，纸本水墨，层层平远山水，富春山居的隐逸之境。

## (2) 色板方向

- 主色（颜料名）：墨色、淡赭、花青、淡石绿。`verbatim` / `artifact`
- 辅色：淡赭（浅绛本色）淡染，淡花青染水天，墨色为主、赭石淡染。
- 禁色：青绿重彩；浓墨重皴；单峰满幅。
- 冷暖：墨分浓淡为主，暖色只作点染；整体清、亮、透，不沉。
- 明暗 / 饱和：靠墨的浓淡干湿，不靠明暗渐变；饱和度克制，亮在留白。

## (3) 笔触与线条

- 笔触：披麻皴：长短披麻皴写山石，干笔、渴笔见骨；长披麻皴如麻丝披覆，是黄公望的标志。`artifact`（画史通说；台北故宫说明）
- 线条：书法性线条，中锋为主；轮廓不封闭，靠笔意收住形。
- 质感：绢 / 纸上水墨晕染 + 枯笔飞白；无油彩堆积，无工笔细线。

## (4) 构图习惯

- 画幅：平远长卷：自右向左，江面、山峦、江汀交替，层层推远；山形圆浑，层层叠叠，意在可居可游。`verbatim`（《富春山居图》）
- 视点：平视 / 轻微俯视；无焦点透视，散点 / 平面构成。
- 布局：题款、印章是构图的一部分，位置计入画面平衡。
- 裁切：平远长卷自右向左，江面、山峦、江汀交替、层层推远；横向展开，不画满幅。

## (5) 光影与透视

- 光源：无固定光源；亮在留白江面，暗在披麻皴的层染；空间靠平远层层推远。`verbatim`
- 阴影：无写实阴影；墨的浓淡即体积，淡即远、浓即近。
- 透视：无焦点透视；空间靠留白 + 墨色浓淡推远近。

## (6) 该画什么 / 不该画什么

- 该画：富春山居、九峰雪霁、披麻皴、平远长卷、干笔渴笔、隐逸山水。`verbatim`
- 不该画：全景满幅高山、雨点皴密点、重彩青绿、焦点透视、工笔细节、热闹人物。
- Negative prompt: `towering peak filling the whole picture, dense raindrop texture, heavy blue-green colour, linear perspective, meticulous gongbi detail, crowded lively figures`

## (7) 测试提示词示例（现代题材：便利店夜景（秋））

- Prompt: `In the style of Huang Gongwang, a small convenience store at night in autumn in a modern city, dry brush and hemp-fibre texture strokes, ink on paper, layered mountains in level distance behind the street, reclusion in the midst of the city`
- 中文对照：黄公望风格，现代城市秋夜一家便利店，干笔披麻皴，纸本水墨，街后层层平远山水，闹中取静的隐逸之境。
- Negative: 见第 (6) 节。
- 检验点：披麻皴与平远长卷构图二者至少其一成立；山形是否圆浑层叠、可居可游，而不是只换了题材。
