# Tang Yin — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tang Yin, elegant literati painting on paper, graceful flowing lines, refined ink with light colour, beautiful lady or scholar in a quiet landscape, pine and mountain in Southern Song manner, poetic and romantic, light ochre accents`
- ZH: 唐寅风格，纸上俊逸文人画，线条流畅秀润，淡墨轻彩，幽静山水中的美人或文人，松山取南宋一路，诗意浪漫，淡赭微染。

## (2) 色板方向

- 主色（6 色，颜料名）：
- 墨色（浓—淡—干—湿分层）
- 淡赭石
- 淡花青
- 淡石绿
- 淡朱砂（仕女衣饰微染）
- 纸白（留白即秋意）
- 主色 / 辅色：主色是淡墨 + 淡赭；辅色淡花青、淡石绿微染，仕女衣饰淡朱砂点睛。`verbatim`
- 禁色：粗野狂笔；重彩大面积平涂；满幅密体；板滞院体。
- 冷暖：暖调为主，淡赭暖色轻轻压住全幅；整体俊逸、明润。
- 明暗 / 饱和：靠墨的浓淡与线条的流畅，不靠明暗渐变；饱和度低中，亮在留白与仕女衣饰处。

## (3) 笔触与线条

- 笔触：笔法兼擅：山水学李唐、马夏一路，粗笔中见秀润；人物衣纹细劲流畅，如行云流水。`verbatim` / `artifact`（台北故宫：笔法略粗而线条劲健有神）
- 线条：线条流畅秀润，仕女衣纹如行云流水；轮廓清晰而柔美，靠细笔的提按收住形。
- 质感：纸上淡墨轻染 + 细笔擦出的细腻感；墨色薄而透，无堆积。
- 关键技法：兼擅——山水取南宋李唐、马远、夏圭一路，人物取仕女一路，花鸟取文人一路，三路同属一个 skill；临古化古，不泥古人。`artifact`（中国在线博物馆）

## (4) 构图习惯

- 画幅：竖幅 / 手卷皆有；《秋风纨扇图》为竖幅小品，仕女独占画面。
- 视点：平视 / 轻微俯视；无焦点透视，散点构成。
- 布局：仕女或文人偏一角，山水环抱；留白适中，视线从人物游向山水，再由题诗收回来。
- 裁切：主体不顶边；山势舒缓，不画高耸主峰；不画满幅。

## (5) 光影与透视

- 光源：无固定光源；亮在留白秋意与仕女衣饰处。
- 阴影：无写实阴影；墨的浓淡即远近，淡即远、浓即近。
- 透视：无焦点透视；空间靠山水的舒缓与留白推远近。

## (6) 该画什么 / 不该画什么

- 该画：仕女、文人、松山、秋意小景；山水与人物兼擅的俊逸一路。`verbatim`
- 不该画：粗野狂笔；重彩满幅；密体满幅；板滞院体。
- Negative prompt: `wild unrestrained brushwork, heavy colour filling the whole paper, dense full composition, stiff academic style, photorealistic detail, oil paint texture`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Tang Yin, a small Yorkshire terrier sitting on a subway seat, elegant literati painting on paper, graceful flowing lines, refined ink with light colour, the little dog as a beautiful lady in a quiet landscape, light ochre accents, poetic and romantic`
- 中文对照：唐寅风格，一只小约克夏犬坐在地铁座位上，俊逸文人画，线条流畅秀润，淡墨轻彩，小狗如幽静山水中的美人，淡赭微染，诗意浪漫。
- Negative: 见第 (6) 节。
- 检验点：小狗是否画得俊逸有神而不是工笔描毛；线条是否流畅；背景是否留白而不是画满车厢。
