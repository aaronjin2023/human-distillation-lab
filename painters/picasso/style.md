# Pablo Picasso — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pablo Picasso, Cubist oil painting, fragmented geometric facets, multiple viewpoints in one picture, African-mask faces, black white and grey in Guernica, ochre and blue in early Cubism, sharp angular planes`
- ZH: 毕加索风格，立体主义油画，破碎的几何切面，同一画面多视点，非洲面具式面孔，《格尔尼卡》黑白灰、早期立体主义赭石与蓝，锐利的角形平面。

## (2) 色板方向

- 主色（7 色，颜料名）：赭石、灰蓝、黑色、白色、灰色、土黄、暗红。`verbatim`
- 分两路：早期立体主义赭石 + 灰蓝的低饱和土调；《格尔尼卡》黑、白、灰单色。禁：高饱和愉快大面积、平滑写实渐变。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：切面式短笔，笔触方向随切面走；线条：锐利的角形轮廓线，形体被切成多面。质感：油彩平涂 + 局部厚涂，拼贴时期加入报纸、木纹等现成品。

## (4) 构图习惯

- 画幅：横幅大画为主（《格尔尼卡》近 8 米）；视点：多视点并置，正面与侧面同现；布局：人物与物象挤满画面、无留白、地平线消失；裁切：人物顶边出画，画面即战场。

## (5) 光影与透视

- 光源：无统一光源，光来自切面的明暗对比；阴影是切面本身，不用渐变。透视：多视点、反透视，空间被切碎重组。

## (6) 该画什么 / 不该画什么

- 该画：少女、吉他、静物、牛头、马、斗牛、画室、和平鸽。
- 不该画：见下 Negative prompt。
- Negative prompt: `no single-point perspective, no smooth academic shading, no bright cheerful palette, no photographic realism, no empty background`

## (7) 测试提示词示例（现代题材：一辆停在街边的共享单车）

- Prompt: `In the style of Pablo Picasso, a shared bicycle parked on a city street, Cubist oil painting, fragmented geometric facets, multiple viewpoints in one picture, African-mask faces, black white and grey in Guernica, ochre and blue in early Cubism, sharp angular planes`
- 中文对照：毕加索风格，一辆停在街边的共享单车，立体主义油画，破碎的几何切面，同一画面多视点，非洲面具式面孔，《格尔尼卡》黑白灰、早期立体主义赭石与蓝，锐利的角形平面。
- Negative: 见第 (6) 节。
- 检验点：题材是否被毕加索的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
