# Wang Wei — 园林风格规格 style.md（给图像模型）

> 只描述园林，不描述人生。引用造园理论著作时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Wei, Tang literati garden, poetry in landscape, misty mountains and still water, pines and clear springs, empty and quiet, a poem made into a garden`
- ZH: 王维风格，唐代文人园林，诗中有画，烟雾山水与静水，松与清泉，空寂幽静，诗化为园。

## (2) 空间布局

- 自然不对称布局，山水为主、建筑为客；辋川二十景以一景一诗串联，游线沿溪谷曲折，视线落点在远山与水面；尺度宏大而意境空灵，人小景大，咫尺山林而有千里之势。`artifact`

## (3) 水石植物

- 水：清泉、溪流、静潭，水面平静如镜，驳岸自然土石；石：远山为石，园内少叠假山，以真山为骨；植物：松、竹为主，配以清泉边的野花，素雅无浓艳花坛；季相以秋月与春泉为高光。`artifact`

## (4) 借景与框景

- 借景为主：借远山、借云雾、借月光；框景以茅亭、柴门为框，框内取一山一水；对景少而精，一景只取一意，不堆叠。`artifact`

## (5) 材料与季节变化

- 材料：茅屋、土墙、木桥、石径，取材天然、做旧自然；季节：秋月最胜，春泉次之，夏绿冬雪皆为留白；光影：月光与水光为主，阴影淡而远，不用浓黑。`impression`

## (6) 该造什么 / 不该造什么

- 该造：辋川二十景的一景一诗、清泉与静潭、松间明月、远山借景、茅亭柴门、溪谷曲折游线。`artifact`
- 不该造：no symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded pavilions, no ornate rockery。
- Negative prompt: `No symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded pavilions, no ornate rockery`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Wang Wei, a small rooftop garden in a modern city, a still pond with a clear spring, pines and bamboo, a thatched pavilion half-hidden in mist, distant towers borrowed as far mountains, quiet and empty, poetry in landscape`
- 中文对照：王维风格：现代城市里的一座小屋顶花园，一泓静池与清泉，松竹掩映，茅亭半隐于雾中，远处高楼借作远山，空寂幽静，诗中有画。
- Negative: `No symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded pavilions, no ornate rockery`
- 检验点：园是否按第 (1) 节一句话风格成立；第 (6) 节母题是否出现；禁区写法是否未出现。
