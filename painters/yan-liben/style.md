# Yan Liben — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yan Liben, Early Tang court figure painting on silk, firm iron-wire lines, heavy mineral colour with light dyeing, solemn hierarchical composition, historical narrative portraiture`
- ZH: 阎立本风格，唐初宫廷人物画，绢本，铁线描般坚实有力的线条，重彩设色加淡染，庄重等级分明的构图，历史叙事肖像。

## (2) 色板方向

- 主色（颜料名）：墨色、朱砂、赭石、花青、石绿、石青、藤黄。`verbatim` / `artifact`
- 辅色：石青、石绿重彩，赭石染面，朱砂点服饰，色浓而匀。
- 禁色：水墨写意；淡彩留白；浓墨皴染。
- 冷暖：墨分浓淡为主，暖色只作点染；整体清、亮、透，不沉。
- 明暗 / 饱和：靠墨的浓淡干湿，不靠明暗渐变；饱和度克制，亮在留白。

## (3) 笔触与线条

- 笔触：线条坚实劲健，近铁线描：粗细变化小，顿挫明确，衣纹转折方硬有力；人物面部以淡墨细线勾五官，敷淡色，神态端庄。`verbatim`
- 线条：书法性线条，中锋为主；轮廓不封闭，靠笔意收住形。
- 质感：绢 / 纸上水墨晕染 + 枯笔飞白；无油彩堆积，无工笔细线。

## (4) 构图习惯

- 画幅：等级构图：帝王居中偏右、体量最大，侍从按身份左右分列、体量递减；画面分两组对峙，屏风、步辇、旗仗作分隔与平衡。`verbatim`（《步辇图》）
- 视点：平视 / 轻微俯视；无焦点透视，散点 / 平面构成。
- 布局：题款、印章是构图的一部分，位置计入画面平衡。
- 裁切：等级构图，帝王居中、人物按身份分列；画面满而不乱，屏风、旗仗充填背景，不留大面积空白。

## (5) 光影与透视

- 光源：无固定光源、无明暗体积；亮暗靠设色浓淡与线，空间靠人物前后叠置与器物分隔，不用焦点透视。`verbatim`
- 阴影：无写实阴影；墨的浓淡即体积，淡即远、浓即近。
- 透视：无焦点透视；空间靠留白 + 墨色浓淡推远近。

## (6) 该画什么 / 不该画什么

- 该画：帝王与使节、朝会仪仗、历史事件叙事、等级分明的群像、重彩绢本、屏风步辇等仪物。`verbatim`
- 不该画：写意水墨、焦点透视、明暗体积、松散随意的构图、平民市井小品、满幅山水。
- Negative prompt: `freehand ink wash, linear perspective, chiaroscuro modelling, loose casual composition, crowded full landscape, photorealistic shading`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Yan Liben, a small Yorkshire terrier sitting on a subway seat, early Tang court figure painting on silk, firm iron-wire lines, heavy mineral colour with light dyeing, solemn hierarchical composition, attendants arranged by rank around the central figure`
- 中文对照：阎立本风格，一只小约克夏犬坐在地铁座位上，唐初宫廷人物画，绢本，铁线描般坚实的线条，重彩淡染，等级分明的庄重构图，人物按身份分列。
- Negative: 见第 (6) 节。
- 检验点：铁线描的线与重彩设色、等级构图三者至少其二成立；人物是否按身份体量递减、神态庄重，而不是只换了题材。
