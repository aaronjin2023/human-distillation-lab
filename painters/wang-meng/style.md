# Wang Meng — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Meng, dense literati ink landscape on paper, ropy layered brushstrokes, ox-hair and unravelled-rope texture strokes piled into masses of texture, full composition with no empty space, ochre and light blue-green accents, deep and lush`
- ZH: 王蒙风格，纸上密体文人水墨山水，层层叠叠的绳索状笔触，牛毛皴与解索皴堆出厚重肌理，满幅构图几无留白，赭石与淡青绿点染，深厚华滋。

## (2) 色板方向

- 主色（6 色，颜料名）：
- 墨色（浓—淡—干—湿分层）
- 赭石
- 花青
- 淡石绿
- 淡朱砂（极少，秋色点染）
- 纸白（极少，仅作气口）
- 主色 / 辅色：主色是墨色 + 赭石；辅色花青、淡石绿点染秋色，色比倪瓒暖、比董其昌浓。`verbatim` / `artifact`（台北故宫《林屋洞》说明：树以赭与朱洗出秋意）
- 禁色：大面积留白；纯墨无色一路；疏朗一河两岸。
- 冷暖：暖调为主，赭石暖色压住全幅；花青冷色只作点缀，整体深厚、华滋。
- 明暗 / 饱和：靠墨的层层叠加与赭石点染，不靠明暗渐变；饱和度中高，亮在少数气口与赭石处。

## (3) 笔触与线条

- 笔触：笔触密而多变：解索皴（绳索状曲笔层层叠加）、牛毛皴（细密短笔如牛毛）、渴笔焦墨；笔笔相叠，肌理厚重。`verbatim` / `artifact`
- 线条：线条曲折盘绕，如绳索解开；轮廓不求方折，靠层叠的曲笔堆出山形；线条多而密，一笔压一笔。
- 质感：纸上层层叠加的绳索状肌理，厚而不板；墨色浓淡干湿交错，如乱麻而有条理。
- 关键技法：解索皴与牛毛皴——把马夏的斧劈皴化整为碎、化直为曲，细笔变粗笔、圆转处变断笔，堆出密体山水。`artifact`（画史通说）

## (4) 构图习惯

- 画幅：竖幅大轴为主；满幅构图。
- 视点：平视 / 轻微俯视；无焦点透视，散点构成，但山形层层向内收。
- 布局：满幅：山石、树木、溪流、屋宇层层叠叠塞满画面，只留少数气口；视线在密体中迂回，无一处大留白。
- 裁切：主体顶边是常态；不留大空白；前景遮挡多。

## (5) 光影与透视

- 光源：无固定光源；亮在气口与赭石点染处。
- 阴影：无写实阴影；墨的浓淡干湿即体积，层叠即深远。
- 透视：无焦点透视；空间靠层叠的山形与气口推远近，深而不空。

## (6) 该画什么 / 不该画什么

- 该画：密体山水、层叠山石、曲折溪流、隐居屋宇、秋色点染；满幅的深山。`verbatim`
- 不该画：大面积留白；疏朗一河两岸；纯墨无色；高耸孤峰独占画面。
- Negative prompt: `large empty space, sparse one-river-two-banks composition, monochrome ink only, single isolated peak, photorealistic detail, oil paint texture`

## (7) 测试提示词示例（现代题材：深夜拉面店）

- Prompt: `In the style of Wang Meng, a late-night ramen shop in a modern city, dense literati ink landscape on paper, ropy layered brushstrokes, ox-hair and unravelled-rope texture strokes piled into masses of texture, the shop buried in layered rooftops and tangled wires, ochre and light blue-green accents, deep and lush, almost no empty space`
- 中文对照：王蒙风格，现代城市里一家深夜拉面店，密体文人水墨，绳索状笔触层层叠叠，牛毛皴与解索皴堆出厚重肌理，拉面店埋在层叠屋顶与纠结电线之中，赭石与淡青绿点染，深厚华滋，几乎没有留白。
- Negative: 见第 (6) 节。
- 检验点：画面是否密而不乱；屋顶电线是否像解索皴一样层层盘绕；是否没有大留白；赭石点染是否只作秋色。
