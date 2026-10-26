# Wu Daozi — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wu Daozi, High Tang religious figure painting, Wu belt when wind lines, bold free sweeping ink lines, dynamic drapery in motion, ink with light colour, figures larger than life`
- ZH: 吴道子风格，盛唐宗教人物画，吴带当风的线条，大胆自由的挥洒墨线，衣带飘动如风，墨线为主略施淡彩，人物气势超凡。

## (2) 色板方向

- 主色（颜料名）：墨色、朱砂、赭石、花青、石绿、石青、藤黄。`verbatim` / `artifact`
- 辅色：淡朱砂、淡石青点染，墨线为主、色只点睛。
- 禁色：工笔细描；满幅重彩平涂；静止对称的构图。
- 冷暖：墨分浓淡为主，暖色只作点染；整体清、亮、透，不沉。
- 明暗 / 饱和：靠墨的浓淡干湿，不靠明暗渐变；饱和度克制，亮在留白。

## (3) 笔触与线条

- 笔触：“吴带当风”：线条起伏顿挫、粗细变化大，衣纹如被风吹动，笔势如行云流水；与顾恺之细线、阎立本铁线皆不同，以动取胜。`artifact`（画史通说；潘天寿评语转引）
- 线条：书法性线条，中锋为主；轮廓不封闭，靠笔意收住形。
- 质感：绢 / 纸上水墨晕染 + 枯笔飞白；无油彩堆积，无工笔细线。

## (4) 构图习惯

- 画幅：满幅群像：天王、神将、仙人层层叠置，人物大小参差、动势交错，画面如旋风般卷动；主尊居中，余众环绕呼应。`verbatim`（《送子天王图》摹本）
- 视点：平视 / 轻微俯视；无焦点透视，散点 / 平面构成。
- 布局：题款、印章是构图的一部分，位置计入画面平衡。
- 裁切：满幅群像是其本体——天王神将层层叠置、动势交错，留白只在衣纹翻卷的间隙；画面满而不塞。

## (5) 光影与透视

- 光源：无固定光源、无明暗体积；动势与线的疏密即体积，衣纹的起伏即光影。`verbatim`
- 阴影：无写实阴影；墨的浓淡即体积，淡即远、浓即近。
- 透视：无焦点透视；空间靠留白 + 墨色浓淡推远近。

## (6) 该画什么 / 不该画什么

- 该画：佛道神仙、天王神将、群仙行列、飘动的衣带、壁画式大场面、墨线为主的人物。`verbatim`
- 不该画：细弱游丝线、呆板对称的等级构图、重彩满涂、写实明暗、静态肖像、工笔细描。
- Negative prompt: `thin weak lines, stiff symmetrical court composition, heavy colour filling, photorealistic shading, static portrait, meticulous gongbi detail`

## (7) 测试提示词示例（现代题材：窗台上的咖啡）

- Prompt: `In the style of Wu Daozi, a cup of coffee on a windowsill in a modern city, bold free sweeping ink lines, drapery-like steam curling like wind-blown ribbons, ink with light colour, dynamic movement, figures larger than life in spirit`
- 中文对照：吴道子风格，现代城市窗台上的一杯咖啡，大胆自由的挥洒墨线，蒸汽如被风吹动的衣带般卷曲，墨线为主略施淡彩，动势超凡。
- Negative: 见第 (6) 节。
- 检验点：莼菜条描的线条动势与满幅群像构图二者至少其一成立；衣带是否如风吹动、人物是否大小参差动势交错，而不是只换了题材。
