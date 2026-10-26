# Guru Dutt — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Guru Dutt: lyrical melancholy, expressive chiaroscuro, low-key lighting, graceful camera movement, songs as inner monologue, the artist unrecognised by a commercial world`
- ZH: 古鲁·杜特风格：抒情忧郁，明暗对比强烈的光影，低调布光，优雅的运镜，歌舞即内心独白，不被商业世界承认的艺术家。

## (2) 镜头语言

- 景别：多用中景与近景，人物面部特写承载情绪；歌舞段落拉开为全景。`verbatim`
- 机位：低机位仰拍与缓慢横移、推近并用，摄影机常随人物缓缓移动而非跳切。`verbatim`
- 镜头：与摄影师 V. K. 穆尔蒂合作，善用深焦与前景遮挡，画面层次丰富。`artifact`
- 运镜禁忌：几乎不用手持晃动与快速剪辑，运镜始终克制而抒情。`impression`

## (3) 场面调度

- 人物走位：人物常处于画面边缘或被门框、窗框、栏杆切割，孤独感来自构图本身。`verbatim`
- 景深与层次：前景剪影 + 中景人物 + 背景光斑的三层结构是标志。`verbatim`
- 空间：室内（妓院、豪宅、片场）与雨夜街道并重，空间越拍越逼仄。`impression`
- 演员表演风格：职业演员，表演内敛克制，情绪靠歌声与光影外化而非台词。`impression`

## (4) 剪辑节奏

- 剪辑速度：慢节奏，平均镜头偏长，歌舞段落以长镜头保留完整表演。`impression`
- 转场：叠化与淡入淡出为主，情绪段落用叠化衔接。`impression`
- 段落结构：歌舞段落即叙事段落，歌曲推进人物内心而非插科打诨。`impression`
- 声音剪辑：歌曲与环境音（雨声、风声）先行，画面随后，声画互为回声。`impression`

## (5) 色彩与光影

- 色彩：《皮亚萨》黑白摄影以黑白灰的层次见长；后期彩色片用暖调灯光与暗部。`verbatim`
- 光影：强烈的明暗对比，人物半张脸常隐入阴影，顶光与逆光勾勒剪影。`verbatim`
- 胶片 / 画幅：《纸花》为印度首部 CinemaScope 宽银幕影片，横向构图开阔。`artifact`

## (6) 叙事结构

- 结构：线性叙事，诗人 / 艺术家从希望到幻灭再到出走的三段式。`impression`
- 视点：全知而悲悯，镜头站在被侮辱者一边。`impression`
- 时间：顺时为主，回忆以歌舞与叠化闪回。`impression`
- 类型处理：遵守歌舞片成规（歌舞、爱情、家庭），再以悲剧结局颠覆它。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：失意的诗人与艺术家、雨夜街道、歌舞即独白、门框窗框切割的孤独构图、半张脸隐入阴影的特写
- 不该拍：轻佻喜剧、快速剪辑、手持晃动、明亮扁平的布光、圆满大团圆
- Negative prompt: `No fast cutting, no handheld shaky cam, no bright flat lighting, no slapstick comedy, no happy ending, no explanatory voiceover`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Guru Dutt, a small Yorkshire terrier sitting alone on a subway seat at night, low-key chiaroscuro lighting, half its face in shadow, slow graceful camera move, rain on the window, a melancholy song-like mood, the dog unnoticed by the crowd`
- 中文对照：古鲁·杜特风格：一只约克夏犬深夜独自坐在地铁座位上，低调明暗对比布光，半张脸隐入阴影，缓慢优雅的运镜，车窗上有雨，忧郁如歌的氛围，乘客无人注意它。
- Negative: `No fast cutting, no handheld camera, no bright flat lighting, no cheerful comedy, no happy ending`
- 检验点：明暗对比与剪影是否成立；运镜是否缓慢抒情；孤独感是否来自构图而非台词。
