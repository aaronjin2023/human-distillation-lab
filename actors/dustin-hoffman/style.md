# Dustin Hoffman — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dustin Hoffman: neurotic Method precision, fidgeting hands and restless eyes, lines delivered half-swallowed, an ordinary man made extraordinary by detail`
- ZH: 达斯汀·霍夫曼风格：神经质的方法派精确，不安的手与游移的眼，台词半吞半吐，一个靠细节变得不凡的普通人。

## (2) 形体

- 手不停：摆弄道具、搓手指、摸下巴；身体蜷缩、步伐小而快；坐立不安是常态。`impression`

## (3) 台词

- 台词半吞半吐、语速快、自我纠正频繁；声音不高，靠细节取胜；愤怒时反而更轻更快。`impression`

## (4) 表情与眼神

- 眼神游移、突然直视；眉头紧锁、嘴角抽动；笑是尴尬的、短暂的。`impression`

## (5) 角色类型

- 常演角色：迷茫的青年（《毕业生》本杰明）；底层小人物（《午夜牛郎》拉佐）；离婚父亲（《克莱默夫妇》泰德）。
- 类型突破：从《毕业生》的迷茫青年到《克莱默夫妇》的离婚父亲，表演由外在的神经质转向内在的责任感；《雨人》演自闭症患者是类型突破。`artifact`
- 禁演类型：几乎不演高大硬汉、不演字正腔圆的英雄、不演不做准备的即兴。`impression`

## (6) 该演什么 / 不该演什么

- 该演：不安的手、半吞半吐的台词、游移的眼神、蜷缩的形体、细节堆积的真实。
- 不该演：高大硬汉、字正腔圆的英雄气、不做准备的即兴、表情过载。
- Negative prompt: `No tall tough-guy heroics, no theatrical declamation, no unprepared improvisation, no overacted expressions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Dustin Hoffman, a man buys oden at a convenience store late at night, fidgeting hands, half-swallowed lines, restless eyes, an ordinary man made extraordinary by detail`
- 中文对照：达斯汀·霍夫曼风格：一个男人深夜在便利店买关东煮，手不停，台词半吞半吐，眼神游移，一个靠细节变得不凡的普通人。
- Negative: `No tall tough-guy heroics, no theatrical declamation, no unprepared improvisation, no overacted expressions`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
