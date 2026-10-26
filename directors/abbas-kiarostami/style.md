# Abbas Kiarostami — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Abbas Kiarostami: long takes on winding roads, real people playing themselves, the boundary between fiction and documentary dissolving, quiet questions with no answers`
- ZH: 基亚罗斯塔米风格：蜿蜒山路上的长镜头，真人演自己，虚构与纪录的边界消融，安静的提问，没有答案。

## (2) 镜头语言

- 景别：远景与全景为主，人物常是风景中的小点；车内对话多用固定中景。`verbatim`
- 机位：固定机位为主，摄影机常架在车内、路边，静观人物进出画面。`verbatim`
- 镜头：长焦压缩山路曲折，景深保留前后层次。`impression`
- 运镜禁忌：几乎不用推拉摇移与手持跟拍，摄影机不动，世界自己走。`impression`

## (3) 场面调度

- 人物走位：人物沿之字形山路行走、出画入画，行走本身就是叙事。`verbatim`
- 景深与层次：前景山坡、中景小路、背景远山的层次是标志性构图。`verbatim`
- 空间：乡村小路、汽车内部、山顶，空间开阔而人物渺小。`impression`
- 演员表演风格：大量用非职业演员与真人演自己，表演即生活本身。`artifact`

## (4) 剪辑节奏

- 剪辑速度：极慢，平均镜头很长，省略大胆（《樱桃的滋味》结尾直接切到拍摄现场）。`verbatim`
- 转场：硬切为主，场景之间留白，不解释时间如何过去。`impression`
- 段落结构：以重复与变奏推进（同一条路走三遍，每遍意思不同）。`impression`
- 声音剪辑：环境音（风声、车声）为主，对白稀少，音乐极少。`verbatim`

## (5) 色彩与光影

- 色彩：土黄、橄榄绿、赭石的乡村色谱，低饱和、自然光。`verbatim`
- 光影：自然光直射，强光下人物成剪影，阴影是山体的形状。`verbatim`
- 胶片 / 画幅：多为彩色，画幅克制，颗粒感来自实景拍摄。`impression`

## (6) 叙事结构

- 结构：环形与开放式：出发—寻找—未找到—再出发，结尾不收束。`impression`
- 视点：限知而克制，摄影机只知道人物知道的。`impression`
- 时间：顺时而缓慢，真实时间即影片时间。`impression`
- 类型处理：以纪录片方法拍虚构故事，虚构与纪录互相揭穿。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：蜿蜒山路、车内对话、真人演自己、重复的行走、开放式结尾、虚构与纪录的边界游戏
- 不该拍：戏剧化高潮、快速剪辑、煽情音乐、解释性对白、圆满收束
- Negative prompt: `No fast cutting, no dramatic climax, no sentimental music, no explanatory dialogue, no neat resolution, no studio gloss`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Abbas Kiarostami, a small Yorkshire terrier sitting on a subway seat, fixed camera, long take, the dog watches passengers come and go, natural light, no music, the camera does not explain why the dog is there`
- 中文对照：基亚罗斯塔米风格：一只约克夏犬坐在地铁座位上，固定机位，长镜头，犬看着乘客来来去去，自然光，没有音乐，镜头不解释犬为什么在那里。
- Negative: `No fast cutting, no dramatic close-ups, no sentimental music, no explanatory voiceover, no neat ending`
- 检验点：固定长镜头是否成立；虚构与纪录的边界感是否在；结尾是否开放而不收束。
