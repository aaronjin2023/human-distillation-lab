# Francis Ford Coppola — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Francis Ford Coppola: operatic family saga, chiaroscuro shadow, slow dissolves, power passed down in darkness`
- ZH: 科波拉风格：歌剧般的家族史诗，明暗对照的阴影，缓慢叠化，权力在黑暗中代代相传。

## (2) 镜头语言

- 景别：中景与近景为主，特写给面部阴影；《教父》以暗部与侧光塑造权力面孔。`verbatim`
- 机位与运动：缓慢推近与横移，摄影机如歌剧观众席般庄重；少用手持，运动服务于仪式感。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 家族仪式场面：婚礼、洗礼、会议——群戏深焦调度，权力人物居中，家人在四周环绕。`impression`

## (4) 剪辑节奏

- 缓慢叠化与平行剪辑：家族仪式与暴力行动交叉，时间跨度大，段落以音乐收束。`impression`

## (5) 色彩与光影

- 色彩：暖金与深黑主导：烛光、钨丝灯的暖调对照深重的阴影；《现代启示录》以丛林绿与火光橙对撞。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：史诗三段式：家族崛起、权力顶峰、堕落与孤独；开头常以仪式切入，结尾以孤独的背影或关门收束。`impression`
- 该拍什么：
- 烛光阴影中的家族仪式群戏
- 权力人物居中的深焦调度
- 仪式与暴力交叉的平行剪辑
- 暖金与深黑的明暗对照
- 不该拍什么：
- 手持晃动的即兴感
- 明亮扁平的喜剧光
- 快速跳切
- 轻佻的讽刺语调

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 烛光阴影中的家族仪式群戏；- 权力人物居中的深焦调度；- 仪式与暴力交叉的平行剪辑；- 暖金与深黑的明暗对照
- 不该拍：- 手持晃动的即兴感；- 明亮扁平的喜剧光；- 快速跳切；- 轻佻的讽刺语调
- Negative prompt: `No handheld improvisation, no bright flat comedy lighting, no fast cutting, no flippant ironic tone, no explanatory voiceover`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Francis Ford Coppola, a small Yorkshire terrier sitting on a subway seat, chiaroscuro light, the dog lit like a godfather in shadow, slow dissolve to a family ritual in the next carriage, warm gold against deep black, operatic stillness`
- 中文对照：科波拉风格：一只约克夏犬坐在地铁座位上，明暗对照的光，狗如教父般坐在阴影中，缓慢叠化到下一节车厢的家族仪式，暖金对深黑，歌剧般的静默。
- Negative: `No handheld camera, no bright flat lighting, no fast cutting`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
