# Tao Yuanming — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tao Yuanming: plain five-character verse, garden and field imagery, chrysanthemum and wine, unadorned diction, quiet return, no ornament, serene and self-sufficient`
- ZH: 陶渊明风格：平淡五言，田园意象，菊与酒，语言素朴，归去来兮，不事雕饰，悠然自足。

## (2) 意象

- 主意象：菊、酒、田园、南山、松、豆苗
- 辅意象：飞鸟、孤云、东篱、柴门
- 禁意象：华丽辞藻、功名意象、都市繁华
- 密度：疏朗：意象少而精，一景一意，不堆叠
- 来源：日常田园、农事、自然
`impression`

## (3) 韵律与句式

- 韵律：五言古体为主，句式整齐而松散，押韵自然，不求工对
- 句式：短句平直，主谓分明，少倒装，少跨行，句句落地
- 节奏：缓慢平稳，呼吸均匀，无急促转折，读如闲谈
`impression`

## (4) 语言密度与词汇

- 词汇：日常词域：种、采、饮、归、悠然；少典故，少僻字
- 密度：每行信息量低，一景一句，修饰语极少
- 禁词：华丽形容词、功名词、都市词、僻典
`impression`

## (5) 结构习惯

- 诗体：短篇抒情 / 组诗（《饮酒》二十首、《归园田居》五首）；单篇自足，组诗松散
- 开头：直入眼前之景（种豆、采菊）或直抒归意
- 结尾：以悠然自得收束，不议论、不感慨过度
- 视角：第一人称隐者自述
- 推进：写景 → 生情 → 归意，层层淡出，不用转折
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 田园农事
- 菊与酒
- 南山松菊
- 悠然自得
- 平淡短句
- 不该写：
- 华丽辞藻
- 功名意象
- 都市繁华
- 激烈议论
- 堆砌典故
- Negative prompt: `No ornate adjectives, no fame-and-office imagery, no urban bustle, no heated argument, no piled-up allusions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Tao Yuanming, a person buys oden at a convenience store late at night. plain five-character verse, garden and field imagery, chrysanthemum and wine, unadorned diction, quiet return, no ornament, serene and self-sufficient`
- 中文对照：陶渊明风格：一个人在深夜便利店买关东煮。陶渊明风格：平淡五言，田园意象，菊与酒，语言素朴，归去来兮，不事雕饰，悠然自足。
- Negative: `No ornate adjectives, no fame-and-office imagery, no urban bustle, no heated argument, no piled-up allusions`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
