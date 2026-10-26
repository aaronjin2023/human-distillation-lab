# Michael Curtiz — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Michael Curtiz: Hollywood craftsmanship, fluid camera movement, fog and shadows, romance under pressure, the studio system at its best`
- ZH: 柯蒂斯风格：好莱坞工匠精神，流畅的摄影机运动，雾与阴影，压力下的浪漫，制片厂制度的巅峰。

## (2) 镜头语言

- 流畅运镜：摄影机跟随人物穿越酒吧、街道、甲板，推拉摇移自然；《卡萨布兰卡》里克酒吧的机位如行云流水；雾与阴影作空间分隔。`verbatim`

## (3) 场面调度

- 酒吧与甲板调度：里克酒吧内各色人物分层，钢琴、吧台、门口各有戏；海战与剑斗场面调度开阔，人物在运动中完成浪漫。`verbatim`

## (4) 剪辑节奏

- 流畅剪辑：场景间用推拉与叠化连接，节奏均匀；《卡萨布兰卡》闪回段落剪辑克制，情感靠表演而非剪辑；动作段落剪辑干净。`verbatim`

## (5) 色彩与光影

- 黑白为主，雾、阴影与柔光——里克酒吧的烟雾、卡萨布兰卡的夜色；彩色期《罗宾汉历险记》用 Technicolor 的绿林与金甲，色彩作冒险标示。`verbatim`

## (6) 该拍什么 / 不该拍什么

- 该拍：
- 里克酒吧的雾与阴影
- 流畅穿越酒吧与甲板的运镜
- 压力下的浪漫重逢
- 海战与剑斗的冒险场面
- 雾中的告别结尾
- 不该拍：
- no static theatrical staging, no stiff camera
- no slow contemplative pacing, no long-take stillness
- no psychological exposition, no inner monologue
- no handheld shakiness, no documentary roughness
- no ironic distance, no cynical twist
- Negative prompt: `No static theatrical staging, no stiff camera, slow contemplative pacing, no long-take stillness, psychological exposition, no inner monologue, handheld shakiness, no documentary roughness, ironic distance, no cynical twist`

## (7) 叙事结构

- 压力下的浪漫：里克与伊尔莎在战争阴影下重逢，海鹰与罗宾汉在冒险中获胜；故事是浪漫与责任的拉锯，结尾常以告别或胜利收束，雾中开始，雾中结束。`verbatim`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Michael Curtiz, a small Yorkshire terrier sits on a subway seat in fog and shadow, the camera glides through the carriage like through Rick's café, romance under pressure, a farewell in the mist, studio craftsmanship at its best`
- 中文对照：柯蒂斯风格：好莱坞工匠精神，流畅的摄影机运动，雾与阴影，压力下的浪漫，制片厂制度的巅峰。一只约克夏犬坐在地铁座位上，按本导演的镜头、调度与剪辑拍成现代短片。
- Negative: `No static theatrical staging, no slow contemplative pacing, no psychological exposition, no handheld shakiness, no ironic distance`
- 检验点：镜头语言是否成立；场面调度是否可辨；剪辑节奏是否符合本导演；Negative 清单是否被遵守。
