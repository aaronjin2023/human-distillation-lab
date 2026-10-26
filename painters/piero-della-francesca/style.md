# Piero della Francesca — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Piero della Francesca, early Renaissance painting, geometry and calm light, pale precise colours, still monumental figures, mathematical perspective, silent order, egg tempera and oil on panel`
- ZH: 皮耶罗风格，早期文艺复兴绘画，几何与宁静之光，淡而精确的色彩，人物静止如纪念碑，数学透视，寂静秩序，蛋彩与油彩木板。

## (2) 色板方向

- 主色（7 色，颜料名）：淡粉肤色、群青、朱红、淡绿、土黄、铅白、灰褐。`verbatim`
- 辅色：淡蓝（远山）、银灰（铠甲与建筑）。
- 禁色：高饱和浓艳色；戏剧性明暗；动态模糊的笔触；巴洛克式喧闹。
- 冷暖：整体偏冷的淡彩，朱红与土黄作暖点；光是清澈的日光，不暖不冷。
- 明暗 / 饱和：低对比，色彩淡而准；明暗过渡极缓，体积靠大面积的淡彩平涂。

## (3) 笔触与线条

- 笔触：极细、极平，几乎看不见笔触；蛋彩与油彩薄涂，表面光滑如珐琅。`verbatim`
- 线条：轮廓线清晰但不强调，形体靠几何体积而非线条勾勒。
- 质感：木板蛋彩的平滑质感；远景树木用细密小笔点染，近景人物用大面积平涂。

## (4) 构图习惯

- 画幅：祭坛画与壁画皆有；《基督受洗》为竖幅祭坛画，《基督受鞭刑》为横幅小幅。`verbatim`
- 视点：平视，视线与人物齐平；《基督受洗》中鸽子、圣水钵、基督合十的手严格对齐在同一中轴线上。`artifact`（英国国家美术馆说明）
- 布局：几何构图——人物按网格定位、逐层缩小；《基督受鞭刑》主事件退到后方柱廊，前景三位身份不明人物站立，画面分前后两层。`verbatim`
- 裁切：几乎不裁切，画面完整、对称、静止；人物之间留有大量“空的”间隔。

## (5) 光影与透视

- 光源：均匀、清澈的日光，无戏剧性聚光；光线方向一致但极淡。
- 阴影：极淡的灰影，体积靠淡彩的轻微深浅，不靠明暗反差。
- 透视：数学透视——网格定位、按比例缩小；《基督受洗》用网格定每件物体的位置与大小。`artifact`（英国国家美术馆说明）

## (6) 该画什么 / 不该画什么

- 该画：基督生平、圣徒群像、几何建筑、远山风景；静止的仪式性群像。
- 不该画：激烈动作与表情；浓重阴影；拥挤的群像；装饰性花纹。
- Negative prompt: `dramatic Baroque chiaroscuro, heavy dark shadows, agitated movement, crowded composition, saturated garish colours, rough visible brushstrokes`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Piero della Francesca, a small Yorkshire terrier sitting on a subway seat, early Renaissance painting, geometry and calm light, pale precise colours, still monumental figure, mathematical perspective of the carriage, silent order, egg tempera on panel`
- 中文对照：皮耶罗风格，一只小约克夏犬坐在地铁座位上，早期文艺复兴绘画，几何与宁静之光，淡而精确的色彩，人物静止如纪念碑，车厢的数学透视，寂静秩序，蛋彩木板。
- Negative: 见第 (6) 节。
- 检验点：构图是否几何般精确、对称；小狗是否静止如雕塑而不是活泼卖萌；色彩是否淡而准。
