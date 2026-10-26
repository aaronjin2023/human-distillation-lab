# Kitagawa Utamaro — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Ukiyo-e bijinga beauty print, ōkubi-e large-head close-up, fine delicate outlines, soft beni pink and pale skin, muscovite mica glitter background, individualized faces`
- ZH: 浮世绘美人画，大首绘头部特写，纤细均匀的轮廓线，柔和的胭脂红与淡肤色，云母粉底的闪光，面容各有细微差别。

## (2) 色板方向

- 主色（7 色，颜料名）：墨色、胭脂红（红）、淡粉、淡黄、淡绿、淡紫、云母粉（银白闪光）。`verbatim` / `artifact`
- 肤色极淡、红极克制：胭脂红只点唇、衣纹与发饰，大面积是淡肤色与云母底。`verbatim`
- 辅色：淡绿与淡紫画衣纹、淡黄画发饰。
- 禁色：高饱和大面积平涂；粗黑硬线；油画式明暗。
- 冷暖：整体偏暖偏淡，暖在胭脂红与肤色，冷只一点淡绿淡紫。
- 明暗 / 饱和：无写实明暗；体积靠线的疏密与淡彩的薄染，不靠渐变；亮在云母粉底的闪光处。

## (3) 笔触与线条

- 笔触：不是笔触，是刀味——轮廓线纤细、均匀、有韧性，发丝一根一根刻出，是浮世绘中最细的线。`verbatim`
- 线条：细线定一切，眉、眼、唇的线极细而不断；衣纹线流畅、疏密有致。`verbatim`
- 质感：木刻版画的平滑纸面 + 云母粉底的闪光 + 淡彩薄染；无油彩堆积，无水墨晕染。

## (4) 构图习惯

- 画幅：竖幅大判（ōban）为主，大首绘只取头与肩，画面几乎被人物占满。`artifact`
- 视点：平视特写；无透视，平面构成。
- 布局：《当世三美人》是三角形构图——三人半身并列，中间一人略高，视线在三人之间流转。`verbatim`
- 裁切：大首绘把人物裁到只剩头与肩，身体出画，是歌麿的大胆之处。`verbatim`

## (5) 光影与透视

- 光源：无固定光源；亮在肤色与云母底的闪光处。
- 阴影：无写实阴影；面部的体积靠线的疏密与淡彩的薄染。
- 透视：无透视；空间靠前后人物的叠压与云母底的深浅。

## (6) 该画什么 / 不该画什么

- 该画：美人半身与大首绘、茶屋女与艺伎、母子、闺中情景。`verbatim`
- 不该画：风景的大场面；粗黑硬线；高饱和大面积平涂；油画式明暗；千人一面的程式化美人脸。
- Negative prompt: `landscape panorama, thick bold outlines, high-saturation flat colour, oil-painting shading, identical stereotyped faces`

## (7) 测试提示词示例（现代题材：共享单车）

- Prompt: `In the style of Kitagawa Utamaro, a young woman riding a shared bicycle in a modern city, ukiyo-e bijinga beauty print, ōkubi-e large-head close-up, fine delicate outlines, soft beni pink, muscovite mica glitter background, individualized face`
- 中文对照：歌麿风格，一位年轻女子骑着共享单车，浮世绘美人画，大首绘头部特写，纤细均匀的轮廓线，柔和的胭脂红，云母粉底闪光，面容有细微个性。
- Negative: 见第 (6) 节。
- 检验点：线是否纤细均匀、面容是否有细微个性而不是程式化；云母底是否闪光；红是否克制。
