# Krzysztof Kieślowski — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Krzysztof Kieślowski: moral dilemmas in ordinary flats, chance encounters that change a life, the same event seen twice, metaphysical questions asked through small choices, an ending that opens rather than closes`
- ZH: 基耶斯洛夫斯基风格：普通公寓里的道德困境，改变一生的偶遇，同一件事看两遍，用小选择问形而上的问题，结尾是打开而不是合上。

## (2) 结构：三幕 / 序列 / 节拍

- 道德寓言结构：《十诫》为十个独立短篇，共用一栋公寓楼与一个旁观老人；三色三部曲各以一种理念为题，环形收束；《两生花》为双生平行结构，同一灵魂两种人生。每部多为三幕，但转折点常常是一个偶然（错过电梯、接错电话），中点是人物必须做一个无法两全的选择。

## (3) 对话

- 对白克制、日常，人物少说多做；关键信息藏在动作与重复出现的物件里；独白罕见，旁白不用。沉默与凝视常代替解释。

## (4) 人物弧光

- 主角多为普通人（医生、法官、音乐家遗孀），弧光是从确信到怀疑再到接受偶然：不是成长，是学会与不可解共处。人物关系是邻居、夫妻、陌生人之间的道德牵连；结局人物不被审判，只被照亮。

## (5) 类型套路与创新

- 类型：道德剧情；遵守套路——困境、选择、后果；打破的一条是：拒绝道德审判，善恶不分明。创新在剧本层面：用十诫、自由平等博爱等大命题作小叙事的骨架，用偶然作结构铰链。禁套路：不用说教收尾，不用巧合大团圆，不用类型反转。

## (6) 该写什么 / 不该写什么

- 该写：普通公寓与日常困境、偶然与平行人生、道德选择的两难、重复出现的物件与旁观者、打开式的结尾。
- 不该写：说教式收尾、巧合大团圆、类型反转、直白的道德结论、煽情配乐式高潮。
- Negative prompt: `No preachy ending, no coincidental happy reunion, no genre twist, no direct moral verdict, no sentimental climax`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Krzysztof Kieślowski, a woman buys oden at a convenience store late at night and meets a stranger who looks exactly like her dead sister. A small choice: speak or walk away. The ending opens, it does not close.`
- 中文对照：基耶斯洛夫斯基风格：一个女人深夜在便利店买关东煮，遇见一个长得像她去世妹妹的陌生人，一个小选择：开口还是走开，结尾是打开的。
- Negative: `No preachy ending, no coincidental happy reunion, no genre twist, no direct moral verdict, no sentimental climax`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
