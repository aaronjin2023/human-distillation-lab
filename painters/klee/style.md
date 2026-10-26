# Paul Klee — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paul Klee, Bauhaus watercolour and oil, witty linear drawing, fish and birds and machines made of thin lines, muted ochre blue and rose, small scale, humour and music`
- ZH: 克利风格，包豪斯水彩与油彩，机智的线描，鱼、鸟与机器由细线构成， muted 的赭石、蓝与玫瑰色，小幅，幽默与音乐。

## (2) 色板方向

- 主色（7 色，颜料名）：赭石、群青、玫瑰红、土黄、灰绿、黑色、白色。`verbatim`
- 主色赭石 + 群青 + 玫瑰红，低饱和、温和；线是主角、色是配角。禁：高饱和大面积、厚涂、写实明暗。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：水彩薄涂，轻而透明；线条是本体——细、自由、机智的线，时而颤抖、时而精确。质感：纸面轻、薄，无厚涂。

## (4) 构图习惯

- 画幅：小幅为主；视点：无视点、平面；布局：符号与小物居中、疏密有致，留白即纸面；画面如乐谱或日记页。裁切：物象完整、小而居中。

## (5) 光影与透视

- 光源：无光源、无阴影；明暗只来自水彩的深浅。透视：无透视，平面即全部。

## (6) 该画什么 / 不该画什么

- 该画：鱼、鸟、机器、星、月、字母、建筑。
- 不该画：见下 Negative prompt。
- Negative prompt: `no thick impasto, no bright saturated large areas, no photographic realism, no single-point perspective, no grey dull wash filling the paper`

## (7) 测试提示词示例（现代题材：深夜拉面店）

- Prompt: `In the style of Paul Klee, a late-night ramen shop, Bauhaus watercolour and oil, witty linear drawing, fish and birds and machines made of thin lines, muted ochre blue and rose, small scale, humour and music`
- 中文对照：克利风格，深夜拉面店，包豪斯水彩与油彩，机智的线描，鱼、鸟与机器由细线构成， muted 的赭石、蓝与玫瑰色，小幅，幽默与音乐。
- Negative: 见第 (6) 节。
- 检验点：题材是否被克利的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
