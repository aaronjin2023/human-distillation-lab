# John Williams — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Film score composition, leitmotif system, late-Romantic orchestral writing, brass fanfares, lyrical violin themes, precise picture synchronisation`
- ZH: 电影配乐作曲，主导动机体系，晚期浪漫管弦写作，铜管号角，抒情小提琴主题，精确的画面同步。

## (2) 旋律与和声

- 旋律：号角式大跳与抒情级进并存，主题轮廓鲜明、易记，歌唱性强。
- 和声：晚期浪漫功能和声，半音化丰富；主：大调—小调功能和声；禁：无调性与持续不协和；不协和度中，解决明确。

## (3) 节奏与织体

- 节奏：进行曲与舞曲律动，强拍明确；织体：主调管弦织体，声部密度高，主题始终清晰。

## (4) 配器与音色

- 配器：大型管弦乐团，铜管与弦乐主导，定音鼓与打击乐标点；音色：明亮、饱满、好莱坞式；力度：动态极宽。

## (5) 曲式与结构

- 曲式：主导动机组曲式，主题—变奏—再现；结构：动机按人物与情境分配；高潮在主题全奏处；结尾常以主题完整再现收束。

## (6) 该写什么 / 不该写什么

- 该写：主导动机与铜管号角、抒情小提琴主题、大型管弦乐全奏、精确的画面同步点。
- 不该写：无主题的氛围音乐、持续无调性、稀疏到听不清主题、电子音色主导。
- Negative prompt: `No theme-free ambient music, no sustained atonality, no sparse texture that loses the theme, no electronic-dominated score, no vague wandering without a leitmotif`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of John Williams, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a brass fanfare leitmotif, lyrical strings, late-Romantic harmony, clear heroic arc`
- 中文对照：约翰·威廉姆斯风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，铜管号角主导动机，抒情弦乐，晚期浪漫和声，清晰的英雄弧线。。
- Negative: `No theme-free ambient music, no sustained atonality, no sparse texture that loses the theme, no electronic-dominated score, no vague wandering without a leitmotif`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
