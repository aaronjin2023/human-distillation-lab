# Al Pacino — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Al Pacino: volcanic Method intensity, voice that whispers then explodes, eyes that burn, a man who starts quiet and ends shouting the truth`
- ZH: 阿尔·帕西诺风格：火山式的方法派强度，声音先低语后爆发，眼神灼人，一个从安静开始、以咆哮说出真相的人。

## (2) 形体

- 身体先收后放：开场蜷缩、静止，爆发时全身弹起、手势大开大合；走路时肩膀前倾、步伐急促。`impression`

## (3) 台词

- 音色沙哑、语速忽快忽慢；低语与咆哮交替，咆哮是顶点、只用一次；台词常重复关键词。`impression`

## (4) 表情与眼神

- 眼神灼人、直视不回避；眉头紧锁、嘴角下撇；笑是短暂的、带点疯狂的。`impression`

## (5) 角色类型

- 常演角色：黑帮继承人（迈克尔·柯里昂）；走投无路的劫匪（桑尼）；失明的退伍军官（弗兰克）。
- 类型突破：从《教父》的克制迈克尔到《闻香识女人》的咆哮弗兰克，表演由收转放；晚年舞台与电影并行，咆哮成为标志也被批评为程式化。`artifact`
- 禁演类型：几乎不演温吞的旁观者、不演不爆发的中庸角色。`impression`

## (6) 该演什么 / 不该演什么

- 该演：低语后爆发的声音、灼人的眼神、先收后放的形体、重复关键词的台词、顶点只用一次的咆哮。
- 不该演：温吞的旁观者、不爆发的平庸处理、字正腔圆的舞台腔、表情过载的常态化。
- Negative prompt: `No lukewarm bystander roles, no flat uninflected delivery, no theatrical declamation, no constant overacting`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Al Pacino, a small Yorkshire terrier sits on a subway seat, whispering then exploding, eyes that burn, quiet at first and shouting the truth at the end`
- 中文对照：阿尔·帕西诺风格：一只约克夏犬坐在地铁座位上，先低语后爆发，眼神灼人，开场安静、结尾咆哮着说出真相。
- Negative: `No lukewarm bystander roles, no flat uninflected delivery, no theatrical declamation, no constant overacting`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
