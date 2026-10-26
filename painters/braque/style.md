# Georges Braque — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Georges Braque, Cubist oil painting, muted ochre grey and green facets, quiet geometric still life, guitar and houses broken into interlocking planes, stencilled letters, sand texture`
- ZH: 布拉克风格，立体主义油画， muted 的赭石、灰、绿切面，安静的几何静物，吉他与房屋碎成咬合的平面，模板字母，沙粒质感。

## (2) 色板方向

- 主色（7 色，颜料名）：赭石、灰绿、灰色、土黄、黑色、白色、暗褐。`verbatim`
- 主色赭石 + 灰绿 + 灰，低饱和、安静的土调；比毕加索更克制。禁：高饱和亮色、平滑写实渐变、空背景。
- 冷暖：见上；明暗 / 饱和：靠色块本身的明度与对比，不靠写实明暗渐变。

## (3) 笔触与线条

- 笔触：小切面短笔，笔触细密均匀；常在颜料中掺沙，增加粗糙质感。线条：细而克制的轮廓线，切面边缘即线。质感：沙粒粗糙 + 平涂，触感强。

## (4) 构图习惯

- 画幅：中小幅静物与风景为主；视点：多视点但比毕加索更收敛；布局：物象居中、切面咬合、地平线消失；画面安静、均衡。裁切：吉他、桌角常被画幅切断。

## (5) 光影与透视

- 光源：无统一光源，光来自切面的明暗；阴影是切面本身。透视：多视点、空间压缩，前景与背景咬合在一起。

## (6) 该画什么 / 不该画什么

- 该画：吉他、静物、莱斯塔克房屋、鸟、画室。
- 不该画：见下 Negative prompt。
- Negative prompt: `no bright saturated colour, no smooth academic shading, no single-point perspective, no photographic realism, no empty background`

## (7) 测试提示词示例（现代题材：现代城市街角的便利店夜景）

- Prompt: `In the style of Georges Braque, a small convenience store at night in a modern city, Cubist oil painting, muted ochre grey and green facets, quiet geometric still life, guitar and houses broken into interlocking planes, stencilled letters, sand texture`
- 中文对照：布拉克风格，现代城市街角的便利店夜景，立体主义油画， muted 的赭石、灰、绿切面，安静的几何静物，吉他与房屋碎成咬合的平面，模板字母，沙粒质感。
- Negative: 见第 (6) 节。
- 检验点：题材是否被布拉克的风格吃掉、而不是只贴了一层滤镜；该有的笔触 / 色块 / 线条是否成立；不该有的东西（见 Negative）是否出现。
