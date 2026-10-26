# Wang Xianchen — 园林风格规格 style.md（给图像模型）

> 只描述园林，不描述人生。引用造园理论著作时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Xianchen, Ming Jiangnan private garden, the Humble Administrator's Garden, a great pond with forested islets, water first, pavilions half-hidden, natural and spacious, a retired official's garden`
- ZH: 王献臣风格，明代江南私家园林，拙政园，大池林岛，水为主，亭榭半隐，自然开阔，退官归隐之园。

## (2) 空间布局

- 以水为中心的大布局：中部大池占园近半，水面开阔，林岛散布；建筑沿水布列，游线环水曲折；视线落在水面与远亭；尺度开阔，园如湖上林野。`artifact`

## (3) 水石植物

- 水：大池、曲溪，水面占比高，驳岸自然土石间以湖石；石：湖石点缀水边与岛上，不做高大假山；植物：松、竹、荷、柳，水生植物为主，季相以夏荷与秋色为高光。`artifact`

## (4) 借景与框景

- 借景：借北寺塔、借远处水天；框景以亭廊门窗为框，框内取水与岛；对景以水中岛屿为对景。`artifact`

## (5) 材料与季节变化

- 材料：湖石、木、竹、粉墙黛瓦；季节：夏荷最胜，春秋亦佳，冬雪留白；光影：水光为主，日光洒水面。`artifact`

## (6) 该造什么 / 不该造什么

- 该造：中部大池、水中林岛、荷与柳、临水亭榭、环水曲径、北寺塔借景。`artifact`
- 不该造：no symmetrical axis, no tall rockery mountains, no large geometric flower beds, no bright heavy colours, no crowded pavilions。
- Negative prompt: `No symmetrical axis, no tall rockery mountains, no large geometric flower beds, no bright heavy colours, no crowded pavilions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Wang Xianchen, a modern urban wetland park, a great pond with wooded islets, lotus and willows, waterside pavilions half-hidden by trees, a winding path around the water, a distant tower borrowed as a landmark, natural and spacious`
- 中文对照：王献臣风格：现代城市里的一座湿地公园，大池配林岛，荷柳相映，临水亭榭半隐，环水曲径，远塔借景，自然开阔。
- Negative: `No symmetrical axis, no tall rockery mountains, no large geometric flower beds, no bright heavy colours, no crowded pavilions`
- 检验点：园是否按第 (1) 节一句话风格成立；第 (6) 节母题是否出现；禁区写法是否未出现。
