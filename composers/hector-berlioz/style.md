# Hector Berlioz — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `French Romantic programme symphony, idée fixe, huge orchestra, vivid orchestral colour, dramatic contrasts, literary imagination, inventor of modern orchestration`
- ZH: 法国浪漫主义标题交响曲，固定乐思，庞大乐队，生动的管弦乐色彩，戏剧对比，文学想象，现代配器的发明者。

## (2) 旋律与和声

- 旋律：旋律富于戏剧，固定乐思（idée fixe）在各乐章变形；线条随剧情起伏。`artifact` 和声：功能和声为基底，半音与突然转调作戏剧；禁用无剧情支撑的随意半音。调性：调性游移靠剧情，终止有力。

## (3) 节奏与织体

- 节奏：节奏戏剧化，舞曲（圆舞曲、进行曲）与自由节奏交替；断头台进行曲以节奏摹画。织体：庞大管弦乐队织体，声部密度大；留白靠突然静默。

## (4) 配器与音色

- 配器与音色：庞大管弦乐队（扩编木管、铜管、打击乐、竖琴）为本体；音色富于戏剧对比，是现代配器的范本；力度变化极大；空间感来自大型音乐厅的宏大。

## (5) 曲式与结构

- 曲式：标题交响曲（《幻想》五乐章）、歌剧（《特洛伊人》）、安魂曲并重。结构：文学情节驱动，高潮在末乐章；固定乐思贯穿全曲；结尾以宏大合唱或乐队全奏收束。

## (6) 该写什么 / 不该写什么

- 该写：固定乐思（idée fixe）、标题交响曲、庞大管弦乐配器、文学情节驱动、戏剧对比。
- 不该写：无情节支撑的随意半音、固定乐思的机械重复、管弦乐无层次堆砌、与剧情无关的装饰、古典奏鸣曲式的刻板套用。
- Negative prompt: `No plot-free chromaticism, no mechanical idée fixe repetition, no unlayered orchestral piling, no plot-irrelevant ornament, no rigid Classical sonata cliché, no pop phrasing`

## (7) 测试提示词示例（现代题材：雨后阳台上的植物）

- Prompt: `In the style of Hector Berlioz, a 30-second piece for plants on a balcony after rain, french romantic programme symphony, idée fixe, huge orchestra, vivid orchestral colour, dramatic contrasts, literary imagination, inventor of modern orchestration`
- 中文对照：柏辽兹风格，为雨后阳台上的植物写 30 秒配乐，法国浪漫主义标题交响曲，固定乐思，庞大乐队，生动的管弦乐色彩，戏剧对比，文学想象，现代配器的发明者。
- Negative: `No plot-free chromaticism, no mechanical idée fixe repetition, no unlayered orchestral piling, no plot-irrelevant ornament, no rigid Classical sonata cliché, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
