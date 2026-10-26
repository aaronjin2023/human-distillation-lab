# Montserrat Caballé — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Lyric soprano in the style of Montserrat Caballé: creamy Catalan soprano, floating pianissimo, bel canto purity, regal line, crossover warmth`
- ZH: 卡巴耶风格：奶油般柔滑的加泰罗尼亚女高音，漂浮的弱音，美声的纯净，帝王般的线条，跨界的暖意。

## (2) 音色与音域

- 抒情女高音，音色奶油般柔滑，弱音漂浮；主音色为柔滑的抒情女高音，辅音色为弱音的漂浮，禁音色为戏剧性的胸声吼叫与粗粝边缘。`artifact`

## (3) 唱腔与发声技法

- 发声：气息深厚，起音柔和，收尾多渐弱漂浮；唱腔：弱音（pianissimo）极致控制，legato 长线条，颤音细腻。`artifact`

## (4) 咬字与语言

- 意大利语与西班牙语咬字清晰，元音圆润；换气点藏在长乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 乐句宽广，速度从容；慢板更沉，高潮处不抢拍。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：贝里尼与多尼采蒂女主角（诺尔玛、露琪亚）、威尔第与普契尼抒情女主角、西班牙歌曲与萨苏埃拉、跨界合作《巴塞罗那》、弱音漂浮的抒情段落。
- 不该唱：`No dramatic chest belt, no breathy pop tone, no jazz scat, no clipped coloratura, no harsh edge`
- Negative prompt: `No dramatic chest belt, no breathy pop tone, no jazz scat, no clipped coloratura, no harsh edge`

## (7) 测试提示词示例（现代题材：凌晨机场）

- Prompt: `Sing in the style of Montserrat Caballé, a song about a traveller waiting alone at an airport before dawn. Creamy soprano, floating pianissimo, bel canto purity, regal line, warm orchestral accompaniment.`
- 中文对照：卡巴耶风格：唱一首关于黎明前独自在机场等候的旅人的歌。奶油般柔滑的女高音，漂浮的弱音，美声的纯净，帝王般的线条，管弦乐伴奏。
- Negative: `No dramatic chest belt, no breathy pop tone, no jazz scat, no clipped coloratura, no harsh edge`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
