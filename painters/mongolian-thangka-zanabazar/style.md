# Mongolian Thangka — Zanabazar School — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Mongolian thangka painting, mineral pigments on cotton, iconometric grid (ten-palms proportion), central deity in strict symmetry, flat gold lapis blue and vermilion, fine outlines, no perspective or shadow`
- ZH: 蒙古唐卡，棉布矿物颜料，造像度量网格（十掌比例），中央尊像严格对称，平涂金、青金石蓝与朱红，细线勾边，无透视无阴影。

## (2) 色板方向

- 主色（7 色，颜料名）：金色、青金石蓝、朱红、孔雀石绿、墨色、黄赭、白垩白。`verbatim` / `artifact`
- 金蓝红三色并置是唐卡的标志：金饰、青金石蓝衣、白度母的白与绿度母的绿各有定色。`verbatim`
- 辅色：淡黄画光晕、白垩白画白度母身色。
- 禁色：油画式渐变与明暗；焦点透视；写实肤色渐变；自由构图。
- 冷暖：整体偏暖，金与朱红定暖调，青金石蓝与石绿作冷色对照。
- 明暗 / 饱和：无明暗；体积靠平涂色块与细线；亮在金色与白垩白处。

## (3) 笔触与线条

- 笔触：不是笔触，是细线与平涂——以极细的笔勾线，矿物颜料平涂，笔触不可见。`verbatim`
- 线条：细墨线勾边定一切，线均匀、精细、有韧性；尊像的面部、手印、饰物全靠线。`verbatim`
- 质感：棉布的织纹 + 矿物颜料的粉质平涂 + 金的反光；无油彩堆积，无水墨晕染。

## (4) 构图习惯

- 画幅：竖幅卷轴唐卡为主，中央尊像、上下眷属、左右对称。`artifact`
- 视点：正面为主；尊像正面端坐，眷属略侧，无透视，平面构成。
- 布局：严格对称——中央尊像最大，上下左右眷属按等级排，莲座居中，视线落在尊像面部。`verbatim`
- 裁切：画面满幅，不留空白；边框织锦亦为画面的一部分。

## (5) 光影与透视

- 光源：无固定光源；全幅均匀受光，无阴影。
- 阴影：无阴影——体积靠平涂与细线；光晕以同心圆色带表示。
- 透视：无透视；空间靠叠压与等级，不靠焦点透视。

## (6) 该画什么 / 不该画什么

- 该画：白度母、绿度母、五方佛、二十一度母、护法与眷属、佛传故事。`verbatim`
- 不该画：焦点透视；写实阴影；自由不对称构图；无度量网格的随意人体；世俗风景。
- Negative prompt: `single-point perspective, realistic shadows, asymmetrical free composition, empty background, oil-painting shading, photorealistic faces`

## (7) 测试提示词示例（现代题材：便利店夜景）

- Prompt: `In the style of Mongolian thangka, a small convenience store at night in a modern city, mineral pigments on cotton, iconometric grid, central deity-like shop in strict symmetry, flat gold lapis blue and vermilion, fine outlines, no perspective or shadow`
- 中文对照：蒙古唐卡风格，现代城市街角的便利店夜景，棉布矿物颜料，造像度量网格，店铺如中央尊像般严格对称，平涂金、青金石蓝与朱红，细线勾边，无透视无阴影。
- Negative: 见第 (6) 节。
- 检验点：构图是否严格对称、中央是否最大；度量网格是否在场；金蓝红是否并置。
