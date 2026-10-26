# Raphael Sanzio — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Raphael, High Renaissance fresco, perfect harmony and balance, graceful natural figures, clear luminous colours, one-point perspective, serene clarity, oil and fresco`
- ZH: 拉斐尔风格，盛期文艺复兴湿壁画与油画，完美和谐均衡，人物优雅自然，色彩明朗，单点透视，宁静清明。

## (2) 色板方向

- 主色（7 色，颜料名）：群青、朱红、土黄、淡粉肤色、墨绿、铅白、赭石。`verbatim`
- 辅色：淡紫（阴影）、金黄（衣袍）。
- 禁色：激烈扭曲的人体；浓重阴影；拥挤杂乱的构图；高饱和的刺眼色。
- 冷暖：冷暖均衡——群青与朱红并置，暖肤与冷建筑对照，无一边倒。
- 明暗 / 饱和：中低对比，明暗过渡柔和；饱和度适中而明亮，色彩清晰不浑。

## (3) 笔触与线条

- 笔触：细腻、平滑，几乎看不见笔触；湿壁画与油画皆以薄涂为主，表面光洁。`verbatim`
- 线条：轮廓线清晰、优雅、流畅，衣纹线如水波般自然下垂。
- 质感：湿壁画哑光 + 油画光滑；人物皮肤如瓷，衣料轻软。

## (4) 构图习惯

- 画幅：壁画与祭坛画皆有；《雅典学院》为横幅，建筑拱门框住全幅。`verbatim`
- 视点：平视；灭点在柏拉图与亚里士多德两首之间，是全幅的中心。`artifact`
- 布局：严格对称——柏拉图与亚里士多德居中，左右各有哲人分组，台阶、柱子、拱顶层层后退；《西斯廷圣母》为金字塔构图，圣母居中、两位圣徒分列、底部两个小天使。`verbatim`
- 裁切：几乎不裁切，画面完整、均衡，人物各有位置，无一处拥挤。

## (5) 光影与透视

- 光源：均匀、明朗的光，《雅典学院》光从画面外上方来，与真实房间的窗光一致。
- 阴影：淡而柔的阴影，体积靠明暗的轻微深浅，不靠强烈反差。
- 透视：单点线性透视，建筑正交线收向灭点；人物按透视逐层缩小，空间深远而清晰。`artifact`

## (6) 该画什么 / 不该画什么

- 该画：哲人集会、圣母与圣婴、圣徒群像；古典建筑拱门；优雅的对话群像。
- 不该画：激烈扭曲的人体；浓重阴影；拥挤杂乱；装饰性花纹喧宾夺主。
- Negative prompt: `violent twisted bodies, heavy dark shadows, crowded chaotic composition, saturated garish colours, rough visible brushstrokes, gold leaf background`

## (7) 测试提示词示例（现代题材：大学图书馆阅览室）

- Prompt: `In the style of Raphael, a university library reading room in the modern day, High Renaissance fresco, perfect harmony and balance, graceful natural figures of students reading, clear luminous colours, one-point perspective with vanishing point between two central readers, serene clarity`
- 中文对照：拉斐尔风格，现代大学图书馆阅览室，盛期文艺复兴湿壁画，完美和谐均衡，学生优雅自然地阅读，色彩明朗，单点透视、灭点在两位中央读者之间，宁静清明。
- Negative: 见第 (6) 节。
- 检验点：构图是否对称均衡、无一处拥挤；人物是否优雅自然；灭点是否落在画面中心。
