# Leonardo DiCaprio — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Leonardo DiCaprio: intense boyish charm hardened into obsession, restless energy, a face that runs toward danger, commitment that borders on endurance`
- ZH: 莱昂纳多·迪卡普里奥风格：强烈的少年魅力硬化为执念，不安的能量，一张向危险奔去的脸，近乎忍耐的投入。

## (2) 形体

- 动作快而有力，奔跑、攀爬、搏斗皆以真实体能完成；静止时肩膀前倾、像随时会冲出去；晚年以胡须与体重改造形体。`impression`

## (3) 台词

- 音色清亮、语速快；台词带点急促的真诚；愤怒时声音升高、咬字更重。`impression`

## (4) 表情与眼神

- 眼神直视、带着渴望；眉头紧锁、嘴角下撇；笑是短暂的、带点少年气的。`impression`

## (5) 角色类型

- 常演角色：浪漫的少年（杰克）；偏执的野心家（休斯）；忍耐的幸存者（格拉斯）。
- 类型突破：从《泰坦尼克号》的浪漫少年到《荒野猎人》的幸存者，表演由魅力转向忍耐；《飞行家》的偏执是中间形态。`artifact`
- 禁演类型：几乎不演温吞的旁观者、不演不投入的轻浮主角。`impression`

## (6) 该演什么 / 不该演什么

- 该演：不安的能量、向危险奔去的形体、急促真诚的台词、直视渴望的眼神、近乎忍耐的投入。
- 不该演：温吞的旁观者、不投入的轻浮主角、字正腔圆的舞台腔、表情过载。
- Negative prompt: `No lukewarm bystander roles, no uncommitted pretty-boy leads, no theatrical declamation, no overacted expressions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Leonardo DiCaprio, a man buys oden at a convenience store late at night, restless energy, running toward danger, commitment bordering on endurance`
- 中文对照：莱昂纳多·迪卡普里奥风格：一个男人深夜在便利店买关东煮，不安的能量，向危险奔去，近乎忍耐的投入。
- Negative: `No lukewarm bystander roles, no uncommitted pretty-boy leads, no theatrical declamation, no overacted expressions`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
