# Leonardo da Vinci — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Leonardo da Vinci, High Renaissance oil painting, sfumato smoky gradations, no hard outlines, chiaroscuro, atmospheric perspective, enigmatic half-smile, deep warm shadows, oil on panel`
- ZH: 达·芬奇风格，盛期文艺复兴油画，晕涂法烟雾般过渡，无硬轮廓线，明暗法，空气透视，含糊的半笑，深暖阴影，木板油画。

## (2) 色板方向

- 主色（7 色，颜料名）：赭石、土黄、群青、墨绿、朱红、铅白、暗褐。`verbatim`
- 辅色：灰蓝（远山空气透视）、暖灰（阴影过渡）。
- 禁色：硬轮廓线；高饱和的平涂色块；清晰的黑白明暗二分；卡通式的明确表情。
- 冷暖：暖调为主——暖褐、暖肤、暖金；远景转冷灰蓝，冷暖随距离变化。
- 明暗 / 饱和：中对比，但过渡极缓；亮部柔和、暗部深暖；饱和度克制，靠明暗不靠色相。

## (3) 笔触与线条

- 笔触：极细、极薄，层层晕涂，几乎看不见笔触；手指或软笔晕开边缘是常用手法。`artifact`
- 线条：无硬轮廓线——轮廓在明暗过渡中融化，所谓晕涂（sfumato）即“如烟雾般消失”。`artifact`
- 质感：木板油画光滑如镜；《最后的晚餐》因实验性技法（油彩加树脂画在干墙上）而剥落严重，质感与原作有别，见 conflicts.md。

## (4) 构图习惯

- 画幅：祭坛画与壁画皆有；《最后的晚餐》为横幅，基督居中、门徒左右各六人分四组。`verbatim`
- 视点：平视；《最后的晚餐》灭点在基督头部，视线与餐桌平行。`verbatim`
- 布局：金字塔与对称构图——《蒙娜丽莎》为金字塔式坐姿，《最后的晚餐》以基督为中心对称展开；《岩间圣母》人物成金字塔，岩洞框住。`verbatim`
- 裁切：人物半身或全身完整，少有裁切；背景风景占大幅，人物与风景同等重要。

## (5) 光影与透视

- 光源：柔和的漫射光，《最后的晚餐》光从左侧窗户来，全幅一致。
- 阴影：深暖的阴影，亮暗之间有极长的中间调过渡——晕涂的本体。
- 透视：线性透视 + 空气透视并用；远山随距离变淡、变蓝、变模糊，是空气透视的范本。`artifact`

## (6) 该画什么 / 不该画什么

- 该画：半身肖像、圣母与圣婴、最后的晚餐式群像；岩洞、远山、蜿蜒河流；含糊的微笑。
- 不该画：硬轮廓线；平涂高饱和色；明确夸张的表情；装饰性金底。
- Negative prompt: `hard outlines, flat saturated colour blocks, sharp black-and-white contrast, exaggerated cartoon expression, gold leaf background, visible rough brushstrokes`

## (7) 测试提示词示例（现代题材：便利店夜景）

- Prompt: `In the style of Leonardo da Vinci, a small convenience store at night in a modern city, High Renaissance oil painting, sfumato smoky gradations, no hard outlines, warm light glowing from the shop window dissolving into deep blue night, atmospheric perspective, enigmatic calm, oil on panel`
- 中文对照：达·芬奇风格，现代城市里的一家便利店夜景，盛期文艺复兴油画，晕涂法烟雾般过渡，无硬轮廓线，店窗暖光融化在深蓝夜色里，空气透视，含糊的宁静，木板油画。
- Negative: 见第 (6) 节。
- 检验点：边缘是否融化在夜色里而不是硬线勾出；暖光与深蓝夜色之间是否有长长的过渡；表情与氛围是否含糊而深邃。
