# Matsuo Basho — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Matsuo Basho: haiku of seventeen sounds, an old pond and a frog's splash, summer grass and soldiers' dreams, one season-word and one cut, the world in a breath, no abstraction, still and vast`
- ZH: 芭蕉风格：俳句十七音，古池蛙跳，夏草兵梦，一季语一切字，世界在一息之中，绝无抽象，静而辽阔。

## (2) 意象

- 主意象：古池、蛙、夏草、季语、切字
- 辅意象：兵梦、月、雪、旅
- 禁意象：抽象议论、长句铺排、华丽辞藻
- 密度：极疏朗：一句一景，一字一意，留白极大
- 来源：旅途实景、四季、自然
`impression`

## (3) 韵律与句式

- 韵律：俳句（五七五），季语必备，切字一断
- 句式：短句极短，五七五音数，一句即全篇
- 节奏：一息之静，呼吸一顿，切字处断开
`impression`

## (4) 语言密度与词汇

- 词汇：极简词域：古池、蛙、夏草；动词多飞、跳、梦；少抽象词
- 密度：每行信息量极低，一字一意
- 禁词：抽象议论、长句铺排、华丽辞藻、口语俗词
`impression`

## (5) 结构习惯

- 诗体：俳句（五七五）；结构为季语起兴 → 一景 → 切字收束
- 开头：以季语直入（古池や）
- 结尾：以切字收束，不解释
- 视角：第一人称旅者，偶隐去人称
- 推进：季语 → 一景 → 收束，一息而成
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 古池蛙跳
- 季语切字
- 五七五音数
- 一息之静
- 旅途实景
- 不该写：
- 抽象议论
- 长句铺排
- 华丽辞藻
- 口语俗词
- 解释说明
- Negative prompt: `No abstract discourse, no long explanatory lines, no ornate diction, no colloquial diction, no explanation`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Matsuo Basho, a letter to oneself ten years from now. haiku of seventeen sounds, an old pond and a frog's splash, summer grass and soldiers' dreams, one season-word and one cut, the world in a breath, no abstraction, still and vast`
- 中文对照：松尾芭蕉风格：一封写给十年后自己的信。芭蕉风格：俳句十七音，古池蛙跳，夏草兵梦，一季语一切字，世界在一息之中，绝无抽象，静而辽阔。
- Negative: `No abstract discourse, no long explanatory lines, no ornate diction, no colloquial diction, no explanation`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
