# T. S. Eliot — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of T. S. Eliot: fragments shored against ruin, the unreal city and the river, mythic method binding broken voices, objective correlative instead of statement, time present and time past in one line`
- ZH: 艾略特风格：以碎片抵御毁灭，虚幻的城市与河流，神话方法缀合破碎的声音，以客观对应物代替直陈，过去与现在同在一行诗里。

## (2) 意象

- 荒原（干枯的土地与空洞的人）
- 虚幻的城市（伦敦桥上的人流）
- 河流与火（《四个四重奏》的两极）
- 玫瑰与花园（时间的玫瑰园）
- 空洞的人与老鼠（《空心人》）
- 禁意象：直白的抒情告白、无典故的口语
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 自由体与空白体交错：《普鲁弗洛克》以戏剧独白的长句与短句交错；《荒原》以碎片并置、多声部跳接，节奏断裂；《四个四重奏》以四乐章结构，句式绵长、冥想式推进；整体由碎片向冥想演变。

## (4) 语言密度与词汇

- 词汇：典故极密（但丁、莎士比亚、圣经、梵语），多语并置（英、法、德、意、梵）；抽象词借具体物（河、火、玫瑰）落地；禁词：直白的情感告白、无典故支撑的口语。

## (5) 结构习惯

- 《荒原》五章碎片并置，以神话方法缀合；《四个四重奏》四乐章，每章以一地（伯恩特·诺顿等）起兴，冥想推进；单篇多以场景切入、声音跳接、悖论收束。

## (6) 该写什么 / 不该写什么

- 该写：
- 碎片并置与多声部
- 神话方法与典故密度
- 客观对应物
- 时间与河流、火的冥想
- 不该写：
- 直白的抒情告白
- 无典故的口语絮叨
- 单一声部的独白
- 温情的团圆收束
- Negative prompt: `No direct lyrical confession, no plain talk without allusion, no single unbroken voice, no sentimental happy ending, no explanation of the image, no loose formless verse`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of T. S. Eliot, a small Yorkshire terrier sits on a subway seat at night. Fragments shored against ruin, the unreal city of the carriage, the river of commuters, the dog as an objective correlative, time present and time past in one line.`
- 中文对照：艾略特风格：一只约克夏犬深夜坐在地铁座位上。以碎片抵御毁灭，车厢是虚幻的城市，乘客是河流，狗是一个客观对应物，过去与现在同在一行诗里。
- Negative: `No direct confession, no plain talk, no single voice, no sentimental ending, no explanation`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
