# Tawaraya Sōtatsu — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Rinpa decorative screen painting, gold-leaf ground, bold cropped figures, tarashikomi pooled ink and colour, flat vivid colour, playful gods on drifting clouds`
- ZH: 琳派装饰屏风画，金箔地，大胆裁切的人物，垂洒法晕染的墨色与色彩，平涂鲜明，风神雷神乘云嬉戏。

## (2) 色板方向

- 主色（7 色，颜料名）：金箔、银粉、墨色、朱红、石绿、群青、赭石。`verbatim` / `artifact`
- 金地是主色而非背景：风神雷神屏风以金箔满地，神只与云浮于金上。`verbatim`
- 辅色：银粉入云、淡墨染水；花卉一路石绿与朱红并用。
- 禁色：灰暗土色大面积平涂；写实明暗渐变；无金地的素纸大面积留白（与雪舟相反）。
- 冷暖：整体暖亮，金地定暖调，石绿与群青作冷色点缀。
- 明暗 / 饱和：无写实明暗；体积靠平涂色块的并置与垂洒的浓淡，不靠渐变。

## (3) 笔触与线条

- 笔触：垂洒法（tarashikomi）——第一层未干即加第二层，墨与色在湿处自然晕化，云、水、雾皆由此生。`artifact`（维基百科“Tawaraya Sōtatsu”）
- 线条：自由奔放的粗线，风神雷神的轮廓线粗而不断，神态靠线走；花卉一路线更细、更装饰。`verbatim`
- 质感：金箔的平滑反光 + 垂洒的偶然晕染 + 平涂的厚实，三种质感并置。

## (4) 构图习惯

- 画幅：二曲一双屏风为主，横长幅面；也有扇面、卷轴与光悦和歌料纸装饰。`artifact`
- 视点：平视 / 轻微俯视；无焦点透视，平面构成。
- 布局：风神雷神屏风的经典布局——左右两神各占一扇、体大到裁掉边角，中间大面积留空（金地），视线在两神之间来回。`verbatim`
- 裁切：主体故意裁掉边缘，神只的身体出画，是装饰屏风的大胆之处。`verbatim`

## (5) 光影与透视

- 光源：无固定光源；亮在金箔本身，金地即光源。
- 阴影：无写实阴影；云的体积靠垂洒的浓淡。
- 透视：无透视；空间靠前后色块的叠压，云在前、神在后、金地在最深处。

## (6) 该画什么 / 不该画什么

- 该画：风神雷神、莲池水禽、四季花卉、源氏物语场面、和歌料纸装饰。`verbatim`
- 不该画：写实风景的焦点透视；灰调写实；素纸大面积留白；精细工笔的满幅描绘。
- Negative prompt: `single-point perspective, photorealistic shading, grey muted palette, plain paper background without gold, meticulous gongbi rendering`

## (7) 测试提示词示例（现代题材：窗台上的咖啡）

- Prompt: `In the style of Tawaraya Sōtatsu, a cup of coffee on a windowsill, Rinpa decorative screen painting, gold-leaf ground, tarashikomi pooled ink clouds drifting behind the cup, flat vivid colour, bold cropped composition`
- 中文对照：宗达风格，一杯放在窗台上的咖啡，琳派装饰屏风画，金箔地，垂洒法晕染的云气在杯后流动，平涂鲜明，大胆裁切的构图。
- Negative: 见第 (6) 节。
- 检验点：金地是否满铺、是否亮；云气是否有垂洒的偶然晕染而不是画出来的轮廓；杯子是否被裁切、是否够大胆。
