# Du Mu — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Du Mu: seven-character quatrains, history in four lines, spring rain and dusk, a single turn that overturns the past, elegant and sharp, no excess, wistful and clear`
- ZH: 杜牧风格：七绝咏史，四句见史，春雨黄昏，一转而翻覆往事，清俊而锋利，绝无铺张，怅惘而清明。

## (2) 意象

- 主意象：赤壁、秦淮、清明雨、铜雀台、后庭花
- 辅意象：商女、行人、东风、二乔
- 禁意象：铺张排比、直白议论、豪放壮语
- 密度：疏朗：四句一景一转，意象少而精
- 来源：史地实景、节令风物
`impression`

## (3) 韵律与句式

- 韵律：七言绝句为主，对仗自然，平仄稳健，押韵清朗
- 句式：短句平直，末句转折（东风不与周郎便），少跨行
- 节奏：平稳中一转，末句扬起，全篇收于一转
`impression`

## (4) 语言密度与词汇

- 词汇：清俊词域：雨纷纷、隔江、春深；动词多问、唱、锁；少僻字
- 密度：每行信息量适中，一景一句，转折在末句
- 禁词：铺张排比、直白议论、豪放壮语、僻典
`impression`

## (5) 结构习惯

- 诗体：七言绝句；结构为写景 → 生情 → 末句一转
- 开头：直入眼前之景（清明雨、秦淮夜）
- 结尾：以末句一转收束，余味在转折处
- 视角：第一人称凭吊者
- 推进：景 → 情 → 转，层层收于一转
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 七绝咏史
- 末句一转
- 春雨黄昏
- 清俊短句
- 以小见大
- 不该写：
- 铺张排比
- 直白议论
- 豪放壮语
- 堆砌典故
- 温情絮叨
- Negative prompt: `No lavish parallelism, no direct preaching, no grand heroic diction, no piled-up allusions, no sentimental chatter`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Du Mu, a person buys oden at a convenience store late at night. seven-character quatrains, history in four lines, spring rain and dusk, a single turn that overturns the past, elegant and sharp, no excess, wistful and clear`
- 中文对照：杜牧风格：一个人在深夜便利店买关东煮。杜牧风格：七绝咏史，四句见史，春雨黄昏，一转而翻覆往事，清俊而锋利，绝无铺张，怅惘而清明。
- Negative: `No lavish parallelism, no direct preaching, no grand heroic diction, no piled-up allusions, no sentimental chatter`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
