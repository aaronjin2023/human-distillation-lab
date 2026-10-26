# Wong Kar-wai — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wong Kar-wai: Hong Kong at 2 a.m., lovers who miss each other by minutes, time stamped on every can of pineapple, longing in voiceover, a mood that outlasts plot`
- ZH: 王家卫风格：凌晨两点的香港，恋人擦肩而过只差几分钟，每个凤梨罐头都标着时间，画外音里的思念，情绪比情节留得更久。

## (2) 结构：三幕 / 序列 / 节拍

- 情绪型结构而非三幕：以时间标记与偶遇组织全片；《阿飞正传》为数段式，《重庆森林》为两个平行故事，《花样年华》为邻居之间的克制试探。转折点不是事件而是时间过期（罐头过期、租约到期）；结尾常常是一个人独白，另一个人已经走了。

## (3) 对话

- 对白少而精，多为画外音独白与短促对话；人物用时间、数字、食物说话；潜台词是错过——没说出口的比说出口的多。动作描写多写钟表、食物、街道、雨。

## (4) 人物弧光

- 主角多为都市男女，弧光是从渴望到错过再到怀念：不是成长，是学会与错过共处。人物关系是擦肩的恋人、邻居、警察与空姐；结局人物不在一起，只各自怀念。

## (5) 类型套路与创新

- 类型：都市爱情与情绪片；遵守套路——相遇、错过、怀念；打破的一条是：情节几乎可以没有，情绪即结构。创新在剧本层面：把时间标记（过期、倒数）写成结构铰链，让画外音承担叙事。禁套路：不用直白表白，不用大团圆，不用解释性对白。

## (6) 该写什么 / 不该写什么

- 该写：凌晨的香港与时间标记、擦肩而过的恋人、画外音独白、过期与倒数、怀念的收束。
- 不该写：直白表白、大团圆、解释性对白、类型反转、让人物说清自己的感受。
- Negative prompt: `No direct love declaration, no happy reunion, no explanatory dialogue, no genre twist, no character who explains their own feelings`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Wong Kar-wai, a man buys oden at a convenience store at 2 a.m. and realises the woman he missed was here one minute ago. Voiceover, clocks, steam. He buys two portions anyway.`
- 中文对照：王家卫风格：一个男人凌晨两点在便利店买关东煮，发现错过的女人一分钟前刚来过，画外音、钟表、蒸汽，他还是买了两份。
- Negative: `No direct love declaration, no happy reunion, no explanatory dialogue, no genre twist`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
