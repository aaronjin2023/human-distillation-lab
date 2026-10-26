# Joel Coen — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joel Coen (with Ethan Coen): a small crime that unravels by geometry, deadpan Midwestern politeness over blood, fate as a coin toss, dialogue that is funny precisely because no one is joking`
- ZH: 乔尔·科恩风格（与伊桑·科恩合著）：一桩小罪按几何学 unravel，血腥之上的明尼苏达式客气，命运如抛硬币，对白好笑正因为没人开玩笑。

## (2) 结构：三幕 / 序列 / 节拍

- 犯罪几何学：一个小计划（绑架、找钱、换包）按连锁反应失控；三幕之间用‘巧合’而非‘动机’推进；结局不是正义伸张，而是命运收网；《老无所依》连高潮都拒绝交付。`impression`

## (3) 对话

- 对白是方言与死板的礼貌：明尼苏达口音、‘yah’、重复与纠正；人物一本正经地说荒唐话，喜剧来自语气与内容的错位；潜台词藏在客气话后面。`impression`

## (4) 人物弧光

- 主角类型：贪小便宜的普通人、追钱的杀手、被命运选中的倒霉蛋；弧光多是‘堕落’或‘原地打转’：小人物越挣扎陷得越深，世界没有变，人物也没有得救。`impression`

## (5) 类型套路与创新

- 类型：犯罪 / 黑色喜剧 / 西部，遵守‘小罪酿大祸’的套路；创新是把命运写成几何与巧合，把喜剧写进血腥里。禁套路：不用煽情救赎，不用直白的道德评判。`impression`

## (6) 该写什么 / 不该写什么

- 该写：小计划按连锁反应失控、方言与死板的礼貌、巧合推进情节、血腥中的冷幽默、命运收网式结局。
- 不该写：煽情救赎、直白道德评判、主角靠聪明翻盘、解释动机的长独白。
- Negative prompt: `No sentimental redemption, no direct moral judgement, no clever hero who outsmarts fate, no explanatory monologue about motive, no warm reassurance`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Joel Coen (with Ethan Coen), a small Yorkshire terrier sits on a subway seat and a man with a plan to steal a dog ends up stealing the wrong dog, then the wrong bag, then the wrong life. Polite dialogue, deadpan, a coin toss decides it. No redemption.`
- 中文对照：乔尔·科恩风格（与伊桑·科恩合著）：一只约克夏犬坐在地铁座位上，一个想偷狗的男人偷错了狗，又偷错了包，又偷错了人生。客气的对白，面无表情，抛硬币决定结局。没有救赎。
- Negative: `No sentimental redemption, no direct moral judgement, no clever hero who outsmarts fate, no explanatory monologue about motive, no warm reassurance`
- 检验点：结构、对白、人物弧光与收束是否符合本编剧的风格；禁区写法是否出现。
