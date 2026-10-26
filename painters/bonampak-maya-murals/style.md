# Bonampak Maya Murals — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Classic Maya fresco, mineral colours on wet plaster, flat red blue green and yellow, black outlines, dense narrative registers full of figures, hieroglyphic captions, no perspective or shadow`
- ZH: 玛雅古典期湿壁画，湿灰泥上矿物色平涂，红蓝绿黄平色，黑线勾边，满幅叙事分格、人物密集，象形文字题铭，无透视无阴影。

## (2) 色板方向

- 主色（7 色，颜料名）：红赭（红底）、玛雅蓝、孔雀石绿、黄赭、淡紫、烟黑、白垩白。`verbatim` / `artifact`
- 先涂红底，再覆蓝、绿、黄、紫等矿物色，最后黑线勾边；玛雅蓝是该传统的标志色。`artifact`
- 辅色：白垩白画衣饰与面部粉饰、淡黄画金饰。
- 禁色：油画式渐变与明暗；焦点透视；写实肤色渐变；留白构图。
- 冷暖：整体偏暖，红底定暖调，玛雅蓝与绿作冷色对照。
- 明暗 / 饱和：无明暗；体积靠平涂色块与黑线；亮在白垩白与玛雅蓝处。

## (3) 笔触与线条

- 笔触：不是笔触，是平涂与勾线——颜料以笔平涂于湿灰泥上，笔触不可见；轮廓线以黑线收边。`artifact`
- 线条：黑线勾边定一切，线均匀有力；人物服饰、羽饰、乐器的细节全靠线。`verbatim`
- 质感：湿灰泥墙面的粉质平涂 + 矿物颜料的鲜明平色；无油彩堆积，无水墨晕染。

## (4) 构图习惯

- 画幅：壁画殿三厅，墙面与天花板满幅覆盖，约 281 个人物。`artifact`
- 视点：正侧面混合——人物多为侧面，间有正面，眼睛与身体角度按玛雅规范，不按写实。`verbatim`
- 布局：叙事分格——一厅一幕，按时间顺序读：一厅觐见、二厅战役、三厅庆典；每厅内部又分上下带。`verbatim`
- 裁切：画面满幅，人物密集到几乎无空地；天花板亦有画，视线须仰视。

## (5) 光影与透视

- 光源：无固定光源；全幅均匀受光，无阴影。
- 阴影：无阴影——体积靠平涂与黑线。
- 透视：无透视；远近靠上下位置与人物大小，叙事靠分格而非空间。

## (6) 该画什么 / 不该画什么

- 该画：觐见继承人、歌舞乐队、战役与俘虏、舞蹈、放血仪式、羽饰与织物。`verbatim`
- 不该画：焦点透视；写实阴影；留白构图；人物稀疏的空旷画面；无题铭的纯装饰。
- Negative prompt: `single-point perspective, realistic shadows, empty background, sparse composition, oil-painting shading, no hieroglyphic captions`

## (7) 测试提示词示例（现代题材：深夜拉面店）

- Prompt: `In the style of Bonampak Maya murals, a ramen shop late at night in a modern city, Classic Maya fresco, flat mineral colours of red, Maya blue, green and yellow on wet plaster, black outlines, dense narrative registers, hieroglyphic-style captions, no perspective or shadow`
- 中文对照：波南帕克玛雅壁画风格，深夜的拉面店，古典期湿壁画，红、玛雅蓝、绿、黄矿物色平涂，黑线勾边，满幅叙事分格、人物密集，象形文字式题铭，无透视无阴影。
- Negative: 见第 (6) 节。
- 检验点：画面是否满幅密集、无留白；颜色是否矿物平涂；叙事是否分格；有无题铭带。
