# Sesshu Toyo — 园林风格规格 style.md（给图像模型）

> 只描述园林，不描述人生。引用造园理论著作时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sesshu Toyo, Muromachi ink-painting garden, a garden like a landscape painting in ink, rocks as mountains, white sand as water, pines, sparse and bold, the garden as a painting you can walk in`
- ZH: 雪舟等杨风格，室町水墨庭园，园如水墨山水画，石为山，白砂为水，松相映，疏朗而雄健，园为可行之画。

## (2) 空间布局

- 枯山水与池泉并用：石组为山，白砂为水，游线沿石组曲折；视线落在主石与远山；尺度疏朗，园如画卷，人在园中如在画中。`impression`

## (3) 水石植物

- 水：白砂代水，间以小池；石：立石为山，石形雄健，如水墨笔意；植物：松、苔为主，素雅；季相以秋色与雪景为高光。`impression`

## (4) 借景与框景

- 借景：借远山；框景以书院为框，框内取石与砂；对景以主石相望。`impression`

## (5) 材料与季节变化

- 材料：石、白砂、苔、松；季节：秋色与雪景为高光；光影：日光洒石，砂纹映光。`impression`

## (6) 该造什么 / 不该造什么

- 该造：石为山砂为水、水墨笔意的立石、松与苔、疏朗留白、借远山、园如水墨画。`artifact`
- 不该造：no symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded pavilions, no dense planting。
- Negative prompt: `No symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded pavilions, no dense planting`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Sesshu Toyo, a modern museum courtyard garden, rocks as mountains in ink-painting style, white sand as water, a few pines and moss, sparse and bold, a garden like a landscape painting you can walk in`
- 中文对照：雪舟等杨风格：现代美术馆庭院里的一座水墨园，石为山，白砂为水，松苔相映，疏朗雄健，园为可行之画。
- Negative: `No symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded pavilions, no dense planting`
- 检验点：园是否按第 (1) 节一句话风格成立；第 (6) 节母题是否出现；禁区写法是否未出现。
