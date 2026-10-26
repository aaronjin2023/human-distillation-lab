# Sandro Botticelli — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sandro Botticelli, Early to High Renaissance tempera on canvas, graceful flowing line, light floating figures, pale delicate colours, mythological spring, linear elegance, no heavy shadow`
- ZH: 波提切利风格，早期—盛期文艺复兴布面蛋彩，线条优美流畅，人物轻盈漂浮，色彩淡雅如春，神话感，线条的优雅，无重阴影。

## (2) 色板方向

- 主色（7 色，颜料名）：淡粉肤色、群青、淡绿、朱红、土黄、铅白、金箔金。`verbatim`
- 辅色：淡紫（阴影）、灰绿（树叶）。
- 禁色：浓重阴影；厚重油彩；肌肉发达的扭曲人体；写实透视的深远空间。
- 冷暖：整体偏暖的淡彩，淡粉与土黄为主，群青与淡绿作冷点。
- 明暗 / 饱和：低对比，明暗过渡柔和；饱和度低而明亮，像春天的光。

## (3) 笔触与线条

- 笔触：蛋彩薄涂，笔触细腻、几乎不可见；色彩平涂为主，少有厚涂。`verbatim`
- 线条：线条是本体——轮廓线流畅、优美、富有韵律，衣纹线如水波般起伏；线条比明暗更重要。`artifact`（学界共识：波提切利是线条画家）
- 质感：布面蛋彩哑光，表面平滑；金色细节（发饰、衣纹）用金箔或金粉点缀。

## (4) 构图习惯

- 画幅：布面蛋彩横幅为主；《维纳斯的诞生》与《春》皆为大横幅。`verbatim`
- 视点：平视，人物与观者齐平，无仰视或俯视。
- 布局：人物横向排列如浮雕——《春》中九个人物一字排开，《维纳斯的诞生》中维纳斯居中、西风在左、时辰女神在右；背景为暗色树林，人物浮于其前。`verbatim`
- 裁切：人物完整，少有裁切；画面如挂毯般平展。

## (5) 光影与透视

- 光源：均匀、柔和的光，无明确光源方向；光不制造戏剧，只照亮线条。
- 阴影：极淡的阴影，体积靠线条与淡彩的轻微深浅，不靠明暗反差。
- 透视：几乎无线性透视——人物按横向排列，空间是平面的、挂毯式的；远近靠重叠，不靠灭点。`artifact`

## (6) 该画什么 / 不该画什么

- 该画：维纳斯、春之女神、花神；轻盈的舞姿与飘动的衣纹；花草繁密的春日树林。
- 不该画：浓重阴影；肌肉发达的人体；深远透视空间；厚重油彩。
- Negative prompt: `heavy dark shadows, muscular twisted bodies, deep linear perspective, thick oil impasto, saturated garish colours, photorealistic detail`

## (7) 测试提示词示例（现代题材：阳台上的猫与花）

- Prompt: `In the style of Sandro Botticelli, a cat with flowers on a balcony in spring, Early to High Renaissance tempera on canvas, graceful flowing line, light floating figure, pale delicate colours, mythological spring feeling, linear elegance, no heavy shadow`
- 中文对照：波提切利风格，春天阳台上的一只猫与花，早期—盛期文艺复兴布面蛋彩，线条优美流畅，猫轻盈漂浮，色彩淡雅如春，神话感，线条的优雅，无重阴影。
- Negative: 见第 (6) 节。
- 检验点：线条是否优美流畅而不是写实描摹；猫是否轻盈漂浮而不是沉重落地；色彩是否淡雅如春。
