# Elia Kazan — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Elia Kazan: method acting intensity, social realism, the outsider against the system, sweaty close-ups, location streets, moral confrontation`
- ZH: 卡赞风格：方法派表演强度，社会现实主义，局外人对抗体制，汗水特写，实景街道，道德对峙。

## (2) 镜头语言

- 表演特写：方法派演员的面部是核心，机位贴近，汗水与颤抖入画；实景街道与码头拍社会，机位如纪录片般贴近生活；运镜服务于表演。`verbatim`

## (3) 场面调度

- 街道调度：码头、街车、电车轨道，人物在实景中对峙；《欲望号街车》狭小公寓内三人拉锯，空间越小，冲突越大；群戏按阶级分层。`verbatim`

## (4) 剪辑节奏

- 表演剪辑：剪辑点在台词的爆发处，长镜头保留表演的完整；《码头风云》码头演讲段落剪辑克制，情感靠表演而非剪辑；节奏由演员的呼吸决定。`verbatim`

## (5) 色彩与光影

- 黑白为主，汗水与硬光——街车的闷热、码头的灰调；彩色期《伊甸园之东》用 Technicolor 的加州金黄与绿野，色彩作青春与欲望标示。`verbatim`

## (6) 该拍什么 / 不该拍什么

- 该拍：
- 方法派的汗水特写
- 码头与街车的实景对峙
- 狭小公寓的三人拉锯
- 道德告白的演讲段落
- 局外人的和解结尾
- 不该拍：
- no polished studio artificiality, no fake backdrops
- no detached irony, no cool distance
- no fast MTV cutting, no chaotic montage
- no handheld shakiness for its own sake
- no sentimental melodrama without social grounding
- Negative prompt: `No polished studio artificiality, no fake backdrops, detached irony, no cool distance, fast MTV cutting, no chaotic montage, handheld shakiness for its own sake, sentimental melodrama without social grounding`

## (7) 叙事结构

- 局外人对抗体制：码头工人告密、街车上的布兰奇、伊甸园的卡尔；故事是道德的对峙，结尾常以告白或和解收束，社会即舞台。`verbatim`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Elia Kazan, a small Yorkshire terrier sits on a subway seat while a method actor in the next row sweats through a moral confrontation about who it belongs to, location streets, sweaty close-ups, social realism, the outsider against the system`
- 中文对照：卡赞风格：方法派表演强度，社会现实主义，局外人对抗体制，汗水特写，实景街道，道德对峙。一只约克夏犬坐在地铁座位上，按本导演的镜头、调度与剪辑拍成现代短片。
- Negative: `No polished studio artificiality, no detached irony, no fast MTV cutting, no handheld shakiness for its own sake, no sentimental melodrama without social grounding`
- 检验点：镜头语言是否成立；场面调度是否可辨；剪辑节奏是否符合本导演；Negative 清单是否被遵守。
