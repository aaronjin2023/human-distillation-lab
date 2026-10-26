# Ang Lee — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ang Lee: quiet restraint holding back strong feeling, family ritual as drama, the camera patient with people who cannot speak`
- ZH: 李安风格：克制的镜头兜住强烈的情感，家庭仪式即戏剧，摄影机耐心地对着说不出话的人。

## (2) 镜头语言

- 景别：中景与全景为主，家庭场景多用全景保留仪式感。`verbatim`
- 机位：固定机位与缓慢推近，摄影机耐心而不催促。`impression`
- 镜头：标准焦段，景深保留家庭空间的多层关系。`impression`
- 运镜禁忌：几乎不用手持晃动与快速剪辑，运镜服务于克制。`impression`

## (3) 场面调度

- 人物走位：人物在餐桌、客厅、山野之间克制地移动，礼仪即走位。`verbatim`
- 景深与层次：前景餐具、中景人物、背景门窗的三层家庭结构是标志。`impression`
- 空间：家庭室内与开阔山野并置，空间越开阔，人物越孤独。`impression`
- 演员表演风格：职业演员，表演内敛，情绪靠停顿与眼神。`impression`

## (4) 剪辑节奏

- 剪辑速度：中慢速，长镜头保留家庭仪式的完整时间。`impression`
- 转场：叠化与淡入淡出为主，情绪段落用叠化衔接。`impression`
- 段落结构：以家庭仪式（吃饭、婚礼、葬礼）作章节推进。`impression`
- 声音剪辑：环境音与音乐克制，对白稀少，沉默是语言。`impression`

## (5) 色彩与光影

- 色彩：家庭片暖调，山野片青绿与土黄，低饱和、自然。`verbatim`
- 光影：自然光与室内暖光，阴影柔和，不做戏剧化布光。`impression`
- 胶片 / 画幅：彩色，画幅随类型而变（《卧虎藏龙》宽银幕山野）。`impression`

## (6) 叙事结构

- 结构：线性为主，家庭三部曲式推进，结尾克制而开放。`impression`
- 视点：全知而悲悯，镜头站在理解的一边。`impression`
- 时间：顺时，时间在家庭仪式里流逝。`impression`
- 类型处理：跨类型（家庭剧、武侠、西部、科幻），类型成规被克制的人物观察柔化。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：家庭仪式、克制的长镜头、说不出话的人物、餐桌与山野、沉默与停顿、跨文化的两难
- 不该拍：煽情音乐、快速剪辑、戏剧化高潮、解释性对白、直白的情感宣泄
- Negative prompt: `No sentimental music, no fast cutting, no melodramatic climax, no explanatory dialogue, no loud emotional outburst, no handheld shaky cam`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Ang Lee, a small Yorkshire terrier sitting on a subway seat, patient static camera, the dog watches a family saying goodbye in silence, warm interior light, long take, feeling held back, no music`
- 中文对照：李安风格：一只约克夏犬坐在地铁座位上，耐心的固定机位，犬看着一个家庭沉默地告别，室内暖光，长镜头，情感被克制地兜住，没有音乐。
- Negative: `No sentimental music, no fast cutting, no melodramatic climax, no explanatory voiceover, no loud outburst`
- 检验点：克制是否成立；情感是否靠停顿而非台词；家庭仪式感是否在。
