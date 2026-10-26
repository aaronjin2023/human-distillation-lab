# Georgia O'Keeffe — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Georgia O'Keeffe, American modernist oil painting, enlarged flower filling the whole canvas, soft smooth gradients of white and pale colour, black iris centre, desert bones and sky, quiet monumentality`
- ZH: 欧姬芙风格，美国现代主义油画，放大到满幅的花，白色与淡色的柔和渐变，黑鸢尾中心，沙漠骨骼与天空，安静的纪念性。

## (2) 色板方向

- 主色（7 色，颜料名）：白色、淡粉、淡黄、黑色、深紫、赭石、天蓝。`verbatim`
- 主色白色 + 淡粉、淡黄的柔和渐变；黑鸢尾以黑、深紫为中心。禁：高饱和刺目色、厚涂笔触、拥挤细节。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：极平滑的渐变，笔触不可见，如空气般过渡；线条：花瓣轮廓线柔和、连续。质感：光滑、薄涂，如缎面。

## (4) 构图习惯

- 画幅：方形与竖幅为主；视点：极近距离、放大；布局：单朵花占满画面，边缘出画；沙漠风景则地平线低、天空占大半。裁切：花瓣被画幅切断，放大即构图。

## (5) 光影与透视

- 光源：柔和、均匀的日光，无戏剧阴影；阴影是色彩渐变本身。透视：无透视，花即平面，放大后花即风景。

## (6) 该画什么 / 不该画什么

- 该画：放大的花、鸢尾、曼陀罗、沙漠骨骼、牛头骨、新墨西哥天空与山。
- 不该画：见下 Negative prompt。
- Negative prompt: `no visible brushstrokes, no thick impasto, no bright harsh saturated colour, no crowded detail, no single-point perspective`

## (7) 测试提示词示例（现代题材：现代城市街角的便利店夜景）

- Prompt: `In the style of Georgia O'Keeffe, a small convenience store at night in a modern city, American modernist oil painting, enlarged flower filling the whole canvas, soft smooth gradients of white and pale colour, black iris centre, desert bones and sky, quiet monumentality`
- 中文对照：欧姬芙风格，现代城市街角的便利店夜景，美国现代主义油画，放大到满幅的花，白色与淡色的柔和渐变，黑鸢尾中心，沙漠骨骼与天空，安静的纪念性。
- Negative: 见第 (6) 节。
- 检验点：题材是否被欧姬芙的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
