# John Huston — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Huston: hard-boiled adventure, the quest for a false idol, men under pressure, location realism, laconic dialogue, the treasure that corrupts`
- ZH: 休斯顿风格：硬汉冒险，追逐虚假偶像，压力下的人，实景写实，寡言对白，腐蚀人心的宝藏。

## (2) 镜头语言

- 实景机位：非洲河流、墨西哥山地、旧金山街头实拍，机位平稳，景别克制；《非洲女王号》用实景河流拍冒险；特写只给贪婪与疲惫。`verbatim`

## (3) 场面调度

- 冒险调度：人物在实景中跋涉、划船、挖掘，空间即考验；《夜阑人未静》中寻宝者在山地中分裂，群戏按贪婪程度分层。`verbatim`

## (4) 剪辑节奏

- 冷静剪辑：节奏平稳，冒险段落按空间逻辑切；《马耳他之鹰》靠对白剪辑推进阴谋，动作段落不炫技；结尾常以宝藏成空的冷峻收束。`verbatim`

## (5) 色彩与光影

- 黑白为主，硬光与实景灰调；《非洲女王号》用 Technicolor 的河流绿与丛林，色彩作冒险标示；《夜阑人未静》用尘土黄标示贪婪。`verbatim`

## (6) 该拍什么 / 不该拍什么

- 该拍：
- 实景河流与山地的冒险
- 黑鸟雕像与金矿的追逐
- 寡言硬汉的对白
- 贪婪分层的群戏
- 宝藏成空的冷峻结尾
- 不该拍：
- no studio-bound artificiality, no fake backdrops
- no sentimental redemption, no warm uplift
- no fast MTV cutting, no chaotic montage
- no handheld shakiness, no documentary roughness
- no psychological exposition, no inner monologue
- Negative prompt: `No studio-bound artificiality, no fake backdrops, sentimental redemption, no warm uplift, fast MTV cutting, no chaotic montage, handheld shakiness, no documentary roughness, psychological exposition, no inner monologue`

## (7) 叙事结构

- 追逐虚假偶像：黑鸟雕像、金矿、宝藏皆为幻影；故事是欲望的连锁，人物在追逐中暴露本性，结尾常以宝藏成空收束——“那东西做成的梦”。`verbatim`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of John Huston, a small Yorkshire terrier sits on a subway seat while three hard-boiled passengers trade laconic dialogue over who it belongs to, location realism, the dog as a false idol, the treasure that corrupts, a cold empty ending`
- 中文对照：休斯顿风格：硬汉冒险，追逐虚假偶像，压力下的人，实景写实，寡言对白，腐蚀人心的宝藏。一只约克夏犬坐在地铁座位上，按本导演的镜头、调度与剪辑拍成现代短片。
- Negative: `No studio-bound artificiality, no sentimental redemption, no fast MTV cutting, no handheld shakiness, no psychological exposition`
- 检验点：镜头语言是否成立；场面调度是否可辨；剪辑节奏是否符合本导演；Negative 清单是否被遵守。
