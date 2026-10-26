# Luo Guorong — 厨艺风格规格 style.md（给图像模型）

> 只描述菜品，不描述人生。引用食谱时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Luo Guorong: state-banquet Sichuan, bold flavours tuned for ceremony, gongbao chicken, precise heat, grandeur without roughness, no dish too crude for the table`
- ZH: 罗国荣风格：国宴川菜，浓烈为典礼调和，宫保鸡丁，火候精准，气派而不粗野，没有上不了台面的菜。

## (2) 味型方向

- 主味：麻辣鲜香——麻、辣、鲜、香并重，为国宴调和，浓烈而有分寸。`impression`
- 辅味：甜，宫保鸡丁的荔枝味，甜酸相衬。`artifact`
- 禁味：生辣刺喉、死咸、油腻。
- 味型层次：多层复合，麻辣在前，荔枝味在后，分层调准。`impression`
- 浓淡对比度：浓，以浓见长；辣度中高，麻度中，酸度低。

## (3) 刀工与火候

- 刀工：川菜刀工，丁、丝、片皆匀，刀工服务于国宴的精致。`impression`
- 火候：爆炒镬气，火大而快，宫保鸡丁以大火快炒，花生以小火炸脆。`impression`
- 质感：嫩、脆、麻、辣并存；鸡丁靠大火得嫩，花生靠小火得脆。

## (4) 调味

- 调味料：豆瓣、花椒、辣椒、豆豉、蒜、姜，川菜调料皆备。`impression`
- 调味顺序：豆瓣先炒出红油，花椒后下提麻，荔枝味最后调准。
- 禁调味：不问火候一味到底；不用生辣压过鲜香。

## (5) 摆盘与食材选择

- 摆盘：国宴摆盘，满盘丰盛而有序，红油亮泽，宫保鸡丁以红亮为要。`impression`
- 食材选择：鸡丁取嫩，花生取脆，皆取上品。
- 上菜节奏：国宴之序，先凉后热，先淡后浓，宫保鸡丁多为热菜。

## (6) 该做什么菜 / 不该做什么菜

- 该做：宫保鸡丁、国宴川菜、北京饭店川菜、荔枝味、豆瓣红油、花椒提麻、气派而不粗野。
- 不该做：`No raw chilli burn, no dead saltiness, no greasy richness, no crude presentation, no dish too rough for ceremony, no bland adaptation`
- Negative prompt: `No raw chilli burn, no dead saltiness, no greasy richness, no crude presentation, no dish too rough for ceremony, no bland adaptation`

## (7) 测试提示词示例（现代题材：一碗现代拉面）

- Prompt: `In the style of Luo Guorong, a modern bowl of ramen reimagined as state-banquet Sichuan: gongbao-style chicken over noodles, douban red oil, lychee flavour sweet and sour, peanuts crisp, bold flavours tuned for ceremony, grandeur without roughness`
- 中文对照：罗国荣风格：一碗现代拉面，按国宴川菜重做：宫保鸡丁盖面，豆瓣红油，荔枝味酸甜，花生脆，浓烈为典礼调和，气派而不粗野。
- Negative: `No raw chilli burn, no dead saltiness, no greasy richness, no crude presentation, no bland adaptation`
- 检验点：摆盘、味型与质感是否按本厨师的风格成立；是否误入 Negative prompt 的禁区。
