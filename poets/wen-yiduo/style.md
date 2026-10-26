# Wen Yiduo — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wen Yiduo: Crescent School verse of formal beauty, red candles and dead water, music and painting and architecture in one line, grief forged into form, no looseness, solemn and sculpted`
- ZH: 闻一多风格：新月派格律，红烛死水，音乐美、绘画美、建筑美，悲愤铸于形式，绝无松散，庄严而雕塑。

## (2) 意象

- 主意象：红烛、死水、七子、祈祷
- 辅意象：绝望的沟、清风、漪沦、耕耘
- 禁意象：松散自由体、口语俗词、直白议论
- 密度：疏密相间：意象沉实，格律精严，一句一意
- 来源：红烛实景、死水意象、爱国情怀
`impression`

## (3) 韵律与句式

- 韵律：新月格律：三美并重，句式整齐，押韵精严，节式讲究
- 句式：短句庄严，长短交错，跨行随格律走
- 节奏：庄严沉重，呼吸深长，顿挫在节式转换处
`impression`

## (4) 语言密度与词汇

- 词汇：庄严词域：红烛、死水、祈祷、耕耘；动词多问、烧、沉、盼；少口语
- 密度：每行信息量适中，一景一句，格律即意义
- 禁词：松散自由体、口语俗词、直白议论、轻佻小调
`impression`

## (5) 结构习惯

- 诗体：抒情短诗 / 组诗；结构为意象起兴 → 层层铺写 → 庄严收束
- 开头：以沉实意象直入（红烛啊、这是一沟绝望的死水）
- 结尾：以庄严收束（莫问收获，但问耕耘）
- 视角：第一人称庄严者
- 推进：意象 → 铺写 → 收束，层层加深
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 红烛死水
- 三美格律
- 音乐绘画建筑
- 庄严收束
- 意象沉实
- 不该写：
- 松散自由体
- 口语俗词
- 直白议论
- 轻佻小调
- 铺张排比
- Negative prompt: `No loose free verse, no colloquial diction, no direct preaching, no frivolous trifles, no lavish parallelism`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Wen Yiduo, a letter to oneself ten years from now. Crescent School verse of formal beauty, red candles and dead water, music and painting and architecture in one line, grief forged into form, no looseness, solemn and sculpted`
- 中文对照：闻一多风格：一封写给十年后自己的信。闻一多风格：新月派格律，红烛死水，音乐美、绘画美、建筑美，悲愤铸于形式，绝无松散，庄严而雕塑。
- Negative: `No loose free verse, no colloquial diction, no direct preaching, no frivolous trifles, no lavish parallelism`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
