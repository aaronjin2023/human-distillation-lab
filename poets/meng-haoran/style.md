# Meng Haoran — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Meng Haoran: five-character verse, spring dawn and village fields, misty rivers and green hills, plain diction, quiet contentment, no ambition, gentle and unhurried`
- ZH: 孟浩然风格：五言田园，春晓村野，烟波绿嶂，语言素朴，闲适自足，不事功名，温和而不迫。

## (2) 意象

- 主意象：春晓、田园、故人庄、洞庭湖、烟波、绿嶂
- 辅意象：花落、啼鸟、渔舟、松月
- 禁意象：功名意象、都市繁华、豪言壮语
- 密度：疏朗：意象少而精，一景一意
- 来源：襄阳田园、实地山水
`impression`

## (3) 韵律与句式

- 韵律：五言律绝为主，对仗自然，平仄稳健
- 句式：短句平直，少倒装，少跨行，句句落地
- 节奏：缓慢平稳，呼吸均匀，如闲谈
`impression`

## (4) 语言密度与词汇

- 词汇：日常词域：春眠、花落、把酒、话桑麻；少典故
- 密度：每行信息量低，一景一句
- 禁词：功名词、都市词、豪壮词、僻典
`impression`

## (5) 结构习惯

- 诗体：五言律绝 / 绝句；结构为写景 → 生情 → 闲适收束
- 开头：直入眼前之景（春眠、过庄）
- 结尾：以闲适或期约收束，不议论
- 视角：第一人称闲居者
- 推进：景 → 情 → 闲，层层淡出
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 春晓田园
- 故人把酒
- 洞庭烟波
- 闲适自足
- 平淡短句
- 不该写：
- 功名意象
- 都市繁华
- 豪言壮语
- 激烈议论
- 堆砌典故
- Negative prompt: `No fame-and-office imagery, no urban bustle, no grand heroic diction, no heated argument, no piled-up allusions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Meng Haoran, a person buys oden at a convenience store late at night. five-character verse, spring dawn and village fields, misty rivers and green hills, plain diction, quiet contentment, no ambition, gentle and unhurried`
- 中文对照：孟浩然风格：一个人在深夜便利店买关东煮。孟浩然风格：五言田园，春晓村野，烟波绿嶂，语言素朴，闲适自足，不事功名，温和而不迫。
- Negative: `No fame-and-office imagery, no urban bustle, no grand heroic diction, no heated argument, no piled-up allusions`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
