# Billy Wilder — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Billy Wilder: noir cynicism and comedy in one hand, sharp dialogue, the corrupt city, the has-been and the hustler, a perfect last line`
- ZH: 怀尔德风格：黑色电影的 cynicism 与喜剧集于一身，锋利对白，腐败的都市，过气者与骗子，一句完美的结尾台词。

## (2) 镜头语言

- 冷静中景：人物在都市室内对峙，机位平稳，景别克制；《日落大道》用泳池倒影与特写拍过气明星的幻觉；运镜服务于对白，不抢戏。`verbatim`

## (3) 场面调度

- 室内对峙调度：保险推销员与蛇蝎女人在客厅谈判，编剧与过气明星在豪宅拉锯；人物在封闭空间内交换台词，空间越小，张力越大。`verbatim`

## (4) 剪辑节奏

- 对白剪辑：台词如乒乓，剪辑点在妙语之后；闪回结构（《双重赔偿》《日落大道》皆以倒叙开场）靠剪辑制造宿命感；喜剧段落剪辑轻快，黑色段落剪辑冷峻。`verbatim`

## (5) 色彩与光影

- 黑白黑色电影的硬光深影，百叶窗阴影是标志；《热情如火》用黑白拍性别喜剧，色彩缺席反成风格；晚期彩色片仍以冷调为主。`verbatim`

## (6) 该拍什么 / 不该拍什么

- 该拍：
- 百叶窗阴影下的谈判
- 倒叙开场的宿命结构
- 锋利如乒乓的对白
- 过气明星的豪宅幻觉
- 一句完美的结尾台词
- 不该拍：
- no warm sentimentality, no earnest uplift
- no loose improvisation, no rambling dialogue
- no handheld camera, no documentary roughness
- no fast MTV cutting, no chaotic montage
- no happy ending without a sting
- Negative prompt: `No warm sentimentality, no earnest uplift, loose improvisation, no rambling dialogue, handheld camera, no documentary roughness, fast MTV cutting, no chaotic montage, happy ending without a sting`

## (7) 叙事结构

- 骗子与过气者：保险骗局、过气明星、男扮女装的乐手；故事是欲望与欺骗的连锁，结尾常以一句完美台词收束——“没有人是完美的”。`verbatim`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Billy Wilder, a small Yorkshire terrier sits on a subway seat while two hustlers in the next row trade razor-sharp dialogue over who owns it, venetian-blind shadows, flashback structure, a perfect last line, nobody's perfect`
- 中文对照：怀尔德风格：黑色电影的 cynicism 与喜剧集于一身，锋利对白，腐败的都市，过气者与骗子，一句完美的结尾台词。一只约克夏犬坐在地铁座位上，按本导演的镜头、调度与剪辑拍成现代短片。
- Negative: `No warm sentimentality, no loose improvisation, no handheld camera, no fast MTV cutting, no happy ending without a sting`
- 检验点：镜头语言是否成立；场面调度是否可辨；剪辑节奏是否符合本导演；Negative 清单是否被遵守。
