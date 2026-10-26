# Harold Pinter — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Harold Pinter: menace in the pause, power shifting with every sentence, ordinary rooms turning into interrogation chambers, the past that will not stay past`
- ZH: 品特风格：停顿里藏着威胁，每句话都在转移权力，日常房间变成审讯室，过去不肯过去。

## (2) 结构：三幕 / 序列 / 节拍

- 两幕式密室结构：一个外来者进入封闭空间，权力天平缓慢倾斜。激励事件往往是一句看似无害的问话；中点是某人说出与先前说法矛盾的往事；结尾不解决，只留下一个更冷的停顿。时间多为单日或数日，闪回只以对白里的互相矛盾的回忆出现，从不以画面闪回确证真相。

## (3) 对话

- 对白短促、重复、抢白，停顿与沉默是台词的一部分；潜台词占比极高，人物用日常寒暄互相试探、威胁、否认。动作描写极少，几乎全靠对白推进；独白罕见，旁白不用。

## (4) 人物弧光

- 主角多为局外人或闯入者（仆人、情人、归来者），弧光不是成长而是权力位置的翻转：起初弱势者最后掌控房间，或起初掌控者最后被自己的谎言困住。人物关系是二人或三人的权力三角；结局人物不改变，改变的是谁说了算。

## (5) 类型套路与创新

- 类型：心理惊悚与室内剧；遵守类型套路——封闭空间、陌生人、秘密；打破的一条是：从不揭晓真相，悬念不靠信息差靠权力差。创新在剧本层面：把停顿写进剧本（Pause / Silence 成为舞台指示），让省略本身成为情节。禁套路：不用直白解释动机，不用闪回定案，不用道德审判式收尾。

## (6) 该写什么 / 不该写什么

- 该写：密室与二人权力博弈、停顿、沉默与重复句式、互相矛盾的往事叙述、日常问话里的威胁、戛然而止的冷结尾。
- 不该写：直白解释人物动机、用闪回确证真相、道德审判式收尾、煽情和解、功能性 exposition 对白。
- Negative prompt: `No on-the-nose exposition of motive, no flashback that settles the truth, no moralising verdict, no sentimental reconciliation, no explanatory monologue`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Harold Pinter, a man buys oden at a convenience store late at night. A stranger asks him three questions about where he has been. Each answer contradicts the last. Long pauses. Nothing is explained.`
- 中文对照：品特风格：一个男人深夜在便利店买关东煮，一个陌生人问他去过哪里，三次回答互相矛盾，停顿很长，什么都不解释。
- Negative: `No on-the-nose exposition, no flashback that settles the truth, no moralising verdict, no sentimental reconciliation`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
