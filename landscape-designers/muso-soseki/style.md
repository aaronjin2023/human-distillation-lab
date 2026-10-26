# Muso Soseki — 园林风格规格 style.md（给图像模型）

> 只描述园林，不描述人生。引用造园理论著作时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Muso Soseki, Kamakura-Muromachi Zen garden, moss temple garden, a pond as the mind, islands as the Pure Land, borrowed mountains, quiet and profound, the garden as meditation`
- ZH: 梦窗疏石风格，镰仓至室町禅庭，苔寺之园，池即心，岛即净土，借远山，幽静深邃，园即禅修。

## (2) 空间布局

- 池泉回游式布局：大池为中心，岛屿散布，游线环池曲折；主景为池中岛与借山；尺度开阔而幽静，人在园中如在净土。`artifact`

## (3) 水石植物

- 水：大池、溪流，水面静，驳岸自然石岸；石：立石为岛为峰，石组取自然之势；植物：苔、枫、松为主，苔为地被，季相以秋枫与苔色为高光。`artifact`

## (4) 借景与框景

- 借景：借嵐山远峰、借天龙寺后山；框景以方丈、书院为框，框内取池与岛；对景以池中岛与远山相望。`artifact`

## (5) 材料与季节变化

- 材料：石、苔、水、木，取材天然；季节：秋枫最胜，苔色四季；光影：日光透树，水光映苔。`artifact`

## (6) 该造什么 / 不该造什么

- 该造：池泉回游、苔寺苔地、池中净土岛、借嵐山远峰、枫与苔、立石成峰。`artifact`
- 不该造：no symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded pavilions, no flat empty lawn。
- Negative prompt: `No symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded pavilions, no flat empty lawn`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Muso Soseki, a modern hospital healing garden, a large still pond with wooded islets, moss ground, maples, borrowed distant hills, a quiet path around the water, the garden as meditation`
- 中文对照：梦窗疏石风格：现代医院里的一座疗愈园，大池配林岛，苔地铺展，枫影相映，借远山，环水静径，园即禅修。
- Negative: `No symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded pavilions, no flat empty lawn`
- 检验点：园是否按第 (1) 节一句话风格成立；第 (6) 节母题是否出现；禁区写法是否未出现。
