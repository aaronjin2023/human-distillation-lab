# György Ligeti — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Micropolyphony, dense sound masses, cluster harmony, rhythmic illusion, luminous texture, mechanical patterns turning lyrical`
- ZH: 微复调，密集音块，簇和声，节奏幻觉，明亮织体，机械音型转为抒情。

## (2) 旋律与和声

- 旋律：微复调中无单一旋律线，线条在密集声部中浮现；练习曲有机械音型旋律。`artifact`
- 和声：音簇与密集和声，调性无；和声靠密度与音区移动。`artifact`

## (3) 节奏与织体

- 节奏：多层复节奏，听感上节拍模糊；练习曲有精确机械节奏；织体：极密微复调与极稀疏留白并置。

## (4) 配器与音色

- 配器：大编制管弦，声部极多；钢琴练习曲独奏；人声在《安魂曲》中作音色层。

## (5) 曲式与结构

- 曲式：音块渐变结构、练习曲集；高潮靠密度变化，结尾常渐弱或突断。

## (6) 该写什么 / 不该写什么

- 该写：微复调音块、音簇和声、多层复节奏、机械音型、密度渐变、明亮音色层。
- 不该写：functional harmony、no singable melody as the main line、no regular metre throughout、no traditional form、no sentimental swell、no thin texture as climax。
- Negative prompt: `No functional harmony, no singable melody as the main line, no regular metre throughout, no traditional form, no sentimental swell, no thin texture as climax`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of György Ligeti, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, micropolyphonic sound mass, cluster harmony, shimmering texture, mechanical piano pattern underneath`
- 中文对照：利盖蒂风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，微复调音块，簇和声，闪烁织体，机械钢琴音型在底层。
- Negative: `No functional harmony, no singable melody as the main line, no regular metre throughout, no traditional form, no sentimental swell, no thin texture as climax`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
