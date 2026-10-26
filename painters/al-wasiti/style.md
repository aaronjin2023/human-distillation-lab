# Yahya ibn Mahmud al-Wasiti — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Arab miniature painting, Baghdad school, fine ink outlines with flat opaque colour and gold, multi-level stacked composition, lively everyday narrative, no perspective or shadow`
- ZH: 阿拉伯细密画，巴格达画派，细墨线勾边、平涂不透明色与描金，多层叠压构图，生动的日常生活叙事，无透视无阴影。

## (2) 色板方向

- 主色（7 色，颜料名）：朱红、群青、金色、墨色、石绿、黄赭、淡紫。`verbatim` / `artifact`
- 金色是主色之一：多数细密画饰以金地或金线，是巴格达画派的豪华感来源。`artifact`
- 辅色：淡紫画衣纹、淡黄画沙地。
- 禁色：油画式渐变与明暗；焦点透视；写实肤色渐变；大面积留白。
- 冷暖：整体偏暖，朱红与金定暖调，群青与石绿作冷色点缀。
- 明暗 / 饱和：无明暗；体积靠平涂色块与细线；亮在金色与朱红处。

## (3) 笔触与线条

- 笔触：不是笔触，是细线与平涂——以极细的笔勾线，颜料平涂，笔触不可见。`verbatim`
- 线条：细墨线勾边定一切，线均匀、精细、有韧性；人物面部、建筑、骆驼的细节全靠线。`verbatim`
- 质感：纸面光滑 + 不透明颜料的粉质平涂 + 金的反光；无油彩堆积，无水墨晕染。

## (4) 构图习惯

- 画幅：书页插图，小幅；每幅配一段文字，图文一体。`artifact`
- 视点：多层叠压——以多层表现不同平面，同一小幅内压缩村庄、街道、室内多个场景。`artifact`
- 布局：人物密集、满幅，建筑与人物按叙事排，不按透视；清真寺讲道一幅以讲坛为中心、听众环绕。`verbatim`
- 裁切：画面满幅，建筑常被裁掉边缘，人物出画边。

## (5) 光影与透视

- 光源：无固定光源；全幅均匀受光，无阴影。
- 阴影：无阴影——体积靠平涂与细线。
- 透视：无透视；远近靠上下位置（上即远）与多层叠压，不靠焦点透视。

## (6) 该画什么 / 不该画什么

- 该画：清真寺讲道、商队、骆驼群、村庄生活、市集、学堂、船旅。`verbatim`
- 不该画：焦点透视；写实阴影；留白构图；人物稀疏的空旷画面；无叙事的纯装饰。
- Negative prompt: `single-point perspective, realistic shadows, empty background, sparse composition, oil-painting shading, photorealistic faces`

## (7) 测试提示词示例（现代题材：共享单车）

- Prompt: `In the style of Yahya ibn Mahmud al-Wasiti, people riding shared bicycles in a modern city, Arab miniature painting, Baghdad school, fine ink outlines, flat opaque colour and gold, multi-level stacked composition, lively everyday narrative, no perspective or shadow`
- 中文对照：瓦西提风格，现代城市里人们骑着共享单车，阿拉伯细密画，巴格达画派，细墨线勾边，平涂不透明色与描金，多层叠压构图，生动的日常生活叙事，无透视无阴影。
- Negative: 见第 (6) 节。
- 检验点：构图是否多层叠压、人物是否密集；金色是否在场；线是否细而精。
