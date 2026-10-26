# Michelangelo Buonarroti — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Michelangelo Buonarroti, painting only, High Renaissance fresco, sculptural muscular bodies in torsion, monumental scale, vivid clear colours, dramatic foreshortening, ignudi and prophets, no sculpture`
- ZH: 米开朗基罗风格，只蒸绘画，盛期文艺复兴湿壁画，肌肉如雕塑、身体扭曲伸展，宏大规模，色彩鲜明，戏剧性透视缩短，裸体青年与先知。

## (2) 色板方向

- 主色（7 色，颜料名）：群青、朱红、赭石、土黄、淡粉肤色、墨绿、铅白。`verbatim`
- 辅色：紫灰（阴影）、金黄（衣袍）。
- 禁色：纤细柔弱的人体；小幅精致构图；灰暗土色大面积平涂；温柔的田园风景。
- 冷暖：暖肤色与朱红为主，群青与墨绿作冷对比；修复后色彩比旧时所见更鲜明、更冷。`artifact`（1980–1990 年修复争议，见 conflicts.md）
- 明暗 / 饱和：高对比，肌肉明暗分明；亮部亮、暗部沉，但色彩始终清晰不浑。

## (3) 笔触与线条

- 笔触：湿壁画笔触有力、肯定，肌肉用宽阔明暗带塑形，轮廓线如雕刻般果断。`verbatim`
- 线条：轮廓线粗重、起伏，身体的扭转靠轮廓线的张力表达；常直接在湿灰泥上以硬物刻线起稿，少用全尺寸底稿。`artifact`
- 质感：灰泥哑光；修复后色彩鲜明，肌肉的体积感如大理石。

## (4) 构图习惯

- 画幅：天顶画为超大横幅组画（西斯廷天顶约 40×13 米，300 余个人物）；《最后的审判》为整面墙。`artifact`
- 视点：仰视——天顶画为仰视构图，人物按仰视透视缩短，观者在地面向上看。
- 布局：九幅创世场景居中，先知与女先知分列两侧，裸体青年（ignudi）居四角；《创造亚当》中上帝与亚当的手指在画面中心几近相触。`verbatim`
- 裁切：人物常被建筑框截断，巨幅构图无“边”，视线在天顶上环绕。

## (5) 光影与透视

- 光源：均匀而强烈的光，无单一戏剧光源；体积靠肌肉本身的明暗，不靠环境光影。
- 阴影：肌肉阴影深而暖，亮面高而亮，明暗交界果断。
- 透视：仰视透视缩短（foreshortening）——身体在透视中扭曲、拉长，是画面动感的来源；建筑为手绘的假建筑框，制造深远空间。`artifact`

## (6) 该画什么 / 不该画什么

- 该画：创世与末日审判群像；肌肉发达的裸体与先知；手指相触的瞬间；假建筑框。
- 不该画：纤细柔弱的人体；小幅静物；温柔的田园风景；雕塑与建筑本身（不在蒸馏范围）。
- Negative prompt: `slender delicate figures, small-scale pretty composition, dull muddy palette, sculpture or architecture as subject, smooth academic blending, photorealistic faces`

## (7) 测试提示词示例（现代题材：城市健身房里举重的人）

- Prompt: `In the style of Michelangelo Buonarroti, painting only, a person lifting weights in a modern city gym, High Renaissance fresco, sculptural muscular body in torsion, monumental scale, vivid clear colours, dramatic foreshortening, seen from below, powerful anatomy`
- 中文对照：米开朗基罗风格，只画绘画，现代城市健身房里一个举重的人，盛期文艺复兴湿壁画，肌肉如雕塑、身体扭曲伸展，宏大规模，色彩鲜明，戏剧性透视缩短，仰视构图，强健的解剖。
- Negative: 见第 (6) 节。
- 检验点：人体是否如雕塑般有力、扭曲，而不是普通的健身照片；构图是否宏大、有仰视感；色彩是否鲜明清晰。
