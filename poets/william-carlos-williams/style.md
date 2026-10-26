# William Carlos Williams — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Carlos Williams: no ideas but in things, the red wheelbarrow glazed with rain, plums in the icebox, American idiom, the triadic line stepping down, the local as the universal`
- ZH: 威廉斯风格：没有观念，只有物，雨后釉光的红色手推车，冰箱里的李子，美国口语，三段下阶的行，地方的即普遍的。

## (2) 意象

- 红色手推车（雨后釉光，物即全部）
- 冰箱里的李子（《这不过是想说》）
- 花与雏菊（《春天及一切》）
- 帕特森的瀑布与河流（地方史诗）
- 美国口语（地方的语言）
- 禁意象：欧洲的典雅、抽象的大词、华丽的修辞
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 三段下阶行（triadic line）为主，行断如阶梯；短行、口语化，节奏轻快；《帕特森》以长诗组诗推进，散文与诗交错；整体由意象派的短诗向地方史诗的长诗演变。

## (4) 语言密度与词汇

- 词汇：日常物词极准（手推车、李子、花），美国口语；抽象词极少，每词借物落地；禁词：欧洲典雅词、抽象大词、华丽形容词。

## (5) 结构习惯

- 意象诗：以一物起兴，凝视—呈现—收束，无议论；《帕特森》以五卷组诗写地方，瀑布与河流为轴；单篇多以物起兴，结尾多为物的呈现而非收束。

## (6) 该写什么 / 不该写什么

- 该写：
- 红色手推车、李子、花的物象
- 三段下阶行的节奏
- 美国口语
- 物即全部的结构
- 不该写：
- 欧洲典雅与抽象大词
- 华丽修辞
- 直白说教
- 冗长铺陈
- Negative prompt: `No European elegance, no grand abstract words, no ornate rhetoric, no direct preaching, no long explanatory passages, no ideas without things`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of William Carlos Williams, a small Yorkshire terrier sits on a subway seat at night. No ideas but in things, the red wheelbarrow of the carriage, plums in the icebox of the commuters, American idiom, the triadic line stepping down, the dog as a thing.`
- 中文对照：威廉斯风格：一只约克夏犬深夜坐在地铁座位上。没有观念，只有物，车厢里的红色手推车，乘客冰箱里的李子，美国口语，三段下阶的行，狗即一物。
- Negative: `No European elegance, no grand abstractions, no ornate rhetoric, no preaching, no long passages, no ideas without things`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
