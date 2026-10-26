# Wang Hui — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Hui, orthodox literati ink landscape on paper, synthesis of ancient masters, fine controlled brushwork, light ochre and blue-green washes, layered mountains in the manner of Huang Gongwang, calm and accomplished, scholarly and complete`
- ZH: 王翚风格，纸上正统文人山水，集古人大成，笔法细劲从容，浅绛设色，层叠山峦取黄公望一路，沉静华滋，学养完备。

## (2) 色板方向

- 主色（6 色，颜料名）：
- 墨色（浓—淡—干—湿分层）
- 赭石
- 花青
- 淡石绿
- 淡朱砂（秋色点染）
- 纸白（留白即云雾）
- 主色 / 辅色：主色是淡墨 + 赭石浅绛；辅色花青、淡石绿微染，秋色淡朱砂点睛。`verbatim`
- 禁色：狂笔写意；重彩大面积平涂；满幅密体；写实透视。
- 冷暖：暖调为主，赭石暖色轻轻压住全幅；整体沉静、华滋。
- 明暗 / 饱和：靠墨的浓淡与设色的浅绛，不靠明暗渐变；饱和度中等，亮在秋色与留白处。

## (3) 笔触与线条

- 笔触：笔法细劲从容，集各家之长：黄公望的披麻、董源的披麻、倪瓒的折带，皆化入一笔。`verbatim` / `artifact`（普林斯顿美术馆：仿黄公望一路）
- 线条：线条细劲挺拔，如行书；轮廓清晰而秀润，靠细笔的提按收住形。
- 质感：纸上淡墨轻染 + 细笔擦出的细腻感；墨色薄而透，无堆积。
- 关键技法：仿古集大成——一幅画中兼仿数家而不露痕迹；浅绛设色——赭石为主的淡彩，华滋而不俗。`artifact`（画史通说）

## (4) 构图习惯

- 画幅：竖幅大轴 / 手卷皆有；《千岩万壑图》为大轴，层叠千岩。
- 视点：平视 / 轻微俯视；无焦点透视，散点构成。
- 布局：层叠山峦占画面大半，山脚溪流屋宇，留白适中；视线从山脚游向远山，再由题跋收回来。
- 裁切：主体可顶边；山势层叠，不画孤峰；不画满幅细节。

## (5) 光影与透视

- 光源：无固定光源；亮在留白云雾与秋色处。
- 阴影：无写实阴影；墨的浓淡即远近，淡即远、浓即近。
- 透视：无焦点透视；空间靠层叠的山形与留白推远近，深而不空。

## (6) 该画什么 / 不该画什么

- 该画：层叠山水、仿古山水、秋色山水；正统派的集大成一路。`verbatim`
- 不该画：狂笔写意；重彩满幅；密体满幅；写实透视。
- Negative prompt: `wild unrestrained brushwork, heavy colour filling the whole paper, dense full composition, realistic perspective space, photorealistic detail, oil paint texture`

## (7) 测试提示词示例（现代题材：雨夜公交站）

- Prompt: `In the style of Wang Hui, a bus stop on a rainy night in a modern city, orthodox literati ink landscape on paper, synthesis of ancient masters, fine controlled brushwork, light ochre and blue-green washes, layered rooftops in the manner of Huang Gongwang, calm and accomplished`
- 中文对照：王翚风格，现代城市雨夜公交站，正统文人山水，集古人大成，笔法细劲从容，浅绛设色，层叠屋顶取黄公望一路，沉静华滋。
- Negative: 见第 (6) 节。
- 检验点：屋顶是否层叠有致而不是杂乱；浅绛设色是否华滋而不俗；画面是否沉静而不是拥挤。
