# Guo Xi — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Guo Xi, Northern Song landscape, three distances in one painting, high deep and level distance, cloud-like texture strokes, misty spring mountains, trees like crab claws and dragons`
- ZH: 郭熙风格，北宋山水，一幅三远，高远深远平远并用，云头皴，烟雾春山，树如蟹爪龙爪，雾气氤氲。

## (2) 色板方向

- 主色（颜料名）：墨色、淡赭、花青、淡石绿、淡石青、朱砂（点人物）。`verbatim` / `artifact`
- 辅色：淡赭、淡花青、淡石绿，朱砂只点人物，色不盖墨。
- 禁色：青绿重彩；单峰满幅；工笔细描。
- 冷暖：墨分浓淡为主，暖色只作点染；整体清、亮、透，不沉。
- 明暗 / 饱和：靠墨的浓淡干湿，不靠明暗渐变；饱和度克制，亮在留白。

## (3) 笔触与线条

- 笔触：云头皴：皴擦如云头翻卷，圆浑而有体积，写山石的团块感；树多蟹爪、龙爪枝，枝干屈曲如龙。`artifact`（画史通说；《早春图》画面可见）
- 线条：书法性线条，中锋为主；轮廓不封闭，靠笔意收住形。
- 质感：绢 / 纸上水墨晕染 + 枯笔飞白；无油彩堆积，无工笔细线。

## (4) 构图习惯

- 画幅：三远并用：一幅之中高远居中、深远在右、平远在左，各段自成一景又以雾气相连；山水、人物、屋宇各段皆可独立观。`artifact`（郭熙《林泉高致·山水训》三远说）
- 视点：平视 / 轻微俯视；无焦点透视，散点 / 平面构成。
- 布局：题款、印章是构图的一部分，位置计入画面平衡。
- 裁切：三远并用，一幅之中高远、深远、平远各段自成一景又以雾气相连；山水可满幅，但段与段之间以云雾留白隔开。

## (5) 光影与透视

- 光源：无固定光源；亮在雾气留白，暗在云头皴的团块；空间靠三远切换，不用焦点透视。`verbatim`
- 阴影：无写实阴影；墨的浓淡即体积，淡即远、浓即近。
- 透视：无焦点透视；空间靠留白 + 墨色浓淡推远近。

## (6) 该画什么 / 不该画什么

- 该画：早春山水、三远并用、云头皴、雾中山峦、窠石、平远、春雪关山。`verbatim`
- 不该画：单一透视、满幅一峰、重彩青绿、焦点透视、工笔细节、松散无结构的留白。
- Negative prompt: `single fixed perspective, one peak filling the whole picture, heavy blue-green colour, linear perspective, meticulous gongbi detail, unstructured empty space`

## (7) 测试提示词示例（现代题材：地铁站台上的约克夏犬）

- Prompt: `In the style of Guo Xi, a small Yorkshire terrier on a subway platform in a modern city, three distances in one painting, high deep and level distance, cloud-like texture strokes, misty spring mountains in the distance, trees like crab claws`
- 中文对照：郭熙风格，现代城市地铁站台上的一只小约克夏犬，一幅三远，高远深远平远并用，云头皴，远处雾中山峦，树如蟹爪。
- Negative: 见第 (6) 节。
- 检验点：云头皴与三远构图二者至少其一成立；一幅之中是否高远、深远、平远并存，而不是只换了题材。
