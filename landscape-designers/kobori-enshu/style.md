# Kobori Enshu — 园林风格规格 style.md（给图像模型）

> 只描述园林，不描述人生。引用造园理论著作时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kobori Enshu, Edo daimyo garden, elegant and grand, a pond as the centre, islands and bridges, borrowed mountains, refined and spacious, the garden as a noble's poem`
- ZH: 小堀远州风格，江户大名庭园，雅致而宏大，池为中心，岛屿桥梁，借远山，精致开阔，园为贵族之诗。

## (2) 空间布局

- 池泉回游式大布局：大池为中心，岛屿、桥梁散布，建筑沿池布列；游线环池曲折，视线落在池中岛与借山；尺度宏大，园如贵族诗卷。`artifact`

## (3) 水石植物

- 水：大池、溪流，水面开阔；石：立石为岛为峰，石组取自然之势；植物：松、枫、樱、苔，季相以春樱秋枫为高光。`artifact`

## (4) 借景与框景

- 借景：借比睿山、借远峰；框景以书院、茶室为框；对景以池中岛相望。`artifact`

## (5) 材料与季节变化

- 材料：石、苔、水、松、木；季节：春樱秋枫为高光；光影：日光洒水面。`artifact`

## (6) 该造什么 / 不该造什么

- 该造：池泉回游、池中岛屿、石桥与土桥、借比睿山、春樱秋枫、大名庭园的雅致。`artifact`
- 不该造：no symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded pavilions, no flat empty lawn。
- Negative prompt: `No symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded pavilions, no flat empty lawn`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Kobori Enshu, a modern university campus garden, a large pond with wooded islets and arched bridges, borrowed distant hills, pines, cherries and maples, a winding path around the water, elegant and spacious`
- 中文对照：小堀远州风格：现代大学校园里的一座大园，大池配林岛与拱桥，借远山，松樱枫相映，环水曲径，雅致开阔。
- Negative: `No symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded pavilions, no flat empty lawn`
- 检验点：园是否按第 (1) 节一句话风格成立；第 (6) 节母题是否出现；禁区写法是否未出现。
