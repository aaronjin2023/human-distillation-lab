# Li He — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li He: strange and precipitous verse, black clouds and golden scales, ghostly music and cold moonlight, jewelled words piled like broken jade, brief life burning bright, no warmth, eerie and gorgeous`
- ZH: 李贺风格：奇崛鬼才，黑云金鳞，鬼乐冷月，丽字如碎玉堆叠，短命而炽烈，绝无温情，瑰丽而阴冷。

## (2) 意象

- 主意象：黑云、甲光、昆山玉、凤凰、冷月、鬼
- 辅意象：芙蓉泣露、香兰、梦天、老鱼
- 禁意象：平淡田园、温情小调、直白议论
- 密度：极高密度：丽字堆叠，一句多象，色彩浓烈
- 来源：神话、乐府旧题、梦境
`impression`

## (3) 韵律与句式

- 韵律：七言歌行 / 乐府，句式奇崛，跨行跳跃，押韵冷峻
- 句式：长短句交错，意象跳接，倒装奇崛，跨行连续
- 节奏：急促冷峻，呼吸短促，顿挫在色彩转换处
`impression`

## (4) 语言密度与词汇

- 词汇：瑰丽词域：黑云、金鳞、昆山玉、凤凰；动词多碎、泣、飞、冷；少日常词
- 密度：每行信息量极高，一句多象，修饰语占比高
- 禁词：平淡田园、温情小调、直白议论、口语俗词
`impression`

## (5) 结构习惯

- 诗体：乐府 / 歌行；结构为奇象起兴 → 跳接铺陈 → 冷峻收束
- 开头：以奇象直入（黑云压城）
- 结尾：以冷月或梦醒收束，不温情
- 视角：第一人称奇观见证者
- 推进：奇象 → 再奇象 → 冷收束，层层加冷
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 黑云金鳞
- 昆山玉碎
- 鬼乐冷月
- 丽字堆叠
- 奇象跳接
- 不该写：
- 平淡田园
- 温情小调
- 直白议论
- 口语俗词
- 工整无气之律
- Negative prompt: `No plain pastoral, no sentimental trifles, no direct preaching, no colloquial diction, no neat verse without strangeness`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Li He, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. strange and precipitous verse, black clouds and golden scales, ghostly music and cold moonlight, jewelled words piled like broken jade, brief life burning bright, no warmth, eerie and gorgeous`
- 中文对照：李贺风格：一只约克夏犬深夜坐在地铁座位上，乘客们看着它。李贺风格：奇崛鬼才，黑云金鳞，鬼乐冷月，丽字如碎玉堆叠，短命而炽烈，绝无温情，瑰丽而阴冷。
- Negative: `No plain pastoral, no sentimental trifles, no direct preaching, no colloquial diction, no neat verse without strangeness`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
