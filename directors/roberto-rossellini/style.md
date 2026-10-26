# Roberto Rossellini — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Roberto Rossellini: neorealist immediacy, non-actors in real streets, documentary camera inside fiction, moral witness without judgement, raw light`
- ZH: 罗塞里尼风格：新现实主义的即时性，真实街头的非职业演员，纪录片镜头进入虚构，道德见证而不审判，粗粝的光。

## (2) 镜头语言

- 景别：全景与中景为主，记录街头与废墟的空间；少用特写抒情。`verbatim`
- 机位：手持与实景跟拍并存，机位常随人物行走；拒绝影棚式精致运镜。`impression`
- 镜头：标准焦距，深焦呈现街道层次。`impression`

## (3) 场面调度

- 场面调度：实景拍摄，人物在真实街道、废墟中自然走位，群众场面不排练痕迹。`verbatim`
- 演员：非职业演员与职业演员混用，表演去戏剧化。`artifact`
- 空间：战后罗马与柏林的废墟本身就是布景，空间即历史。`impression`

## (4) 剪辑节奏

- 剪辑：段落式结构，六个片段（《战火》）之间硬切，节奏如新闻片。`verbatim`
- 转场：硬切为主，省略不作交代，时间跳跃靠片段并置。`impression`
- 声音：现场收音，环境音与方言保留，不配煽情音乐。`artifact`

## (5) 色彩与光影

- 色彩：黑白为主，粗颗粒、高反差；废墟的灰与人脸的亮构成主调。`impression`
- 光影：自然光与实景光，明暗不修饰，阴影即废墟的一部分。`impression`
- 画幅：1.37:1，纪录片式画幅。`impression`

## (6) 叙事结构

- 结构：片段并置（《战火》六段）、开放式结尾，拒绝闭合。`verbatim`
- 视点：见证者视角，多人物轮换，不设全知叙述者。`impression`
- 时间：当下即时性，历史正在发生而非被回忆。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：战后废墟与街头、非职业演员的日常、儿童视角、片段并置的战争叙事。
- 该拍：实景中的群众场面、方言对白、道德困境而不审判。
- 不该拍：不拍影棚布景、不拍明星式特写、不拍煽情配乐、不拍闭合式大团圆。
- Negative prompt: `No studio sets, no star close-ups, no sentimental score, no closed happy ending, no polished crane shots, no explanatory voiceover`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Roberto Rossellini, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat among real commuters, non-actors, documentary camera, raw natural light, post-war street immediacy, moral witness without judgement`
- 中文对照：罗塞里尼风格：一只约克夏犬坐在地铁座位上，周围是真实乘客，非职业演员，纪录片镜头，粗粝自然光，战后街头的即时性，道德见证而不审判。
- Negative: `No studio polish, no star close-ups, no sentimental music, no closed ending`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
