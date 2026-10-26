# Masaccio — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Masaccio, early Renaissance fresco, systematic one-point linear perspective, solid sculptural figures, consistent light from the upper right, muted earth colours, clear rational space, painting as a window`
- ZH: 马萨乔风格，早期文艺复兴湿壁画，系统单点透视，人物结实如雕塑，光线统一从右上方来，土色为主，空间清晰理性，如窗外真实世界。

## (2) 色板方向

- 主色（7 色，颜料名）：赭石、土红、群青、土黄、铅白、灰绿、暗褐。`verbatim`
- 辅色：淡灰（远山空气透视）、暗灰（阴影）。
- 禁色：金底；装饰性图案；不统一的多光源；哥特式纤细人物。
- 冷暖：暖土色人物配冷灰绿远景；光是暖的，影是冷灰的。
- 明暗 / 饱和：中对比，靠明暗塑造体积；亮部集中，暗部沉稳；饱和度克制。

## (3) 笔触与线条

- 笔触：湿壁画笔触肯定、简练，色块大而明确；衣纹用几笔宽阔明暗带出，不细碎。`verbatim`
- 线条：轮廓线为体积服务，不独立装饰；人物造型靠明暗，不靠线条。
- 质感：灰泥哑光，颜料渗入墙体；远景用空气透视变淡、变灰。

## (4) 构图习惯

- 画幅：壁画横幅为主；《纳税钱》为连续叙事——同一画面中三个时刻（中央问税、左侧取币、右侧缴税）。`verbatim`
- 视点：平视，灭点在观者视线高度（《圣三位一体》灭点在祭坛高度，约常人视线高）。`artifact`
- 布局：《圣三位一体》为金字塔构图——上帝居顶、基督居中、圣母与圣约翰分列、供养人跪于两侧；《纳税钱》以基督头部为灭点，人物半圆形环绕。`verbatim`
- 裁切：人物不顶边，空间完整；建筑与山体框出叙事舞台。

## (5) 光影与透视

- 光源：单一、统一的光源，《纳税钱》光从右上方来，全幅人物的受光与投影方向一致。`verbatim`
- 阴影：明暗交界明确，亮面、中间调、暗面三段分明，塑造雕塑感。
- 透视：单点线性透视 + 空气透视并用；《圣三位一体》是现存最早系统使用单点透视的作品，拱顶与地面正交线收向同一灭点。`artifact`（大英百科全书）

## (6) 该画什么 / 不该画什么

- 该画：圣经叙事群像；连续叙事；古典建筑拱门；远山风景；供养人肖像。
- 不该画：金底；无空间感的平面排列；多光源；装饰性花纹喧宾夺主。
- Negative prompt: `gold leaf background, flat pattern without space, multiple inconsistent light sources, thin Gothic figures, ornate decoration, smooth academic blending`

## (7) 测试提示词示例（现代题材：共享单车停放点）

- Prompt: `In the style of Masaccio, a shared-bicycle parking area in a modern city at noon, early Renaissance fresco, systematic one-point linear perspective, solid sculptural figures, a row of bicycles receding to a single vanishing point, consistent light from the upper right, muted earth colours, clear rational space`
- 中文对照：马萨乔风格，正午现代城市里的共享单车停放点，早期文艺复兴湿壁画，系统单点透视，人物结实如雕塑，一排单车向同一灭点退去，光线统一从右上方来，土色为主，空间清晰理性。
- Negative: 见第 (6) 节。
- 检验点：透视线是否收向同一灭点；光线方向是否全幅统一；人物与单车是否有体积感而不是平面剪贴。
