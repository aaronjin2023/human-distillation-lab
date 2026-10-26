# Ai Qing — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ai Qing: modern free verse of the land, earth and sun and sea, plain words carrying deep feeling, long lines breathing like the earth, love of the land without ornament, no obscurity, sincere and enduring`
- ZH: 艾青风格：现代自由体，土地、太阳、大海，朴素词语承载深情，长行如大地呼吸，爱土地而不加修饰，绝无晦涩，真挚而深沉。

## (2) 意象

- 主意象：土地、太阳、大海、礁石、大堰河
- 辅意象：雪、黎明、吹号者、北方
- 禁意象：晦涩用典、华丽堆砌、轻佻小调
- 密度：疏朗：意象朴素，一景一意，情感深沉
- 来源：北方大地、太阳、海洋
`impression`

## (3) 韵律与句式

- 韵律：现代自由体，行长参差，断行自然，押韵自由
- 句式：长行连写，短句间插，跨行连续，少倒装
- 节奏：缓慢深沉，呼吸绵长，如大地呼吸
`impression`

## (4) 语言密度与词汇

- 词汇：朴素词域：土地、太阳、大海、雪；动词多爱、望、吹、立；少僻字
- 密度：每行信息量适中，一景一句，情感在末句点出
- 禁词：晦涩用典、华丽堆砌、轻佻小调、口语俗词
`impression`

## (5) 结构习惯

- 诗体：现代抒情长诗 / 短诗；结构为意象起兴 → 层层铺写 → 深情收束
- 开头：以土地意象直入（假如我是一只鸟）
- 结尾：以深情收束（为什么我的眼里常含泪水）
- 视角：第一人称土地之子
- 推进：意象 → 铺写 → 深情，层层加深
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 土地太阳
- 朴素深情
- 自由体长行
- 意象沉实
- 真挚收束
- 不该写：
- 晦涩用典
- 华丽堆砌
- 轻佻小调
- 口语俗词
- 直白说教
- Negative prompt: `No obscure allusions, no ornate piling-up, no frivolous trifles, no colloquial diction, no direct preaching`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ai Qing, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. modern free verse of the land, earth and sun and sea, plain words carrying deep feeling, long lines breathing like the earth, love of the land without ornament, no obscurity, sincere and enduring`
- 中文对照：艾青风格：一只约克夏犬深夜坐在地铁座位上，乘客们看着它。艾青风格：现代自由体，土地、太阳、大海，朴素词语承载深情，长行如大地呼吸，爱土地而不加修饰，绝无晦涩，真挚而深沉。
- Negative: `No obscure allusions, no ornate piling-up, no frivolous trifles, no colloquial diction, no direct preaching`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
