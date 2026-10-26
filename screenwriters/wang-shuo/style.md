# Wang Shuo — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Shuo: Beijing banter, hooligan wit, authority mocked by wordplay, earnest feeling hidden under jokes, a rogue who refuses to grow up`
- ZH: 王朔风格：京味贫嘴，痞子式机智，权威被俏皮话消解，真情藏在玩笑底下，一个拒绝长大的混不吝。

## (2) 结构：三幕 / 序列 / 节拍

- 喜剧型三幕：第一幕北京胡同或大院切入，一群闲人靠嘴皮子过日子；第二幕一个馊主意（开公司、拍电影、冒充）把众人卷进麻烦，中点是玩笑开过了火；第三幕不靠圆满收束，靠一句自嘲或一场散伙收束。时间跨度数周至数月，多用北京口语场景串联。

## (3) 对话

- 对白京味贫嘴、快语速、抢白，俏皮话密度极高；反讽与调侃是主要武器；真情只在极少数时刻直言，且立刻被玩笑盖住。动作描写简洁，多写胡同、饭馆、街头。

## (4) 人物弧光

- 主角多为北京闲人、顽主、文艺青年，弧光是从混不吝到一瞬间的认真：不是成长，是终于有一句话是真的。人物关系是哥们儿圈子与权威（单位、家长、体制）的调侃式对抗；结局人物不改行，只改一句台词。

## (5) 类型套路与创新

- 类型：京味喜剧与青春片；遵守套路——哥们儿、馊主意、散伙；打破的一条是：拒绝主旋律与煽情，幽默即立场。创新在剧本层面：把北京口语的贫嘴写成结构性的反讽。禁套路：不用说教收尾，不用煽情和解，不用英雄主义。

## (6) 该写什么 / 不该写什么

- 该写：京味贫嘴与哥们儿圈子、馊主意与散伙、调侃权威、玩笑底下的真情、自嘲式收束。
- 不该写：说教式收尾、煽情和解、英雄主义、直白的政治结论、让主角突然正经长大。
- Negative prompt: `No preachy ending, no sentimental reconciliation, no heroism, no direct political verdict, no hero who suddenly grows up straight`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Wang Shuo, a Beijing idler buys oden at a convenience store late at night and banters with the clerk about who owes whom. Jokes all the way down, until one true sentence slips out.`
- 中文对照：王朔风格：一个北京闲人深夜在便利店买关东煮，跟店员贫嘴谁欠谁的，一路玩笑，直到滑出一句真话。
- Negative: `No preachy ending, no sentimental reconciliation, no heroism, no direct political verdict`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
