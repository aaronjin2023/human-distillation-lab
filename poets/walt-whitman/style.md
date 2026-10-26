# Walt Whitman — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Walt Whitman: long free-verse lines like breath, catalogues that swallow the world, I celebrate myself and sing myself, the body and the grass, democracy as a chorus, no metre but the pulse`
- ZH: 惠特曼风格：自由体的长行如呼吸，目录式的铺陈吞下世界，我歌颂我自己，身体与草叶，民主即合唱，没有格律，只有脉搏。

## (2) 意象

- 草叶（民主的草，卑微而普遍）
- 身体（歌颂身体即歌颂灵魂）
- 大海与道路（漫游与开放）
- 我（包容一切的自我）
- 美国在歌唱（劳动者的合唱）
- 禁意象：精致的格律、含蓄的暗示、贵族的典雅
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 自由体长行，行长参差、排比叠咏，呼吸绵长；以目录式铺陈推进，跨行奔涌；《桴鼓集》以短促的鼓点对照长行；整体由《草叶集》的初版短章向晚期的长行合唱演变。

## (4) 语言密度与词汇

- 词汇：日常词极密（草、身体、海、路），动词多为歌颂态（歌颂、包含、拥抱）；抽象词（民主、灵魂）借身体落地；禁词：精致的典雅词、含蓄的暗示词、讽刺的冷词。

## (5) 结构习惯

- 目录式：以铺陈推进，一物接一物，无转折而有累积；单篇多以“我”起兴，铺陈—拥抱—收束；《草叶集》逐版增补，组诗以增补而非定稿推进；结尾多为开放的拥抱而非收束。

## (6) 该写什么 / 不该写什么

- 该写：
- 自由体长行与目录铺陈
- 身体与草叶的歌颂
- “我”的包容与合唱
- 开放的拥抱收束
- 不该写：
- 精致格律与含蓄暗示
- 讽刺冷嘲
- 直白说教
- 封闭的收束
- Negative prompt: `No neat metre, no coy allusion, no ironic detachment, no direct preaching, no closed conclusive ending, no small timid lines`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Walt Whitman, a small Yorkshire terrier sits on a subway seat at night. Long free-verse lines like breath, catalogues of commuters, I celebrate the dog and sing the subway, the body and the grass, democracy as a chorus, an open embrace.`
- 中文对照：惠特曼风格：一只约克夏犬深夜坐在地铁座位上。自由体的长行如呼吸，乘客的目录式铺陈，我歌颂狗、歌颂地铁，身体与草叶，民主即合唱，开放的拥抱收束。
- Negative: `No neat metre, no coy allusion, no ironic detachment, no preaching, no closed ending, no timid lines`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
