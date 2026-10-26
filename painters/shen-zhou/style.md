# Shen Zhou — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shen Zhou, literati ink landscape on paper, coarse bold brushwork, thick wet ink with dry-brush texture, monumental mountain mass, small scholar figure, poetry and calligraphy integrated, warm ochre accents, calm and monumental`
- ZH: 沈周风格，纸上文人水墨山水，粗笔厚重，湿墨浓厚兼枯笔皴擦，山体雄浑高大，山中小小文人，诗书画合一，赭石微染，沉静雄浑。

## (2) 色板方向

- 主色（6 色，颜料名）：
- 墨色（浓—淡—干—湿分层）
- 赭石
- 淡花青
- 淡石绿
- 淡朱砂（极少）
- 纸白（留白即云雾）
- 主色 / 辅色：主色是墨色 + 赭石；辅色淡花青、淡石绿微染，色比王蒙淡、比倪瓒暖。`verbatim`
- 禁色：工笔细描满幅；重彩大面积平涂；院体式的精细楼阁。
- 冷暖：暖调为主，赭石暖色压住全幅；墨色偏暖厚，整体沉静、雄浑。
- 明暗 / 饱和：靠墨的浓淡干湿与粗笔的厚重，不靠明暗渐变；饱和度中等，亮在留白云雾处。

## (3) 笔触与线条

- 笔触：粗笔为主，笔触厚重、湿润，兼用枯笔皴擦；山石用粗笔横扫，树木用渴笔点写。`verbatim` / `artifact`
- 线条：线条粗壮有力，如书法中的大字；轮廓不求精细，靠粗笔的势收住形；线条少而重。
- 质感：纸上湿墨晕染 + 枯笔擦出的粗粝感；墨色厚而不板，有“粗而不野”的质感。
- 关键技法：粗笔——以粗壮笔触写山石大势，学元四家而化出自己的厚重；没骨花卉——不用勾线，以墨色直接点染花叶。`artifact`（维基百科“沈周”）

## (4) 构图习惯

- 画幅：竖幅大轴为主；《庐山高》近 2 米高，是厅堂陈设的大画。`artifact`
- 视点：平视 / 仰视；无焦点透视，散点构成，山体高大压住画面。
- 布局：主峰居中偏上，山体占画面三分之二以上；山脚小小文人、松树、茅屋，视线从山脚仰望主峰。
- 裁切：主峰可顶边；山脚留白作云雾；不画满幅细节。

## (5) 光影与透视

- 光源：无固定光源；亮在留白云雾与山间空处。
- 阴影：无写实阴影；墨的浓淡即体积，浓即近、淡即远。
- 透视：无焦点透视；空间靠山体的高大与云雾留白推远近，高而不空。

## (6) 该画什么 / 不该画什么

- 该画：雄浑山水、山中小小文人、松树茅屋、没骨花卉；诗书画合一的文人山水。`verbatim`
- 不该画：工笔细描；重彩满幅；院体楼阁；疏朗一河两岸。
- Negative prompt: `meticulous gongbi fine lines, heavy colour filling the whole paper, court-style detailed pavilions, sparse one-river-two-banks composition, photorealistic detail, oil paint texture`

## (7) 测试提示词示例（现代题材：窗台上的咖啡）

- Prompt: `In the style of Shen Zhou, a cup of coffee on a windowsill in a modern apartment, literati ink landscape on paper, coarse bold brushwork, thick wet ink, the window frame as a monumental mountain mass, the small coffee cup as a scholar figure below, poetry-like calm, warm ochre accents`
- 中文对照：沈周风格，现代公寓窗台上的一杯咖啡，文人水墨，粗笔厚重，湿墨浓厚，窗框如雄浑山体，窗台上的小咖啡杯如山脚文人，沉静如诗，赭石微染。
- Negative: 见第 (6) 节。
- 检验点：窗框是否如山体般雄浑；咖啡杯是否小而立得住；粗笔是否厚重而不野；是否有诗意留白。
