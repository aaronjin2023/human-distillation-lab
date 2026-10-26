# Kakinomoto no Hitomaro — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hitomaro: Man'yoshu choka, long songs of longing and lament, the long night alone, mountain birds and trailing tails, five-seven rhythm rolling like waves, no ornament, ancient and vast`
- ZH: 人麻吕风格：万叶长歌，长夜独寝，山鸟长尾，五七调如波涛，抒情挽歌，绝无雕饰，古朴而辽阔。

## (2) 意象

- 主意象：长夜、山鸟、长歌、挽歌、明日香
- 辅意象：山、川、海、月、草
- 禁意象：华丽辞藻、都市繁华、直白议论
- 密度：疏密相间：长歌铺陈，意象古朴，一景一意
- 来源：奈良实景、山川、神话
`impression`

## (3) 韵律与句式

- 韵律：长歌（五七调长短句）与短歌（五七五七七）并用，长歌铺陈，短歌收束
- 句式：长句连写，五七调滚动，跨行连续，枕词起兴
- 节奏：缓慢辽阔，呼吸绵长，如波涛
`impression`

## (4) 语言密度与词汇

- 词汇：古朴词域：山鸟、长夜、明日香；动词多思、恋、泣、望；少华丽词
- 密度：每行信息量适中，一景一句，枕词即意义
- 禁词：华丽辞藻、都市繁华、直白议论、口语俗词
`impression`

## (5) 结构习惯

- 诗体：长歌 / 短歌；结构为枕词起兴 → 铺陈 → 挽歌收束
- 开头：以枕词直入（あしびきの山鳥の尾の）
- 结尾：以长夜独寝收束，不解释
- 视角：第一人称歌者
- 推进：枕词 → 铺陈 → 收束，层层见古
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 万叶长歌
- 五七调滚动
- 枕词起兴
- 长夜独寝
- 古朴收束
- 不该写：
- 华丽辞藻
- 都市繁华
- 直白议论
- 口语俗词
- 铺张排比
- Negative prompt: `No ornate diction, no urban bustle, no direct preaching, no colloquial diction, no lavish parallelism`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Kakinomoto no Hitomaro, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. Man'yoshu choka, long songs of longing and lament, the long night alone, mountain birds and trailing tails, five-seven rhythm rolling like waves, no ornament, ancient and vast`
- 中文对照：柿本人麻吕风格：一只约克夏犬深夜坐在地铁座位上，乘客们看着它。人麻吕风格：万叶长歌，长夜独寝，山鸟长尾，五七调如波涛，抒情挽歌，绝无雕饰，古朴而辽阔。
- Negative: `No ornate diction, no urban bustle, no direct preaching, no colloquial diction, no lavish parallelism`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
