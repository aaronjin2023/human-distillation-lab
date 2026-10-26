# Fanny Mendelssohn Hensel — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `German Romantic song and piano cycle, lyrical chromatic harmony, intimate chamber music, monthly character pieces, singing lines with harmonic density, sister of Felix, voice of her own`
- ZH: 德国浪漫主义艺术歌曲与钢琴套曲，抒情的半音和声，亲切的室内乐，月份性格小品，歌唱性线条与和声密度，菲利克斯之姐，自有声音。

## (2) 旋律与和声

- 旋律：旋律歌唱性强，级进为主，乐句绵长；艺术歌曲旋律贴合诗歌。`artifact` 和声：功能和声为基底，和声密度高于同时代沙龙音乐，半音作表情；禁用无诗歌支撑的随意半音。调性：调性游移靠半音，终止仍清晰。

## (3) 节奏与织体

- 节奏：节奏随诗歌与旋律流动；钢琴套曲各月性格节奏各异。织体：主调为主，声乐加钢琴；三重奏三声部平等对话；留白靠乐句呼吸。

## (4) 配器与音色

- 配器与音色：声乐与钢琴为本体，弦乐三重奏与四重奏并重；音色温暖、亲切；力度靠旋律与和声对比；空间感来自柏林沙龙的 intimate。

## (5) 曲式与结构

- 曲式：钢琴套曲（《一年》十二月）、艺术歌曲、钢琴三重奏、弦乐四重奏并重。结构：月份或诗歌段落驱动，高潮在和声转折处；三重奏以奏鸣曲式组织；结尾常以静默收束。

## (6) 该写什么 / 不该写什么

- 该写：钢琴套曲《一年》、艺术歌曲、钢琴三重奏、抒情半音和声、月份性格小品。
- 不该写：无诗歌支撑的随意半音、无歌唱性的机械音型、钢琴盖过声乐、与结构无关的装饰、感伤的滥情。
- Negative prompt: `No poetry-free chromaticism, no unlyrical mechanical figuration, no piano covering voices, no structure-irrelevant ornament, no sentimental excess, no pop phrasing`

## (7) 测试提示词示例（现代题材：一只坐在地铁座位上的小约克夏犬）

- Prompt: `In the style of Fanny Mendelssohn Hensel, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, german romantic song and piano cycle, lyrical chromatic harmony, intimate chamber music, monthly character pieces, singing lines with harmonic density, sister of felix, voice of her own`
- 中文对照：范妮·门德尔松·亨塞尔风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，德国浪漫主义艺术歌曲与钢琴套曲，抒情的半音和声，亲切的室内乐，月份性格小品，歌唱性线条与和声密度，菲利克斯之姐，自有声音。
- Negative: `No poetry-free chromaticism, no unlyrical mechanical figuration, no piano covering voices, no structure-irrelevant ornament, no sentimental excess, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
