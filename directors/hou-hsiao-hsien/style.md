# Hou Hsiao-hsien — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hou Hsiao-hsien: distant static long takes, history seen from the edge of the frame, people entering and leaving, time passing without announcement`
- ZH: 侯孝贤风格：远景固定长镜头，历史从画框边缘看，人物出画入画，时间不声不响地过去。

## (2) 镜头语言

- 景别：远景与全景为主，人物常是室内或街景中的一部分。`verbatim`
- 机位：固定机位，机位高度多为坐姿平视，摄影机不动，等人物自己走。`verbatim`
- 镜头：标准焦段偏长，深焦保留前后多层动作。`impression`
- 运镜禁忌：几乎不用推拉摇移、手持与特写，运镜的缺席就是风格。`impression`

## (3) 场面调度

- 人物走位：人物从画框一侧进入、另一侧出去，摄影机不追。`verbatim`
- 景深与层次：前景、中景、背景同时有动作，深焦群戏是标志。`verbatim`
- 空间：室内（客厅、茶楼、妓院）与街景并重，空间即历史现场。`impression`
- 演员表演风格：职业与非职业演员并用，表演克制，生活化，不煽情。`impression`

## (4) 剪辑节奏

- 剪辑速度：极慢，平均镜头很长，场景之间用省略跳接。`impression`
- 转场：硬切与黑场，时间在黑场里过去，不解释。`impression`
- 段落结构：以生活段落并置推进，历史事件只在画外传来。`impression`
- 声音剪辑：环境音（蝉鸣、火车、麻将声）为主，音乐极少，对白常在画外。`verbatim`

## (5) 色彩与光影

- 色彩：低饱和暖调，室内灯光偏黄，室外是台湾的灰绿。`verbatim`
- 光影：自然光与室内 practical 光，阴影柔和，不做戏剧化布光。`impression`
- 胶片 / 画幅：彩色，画幅克制，颗粒感来自实景与长镜头。`impression`

## (6) 叙事结构

- 结构：线性而松散，生活段落并置，历史在边缘发生。`impression`
- 视点：全知而克制，镜头站在历史的边缘，不站在中心。`impression`
- 时间：顺时而缓慢，时间在省略与黑场里流逝。`impression`
- 类型处理：以家庭剧写历史，历史事件只作背景音。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：远景固定长镜头、人物出画入画、深焦群戏、画外传来的历史、黑场省略、低饱和暖调
- 不该拍：大幅度运镜、快速剪辑、特写煽情、解释性对白、戏剧化高潮、历史正剧的正面叙述
- Negative prompt: `No camera movement, no fast cutting, no dramatic close-ups, no sentimental music, no explanatory voiceover, no frontal historical epic`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Hou Hsiao-hsien, a small Yorkshire terrier sitting on a subway seat, distant static long take, the camera does not move, passengers enter and leave the frame, the dog stays, ambient train sounds, no music, time passes without announcement`
- 中文对照：侯孝贤风格：一只约克夏犬坐在地铁座位上，远景固定长镜头，摄影机不动，乘客出画入画，犬一直坐在那里，环境音是列车声，没有音乐，时间不声不响地过去。
- Negative: `No camera movement, no fast cutting, no dramatic close-ups, no sentimental music, no explanatory voiceover`
- 检验点：固定长镜头是否成立；人物出画入画是否自然；时间感是否来自省略而非剪辑。
