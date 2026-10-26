# Chen Kenmin — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chen Kenmin: Sichuan cuisine made Japanese, mapo tofu with soup, ebi chilli, seven flavours bold but tuned for Japan, cooking is love, no dish without heart`
- ZH: 陈建民风格：日本川菜，麻婆豆腐加汤，干烧虾仁，七味浓烈而为日本调和，料理就是爱，没有不用心的菜。

## (2) 味型方向

- 主味：麻辣鲜香——麻、辣、鲜、香并重，七味（酸、辣、麻、甜、苦、香、咸）皆备。`artifact`
- 辅味：甜，日本化改良后甜味稍重，以合日本人口味。`impression`
- 禁味：生辣刺喉、死咸、油腻。
- 味型层次：多层复合，麻辣在前，鲜香在后，七味分层。`impression`
- 浓淡对比度：浓，以浓见长；辣度中高，麻度中高，酸度低。

## (3) 刀工与火候

- 刀工：川菜刀工，丁、丝、片皆匀，刀工服务于火候的均匀。`impression`
- 火候：爆炒镬气，火大而快，麻婆豆腐以小火收汁，干烧虾仁以大火快炒。`impression`
- 质感：嫩、滑、麻、辣并存；豆腐靠小火得嫩，虾仁靠大火得滑。

## (4) 调味

- 调味料：豆瓣、花椒、辣椒、豆豉、蒜、姜，川菜调料皆备；日本化后以山椒代花椒亦有记载。`artifact`
- 调味顺序：豆瓣先炒出红油，花椒后下提麻，调味在烹制之中分步进行。
- 禁调味：不问火候一味到底；不用生辣压过鲜香。

## (5) 摆盘与食材选择

- 摆盘：四川饭店摆盘，满盘丰盛，红油亮泽，麻婆豆腐以红亮为要。`impression`
- 食材选择：豆腐取嫩，虾取鲜，皆取上品；日本食材代川味亦有记载。
- 上菜节奏：川菜之序，麻婆豆腐与干烧虾仁多为热菜，趁热上桌。

## (6) 该做什么菜 / 不该做什么菜

- 该做：麻婆豆腐（日本）、干烧虾仁、四川饭店、七味浓烈、豆瓣红油、花椒提麻、料理是爱。
- 不该做：`No raw chilli burn, no dead saltiness, no greasy richness, no dish without heart, no bland adaptation, no showy plating`
- Negative prompt: `No raw chilli burn, no dead saltiness, no greasy richness, no dish without heart, no bland adaptation, no showy plating`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Chen Kenmin, a modern bowl of ramen reimagined as Japanese Sichuan: mapo-style minced pork over noodles, douban red oil, Sichuan pepper numbing, seven flavours bold but tuned for Japan, cooking is love, no dish without heart`
- 中文对照：陈建民风格：一碗现代拉面，按日本川菜重做：麻婆肉末盖面，豆瓣红油，花椒提麻，七味浓烈而为日本调和，料理就是爱，没有不用心的菜。
- Negative: `No raw chilli burn, no dead saltiness, no greasy richness, no dish without heart, no bland adaptation`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
