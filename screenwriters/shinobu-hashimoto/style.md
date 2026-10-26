# Shinobu Hashimoto — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shinobu Hashimoto: rigorous plotting, a script built like a machine, honour tested to breaking point, a twist that reframes everything, silence before the sword`
- ZH: 桥本忍风格：严密如机器的情节，荣誉被考验到断裂点，一个翻转重构一切，刀出鞘前的沉默。

## (2) 结构：三幕 / 序列 / 节拍

- 严密三幕：第一幕一桩命案或一个武士的请愿切入，规则与荣誉交代清楚；第二幕多视角或层层调查推进，中点是一个翻转——人物动机全盘重估；第三幕决斗或审判，收束在沉默。时间跨度数日，多用审问与复述分段。

## (3) 对话

- 对白精确、克制，带武士与法庭的正式感；人物用陈述与追问推进，不靠抒情；潜台词是荣誉——没说出口的羞耻最重。

## (4) 人物弧光

- 主角多为武士、浪人、请愿者，弧光是从守规矩到看清规矩的虚伪：不是反叛，是终于说出真相。人物关系是武士与主君、证人与法官的对峙；结局人物不胜利，只留下真相。

## (5) 类型套路与创新

- 类型：武士片与法庭悬疑；遵守套路——命案、复述、决斗；打破的一条是：翻转不是为了惊奇，是为了重估荣誉。创新在剧本层面：把剧本写成严密的机器，每场只推进一格。禁套路：不用煽情独白，不用说教收尾，不用单一真相。

## (6) 该写什么 / 不该写什么

- 该写：严密的情节机器、多视角复述、翻转重估动机、荣誉与羞耻、沉默的收束。
- 不该写：煽情独白、说教式收尾、单一真相、直白的道德结论、让翻转只为惊奇。
- Negative prompt: `No sentimental monologue, no preachy ending, no single truth, no direct moral verdict, no twist for surprise alone`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Shinobu Hashimoto, a ronin buys oden at a convenience store late at night and asks, politely, for permission to die with honour. Every word is precise. Silence follows.`
- 中文对照：桥本忍风格：一个浪人深夜在便利店买关东煮，客气地请求体面地死去，每个词都精确，然后是沉默。
- Negative: `No sentimental monologue, no preachy ending, no single truth, no direct moral verdict`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
