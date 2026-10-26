# Xie Lingyun — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xie Lingyun: landscape verse, five-character lines, mountains and waters described in layered detail, precise colour words, neat parallelism, a wanderer's eye moving from near to far`
- ZH: 谢灵运风格：山水诗祖，五言铺写，层层写景，色彩词精当，对仗工整，游目由近及远。

## (2) 意象

- 主意象：山、水、石壁、湖、猿啼、春草
- 辅意象：孤屿、精舍、云霞、松竹
- 禁意象：田园闲适、闺情艳语、都市繁华
- 密度：密集：写景铺陈，一景多笔，色彩与声音并置
- 来源：实地山水、游览所见
`impression`

## (3) 韵律与句式

- 韵律：五言古体，工对，对仗精整，押韵稳健
- 句式：铺陈句式，名词并列，色彩词与动词交错，少跨行
- 节奏：平稳中见起伏，写景处缓，登高处扬
`impression`

## (4) 语言密度与词汇

- 词汇：色彩词域：青、碧、白、红；山水专名多；动词多登、望、溯、攀
- 密度：每行信息量高，一景多词，修饰语占比高
- 禁词：艳情词、都市词、直白议论
`impression`

## (5) 结构习惯

- 诗体：单篇山水长篇 / 游览诗；结构为行程推进：入山 → 登高 → 望远 → 生感
- 开头：由行程切入（登楼、还湖、登屿）
- 结尾：以感慨或玄理收束，景后出情
- 视角：第一人称游者
- 推进：近景 → 远景 → 全景 → 感慨，层层推远
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 山水铺陈
- 色彩词
- 工整对仗
- 由近及远
- 登高望远
- 不该写：
- 艳情铺陈
- 都市繁华
- 直白说教
- 田园闲适
- 口语俗词
- Negative prompt: `No erotic elaboration, no urban bustle, no direct preaching, no pastoral idleness, no colloquial diction`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Xie Lingyun, a letter to oneself ten years from now. landscape verse, five-character lines, mountains and waters described in layered detail, precise colour words, neat parallelism, a wanderer's eye moving from near to far`
- 中文对照：谢灵运风格：一封写给十年后自己的信。谢灵运风格：山水诗祖，五言铺写，层层写景，色彩词精当，对仗工整，游目由近及远。
- Negative: `No erotic elaboration, no urban bustle, no direct preaching, no pastoral idleness, no colloquial diction`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
