# Andrei Tarkovsky — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Andrei Tarkovsky: time sculpted in long takes, memory and dream as present tense, a zone where wishes are tested, faith asked without answer, images that linger longer than plot`
- ZH: 塔可夫斯基风格：长镜头里雕刻时间，记忆与梦即现在，愿望被考验的区，信仰被追问而无答案，意象比情节留得更久。

## (2) 结构：三幕 / 序列 / 节拍

- 诗性结构而非三幕：以时间与记忆的流动组织全片；《卢布廖夫》为七段式编年，《索拉里斯》为太空站内的回忆层叠，《潜行者》为进入“区”的三段旅程。转折点不是事件而是人物内心的转向；结尾常常是一个长镜头静止，问题悬在空中。

## (3) 对话

- 对白稀少、缓慢，多为独白与哲学追问；人物用引文与回忆说话；沉默与自然音（水、雨、风）占很大比重；动作描写多写时间流逝而非动作本身。

## (4) 人物弧光

- 主角多为艺术家、科学家、潜行者，弧光是从寻求答案到接受不可知：不是顿悟，是学会停留。人物关系是向导与追随者、父与子、人与记忆的对峙；结局人物不胜利，只获得片刻的安宁。

## (5) 类型套路与创新

- 类型：诗电影与科幻哲理剧；遵守套路——旅程、考验、归来；打破的一条是：情节几乎停滞，时间本身成为主角。创新在剧本层面：把长镜头与时间流逝直接写进剧本结构，让记忆与梦境不加标记地进入现在。禁套路：不用类型反转，不用解释性对白，不用快节奏剪辑提示。

## (6) 该写什么 / 不该写什么

- 该写：长时间与记忆流动、梦境与回忆不加标记、区、房间等考验空间、哲学独白与引文、静止的长镜头结尾。
- 不该写：类型反转、解释性对白、快节奏剪辑提示、直白的答案、煽情高潮。
- Negative prompt: `No genre twist, no explanatory dialogue, no fast-cutting cues, no direct answer, no sentimental climax`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Andrei Tarkovsky, a man buys oden at a convenience store late at night. Time slows. Steam rises. He remembers a room from childhood. No answer is given, only the long take of waiting.`
- 中文对照：塔可夫斯基风格：一个男人深夜在便利店买关东煮，时间变慢，蒸汽升起，他想起童年的一个房间，没有答案，只有一个等待的长镜头。
- Negative: `No genre twist, no explanatory dialogue, no fast-cutting cues, no direct answer, no sentimental climax`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
