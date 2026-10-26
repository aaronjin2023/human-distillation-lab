# Ni Zan — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ni Zan, sparse literati ink landscape on paper, dry brush, folded-belt texture strokes, a few bare trees on a near bank, vast empty water, distant low hills, no figures, monochrome ink, quiet and austere`
- ZH: 倪瓒风格，纸上疏朗文人水墨山水，枯笔，折带皴，近岸几株枯树，大片空白水面，远处低矮远山，无人物，纯墨色，清寂萧疏。

## (2) 色板方向

- 主色（5 色，颜料名）：
- 墨色（浓—淡—干—湿分层）
- 淡赭石
- 淡花青
- 纸白（留白即水）
- 淡石绿（极少，仅远山微染）
- 主色 / 辅色：主色是墨色浓淡 + 纸白；辅色淡赭、淡花青只作远山微染，绝不抢墨。`verbatim`
- 禁色：重彩大面积平涂；浓艳朱砂、石绿石青大面积设色；满幅构图。
- 冷暖：冷调为主，墨色偏冷；暖只在淡赭微染处，整体清、冷、空。
- 明暗 / 饱和：靠墨的干湿浓淡，不靠明暗渐变；饱和度极低，亮在留白。

## (3) 笔触与线条

- 笔触：枯笔、干笔为主，中锋侧锋并用，折带皴：短促方折的横笔，一层层叠出坡石的棱角。`verbatim` / `artifact`
- 线条：树干线条细劲挺拔，如折钗股；轮廓不封闭，靠枯笔飞白收住形；线条少而精，一笔是一笔。
- 质感：纸上干笔擦出的沙砾感；墨色薄而透，无堆积；水面完全留白，靠纸的白做水。
- 关键技法：折带皴——以方折短笔横向叠擦画坡石，棱角分明；逸笔草草——看似草草，实则一笔不苟。`artifact`（画史通说）

## (4) 构图习惯

- 画幅：横幅 / 竖幅小品为主；一河两岸是定式。
- 视点：平视 / 轻微俯视；无焦点透视，散点构成。
- 布局：近岸（枯树 + 坡石 + 茅亭或空屋）— 中景大片空白水面 — 远岸低矮远山，三段式；主体偏下，留白占画面一半以上。
- 裁切：主体不顶边；远山低矮，不画高耸主峰；不画满幅。

## (5) 光影与透视

- 光源：无固定光源；亮在留白的水面与纸白。
- 阴影：无写实阴影；墨的浓淡即远近，淡即远、浓即近。
- 透视：无焦点透视；空间靠三段式留白 + 墨色浓淡推远近。

## (6) 该画什么 / 不该画什么

- 该画：枯树、坡石、茅亭、远山、空白水面；一河两岸的疏朗山水。`verbatim`
- 不该画：人物（几乎不画人）；满幅山水；重彩；高耸主峰；浓密树林。
- Negative prompt: `figures and people, crowded full composition, heavy colour, tall towering main peak, dense forest, photorealistic detail, oil paint texture`

## (7) 测试提示词示例（现代题材：便利店夜景）

- Prompt: `In the style of Ni Zan, a small convenience store at night in a modern city, sparse literati ink landscape on paper, dry brush, folded-belt texture strokes, the shop as a lone hut on a near bank, vast empty dark water-like street, distant low rooftops, no people, monochrome ink, quiet and austere`
- 中文对照：倪瓒风格，现代城市里一家深夜便利店，疏朗文人水墨，枯笔折带皴，便利店如近岸一座孤亭，大片空白如水的街道，远处低矮屋顶，无人，纯墨色，清寂萧疏。
- Negative: 见第 (6) 节。
- 检验点：画面是否疏朗而不是画满；便利店是否像近岸孤亭；水面式的留白是否成立；是否没有人物。
