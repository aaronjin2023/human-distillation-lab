# Ji Cheng — 园林风格规格 style.md（给图像模型）

> 只描述园林，不描述人生。引用造园理论著作时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ji Cheng, Ming garden theory, though made by man, as if created by heaven, borrowed scenery, winding paths, rockery and pond in natural asymmetry, pavilions half-hidden by trees, white walls and grey tiles, poetic`
- ZH: 计成风格，明代造园理论，虽由人作，宛自天开，借景，曲径，叠山理水自然不对称，亭榭半隐于树，白墙黛瓦，诗意盎然。

## (2) 空间布局

- 自然不对称，小中见大；相地合宜，立意先行；游线曲折，步移景异；分区以隔与透为法，主景池与主峰相望；尺度以小见大，咫尺山林。`artifact`（《园冶》）

## (3) 水石植物

- 水：池、溪、泉，水面曲折，驳岸自然石岸；石：叠山以湖石、黄石为主，石多留土、土多点石，主峰次峰相配；植物：松、竹、梅、枫，留白处铺苔，不种浓艳大花；季相以秋枫与雨后苔色为高光。`artifact`（《园冶》）

## (4) 借景与框景

- 借景为本体：借远山、借塔、借水、借邻园，借景开口须遮挡得法；框景以门洞、窗洞、廊柱为框；对景与障景并用，隔与透相生。`artifact`（《园冶》）

## (5) 材料与季节变化

- 材料：石、木、竹、砖、瓦，取材天然、做旧自然；季节：秋枫最胜，雨后苔色次之，四季皆有景；光影：日光、月光、倒影、水光，阴影以树影水影代浓黑。`artifact`（《园冶》）

## (6) 该造什么 / 不该造什么

- 该造：虽由人作，宛自天开、借景、隔与透、曲径步移景异、池与主峰、白墙黛瓦半隐亭榭、松竹梅枫与苔。`artifact`
- 不该造：no symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded ornaments, no tall artificial mountains。
- Negative prompt: `No symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded ornaments, no tall artificial mountains`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ji Cheng, a small rooftop garden in a modern city, borrowed scenery of distant towers, winding path, a pond with one rockery peak, pavilion half-hidden by bamboo, white walls, grey tiles, poetic, though made by man, as if created by heaven`
- 中文对照：计成风格：现代城市里的一座小屋顶花园，借远处高楼为景，曲径通幽，一池一峰，竹掩亭榭，白墙黛瓦，诗意盎然，虽由人作，宛自天开。
- Negative: `No symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded ornaments, no tall artificial mountains`
- 检验点：园是否按第 (1) 节一句话风格成立；第 (6) 节母题是否出现；禁区写法是否未出现。
