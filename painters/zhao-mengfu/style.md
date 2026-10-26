# Zhao Mengfu — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhao Mengfu, Yuan literati painting, revival of Tang and Song antiquity, calligraphic brushwork, ink and light colour on paper, simple level distance, poetry calligraphy painting in one`
- ZH: 赵孟頫风格，元初文人画，复古唐宋，中锋书法用笔，纸本水墨淡彩，简淡平远，诗书画合一。

## (2) 色板方向

- 主色（颜料名）：墨色、淡赭、花青、淡石绿、淡石青、朱砂（点人物）。`verbatim` / `artifact`
- 辅色：淡赭、淡花青、淡石青，秋色淡染，朱砂只点人物。
- 禁色：青绿重彩；满幅全景；院体工整。
- 冷暖：墨分浓淡为主，暖色只作点染；整体清、亮、透，不沉。
- 明暗 / 饱和：靠墨的浓淡干湿，不靠明暗渐变；饱和度克制，亮在留白。

## (3) 笔触与线条

- 笔触：书法用笔：以中锋行笔如写字，山石、树木、坡岸皆如书法点画；飞白皴写坡石，枯笔见骨。`artifact`（台北故宫说明：中锋简淡笔法）
- 线条：书法性线条，中锋为主；轮廓不封闭，靠笔意收住形。
- 质感：绢 / 纸上水墨晕染 + 枯笔飞白；无油彩堆积，无工笔细线。

## (4) 构图习惯

- 画幅：平远为主：构图简洁，三段式平远，近岸、中水、远山，留白即水天；画面疏朗，诗书画各占其位。`verbatim`（《鹊华秋色图》）
- 视点：平视 / 轻微俯视；无焦点透视，散点 / 平面构成。
- 布局：题款、印章是构图的一部分，位置计入画面平衡。
- 裁切：平远三段，近岸、中水、远山，留白即水天；画面疏朗，不画满幅。

## (5) 光影与透视

- 光源：无固定光源；亮在留白水天，暗在淡墨层染；空间靠平远推远，不用焦点透视。`verbatim`
- 阴影：无写实阴影；墨的浓淡即体积，淡即远、浓即近。
- 透视：无焦点透视；空间靠留白 + 墨色浓淡推远近。

## (6) 该画什么 / 不该画什么

- 该画：鹊华秋色、水村、秋郊饮马、平远山水、枯木竹石、诗书画合一、复古笔意。`verbatim`
- 不该画：全景满幅、繁密皴擦、重彩青绿、焦点透视、院体工整、工笔细节。
- Negative prompt: `full panoramic mountains, dense texture strokes, heavy blue-green colour, linear perspective, neat academy finish, meticulous gongbi detail`

## (7) 测试提示词示例（现代题材：共享单车与落叶街道）

- Prompt: `In the style of Zhao Mengfu, shared bicycles on a leaf-strewn street in a modern city, calligraphic brushwork, ink and light colour on paper, simple level distance, poetry calligraphy painting in one, autumn colours`
- 中文对照：赵孟頫风格，现代城市落叶街道上的共享单车，书法用笔，纸本水墨淡彩，简淡平远，诗书画合一，秋色。
- Negative: 见第 (6) 节。
- 检验点：书法用笔与平远三段构图二者至少其一成立；画面是否简淡、诗书画合一，而不是只换了题材。
