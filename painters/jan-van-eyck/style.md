# Jan van Eyck — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jan van Eyck, Northern Renaissance oil on panel, luminous layered glazes, microscopic detail, jewel-like colour, clear window light, symbolic domestic objects, precise observation`
- ZH: 扬·凡·艾克风格，北方文艺复兴木板油画，透明罩染的宝石光泽，显微镜般的细节，宝石色，窗光清澈，象征性的室内器物，精确观察。

## (2) 色板方向

- 主色（7 色，颜料名）：群青、朱红、墨绿、土黄、铅白、赭石、胭脂红。`verbatim`
- 辅色：金黄（黄铜与织物）、灰蓝（远景）。
- 禁色：粗犷笔触；大面积平涂；模糊的轮廓；巴洛克式戏剧光影。
- 冷暖：暖红与墨绿并置，群青作冷点；光是冷而清的窗光，暖色在光里发亮。
- 明暗 / 饱和：中对比，色彩宝石般浓烈而透明；亮部亮、暗部沉，但细节始终清晰。

## (3) 笔触与线条

- 笔触：极细、极薄，层层罩染，几乎看不见笔触；细笔描摹毛皮、织物、金属的每一种质感。`verbatim`
- 线条：轮廓线精细、清晰，器物的边缘如刀刻般准确。
- 质感：油画罩染的宝石光泽——毛皮柔软、金属反光、织物厚重、玻璃透明，每种材质各不相同。`artifact`

## (4) 构图习惯

- 画幅：祭坛画与肖像皆有；《阿尔诺芬尼夫妇像》为竖幅室内肖像，《根特祭坛画》为十二联大祭坛。`verbatim`
- 视点：平视；《阿尔诺芬尼夫妇像》中天花板、地板、墙面三面收向纵深，凸面镜映出画外两人。`verbatim`
- 布局：室内对称构图——夫妇分列左右，中央为吊灯与凸面镜；《根特祭坛画》上层神圣、下层人间，层层展开。`verbatim`
- 裁切：几乎不裁切，室内器物完整陈列，如珠宝盒般严密。

## (5) 光影与透视

- 光源：左侧窗户的清澈日光，全幅一致；光在黄铜吊灯、凸面镜、玻璃上反射，是质感的来源。`verbatim`
- 阴影：淡而清晰的阴影，体积靠罩染的透明层次，不靠强烈反差。
- 透视：室内透视——天花板、地板、墙面三面收向纵深；凸面镜是第四面，映出画外空间。`artifact`

## (6) 该画什么 / 不该画什么

- 该画：室内肖像、祭坛画、圣母与圣徒；毛皮、金属、织物、玻璃；凸面镜与象征物。
- 不该画：粗犷笔触；大面积平涂；模糊轮廓；戏剧光影。
- Negative prompt: `rough visible brushstrokes, flat matte colour, blurred outlines, dramatic Baroque spotlight, loose impressionist dabs, photorealistic camera blur`

## (7) 测试提示词示例（现代题材：雨夜的公交站）

- Prompt: `In the style of Jan van Eyck, a bus stop on a rainy night in a modern city, Northern Renaissance oil on panel, luminous layered glazes, microscopic detail, jewel-like colour, clear window light from the shelter, rain on glass, symbolic objects, precise observation`
- 中文对照：扬·凡·艾克风格，现代城市雨夜的公交站，北方文艺复兴木板油画，透明罩染的宝石光泽，显微镜般的细节，宝石色，候车亭里清澈的灯光，玻璃上的雨水，象征性的器物，精确观察。
- Negative: 见第 (6) 节。
- 检验点：每种材质（玻璃、金属、雨水、织物）是否各不相同；细节是否极致而不乱；光线是否清澈统一。
