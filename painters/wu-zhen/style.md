# Wu Zhen — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wu Zhen, Yuan literati painting, wet ink and hemp-fibre strokes, ink-drenched mountains, fishermen and ink bamboo, poetry calligraphy painting in one, lonely and archaic`
- ZH: 吴镇风格，元四家文人画，湿笔披麻，墨气淋漓，渔父与墨竹，诗书画合一，苍古孤寂。

## (2) 色板方向

- 主色（颜料名）：墨色、淡赭、花青、淡石绿。`verbatim` / `artifact`
- 辅色：淡赭、淡花青，墨色为主，渔父长卷以墨为主、色极淡。
- 禁色：青绿重彩；满幅全景；工笔细描。
- 冷暖：墨分浓淡为主，暖色只作点染；整体清、亮、透，不沉。
- 明暗 / 饱和：靠墨的浓淡干湿，不靠明暗渐变；饱和度克制，亮在留白。

## (3) 笔触与线条

- 笔触：湿笔披麻：以湿笔、浓墨写山石，墨气淋漓，与黄公望干笔相对；墨竹以画法写竹，竹叶如书法点画。`artifact`（画史通说；Smarthistory《渔夫图》说明）
- 线条：书法性线条，中锋为主；轮廓不封闭，靠笔意收住形。
- 质感：绢 / 纸上水墨晕染 + 枯笔飞白；无油彩堆积，无工笔细线。

## (4) 构图习惯

- 画幅：平远长卷 / 册页：渔父长卷自右向左，渔舟、渔父、江天交替；墨竹册页一竹一石，疏朗而孤寂。`verbatim`
- 视点：平视 / 轻微俯视；无焦点透视，散点 / 平面构成。
- 布局：题款、印章是构图的一部分，位置计入画面平衡。
- 裁切：平远长卷/册页，渔舟、渔父、江天交替；画面疏朗，不画满幅。

## (5) 光影与透视

- 光源：无固定光源；亮在留白江面，暗在湿笔浓墨；空间靠墨色浓淡推远。`verbatim`
- 阴影：无写实阴影；墨的浓淡即体积，淡即远、浓即近。
- 透视：无焦点透视；空间靠留白 + 墨色浓淡推远近。

## (6) 该画什么 / 不该画什么

- 该画：渔父、墨竹、芦花寒雁、湿笔山水、诗书画合一、苍古孤寂的平远。`verbatim`
- 不该画：全景满幅高山、干笔渴笔一路、重彩青绿、焦点透视、热闹人物、工笔细节。
- Negative prompt: `towering peak filling the whole picture, dry thirsty brush only, heavy blue-green colour, linear perspective, crowded lively figures, meticulous gongbi detail`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬（冬））

- Prompt: `In the style of Wu Zhen, a small Yorkshire terrier sitting on a subway seat on a winter day, wet ink and hemp-fibre strokes, ink-drenched mountains in the distance, lonely and archaic, poetry calligraphy painting in one`
- 中文对照：吴镇风格，冬日地铁里一只小约克夏犬坐在座位上，湿笔披麻，远处墨气淋漓的山峦，苍古孤寂，诗书画合一。
- Negative: 见第 (6) 节。
- 检验点：湿笔披麻与平远构图二者至少其一成立；画面是否苍古孤寂、渔父是否渺小，而不是只换了题材。
