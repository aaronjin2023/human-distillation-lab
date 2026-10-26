# Qiu Ying — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Qiu Ying, meticulous gongbi painting on silk, fine strong lines, blue-green landscape with mineral colours, detailed pavilions and architecture, elegant court ladies, rich yet refined colour, orderly and decorative`
- ZH: 仇英风格，绢本工笔重彩，线条精细劲健，青绿山水矿物设色，楼阁界画精细，宫廷仕女秀雅，设色丰富而雅致，工整华美。

## (2) 色板方向

- 主色（7 色，颜料名）：
- 石青
- 石绿
- 朱砂
- 赭石
- 藤黄
- 花青
- 墨色（勾线与分染）
- 主色 / 辅色：主色是石青、石绿青绿一路 + 朱砂点睛；辅色赭石、藤黄、花青，色比吴门淡墨一路浓得多、华美得多。`verbatim` / `artifact`（台北故宫：《汉宫春晓图》笔法精纯劲健、设色妍丽）
- 禁色：大写意狂笔；大面积留白；纯墨无色一路；粗笔皴擦。
- 冷暖：暖调为主，朱砂、赭石暖色点睛；石青石绿冷色作底，冷暖相衬，华美而不俗。
- 明暗 / 饱和：靠设色的层层罩染与线条的精细，不靠明暗渐变；饱和度中高，亮在朱砂楼柱与仕女衣饰处。

## (3) 笔触与线条

- 笔触：工笔细笔为主，笔触精细、劲健；勾线如铁线，皴擦少而精。`verbatim` / `artifact`
- 线条：线条精细劲健，如铁线描；轮廓清晰、比例合度，靠细笔的均匀提按收住形；建筑线条用界尺，横平竖直。
- 质感：绢本设色的平滑细腻感；矿物颜料层层罩染，色薄而透，无堆积。
- 关键技法：界画——以界尺画楼阁建筑，结构准确、可以居住；青绿设色——石青石绿层层罩染，华美而雅致；临古——临唐宋古画几可乱真。`artifact`（台北故宫藏品说明；画史通说）

## (4) 构图习惯

- 画幅：手卷为主；《汉宫春晓图》长卷 574.1 厘米，边展边看。`artifact`
- 视点：略高俯视；楼阁园林尽收眼底；无焦点透视，散点构成。
- 布局：楼阁分段隔景，仕女分群活动；建筑如舞台布景，视线随长卷右至左游走，一景一故事。
- 裁切：楼阁可顶边；园林层层分隔；不留大空白。

## (5) 光影与透视

- 光源：无固定光源；亮在朱砂楼柱与仕女衣饰处。
- 阴影：无写实阴影；设色的浓淡即远近，淡即远、浓即近。
- 透视：无焦点透视；空间靠楼阁的分隔与园林的层次推远近，华美而不乱。

## (6) 该画什么 / 不该画什么

- 该画：宫廷仕女、青绿山水、楼阁园林、历史故事；工笔重彩的华美一路。`verbatim`
- 不该画：大写意狂笔；大面积留白；纯墨无色；粗笔皴擦。
- Negative prompt: `freehand xieyi wild brushwork, large empty space, monochrome ink only, rough texture strokes, photorealistic detail, oil paint texture`

## (7) 测试提示词示例（现代题材：机场候机厅）

- Prompt: `In the style of Qiu Ying, an airport departure lounge in a modern city, meticulous gongbi painting on silk, fine strong lines, blue-green landscape with mineral colours, the lounge as a palace hall with detailed architecture, travellers as elegant court ladies, rich yet refined colour, orderly and decorative`
- 中文对照：仇英风格，现代城市机场候机厅，绢本工笔重彩，线条精细劲健，青绿设色，候机厅如宫殿楼阁，旅客如秀雅仕女，设色丰富而雅致，工整华美。
- Negative: 见第 (6) 节。
- 检验点：楼阁建筑是否界画般准确；人物是否秀雅有神；设色是否华美而不俗；是否没有狂笔留白。
