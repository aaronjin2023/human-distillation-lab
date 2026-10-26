# Georges Méliès — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Georges Méliès: theatrical trick film, fixed frontal camera, hand-painted colour, substitution splices and superimpositions, painted backdrops, féerie spectacle, playful wonder`
- ZH: 梅里爱风格：舞台魔术式特效片，固定正面机位，手工着色，停机再拍与叠印，彩绘布景，仙境奇观，游戏般的惊奇。

## (2) 镜头语言

- 固定正面机位为主，几乎如舞台观众席视角；极少移动镜头；景别以全景与中全景为主，让布景与机关完整入画；停机再拍（substitution splice）是核心运镜替代手段。`verbatim`

## (3) 场面调度

- 舞台式场面调度：演员正面朝向镜头表演，动作夸张如默剧与魔术；多层彩绘布景纵深排列，人物在布景机关间进出；变身、消失、分身靠机位不动、演员换位完成。`verbatim`

## (4) 剪辑节奏

- 按场次拼接的段落剪辑，场景内基本不切；以叠化、淡入淡出连接奇观段落；节奏由魔术效果的揭示点决定，一惊一笑一停顿。`verbatim`

## (5) 色彩与光影

- 黑白片上手绘着色：月亮金黄、火箭红白、仙女裙摆粉蓝；色彩不写实，只为标示奇观与区分人物；布景用浓艳平面色块，近乎舞台布景画。`verbatim`

## (6) 该拍什么 / 不该拍什么

- 该拍：
- 月球、火箭、星空与天文奇观
- 魔术变身、消失、分身与巨头幻象
- 童话仙境与彩绘布景
- 探险队群像与谢幕式亮相
- 手工着色营造的梦幻色彩
- 不该拍：
- no camera movement, no handheld shots
- no psychological realism, no naturalistic acting
- no fast cutting inside a trick, no hidden effects
- no muted documentary palette, no grey realism
- no open ambiguous ending, no off-screen implication
- Negative prompt: `No camera movement, no handheld shots, psychological realism, no naturalistic acting, fast cutting inside a trick, no hidden effects, muted documentary palette, no grey realism, open ambiguous ending, no off-screen implication`

## (7) 叙事结构

- 短篇奇观叙事：出发—遇险—变身—凯旋的简单链条；多取材童话、凡尔纳式科幻与历史传奇；结尾常以谢幕式群像收束，演员向镜头鞠躬。`verbatim`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Georges Méliès, a small Yorkshire terrier sits on a subway seat and suddenly multiplies into three identical dogs, fixed frontal camera, hand-painted colour, painted fairground backdrop behind the carriage window, theatrical wonder, substitution-splice magic`
- 中文对照：梅里爱风格：舞台魔术式特效片，固定正面机位，手工着色，停机再拍与叠印，彩绘布景，仙境奇观，游戏般的惊奇。一只约克夏犬坐在地铁座位上，按本导演的镜头、调度与剪辑拍成现代短片。
- Negative: `No camera movement, no handheld shots, no naturalistic acting, no fast cutting, no muted grey palette`
- 检验点：镜头语言是否成立；场面调度是否可辨；剪辑节奏是否符合本导演；Negative 清单是否被遵守。
