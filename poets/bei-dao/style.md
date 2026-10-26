# Bei Dao — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bei Dao: Misty School verse,卑鄙 is the pass of the base and高尚 the epitaph of the noble, everything is fate and smoke, short lines like hammer blows, refusal without explanation, no softness, cold and clear`
- ZH: 北岛风格：朦胧诗，卑鄙是卑鄙者的通行证，高尚是高尚者的墓志铭，一切都是命运，一切都是烟云，短行如锤击，拒绝而不解释，绝无柔弱，冷峻而清明。

## (2) 意象

- 主意象：回答、一切、通行证、墓志铭、烟云
- 辅意象：命运、八月、梦游者、星空
- 禁意象：直白说教、铺张排比、温情小调
- 密度：疏朗：短行居多，一句一意，留白极大
- 来源：历史、命运、梦境
`impression`

## (3) 韵律与句式

- 韵律：现代自由体，短行居多，断行讲究，押韵自由
- 句式：短句如锤，长短交错，跨行跳跃，少倒装
- 节奏：冷峻短促，呼吸短促，顿挫在拒绝处
`impression`

## (4) 语言密度与词汇

- 词汇：冷峻词域：卑鄙、高尚、命运、烟云；动词多是、说、走、寻；少温情词
- 密度：每行信息量低，一句一意，留白极大
- 禁词：直白说教、铺张排比、温情小调、口语俗词
`impression`

## (5) 结构习惯

- 诗体：现代抒情短诗；结构为宣言起兴 → 层层否定 → 冷峻收束
- 开头：以宣言直入（卑鄙是卑鄙者的通行证）
- 结尾：以冷峻收束，不解释
- 视角：第一人称拒绝者
- 推进：宣言 → 否定 → 收束，层层见冷
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 卑鄙与高尚
- 一切都是
- 短行锤击
- 冷峻拒绝
- 留白极大
- 不该写：
- 直白说教
- 铺张排比
- 温情小调
- 口语俗词
- 解释说明
- Negative prompt: `No direct preaching, no lavish parallelism, no sentimental trifles, no colloquial diction, no explanation`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Bei Dao, a letter to oneself ten years from now. Misty School verse,卑鄙 is the pass of the base and高尚 the epitaph of the noble, everything is fate and smoke, short lines like hammer blows, refusal without explanation, no softness, cold and clear`
- 中文对照：北岛风格：一封写给十年后自己的信。北岛风格：朦胧诗，卑鄙是卑鄙者的通行证，高尚是高尚者的墓志铭，一切都是命运，一切都是烟云，短行如锤击，拒绝而不解释，绝无柔弱，冷峻而清明。
- Negative: `No direct preaching, no lavish parallelism, no sentimental trifles, no colloquial diction, no explanation`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
