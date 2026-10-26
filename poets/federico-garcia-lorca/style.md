# Federico García Lorca — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Federico García Lorca: the duende of deep song, green moon and gypsy ballad, blood and guitar, New York as a nightmare of iron, the refrain that returns like a fate`
- ZH: 洛尔卡风格：深歌的杜恩德，绿色的月亮与吉卜赛谣曲，血与吉他，纽约是铁的噩梦，叠句如命运般返回。

## (2) 意象

- 绿色的月亮（《绿，绿，我爱你这绿色》）
- 血与马（吉卜赛谣曲的暴力）
- 吉他与深歌（杜恩德的歌）
- 纽约的铁与人群（《诗人在纽约》的噩梦）
- 橄榄与安达卢西亚（故乡）
- 禁意象：冷静的议论、温情的田园
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 谣曲体：八音节短行、叠句返回，节奏如歌谣；《深歌》以短句与感叹求杜恩德；《诗人在纽约》以自由体长句奔涌、意象跳接；整体由谣曲的歌谣性向自由体的噩梦演变。

## (4) 语言密度与词汇

- 词汇：色彩词极密（绿、红、黑、白），感官词（血、铁、月）与歌谣词并置；善用叠句压缩意义，一叠抵一节；禁词：冷静议论词、温和安慰语。

## (5) 结构习惯

- 谣曲：以一景起兴，叙事推进，叠句返回，悲剧收束；《诗人在纽约》以组诗推进，意象并置、噩梦层叠；单篇多以感叹起兴，叠句收束。

## (6) 该写什么 / 不该写什么

- 该写：
- 绿月、血、吉他的意象
- 谣曲叠句的返回
- 深歌的杜恩德
- 纽约的铁之噩梦
- 不该写：
- 冷静议论与温情田园
- 无叠句的散漫自由体
- 直白说教
- 温和的安慰收束
- Negative prompt: `No cool detached commentary, no gentle pastoral, no loose free verse without refrain, no direct preaching, no sentimental consolation, no irony without song`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Federico García Lorca, a small Yorkshire terrier sits on a subway seat at night. Green moon over the carriage, blood and guitar, the dog as a small gypsy, the refrain returning like fate, New York iron outside the window.`
- 中文对照：洛尔卡风格：一只约克夏犬深夜坐在地铁座位上。车厢上空是绿色的月亮，血与吉他，狗是一个小小的吉卜赛人，叠句如命运般返回，窗外是纽约的铁。
- Negative: `No cool commentary, no gentle pastoral, no refrain-less drift, no preaching, no sentimental consolation`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
