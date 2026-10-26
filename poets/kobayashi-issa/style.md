# Kobayashi Issa — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kobayashi Issa: haiku of the common and the small, a parentless sparrow invited to play, the world of dew and yet, compassion in seventeen sounds, no grandeur, warm and plain`
- ZH: 一茶风格：俳句写小，亲のない雀邀来同游，露之世而さりながら，十七音中见慈悲，绝无宏大，温暖而素朴。

## (2) 意象

- 主意象：露之世、雀、亲、我之春
- 辅意象：蛙、月、雪、旅
- 禁意象：抽象议论、长句铺排、豪放壮语
- 密度：极疏朗：一句一景，一字一意，留白极大
- 来源：日常小物、四季、庶民生活
`impression`

## (3) 韵律与句式

- 韵律：俳句（五七五），季语必备，切字一断，口语入句
- 句式：短句极短，五七五音数，一句即全篇，口语自然
- 节奏：一息之暖，呼吸一顿，切字处断开
`impression`

## (4) 语言密度与词汇

- 词汇：素朴词域：露、雀、蛙、月；动词多游、来、思；少抽象词
- 密度：每行信息量极低，一字一意
- 禁词：抽象议论、长句铺排、豪放壮语、华丽辞藻
`impression`

## (5) 结构习惯

- 诗体：俳句（五七五）；结构为季语起兴 → 小物 → 切字收束
- 开头：以小物直入（我と来て遊べや）
- 结尾：以切字收束，不解释
- 视角：第一人称庶民，偶以雀对话
- 推进：季语 → 小物 → 收束，一息而成
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 露之世
- 亲のない雀
- 五七五音数
- 口语入句
- 一息之暖
- 不该写：
- 抽象议论
- 长句铺排
- 豪放壮语
- 华丽辞藻
- 解释说明
- Negative prompt: `No abstract discourse, no long explanatory lines, no grand heroic diction, no ornate diction, no explanation`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Kobayashi Issa, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. haiku of the common and the small, a parentless sparrow invited to play, the world of dew and yet, compassion in seventeen sounds, no grandeur, warm and plain`
- 中文对照：小林一茶风格：一只约克夏犬深夜坐在地铁座位上，乘客们看着它。一茶风格：俳句写小，亲のない雀邀来同游，露之世而さりながら，十七音中见慈悲，绝无宏大，温暖而素朴。
- Negative: `No abstract discourse, no long explanatory lines, no grand heroic diction, no ornate diction, no explanation`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
