# Plácido Domingo — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Spinto tenor in the style of Plácido Domingo: dark heroic tenor, baritonal warmth, powerful middle register, dramatic acting through voice, long career versatility`
- ZH: 多明戈风格：带男中音暖色的暗色英雄男高音，中声区力量强，歌声即表演，曲目幅度极广。

## (2) 音色与音域

- 男高音带男中音的暗色，音色浑厚，中声区力量强；主音色为暗暖的戏剧男高音，辅音色为抒情段落的柔和，禁音色为轻飘的抒情甜声。`artifact`

## (3) 唱腔与发声技法

- 发声：气息长，乐句宽广，高音以胸声支撑；唱腔：戏剧力度与抒情线条并存，颤音适中；晚期转唱男中音角色，音色更暗。`artifact`

## (4) 咬字与语言

- 西班牙语母语，意大利语与法语咬字清晰；重音落在词义与剧情上；换气点随剧情呼吸。`artifact`

## (5) 节奏与即兴

- 戏剧节奏，乐句随剧情起伏；慢板更沉，快板更烈。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：威尔第英雄男高音（奥赛罗、拉达梅斯）、普契尼男主角（卡拉夫、卡瓦拉多西）、法国歌剧（《卡门》唐·何塞）、西班牙萨苏埃拉与音乐会曲目、晚期男中音角色（威尔第《西蒙·波卡涅拉》）。
- 不该唱：`No light lyric sweetness, no breathy pop phrasing, no clipped coloratura, no thin head voice, no detached concert delivery`
- Negative prompt: `No light lyric sweetness, no breathy pop phrasing, no clipped coloratura, no thin head voice, no detached concert delivery`

## (7) 测试提示词示例（现代题材：深夜拉面店）

- Prompt: `Sing in the style of Plácido Domingo, a song about a man eating ramen alone at a late-night noodle shop. Dark heroic tenor, baritonal warmth, powerful middle register, dramatic phrasing, warm orchestral accompaniment.`
- 中文对照：多明戈风格：唱一首关于深夜独自在拉面店吃面的男人的歌。暗色英雄男高音，男中音暖色，中声区力量强，戏剧化乐句，管弦乐伴奏。
- Negative: `No light lyric sweetness, no breathy pop phrasing, no clipped coloratura, no thin head voice, no detached concert delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
