# Mary Cassatt — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Impressionism with Japonisme, clear structure, flat decorative pattern, bold blue and warm flesh, steep high viewpoint, intimate mother and child, unsentimental observation`
- ZH: 印象派与日本风味，结构清晰，扁平装饰图案，大胆的蓝与暖肤色，陡峭高视点，亲密母子，冷静观察。

## (2) 色板方向

- 主色（7 色，颜料名）：钴蓝、群青、铅白、赭石、朱红、翠绿、土黄。`verbatim`
- 主色是大胆的蓝（蓝扶手椅、蓝水）+ 暖肤色对撞，图案是扁平的装饰色；整体明亮、平实。`verbatim`
- 辅色：淡紫、粉红、暖灰。
- 禁色：粉彩甜腻；平滑学院渐变；冷灰雾调；美化修饰。
- 冷暖：冷蓝为主，暖肤色与朱红作点缀；冷暖对比是日本风的来源。
- 明暗 / 饱和：中高明度、中饱和、中对比；亮部是蓝扶手椅与白肤，暗部是室内深色。

## (3) 笔触与线条

- 笔触：平滑、清晰、结构感强的笔触；笔触方向跟随结构，不跟随光。`verbatim`
- 线条：轮廓线清晰、实在，母子结构线是画面的骨架；受浮世绘影响，线条比莫奈更重。
- 质感：薄涂平滑，局部稍厚；图案质感靠扁平色块，不靠厚涂。

## (4) 构图习惯

- 画幅：横幅与竖幅并存；《蓝扶手椅上的小女孩》1878 年，横幅，女孩横卧蓝椅；《浴盆里的孩子》1893 年，竖幅，母子俯视浴盆。
- 视点：陡峭高视点：观者从高处俯视母子与浴盆，是其日本风的标志；无平视，视线被高视点牵着望向地面。
- 布局：高视点 + 扁平图案：母子在画面下中，图案地毯 / 墙纸占满幅；视线落点在母子与浴盆。
- 裁切：人物常被画边裁掉，图案绵延出画边；不留安全边距。

## (5) 光影与透视

- 光源：散射的室内光，无固定光源；亮在蓝椅与白肤，暗部是室内深色。
- 阴影：阴影是彩色的（蓝紫、墨绿），不用纯黑；明暗靠结构不靠灰阶。
- 透视：陡峭高视点 + 扁平空间：地面倾斜、浴盆变形，空间靠图案层叠；无严格焦点透视。

## (6) 该画什么 / 不该画什么

- 该画：母子、浴盆、蓝扶手椅、划船、剧院包厢。`verbatim`
- 不该画：粉彩甜腻；平滑渐变；冷灰雾调；美化修饰；历史画。
- Negative prompt: `pastel sweetness, smooth academic blending, cold grey haze, beautified idealisation, staged history painting, photorealistic polish`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Mary Cassatt, a small Yorkshire terrier sitting on a subway seat, Impressionism with Japonisme, clear structure, flat decorative pattern, bold blue and warm fur, steep high viewpoint, intimate and unsentimental`
- 中文对照：卡萨特风格，一只小约克夏犬坐在地铁座位上，印象派与日本风味，结构清晰，扁平装饰图案，大胆的蓝与暖毛色，陡峭高视点，亲密而冷静。
- Negative: 见第 (6) 节。
- 检验点：狗是否从高视点俯视、结构是否清晰、蓝与暖色是否对撞，而不是莫里索式薄纱苍白。
