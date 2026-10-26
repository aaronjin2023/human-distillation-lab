# George Cukor — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of George Cukor: women's pictures, sparkling dialogue, elegant interiors, the actress as the centre, wit and warmth in a drawing room`
- ZH: 库克风格：女性电影，闪耀对白，优雅室内，女演员为中心，客厅里的机智与温暖。

## (2) 镜头语言

- 室内中景：优雅客厅、书房、舞厅，机位平稳，景别克制；特写只给女演员的眼神与微笑；运镜如社交礼仪般得体，不抢戏。`verbatim`

## (3) 场面调度

- 客厅调度：人物在沙发、地毯、楼梯间交换台词与眼神；女性在画面中央，男性作反应与陪衬；空间即社交场，门一开一合即关系转折。`verbatim`

## (4) 剪辑节奏

- 对白剪辑：台词如乒乓，剪辑点在妙语之后；《费城故事》三人对话快速对切，节奏轻快；情感段落放慢，长镜头保留女演员的表演。`verbatim`

## (5) 色彩与光影

- 黑白与彩色并用：黑白期柔光拍女性面孔，彩色期《窈窕淑女》用 Technicolor 的舞会金红，色彩作优雅标示。`verbatim`

## (6) 该拍什么 / 不该拍什么

- 该拍：
- 优雅客厅的三人对话
- 女演员的眼神特写
- 卖花女的蜕变段落
- 舞会与书房的社交场
- 女性的自主选择结尾
- 不该拍：
- no crude slapstick, no vulgar gags
- no male-centred heroics, no sidelining women
- no fast MTV cutting, no chaotic montage
- no handheld camera, no documentary roughness
- no sentimental melodrama, no tearful excess
- Negative prompt: `No crude slapstick, no vulgar gags, male-centred heroics, no sidelining women, fast MTV cutting, no chaotic montage, handheld camera, no documentary roughness, sentimental melodrama, no tearful excess`

## (7) 叙事结构

- 女性觉醒与爱情：被煤气灯操纵的妻子、费城名媛的再选择、卖花女的蜕变；故事是女性在社交场上的机智周旋，结尾常以女性的自主选择收束。`verbatim`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of George Cukor, a small Yorkshire terrier sits on a subway seat while an elegant woman in the next row trades sparkling dialogue with two suitors over it, drawing-room wit, the actress as the centre, warmth and wit, her own choice at the end`
- 中文对照：库克风格：女性电影，闪耀对白，优雅室内，女演员为中心，客厅里的机智与温暖。一只约克夏犬坐在地铁座位上，按本导演的镜头、调度与剪辑拍成现代短片。
- Negative: `No crude slapstick, no male-centred heroics, no fast MTV cutting, no handheld camera, no sentimental melodrama`
- 检验点：镜头语言是否成立；场面调度是否可辨；剪辑节奏是否符合本导演；Negative 清单是否被遵守。
