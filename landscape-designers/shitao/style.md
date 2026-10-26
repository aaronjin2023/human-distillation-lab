# Shitao — 园林风格规格 style.md（给图像模型）

> 只描述园林，不描述人生。引用造园理论著作时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shitao, Qing rockery and painter's garden, one stroke contains all, strange rocks and wild pines, a garden like a painting, free and searching, the rockery as calligraphy`
- ZH: 石涛风格，清代叠山与画家造园，一画含万法，奇石野松，园如画，自由而求索，叠山如书法。

## (2) 空间布局

- 自然不对称，以假山为中心，水池环山；游线穿山入洞，视线落在峰石与松影；尺度以山为园，园如画卷，人在园中如在画中。`impression`

## (3) 水石植物

- 水：池环山脚，水面曲折；石：湖石、黄石叠山，石形奇崛，如书法笔意；植物：松、竹、梅、枫，野趣为主；季相以秋枫与雨后石色为高光。`impression`

## (4) 借景与框景

- 借景：借远山、借塔；框景以洞口、门窗为框；对景以峰峦相望。`impression`

## (5) 材料与季节变化

- 材料：湖石、黄石、木、竹；季节：秋枫最胜，四季皆有画意；光影：日光洒峰，洞内光暗相映。`impression`

## (6) 该造什么 / 不该造什么

- 该造：一画含万法、奇石如书法、片石山房、野松与枫、山中洞壑、园如画卷。`artifact`
- 不该造：no symmetrical axis, no flat lawn rockery, no large geometric flower beds, no bright heavy colours, no crowded pavilions。
- Negative prompt: `No symmetrical axis, no flat lawn rockery, no large geometric flower beds, no bright heavy colours, no crowded pavilions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Shitao, a modern sculpture park built as a walk-through rockery, strange calligraphic rocks piled into peaks, wild pines and maples, a pond around the foot, caves to walk through, a garden like a painting, free and searching`
- 中文对照：石涛风格：现代雕塑公园，一座可穿行的叠山，奇石如书法笔意，野松枫相映，池环山脚，洞壑可游，园如画，自由而求索。
- Negative: `No symmetrical axis, no flat lawn rockery, no large geometric flower beds, no bright heavy colours, no crowded pavilions`
- 检验点：园是否按第 (1) 节一句话风格成立；第 (6) 节母题是否出现；禁区写法是否未出现。
