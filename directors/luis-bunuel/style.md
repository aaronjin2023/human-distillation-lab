# Luis Buñuel — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Luis Buñuel: bourgeois ritual interrupted by dream logic, deadpan absurdity, fetish objects, anticlerical irony, calm camera, violent cut`
- ZH: 布努埃尔风格：资产阶级仪式被梦的逻辑打断，面无表情的荒诞，恋物细节，反教权反讽，冷静镜头，暴力剪切。

## (2) 镜头语言

- 景别：中景与全景为主，少用特写煽情；机位多为平视固定，拒绝炫技运镜。`verbatim`
- 镜头：标准焦距，景深适中；画面冷静克制，荒诞全靠内容而非镜头。`impression`
- 禁忌：不用手持晃动、不用快速推拉制造紧张。`impression`

## (3) 场面调度

- 场面调度：餐桌、客厅、教堂等封闭中产空间，人物按仪式走位，动作突然越轨。`verbatim`
- 演员：职业演员，表演克制、近乎木然，荒诞感来自情境而非表情。`impression`
- 空间：门、走廊、餐桌是反复出现的牢笼，人物进得去出不来。`impression`

## (4) 剪辑节奏

- 剪辑：硬切为主，梦境与现实之间不加过渡标记，跳接制造逻辑断裂。`verbatim`
- 节奏：整体平缓，荒诞瞬间以剪切的突然性呈现，而非加速。`impression`
- 转场：直线硬切，少用叠化；时间省略不作交代。`impression`

## (5) 色彩与光影

- 色彩：早期黑白冷峻；晚期彩色偏暖但克制，资产阶级室内多用暗红、深棕与米色。`impression`
- 光影：均匀的室内光，少用戏剧性明暗；阴影不渲染心理。`impression`
- 画幅：1.37:1 黑白时期为主，晚期宽银幕仍保持室内构图。`impression`

## (6) 叙事结构

- 结构：环形与重复结构（《资产阶级的审慎魅力》屡次赴宴屡次失败）；开头常为日常仪式，结尾悬置。`verbatim`
- 视点：全知而冷漠，不站队、不解释，梦与现实并置不加区分。`impression`
- 时间：线性表皮下藏着梦的折叠与重复；闪回常为假闪回。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：资产阶级晚宴与仪式、梦境插入、昆虫与动物特写、宗教器物、被困的房间、重复赴宴。
- 该拍：恋物细节（脚、鞋、箱子）、突如其来的暴力与荒诞转折。
- 不该拍：不拍心理分析式特写、不拍煽情音乐铺垫、不拍明确的道德审判、不拍梦与现实的分界标记。
- Negative prompt: `No psychological close-ups, no sentimental score, no moral judgement, no dream-reality markers, no handheld shaky cam, no explanatory voiceover`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Luis Buñuel, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier sits perfectly still while commuters repeat the same polite ritual around it, a dinner party that never begins, dream logic, deadpan absurdity, calm static camera, bourgeois interior`
- 中文对照：布努埃尔风格：一只约克夏犬坐在地铁座位上，乘客们围绕它重复着同一套礼貌仪式，一场永远开始不了的晚宴，梦的逻辑，面无表情的荒诞，冷静固定镜头，资产阶级室内。
- Negative: `No polite realism, no warm sentimentality, no psychological close-ups, no clear dream markers`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
