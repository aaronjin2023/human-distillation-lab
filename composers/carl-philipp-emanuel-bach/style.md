# Carl Philipp Emanuel Bach — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Empfindsamer Stil, sudden expressive contrasts, sighing appoggiaturas, unpredictable phrases, sensitive keyboard style, bridge from Baroque to Classical, north German galant`
- ZH: 情感风格，突发的表情对比，叹息式倚音，不可预测的乐句，敏感的键盘风格，巴洛克到古典的桥梁，北德华丽风格。

## (2) 旋律与和声

- 旋律：旋律富于表情，倚音与半音叹息是标志；乐句长短不一，突然停顿。`artifact` 和声：功能和声为基底，半音与突然转调作表情；禁用无表情的功能进行。调性：调性游移靠表情转调，终止仍清晰。

## (3) 节奏与织体

- 节奏：节奏灵活，突然停顿与加速是标志；键盘曲以即兴感见长。织体：主调为主，单声旋律加伴奏；留白靠突然停顿。

## (4) 配器与音色

- 配器与音色：键盘（羽管键琴、古钢琴）为本体，弦乐队与长笛作协奏；音色敏感、细腻；力度变化大，靠突然强弱对比；空间感来自北德宫廷的 intimate。

## (5) 曲式与结构

- 曲式：键盘奏鸣曲（三乐章）、交响曲、协奏曲并重；结构靠表情对比组织，高潮在突然转调处；结尾以清晰终止收束。

## (6) 该写什么 / 不该写什么

- 该写：情感风格的突然对比、叹息式倚音、键盘奏鸣曲、突然停顿与转调、长笛协奏曲的歌唱性。
- 不该写：巴洛克式严格对位、无表情的功能进行、固定不变的乐句长度、管弦乐盖过独奏、感伤的滥情。
- Negative prompt: `No strict Baroque counterpoint, no expressionless functional harmony, no fixed phrase lengths, no orchestra covering soloist, no sentimental excess, no pop phrasing`

## (7) 测试提示词示例（现代题材：一只坐在地铁座位上的小约克夏犬）

- Prompt: `In the style of Carl Philipp Emanuel Bach, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, empfindsamer stil, sudden expressive contrasts, sighing appoggiaturas, unpredictable phrases, sensitive keyboard style, bridge from baroque to classical, north german galant`
- 中文对照：卡尔·菲利普·埃马努埃尔·巴赫风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，情感风格，突发的表情对比，叹息式倚音，不可预测的乐句，敏感的键盘风格，巴洛克到古典的桥梁，北德华丽风格。
- Negative: `No strict Baroque counterpoint, no expressionless functional harmony, no fixed phrase lengths, no orchestra covering soloist, no sentimental excess, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
