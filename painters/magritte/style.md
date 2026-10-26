# René Magritte — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of René Magritte, Surrealist oil painting, flat deadpan realism, bowler-hat man with a green apple hiding his face, ordinary objects in impossible places, blue sky with white clouds, word against image`
- ZH: 马格利特风格，超现实主义油画，扁平的冷面写实，圆顶礼帽男子的脸被青苹果遮住，日常物出现在不可能的地方，蓝天白云，文字与图像对峙。

## (2) 色板方向

- 主色（7 色，颜料名）：天蓝、白色、黑色、青苹果绿、灰色、赭石、深褐。`verbatim`
- 主色天蓝 + 白云 + 黑礼帽，干净、冷静的日常色。禁：厚涂笔触、高饱和情绪色、模糊梦境。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：平滑、均匀，几乎无笔触，如商业插画；线条：清晰、冷静的轮廓线。质感：平面、光滑，无肌理表现。

## (4) 构图习惯

- 画幅：中小幅为主；视点平视；布局：人物或物象居中、孤立，背景是蓝天、白云、海或墙；物象完整、不顶边。裁切：物象不裁切，完整呈现才显荒诞。

## (5) 光影与透视

- 光源：均匀、明亮的日光，无戏剧阴影；阴影轻而清晰。透视：写实透视，但物象组合违反逻辑（苹果挡脸、烟斗不是烟斗）。

## (6) 该画什么 / 不该画什么

- 该画：圆顶礼帽男子、青苹果、烟斗、巨石、鸟、门、镜。
- 不该画：见下 Negative prompt。
- Negative prompt: `no visible brushstrokes, no thick impasto, no emotional saturated colour, no blurred dreamy atmosphere, no ordinary logical combination`

## (7) 测试提示词示例（现代题材：现代城市街角的便利店夜景）

- Prompt: `In the style of René Magritte, a small convenience store at night in a modern city, Surrealist oil painting, flat deadpan realism, bowler-hat man with a green apple hiding his face, ordinary objects in impossible places, blue sky with white clouds, word against image`
- 中文对照：马格利特风格，现代城市街角的便利店夜景，超现实主义油画，扁平的冷面写实，圆顶礼帽男子的脸被青苹果遮住，日常物出现在不可能的地方，蓝天白云，文字与图像对峙。
- Negative: 见第 (6) 节。
- 检验点：题材是否被马格利特的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
