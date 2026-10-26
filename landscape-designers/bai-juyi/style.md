# Bai Juyi — 园林风格规格 style.md（给图像模型）

> 只描述园林，不描述人生。引用造园理论著作时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bai Juyi, Tang literati garden, plain and approachable, a thatched cottage by a stream, pines and bamboo, clear water and simple paths, leisurely and humane, poetry for everyday life`
- ZH: 白居易风格，唐代文人园林，平易近人，溪边草堂，松竹相伴，清水简径，闲适有人情味，诗为日常生活而作。

## (2) 空间布局

- 自然不对称，小中见大；草堂为中心，溪流环绕，游线短而曲，视线落在近水与远山之间；尺度亲切，园如家居，人在园中如在家中。`artifact`

## (3) 水石植物

- 水：溪流、清池，水面小而清，驳岸土石自然；石：少叠假山，以溪石点缀；植物：松、竹、柳为主，配以野花药草，素雅；季相以春草与秋月为高光。`artifact`

## (4) 借景与框景

- 借景：借庐山远峰、借溪水；框景以草堂门窗为框，框内取溪与竹；对景取近景，不取宏大。`impression`

## (5) 材料与季节变化

- 材料：茅草、木、竹、土墙，极简朴；季节：春草最胜，夏荫秋月冬雪皆宜；光影：日光柔和，水光清亮，阴影淡。`impression`

## (6) 该造什么 / 不该造什么

- 该造：溪边草堂、松竹柳、清溪与小池、简径与木桥、野花药草、庐山远峰借景。`artifact`
- 不该造：no symmetrical axis, no grand rockery, no large geometric flower beds, no bright heavy colours, no crowded pavilions。
- Negative prompt: `No symmetrical axis, no grand rockery, no large geometric flower beds, no bright heavy colours, no crowded pavilions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Bai Juyi, a pocket park beside a modern subway station, a small clear stream with a wooden bridge, a thatched reading hut, pines and bamboo, wildflowers and herbs, plain and leisurely, a garden for everyday life`
- 中文对照：白居易风格：现代地铁站边的一座口袋公园，一条清溪配木桥，一间茅草读书亭，松竹掩映，野花药草，平易闲适，日常生活的园。
- Negative: `No symmetrical axis, no grand rockery, no large geometric flower beds, no bright heavy colours, no crowded pavilions`
- 检验点：园是否按第 (1) 节一句话风格成立；第 (6) 节母题是否出现；禁区写法是否未出现。
