# Paul Verlaine — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paul Verlaine: music before all else, grey and vague, autumn violins and rain on the town, short lines that dissolve rather than conclude, tenderness without statement`
- ZH: 魏尔伦风格：音乐先于一切，灰色而朦胧，秋日的提琴与城里的雨，短行消散而不收束，温柔而不作论断。

## (2) 意象

- 秋日与雨（《秋歌》：提琴的长叹）
- 灰色与朦胧（nuance 而非 couleur）
- 月亮与黄昏（微光而非烈日）
- 歌与琴（音乐即意义）
- 囚室与祈祷（晚期《智慧》的忏悔）
- 禁意象：强烈的色彩与宏大的历史场面
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 短行、奇数音节（五音节、七音节、九音节）为主，追求音乐性而非格律工整；跨行柔和，行断如呼吸；《无言的浪漫曲》以无韵或半韵求朦胧；晚期回归传统格律但语气更轻。

## (4) 语言密度与词汇

- 词汇：轻、灰、柔的词域（gris、doux、voilé），形容词少而准；动词多为低声态（呜咽、飘、颤）；禁词：宏大抽象词、尖锐的讽刺词、浓艳的色彩词。

## (5) 结构习惯

- 单篇多为三四节短诗，以一景（雨、秋、月）起兴，层层晕染，结尾消散而非收束；组诗《无言的浪漫曲》以情绪而非叙事推进；晚期《智慧》以祈祷体收束。

## (6) 该写什么 / 不该写什么

- 该写：
- 秋日、雨、灰色的朦胧意象
- 音乐性短行与柔和跨行
- 温柔而不论断的语气
- 消散式结尾
- 不该写：
- 浓艳色彩与宏大场面
- 尖锐讽刺与直白说教
- 工整有力的收束
- 抽象大词的议论
- Negative prompt: `No loud colours, no grand historical scenes, no sharp satire, no direct moralising, no forceful conclusive ending, no abstract discourse without music`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Paul Verlaine, a small Yorkshire terrier sits on a subway seat at night. Music before all else, grey light, rain on the windows, short dissolving lines, the dog as a faint song, tenderness without statement, an ending that fades.`
- 中文对照：魏尔伦风格：一只约克夏犬深夜坐在地铁座位上。音乐先于一切，灰色的光，雨打车窗，短行渐渐消散，狗是一支微弱的歌，温柔而不论断，结尾渐渐淡出。
- Negative: `No loud colours, no satire, no moralising, no forceful ending, no grand scenes`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
