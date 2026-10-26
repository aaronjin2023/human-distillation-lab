# Wen Zhengming — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wen Zhengming, refined literati ink landscape on paper, fine controlled brushwork, elegant and unhurried, light ink with pale ochre and blue-green washes, small scholar studio in a quiet landscape, calligraphy integrated, calm and scholarly`
- ZH: 文徵明风格，纸上细笔文人山水，笔法细劲从容，淡墨轻染，淡赭与淡青绿微染，幽静山水中的小小文斋，书法入画，淡雅秀润。

## (2) 色板方向

- 主色（6 色，颜料名）：
- 墨色（浓—淡—干—湿分层）
- 淡赭石
- 淡花青
- 淡石绿
- 淡朱砂（极少）
- 纸白（留白即云雾）
- 主色 / 辅色：主色是淡墨 + 淡赭；辅色淡花青、淡石绿微染，色比沈周更淡、更雅。`verbatim`
- 禁色：粗野狂笔；重彩大面积平涂；满幅密体。
- 冷暖：暖调为主，淡赭暖色轻轻压住全幅；整体淡、雅、静。
- 明暗 / 饱和：靠墨的浓淡与细笔的从容，不靠明暗渐变；饱和度低，亮在留白处。

## (3) 笔触与线条

- 笔触：细笔为主，笔触细劲、从容、秀润；用笔力求“细而不弱”，皴擦轻而有骨。`verbatim` / `artifact`（大英百科：其画从高度精细到自由洗染皆有）
- 线条：线条细劲挺拔，如行书；轮廓清晰而秀润，靠细笔的提按收住形；线条多而匀，一笔是一笔。
- 质感：纸上淡墨轻染 + 细笔擦出的细腻感；墨色薄而透，无堆积；有“细而不板”的质感。
- 关键技法：仿古——以细笔仿王蒙、吴镇、赵孟頫等古人，仿其意而不泥其形；书法入画——行草书的笔意直接进山水。`artifact`（大英百科；画史通说）

## (4) 构图习惯

- 画幅：竖幅 / 横幅 / 手卷皆有；《真赏斋图》为小品，斋馆小景。
- 视点：平视 / 轻微俯视；无焦点透视，散点构成。
- 布局：山水环抱一小斋，斋馆偏一角，山势舒缓；留白适中，不疏不密，视线从斋馆游向远山。
- 裁切：主体不顶边；山势舒缓，不画高耸主峰；不画满幅。

## (5) 光影与透视

- 光源：无固定光源；亮在留白云雾与纸白。
- 阴影：无写实阴影；墨的浓淡即远近，淡即远、浓即近。
- 透视：无焦点透视；空间靠山水的舒缓与留白推远近，静而不空。

## (6) 该画什么 / 不该画什么

- 该画：幽静山水、文斋小景、兰竹、人物小品；仿古山水与诗书画合一。`verbatim`
- 不该画：粗野狂笔；重彩满幅；密体满幅；院体楼阁。
- Negative prompt: `wild unrestrained brushwork, heavy colour filling the whole paper, dense full composition, court-style detailed pavilions, photorealistic detail, oil paint texture`

## (7) 测试提示词示例（现代题材：共享单车）

- Prompt: `In the style of Wen Zhengming, shared bicycles parked by a street in a modern city, refined literati ink landscape on paper, fine controlled brushwork, elegant and unhurried, light ink with pale ochre and blue-green washes, the bicycles as a quiet scholar studio in a calm landscape, calligraphy-like lines`
- 中文对照：文徵明风格，现代城市街边停放的共享单车，细笔文人水墨，笔法细劲从容，淡墨轻染，淡赭与淡青绿微染，单车如幽静山水中的小小文斋，线条如书法，淡雅秀润。
- Negative: 见第 (6) 节。
- 检验点：单车是否画得从容秀润而不是狂笔；淡彩是否只微染；画面是否淡雅而不是拥挤。
