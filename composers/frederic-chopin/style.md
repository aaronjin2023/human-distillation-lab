# Frédéric Chopin — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Bel canto piano lyricism, rubato, ornamental filigree, chromatic colour within singing melody, Polish dance rhythms, intimate salon scale`
- ZH: 美声式钢琴抒情，rubato 自由伸缩，装饰音如花腔，歌唱旋律中的半音色彩，波兰舞曲节奏，亲密的沙龙尺度。

## (2) 旋律与和声

- 旋律：美声式长线条，装饰音如花腔；和声：半音化功能和声，拿波里和弦、增六和弦作色彩。禁：无调性、德国式动机发展。调性游移但总有归宿，不协和以装饰音柔化。

## (3) 节奏与织体

- 节奏：rubato 自由伸缩，马祖卡切分；织体：右手歌唱加左手伴奏，单声钢琴，旋律突出。

## (4) 配器与音色

- 乐器：独奏钢琴（几乎全部作品）；音色：弱音踏板、半踏板、歌唱性触键；力度：ppp 到 ff 的细腻层次，极少 ff 轰鸣。

## (5) 曲式与结构

- 曲式：夜曲、叙事曲、波兰舞曲、马祖卡、练习曲；结构：三段体、回旋、自由叙事；结尾：辉煌尾声或渐弱余韵。

## (6) 该写什么 / 不该写什么

- 该写：夜曲式歌唱旋律、装饰音、rubato、马祖卡节奏、波兰舞曲、叙事曲式自由结构。
- 不该写：管弦乐厚度、德国式动机发展、无调性、节拍器式僵硬、铜管高潮、流行和弦循环。
- Negative prompt: `no orchestral thickness, no Germanic motivic development, no atonal wandering, no metronomic rigidity, no loud brass climax, no pop chord loop`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡，晨光中）

- Prompt: `In the style of Frédéric Chopin, a cup of coffee sitting on a windowsill in the morning light, Bel canto piano lyricism, rubato, ornamental filigree, chromatic colour within singing melody, Polish dance rhythms, intimate salon scale`
- 中文对照：弗雷德里克·肖邦风格，一杯放在窗台上的咖啡，晨光中，美声式钢琴抒情，rubato 自由伸缩，装饰音如花腔，歌唱旋律中的半音色彩，波兰舞曲节奏，亲密的沙龙尺度。
- Negative: `no orchestral thickness, no Germanic motivic development, no atonal wandering, no metronomic rigidity, no loud brass climax, no pop chord loop`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
