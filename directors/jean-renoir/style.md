# Jean Renoir — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jean Renoir: poetic realism, deep-focus ensemble, the camera that wanders, everyone has their reasons, the country house and the river, humanist warmth`
- ZH: 雷诺阿风格：诗意现实主义，深焦群戏，漫游的摄影机，人人都有道理，乡村别墅与河流，人文主义温暖。

## (2) 镜头语言

- 漫游的摄影机：摄影机在别墅、战俘营、河流间自由移动，跟随人物而不打断；深焦群戏，前景、中景、背景同时有戏；长镜头保留生活的完整。`verbatim`

## (3) 场面调度

- 群戏调度：《游戏规则》别墅内各色人物分层，仆人与主人同框，狩猎与舞会并置；人物在画面内自由进出，调度如生活本身。`verbatim`

## (4) 剪辑节奏

- 流畅剪辑：长镜头内完成场景转换，剪辑点藏在人物移动处；节奏如河流，缓慢而绵密；《大幻影》战俘营段落靠剪辑在国籍与阶级间切换。`verbatim`

## (5) 色彩与光影

- 黑白与彩色并用：黑白期柔光拍战俘营与别墅，彩色期《河流》用 Technicolor 的印度阳光与河水，色彩作生命标示。`verbatim`

## (6) 该拍什么 / 不该拍什么

- 该拍：
- 别墅群戏与深焦分层
- 漫游的摄影机跟随生活
- 人人都有道理的对白
- 河流与乡村的生命意象
- 和解或离别的温暖结尾
- 不该拍：
- no fast cutting, no montage collision
- no single hero without the ensemble
- no cynical distance, no cold irony
- no handheld shakiness, no documentary roughness
- no melodramatic excess, no tearful climax
- Negative prompt: `No fast cutting, no montage collision, single hero without the ensemble, cynical distance, no cold irony, handheld shakiness, no documentary roughness, melodramatic excess, no tearful climax`

## (7) 叙事结构

- 人人都有道理：贵族与仆人、法国与德国、爱情与责任皆有道理；故事是群体的生活，结尾常以和解或离别收束，温暖而不滥情。`verbatim`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Jean Renoir, a small Yorkshire terrier sits on a subway seat while the camera wanders gently through the carriage, deep-focus ensemble — commuters, a guard, a child — everyone has their reasons, humanist warmth, the river of city life`
- 中文对照：雷诺阿风格：诗意现实主义，深焦群戏，漫游的摄影机，人人都有道理，乡村别墅与河流，人文主义温暖。一只约克夏犬坐在地铁座位上，按本导演的镜头、调度与剪辑拍成现代短片。
- Negative: `No fast cutting, no single hero without the ensemble, no cynical distance, no handheld shakiness, no melodramatic excess`
- 检验点：镜头语言是否成立；场面调度是否可辨；剪辑节奏是否符合本导演；Negative 清单是否被遵守。
