# Charlie Chaplin — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charlie Chaplin: silent slapstick with pathos, the Little Tramp, fixed medium shots, balletic physical gags, pantomime timing, sentiment without sentimentality, social satire in a bowler hat`
- ZH: 卓别林风格：默片滑稽戏加悲情，小流浪汉，固定中景，芭蕾式肢体笑料，哑剧节奏，煽情而不滥情，礼帽下的社会讽刺。

## (2) 镜头语言

- 固定中景与全景为主，机位如舞台观众席，极少移动；特写只留给流浪汉的眼神与盲女的脸；长镜头保留肢体笑料的完整节奏。`verbatim`

## (3) 场面调度

- 哑剧式调度：流浪汉在画面中央完成一连串肢体动作——拐杖、手套、面包、皮鞋；配角作反应与阻碍；空间是街道、工厂、舞厅等社会舞台。`verbatim`

## (4) 剪辑节奏

- 按笑料段落剪辑：一个笑料拍完整再切下一个，节奏由肢体动作的停顿与加速决定；《摩登时代》流水线段落靠重复剪辑制造荒诞；有声片后对白只作点缀。`verbatim`

## (5) 色彩与光影

- 黑白为主，流浪汉黑礼帽、黑外套、破鞋与白手套构成黑白对比；《大独裁者》仍坚持黑白，以光影区隔独裁者与理发师；色彩缺席本身就是风格。`verbatim`

## (6) 该拍什么 / 不该拍什么

- 该拍：
- 小流浪汉的拐杖、手套与八字步
- 流水线、面包与皮鞋的肢体笑料
- 盲女与流浪汉的温情段落
- 独裁者演讲的讽刺模仿
- 独自走向远方的背影结尾
- 不该拍：
- no fast cutting inside a gag, no fragmented slapstick
- no dialogue-driven comedy, no verbal wit as the main joke
- no handheld camera, no shaky realism
- no cynical cruelty, no mean-spirited mockery
- no saturated colour, no glossy finish
- Negative prompt: `No fast cutting inside a gag, no fragmented slapstick, dialogue-driven comedy, no verbal wit as the main joke, handheld camera, no shaky realism, cynical cruelty, no mean-spirited mockery, saturated colour, no glossy finish`

## (7) 叙事结构

- 小人物对抗大机器：流浪汉爱上盲女、被流水线吞没、误当独裁者；故事是连串笑料加一段真情，结尾常是流浪汉独自走入远方，背影收束。`verbatim`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Charlie Chaplin, a small Yorkshire terrier in a tiny bowler hat sits on a subway seat, politely offering its seat to an old lady, then tripping over its own leash in a balletic gag, fixed medium shot, black-and-white, pathos and slapstick in one take`
- 中文对照：卓别林风格：默片滑稽戏加悲情，小流浪汉，固定中景，芭蕾式肢体笑料，哑剧节奏，煽情而不滥情，礼帽下的社会讽刺。一只约克夏犬坐在地铁座位上，按本导演的镜头、调度与剪辑拍成现代短片。
- Negative: `No fast cutting inside a gag, no dialogue-driven comedy, no handheld camera, no cynical cruelty, no saturated colour`
- 检验点：镜头语言是否成立；场面调度是否可辨；剪辑节奏是否符合本导演；Negative 清单是否被遵守。
