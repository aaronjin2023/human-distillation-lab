# Alfred Hitchcock — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alfred Hitchcock: suspense as control, the camera as the audience's eye, voyeurism, the MacGuffin, precise storyboards, vertigo and the shower scene, guilt in a close-up`
- ZH: 希区柯克风格：悬念即控制，摄影机即观众的眼睛，窥视，麦格芬，精确分镜，眩晕与淋浴戏，特写中的罪恶感。

## (2) 镜头语言

- 主观镜头与精确分镜：每一镜头事先画好，机位即观众的眼睛；《后窗》全片以杰夫的窗口视角拍对面公寓；《迷魂记》用变焦推拉制造眩晕；特写只给罪恶感。`verbatim`

## (3) 场面调度

- 窥视调度：人物在窗口、楼梯、浴室被窥视，空间越收越紧；《精神病患者》汽车旅馆的房间即陷阱；人物走位按悬念设计，每一步都是伏笔。`verbatim`

## (4) 剪辑节奏

- 精确剪辑：淋浴戏 70 余个镜头快速拼接，节奏由悬念决定；《后窗》靠剪辑在杰夫与对面公寓间切换视线；剪辑即控制，观众的焦虑随剪辑加速。`verbatim`

## (5) 色彩与光影

- 黑白与彩色并用：黑白期硬光深影，彩色期《迷魂记》用绿与红标示迷恋与死亡；《后窗》的暖黄公寓与冷蓝夜色对照；色彩作心理标示。`verbatim`

## (6) 该拍什么 / 不该拍什么

- 该拍：
- 窗口窥视与主观镜头
- 淋浴戏的快速精确剪辑
- 变焦推拉的眩晕感
- 麦格芬引出的阴谋
- 特写中的罪恶感
- 不该拍：
- no loose improvisation, no unplanned coverage
- no flat lighting, no documentary realism
- no explicit gore without suspense, no shock without control
- no handheld shakiness, no chaotic cutting
- no warm sentimentality, no unresolved cosiness
- Negative prompt: `No loose improvisation, no unplanned coverage, flat lighting, no documentary realism, explicit gore without suspense, no shock without control, handheld shakiness, no chaotic cutting, warm sentimentality, no unresolved cosiness`

## (7) 叙事结构

- 无辜者卷入阴谋：被误认的间谍、窥视邻居的摄影师、迷恋死者的侦探；故事是悬念的精密机器，麦格芬只是引子，结尾常以真相揭露或坠落收束。`verbatim`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Alfred Hitchcock, a small Yorkshire terrier sits on a subway seat while a passenger watches it from across the carriage, subjective point-of-view shots, precise suspenseful cutting, deep shadows, the dog as a MacGuffin, tension without explanation`
- 中文对照：希区柯克风格：悬念即控制，摄影机即观众的眼睛，窥视，麦格芬，精确分镜，眩晕与淋浴戏，特写中的罪恶感。一只约克夏犬坐在地铁座位上，按本导演的镜头、调度与剪辑拍成现代短片。
- Negative: `No loose improvisation, no flat lighting, no explicit gore without suspense, no handheld shakiness, no warm sentimentality`
- 检验点：镜头语言是否成立；场面调度是否可辨；剪辑节奏是否符合本导演；Negative 清单是否被遵守。
