# F. W. Murnau — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of F. W. Murnau: German expressionism, flowing camera movement, subjective camera, chiaroscuro shadows, nature as fate, the liberated camera, romantic doom`
- ZH: 茂瑙风格：德国表现主义，流动的摄影机，主观镜头，明暗强烈的阴影，自然即命运，解放的摄影机，浪漫的宿命。

## (2) 镜头语言

- 解放的摄影机：摄影机可升降、穿越窗户、跟随人物穿越街道与沼泽；主观镜头让观众成为吸血鬼或醉汉的眼睛；《最后的笑容》几乎不用字幕卡，全靠镜头讲故事。`verbatim`

## (3) 场面调度

- 阴影调度：诺斯费拉图瘦长的影子爬上墙壁，人物在巨大布景阴影中渺小；室内戏用门框与楼梯分层，人物在纵深中走向命运。`verbatim`

## (4) 剪辑节奏

- 流畅剪辑：长镜头内完成场景转换，叠化连接梦境与现实；节奏缓慢而绵密，恐怖靠阴影的缓慢逼近而非快速剪辑。`verbatim`

## (5) 色彩与光影

- 黑白表现主义：硬光与深影对撞，雾气与月光作柔化；《诺斯费拉图》用淡色调区分白天与夜晚；《日出》用柔光拍乡村与城市的对照。`verbatim`

## (6) 该拍什么 / 不该拍什么

- 该拍：
- 瘦长阴影爬上墙壁
- 解放的摄影机穿越空间
- 雾、海、沼泽的自然宿命
- 主观镜头成为角色的眼睛
- 叠化连接梦境与现实
- 不该拍：
- no fast cutting, no montage collision
- no flat bright lighting, no cheerful palette
- no dialogue-driven exposition, no title-card storytelling
- no handheld shakiness, no documentary roughness
- no ironic distance, no comic relief
- Negative prompt: `No fast cutting, no montage collision, flat bright lighting, no cheerful palette, dialogue-driven exposition, no title-card storytelling, handheld shakiness, no documentary roughness, ironic distance, no comic relief`

## (7) 叙事结构

- 宿命爱情与诱惑：吸血鬼渡海、门房失势、农夫受诱惑又回归；故事是人与命运的拉锯，结尾常以牺牲或和解收束，自然（雾、海、沼泽）即命运本身。`verbatim`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of F. W. Murnau, a small Yorkshire terrier sits on a subway seat at night, its long shadow climbs the carriage wall, the camera floats slowly through the carriage as if through fog, chiaroscuro, subjective shots, romantic doom, no title cards needed`
- 中文对照：茂瑙风格：德国表现主义，流动的摄影机，主观镜头，明暗强烈的阴影，自然即命运，解放的摄影机，浪漫的宿命。一只约克夏犬坐在地铁座位上，按本导演的镜头、调度与剪辑拍成现代短片。
- Negative: `No fast cutting, no flat bright lighting, no dialogue-driven exposition, no handheld shakiness, no ironic distance`
- 检验点：镜头语言是否成立；场面调度是否可辨；剪辑节奏是否符合本导演；Negative 清单是否被遵守。
