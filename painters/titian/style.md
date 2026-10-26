# Titian (Tiziano Vecellio) — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Titian, Venetian oil painting, colorito, rich luminous colour built by layered glazes, sensual flesh, loose expressive brushwork, warm golden light, oil on canvas`
- ZH: 提香风格，威尼斯画派油画，色彩至上，层层罩染的浓烈光感，感性的肌肤，自由的笔触，暖金光线，布面油画。

## (2) 色板方向

- 主色（7 色，颜料名）：群青、朱红、赭石、土黄、铅白、墨绿、胭脂红（红湖）。`verbatim`
- 辅色：金黄（衣袍与光）、灰蓝（远景）。
- 禁色：硬轮廓线；灰暗土色大面积平涂；纤细苍白的人体；线条主导的素描感。
- 冷暖：暖调为主——暖金、暖肤、暖红；群青与墨绿作冷对比，冷暖对撞而和谐。
- 明暗 / 饱和：中高对比，色彩浓烈而透明；亮部金黄、暗部深暖；饱和度高，但靠罩染不靠平涂。

## (3) 笔触与线条

- 笔触：中期笔触肯定、流畅；晚期笔触自由、破碎，手指、干笔、刮刀并用，近看是色块、远看是形。`artifact`
- 线条：无硬轮廓线——形体由色彩塑造，所谓 colorito（色彩至上）即与佛罗伦萨 disegno（素描至上）相对。`artifact`
- 质感：布面油画，罩染透明、厚涂丰盈并置；皮肤如瓷而有温度，织物厚重而有光泽。

## (4) 构图习惯

- 画幅：祭坛画、神话与肖像皆有；《酒神与阿里阿德涅》为横幅，对角线构图。`verbatim`
- 视点：平视略俯；《酒神与阿里阿德涅》中酒神从空中跃下，视线随对角线上升。
- 布局：对角线与三角形构图——《酒神与阿里阿德涅》酒神与阿里阿德涅成对角线，酒神随从成群；《乌尔比诺的维纳斯》维纳斯横卧全幅，背景分两室。`verbatim`
- 裁切：人物常被画框边缘截断，营造近景感；背景风景占大幅，人物与风景同等重要。

## (5) 光影与透视

- 光源：暖金光线，光从画面外上方来，全幅一致；光是色彩的一部分，不是独立的明暗。
- 阴影：深暖的阴影，亮暗之间有罩染的透明过渡。
- 透视：空气透视——远景变淡、变蓝；线性透视克制，空间靠色彩的冷暖推远近。`artifact`

## (6) 该画什么 / 不该画什么

- 该画：神话与维纳斯、圣母与圣徒、帝王肖像；感性的裸体与织物；海天风景。
- 不该画：硬轮廓线；灰暗土色；纤细苍白的人体；线条主导的素描感。
- Negative prompt: `hard outlines, dull muddy palette, slender pale figures, drawing-dominated linear style, flat vector illustration, photorealistic detail`

## (7) 测试提示词示例（现代题材：海边度假酒店的泳池）

- Prompt: `In the style of Titian, a swimming pool at a seaside resort hotel at golden hour, Venetian oil painting, colorito, rich luminous colour built by layered glazes, warm golden light on water and skin, loose expressive brushwork, sensual calm, oil on canvas`
- 中文对照：提香风格，黄昏时分海边度假酒店的泳池，威尼斯画派油画，色彩至上，层层罩染的浓烈光感，暖金光线洒在水面与肌肤上，自由的笔触，感性的宁静，布面油画。
- Negative: 见第 (6) 节。
- 检验点：色彩是否浓烈而透明、会发光；皮肤与水面是否有温度；笔触是否自由而不是精细描摹。
