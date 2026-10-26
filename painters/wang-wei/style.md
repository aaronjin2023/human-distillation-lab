# Wang Wei — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Wei, Tang ink landscape, pale ink wash, sparse texture strokes, poetic emptiness, snow and mist, mountains as silhouettes, painting within poetry`
- ZH: 王维风格，唐人水墨山水，淡墨晕染，皴法极少，诗意空寂，雪溪雾气，山形如剪影，诗中有画、画中有诗。

## (2) 色板方向

- 主色（颜料名）：墨色、淡赭、花青、淡石绿、淡石青。`verbatim` / `artifact`
- 辅色：破墨淡染，淡赭点远山、淡花青染水天，色不盖墨。
- 禁色：青绿重彩；浓墨重皴；满幅重彩平涂。
- 冷暖：墨分浓淡为主，暖色只作点染；整体清、亮、透，不沉。
- 明暗 / 饱和：靠墨的浓淡干湿，不靠明暗渐变；饱和度克制，亮在留白。

## (3) 笔触与线条

- 笔触：淡墨为主，皴极少：山形以淡墨晕染出轮廓，少用或不用繁密皴擦；线条如诗句般简净，笔意在淡不在浓。`artifact`（董其昌题跋转述：雪溪图“惟有山水轮廓，几无皴法”一路的说法，见 conflicts.md）
- 线条：书法性线条，中锋为主；轮廓不封闭，靠笔意收住形。
- 质感：绢 / 纸上水墨晕染 + 枯笔飞白；无油彩堆积，无工笔细线。

## (4) 构图习惯

- 画幅：平远与深远并用：近景小丘、远景淡山，中间以水雾留白隔开；画面疏朗，景物少而意远，辋川二十景式分段列景。`verbatim`（辋川摹本）
- 视点：平视 / 轻微俯视；无焦点透视，散点 / 平面构成。
- 布局：题款、印章是构图的一部分，位置计入画面平衡。
- 裁切：平远疏朗，近景小丘、远景淡山，中以水雾留白隔开；景物少而意远，不画满幅。

## (5) 光影与透视

- 光源：无固定光源；雪与雾即光，淡墨即影；亮在留白，暗在淡染，空间靠墨色由浓到淡推远。`verbatim`
- 阴影：无写实阴影；墨的浓淡即体积，淡即远、浓即近。
- 透视：无焦点透视；空间靠留白 + 墨色浓淡推远近。

## (6) 该画什么 / 不该画什么

- 该画：雪溪、辋川别业、雾中山水、疏林小屋、诗意空寂的淡墨山水、留白作水雾。`verbatim`
- 不该画：繁密皴擦、重彩青绿、满幅山石、焦点透视、浓艳设色、工笔细节。
- Negative prompt: `dense texture strokes, heavy blue-green colour, crowded full mountains, linear perspective, saturated colour, meticulous gongbi detail`

## (7) 测试提示词示例（现代题材：深夜拉面店）

- Prompt: `In the style of Wang Wei, a late-night ramen shop in a modern city, pale ink wash, sparse texture strokes, steam as mist, mountains as silhouettes in the distance, poetic emptiness, painting within poetry`
- 中文对照：王维风格，现代城市一家深夜拉面店，淡墨晕染，皴法极少，蒸汽如雾，远山如剪影，诗意空寂，诗中有画。
- Negative: 见第 (6) 节。
- 检验点：破墨淡染与平远疏朗构图二者至少其一成立；画面是否诗意空寂、景少意远，而不是只换了题材。
