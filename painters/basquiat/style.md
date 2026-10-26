# Jean-Michel Basquiat — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jean-Michel Basquiat, Neo-Expressionist graffiti painting, skull head with teeth and hollow eyes, crown motif, scribbled words crossed out, raw oil stick and acrylic on canvas, urgent street energy`
- ZH: 巴斯奎亚风格，新表现主义涂鸦绘画，露齿空眼的头骨、皇冠符号、涂改的文字，粗糙的油画棒与丙烯，街头般的紧迫能量。

## (2) 色板方向

- 主色（7 色，颜料名）：黑色、白色、红色、黄色、蓝色、灰色、赭石。`verbatim`
- 主色黑、白、红、黄的强烈对撞；色彩如涂鸦般直接。禁：平滑写实、灰调、安静均衡构图。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：油画棒粗暴涂抹、丙烯泼洒，笔触急、乱、有力；线条：涂鸦般的自由线，字即线。质感：粗糙、厚薄并置，画布常露底。

## (4) 构图习惯

- 画幅：大幅为主；视点：无视点；布局：头骨或人物居中、占满画面，文字与符号挤满四周；无留白。裁切：头骨顶边出画，文字出画。

## (5) 光影与透视

- 光源：无光源、无阴影；明暗只来自色彩的对撞。透视：无透视，平面即全部。

## (6) 该画什么 / 不该画什么

- 该画：头骨、皇冠、涂改文字、拳击手、爵士乐手、解剖图。
- 不该画：见下 Negative prompt。
- Negative prompt: `no smooth academic shading, no grey muted palette, no photographic realism, no calm balanced composition, no empty background`

## (7) 测试提示词示例（现代题材：深夜拉面店）

- Prompt: `In the style of Jean-Michel Basquiat, a late-night ramen shop, Neo-Expressionist graffiti painting, skull head with teeth and hollow eyes, crown motif, scribbled words crossed out, raw oil stick and acrylic on canvas, urgent street energy`
- 中文对照：巴斯奎亚风格，深夜拉面店，新表现主义涂鸦绘画，露齿空眼的头骨、皇冠符号、涂改的文字，粗糙的油画棒与丙烯，街头般的紧迫能量。
- Negative: 见第 (6) 节。
- 检验点：题材是否被巴斯奎亚的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
