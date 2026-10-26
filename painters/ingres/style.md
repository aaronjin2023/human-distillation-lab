# Jean-Auguste-Dominique Ingres — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Neoclassical, flowing serpentine line, porcelain-smooth skin, invisible brushwork, cool luminous palette, elegant elongated figures, sensual and serene`
- ZH: 新古典主义，蛇形流畅线条，瓷器般光滑肌肤，无笔触，冷调明亮色调，优雅拉长的人体，感性而宁静。

## (2) 色板方向

- 主色（7 色，颜料名）：铅白、珍珠灰、淡粉红、群青、赭石、墨绿、淡金黄。`verbatim`
- 主色冷而亮：珍珠白肤色 + 群青织物 + 淡金点缀；暖色只给肤色与丝绸，整体清冷高雅。`verbatim`
- 辅色：淡紫、湖绿、暖灰。
- 禁色：粗笔触；高饱和艳色铺满；暖调铺满；强明暗对比。
- 冷暖：冷调为主，肤色暖粉作唯一暖点；冷暖对比柔和，靠线条不靠色彩取胜。
- 明暗 / 饱和：高明度、低饱和、低—中对比；亮部平滑如瓷，暗部极浅。

## (3) 笔触与线条

- 笔触：平滑、看不见笔触；多层薄涂打磨，追求瓷器表面。`verbatim`
- 线条：线条是本体：蛇形、流畅、连续的轮廓线，拉长人体（《大宫女》多画了几节脊椎，见 conflicts.md）；线条优先于一切。
- 质感：光滑无肌理；肌肤、丝绸、织物都打磨到无笔触。

## (4) 构图习惯

- 画幅：横幅与竖幅并存；《大宫女》1814 年，横卧人体占满横幅；《土耳其浴室》初为长方形、1862 年改为圆形（tondo）。
- 视点：平视，观者与人体同高；无俯仰，视线沿蛇形轮廓游走。
- 布局：人体横卧 / 环绕成圆：浴室人物环成圆形“曲线赋格”，视线在圆里转圈；大宫女横卧成 S 形。
- 裁切：人体常顶边，织物与器物裁边，制造亲密感；不留安全边距。

## (5) 光影与透视

- 光源：均匀冷光，无固定光源；亮在肌肤，暗部极浅。
- 阴影：阴影是珍珠灰、淡紫的极浅渐变，几乎无暗部；明暗靠线条转折不靠黑。
- 透视：浅空间，人物贴近画面；无焦点透视，空间靠人物前后错落与织物层叠。

## (6) 该画什么 / 不该画什么

- 该画：横卧裸体、浴女、东方织物与器物、优雅拉长的人体、蛇形轮廓。`verbatim`
- 不该画：粗笔触；高饱和艳色；强明暗；写实解剖；戏剧性斜构图。
- Negative prompt: `visible rough brushstrokes, high-saturation colour, strong chiaroscuro, anatomical realism, dramatic diagonal chaos, photorealistic skin texture`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Jean-Auguste-Dominique Ingres, a small Yorkshire terrier sitting on a subway seat, Neoclassical, flowing serpentine line, porcelain-smooth fur, invisible brushwork, cool luminous palette, elegant elongated pose, serene`
- 中文对照：安格尔风格，一只小约克夏犬坐在地铁座位上，新古典主义，蛇形流畅线条，瓷器般光滑毛发，无笔触，冷调明亮色调，优雅拉长的姿态，宁静。
- Negative: 见第 (6) 节。
- 检验点：狗的轮廓是否如丝绸般流畅拉长、毛发是否光滑无笔触，而不是写实描毛；色调是否冷而亮。
