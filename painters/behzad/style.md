# Kamal al-Din Behzad — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Persian miniature, Herat school, fine brushwork and psychological expression, complex architecture framing the scene, flat vivid blue green and gold, figures in motion against a flat ground`
- ZH: 波斯细密画，赫拉特画派，精细笔法与心理表情，复杂建筑框住场景，平涂鲜明的蓝绿与金，人物在平地上动态行走。

## (2) 色板方向

- 主色（7 色，颜料名）：群青、孔雀石绿、金色、朱红、墨色、淡紫、白垩白。`verbatim` / `artifact`
- 蓝绿金三色并置是赫拉特一路的标志：《优素福与祖莱卡》以浓蓝为地、金为饰、红为点睛。`verbatim`
- 辅色：淡紫画衣纹、白垩白画面部与衣饰。
- 禁色：油画式渐变与明暗；焦点透视；写实肤色渐变；大面积留白。
- 冷暖：整体偏暖，金与朱红定暖调，群青与石绿作冷色对照。
- 明暗 / 饱和：无明暗；体积靠平涂色块与细线；亮在金色与群青处。

## (3) 笔触与线条

- 笔触：不是笔触，是细线与平涂——以极细的笔勾线，颜料平涂，笔触不可见；同代人称其笔法精细、表情传神。`artifact`
- 线条：细墨线勾边定一切，线均匀、精细、有韧性；建筑的几何线与人物的衣纹线同样精密。`verbatim`
- 质感：纸面光滑 + 不透明颜料的粉质平涂 + 金的反光；无油彩堆积，无水墨晕染。

## (4) 构图习惯

- 画幅：书页插图，小幅；每幅配一段文字，图文一体。`artifact`
- 视点：高视点俯瞰 + 平面构成；建筑以多视点拼合，屋顶、墙面、地面各取最佳角度。`verbatim`（《优素福与祖莱卡》的宫殿）
- 布局：建筑框住场景，人物在建筑前景动态行走；平地拉长，视线随人物移动。`verbatim`
- 裁切：画面满幅，建筑常被裁掉边缘，人物出画边。

## (5) 光影与透视

- 光源：无固定光源；全幅均匀受光，无阴影。
- 阴影：无阴影——体积靠平涂与细线。
- 透视：无透视；建筑以多视点拼合，空间靠叠压，不靠焦点透视。

## (6) 该画什么 / 不该画什么

- 该画：优素福与祖莱卡、萨迪蔷薇园故事、亚历山大史、宫廷宴饮、花园与建筑。`verbatim`
- 不该画：焦点透视；写实阴影；留白构图；人物稀疏的空旷画面；无建筑框景的纯人物。
- Negative prompt: `single-point perspective, realistic shadows, empty background, sparse composition, oil-painting shading, photorealistic faces`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Kamal al-Din Behzad, a small Yorkshire terrier sitting on a subway seat, Persian miniature, Herat school, fine brushwork, complex architecture framing the scene, flat vivid blue green and gold, the dog in motion against a flat ground`
- 中文对照：贝赫扎德风格，一只小约克夏犬坐在地铁座位上，波斯细密画，赫拉特画派，精细笔法，复杂建筑框住场景，平涂鲜明的蓝绿与金，狗在平地上动态行走。
- Negative: 见第 (6) 节。
- 检验点：建筑是否框住场景、是否多视点拼合；人物（狗）的表情是否细腻；蓝绿金是否并置。
