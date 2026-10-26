# D. W. Griffith — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of D. W. Griffith: classical narrative cinema, cross-cutting parallel action, close-ups for moral emotion, iris and mask effects, last-minute rescue, sweeping historical epic`
- ZH: 格里菲斯风格：古典叙事电影，平行交叉剪辑，特写承载道德情感，光圈与遮片效果，最后一分钟营救，宏大的历史史诗。

## (2) 镜头语言

- 景别系统化：全景交代史诗场面，特写推进情感与道德判断；机位多为固定，偶用移动跟拍骑马与追逐；光圈（iris）开合引导视线。`verbatim`

## (3) 场面调度

- 宏大场面调度：千人战争场面与室内亲密戏并置；人物按道德阵营分层站位，善恶在画面位置上即分明；最后一分钟营救靠多线人物的空间调度完成。`verbatim`

## (4) 剪辑节奏

- 交叉剪辑（cross-cutting）为核心：平行线索交替推进，节奏越到高潮越快；最后一分钟营救是其标志性结构；淡入淡出与光圈转场连接段落。`verbatim`

## (5) 色彩与光影

- 黑白片加淡色调（tinting）：夜景蓝调、战争场面琥珀色、爱情段落玫瑰色；色彩作时间与情绪标示；史诗场面重明暗对比。`verbatim`

## (6) 该拍什么 / 不该拍什么

- 该拍：
- 最后一分钟营救与平行交叉剪辑
- 史诗战争场面与千人调度
- 特写中的道德情感（丽莲·吉许式表演）
- 四线并行的主题史诗
- 光圈开合与淡色调的情绪标示
- 不该拍：
- no single-take long shots, no static theatrical staging
- no moral ambiguity, no unresolved irony
- no handheld immediacy, no documentary roughness
- no fast MTV cutting, no jump cuts
- no muted naturalism, no desaturated palette
- Negative prompt: `No single-take long shots, no static theatrical staging, moral ambiguity, no unresolved irony, handheld immediacy, no documentary roughness, fast MTV cutting, no jump cuts, muted naturalism, no desaturated palette`

## (7) 叙事结构

- 四段式史诗与道德剧：历史大事件为背景，个人命运为前景；《党同伐异》四线并行，主题皆为“不宽容”；结尾常以道德和解或悲剧收束。`verbatim`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of D. W. Griffith, a small Yorkshire terrier sits on a subway seat while three parallel stories unfold — a child loses it, a guard searches for it, a passenger protects it — cross-cutting quickens toward a last-minute reunion, iris close-up on the dog's face, amber tint`
- 中文对照：格里菲斯风格：古典叙事电影，平行交叉剪辑，特写承载道德情感，光圈与遮片效果，最后一分钟营救，宏大的历史史诗。一只约克夏犬坐在地铁座位上，按本导演的镜头、调度与剪辑拍成现代短片。
- Negative: `No single-take long shots, no handheld camera, no moral ambiguity, no jump cuts, no muted naturalism`
- 检验点：镜头语言是否成立；场面调度是否可辨；剪辑节奏是否符合本导演；Negative 清单是否被遵守。
