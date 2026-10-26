# Fra Angelico — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Fra Angelico, early Renaissance fresco and tempera, serene luminous devotion, pale pastel colours, gold halos, white loggia with slender columns, soft diffused light, stillness and clarity`
- ZH: 弗拉·安杰利科风格，早期文艺复兴湿壁画与蛋彩，宁静发光的虔敬，淡雅粉彩，金色光环，白色拱廊与细柱，柔和漫射光，静止清明。

## (2) 色板方向

- 主色（7 色，颜料名）：群青（圣母袍）、朱红（天使衣与圣母内袍）、金箔金（光环）、淡粉、嫩绿、铅白、赭石。`verbatim`
- 辅色：淡紫（阴影）、灰绿（远景）。
- 禁色：浓重暗色大面积平涂；巴洛克式强烈明暗；粗犷笔触；世俗的喧闹感。
- 冷暖：整体偏冷的淡彩，朱红与金色作暖点；光是冷而亮的，不暖黄。
- 明暗 / 饱和：低对比、柔和过渡；饱和度低而明亮，像清晨的光；阴影极淡。

## (3) 笔触与线条

- 笔触：细腻、平滑、几乎看不见笔触；蛋彩层层薄涂，表面如珐琅。`verbatim`
- 线条：轮廓线纤细、清晰、均匀，衣纹线如水波般平行下垂。
- 质感：湿壁画哑光 + 蛋彩细腻 + 金箔光泽，三种质感并置但都克制。

## (4) 构图习惯

- 画幅：壁画与祭坛画皆有；《圣母领报》为横幅，人物分列拱廊左右。`verbatim`
- 视点：平视，视线与人物齐平，观者如站在拱廊前。
- 布局：严格对称的拱廊建筑框住人物；加百列在左、圣母在右，中间一根细柱分隔；地面大理石透视收向一点。`verbatim`
- 裁切：几乎不裁切，画面完整、安静，人物与建筑都有呼吸的余地。

## (5) 光影与透视

- 光源：柔和漫射光，无明确光源方向，光仿佛从画面本身发出。
- 阴影：极淡的灰紫阴影，体积靠淡彩的轻微深浅，不靠明暗反差。
- 透视：单点透视的拱廊与地面，空间清晰但不深邃；建筑是秩序的象征，不是写实的空间。`artifact`

## (6) 该画什么 / 不该画什么

- 该画：圣母领报、圣徒群像、拱廊与花园；天使的彩色翅膀；细密的花草。
- 不该画：戏剧性的动作与表情；浓重阴影；拥挤的群像；世俗题材的喧闹。
- Negative prompt: `dramatic Baroque chiaroscuro, heavy dark shadows, crowded composition, rough visible brushstrokes, saturated garish colours, photorealistic detail`

## (7) 测试提示词示例（现代题材：窗台上的咖啡）

- Prompt: `In the style of Fra Angelico, a cup of coffee on a windowsill in the morning, early Renaissance fresco and tempera, serene luminous stillness, pale pastel colours, white loggia architecture, soft diffused light, gold halo-like glow around the cup, quiet devotion, no figures`
- 中文对照：弗拉·安杰利科风格，清晨窗台上的一杯咖啡，早期文艺复兴湿壁画与蛋彩，宁静发光，淡雅粉彩，白色拱廊，柔和漫射光，杯子周围淡淡的金色光晕，安静虔敬，无人物。
- Negative: 见第 (6) 节。
- 检验点：画面是否安静、发光，而不是戏剧化；色彩是否淡而亮；建筑线条是否清晰对称。
