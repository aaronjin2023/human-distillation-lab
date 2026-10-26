# Zhang Daqian — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhang Daqian, splashed ink and splashed colour landscape on paper, bold pouring of ink and mineral colour, deep blue-green pools with golden ochre, fine brushwork outlines emerging from the wash, monumental mountains, dramatic and modern`
- ZH: 张大千风格，纸上泼墨泼彩山水，大胆倾泼墨色与矿物色，深青绿彩池间以金赭，细笔勾勒自彩墨中浮现，山势雄浑，浓艳而现代。

## (2) 色板方向

- 主色（7 色，颜料名）：
- 墨色（浓—淡—干—湿分层）
- 石青
- 石绿
- 朱砂
- 赭石
- 藤黄
- 花青
- 主色 / 辅色：主色是泼墨 + 石青石绿泼彩；辅色朱砂、赭石、藤黄点睛，色比传统文人画浓得多、艳得多。`verbatim`
- 禁色：纯墨无色一路；疏朗一河两岸；小品式的淡雅一路。
- 冷暖：冷暖对撞：石青石绿冷色为底，朱砂赭石暖色点睛；整体浓艳、夺人。
- 明暗 / 饱和：靠泼彩的浓艳与墨色的深沉对撞，不靠明暗渐变；饱和度高，亮在彩池与金赭处。

## (3) 笔触与线条

- 笔触：笔法两极：泼墨泼彩时大笔倾泼，勾勒时细笔精到；粗与细同属一个 skill。`verbatim` / `artifact`
- 线条：线条两极：泼彩中无轮廓，勾勒时线条精细劲健；轮廓自彩墨中浮现，靠细笔收住形。
- 质感：纸上泼墨泼彩的水渍 + 细笔勾勒的精到感；彩色厚而不板，有“泼而不乱”的质感。
- 关键技法：泼墨泼彩——先泼墨、再泼彩，待半干以细笔勾勒山石树木；晚年视力衰退后此法大成。`artifact`（画史通说；《雾山茅屋》1965 年即此法）

## (4) 构图习惯

- 画幅：竖幅大轴为主；泼彩山水尺幅巨大，气势夺人。
- 视点：平视 / 俯视；无焦点透视，散点构成，山势雄浑压住画面。
- 布局：彩池与山势对半，山石自彩中浮现；留白极少，视线在彩池与山石之间走。
- 裁切：主体可顶边；彩池可满幅；不留大空白。

## (5) 光影与透视

- 光源：无固定光源；亮在彩池与金赭处。
- 阴影：无写实阴影；彩的浓淡即远近，淡即远、浓即近。
- 透视：无焦点透视；空间靠彩池的晕染与山石的勾勒推远近。

## (6) 该画什么 / 不该画什么

- 该画：泼彩山水、青城山、猿、荷花；泼墨泼彩一路。`verbatim`
- 不该画：纯墨无色；疏朗一河两岸；小品淡雅；工笔满幅。
- Negative prompt: `monochrome ink only, sparse one-river-two-banks composition, small quiet literati sketch, meticulous gongbi full picture, photorealistic detail, oil paint texture`

## (7) 测试提示词示例（现代题材：城市天台夜景）

- Prompt: `In the style of Zhang Daqian, a city rooftop at night, splashed ink and splashed colour landscape on paper, bold pouring of ink and mineral colour, deep blue-green pools with golden ochre, fine brushwork outlines of rooftop plants emerging from the wash, monumental and dramatic`
- 中文对照：张大千风格，现代城市天台夜景，泼墨泼彩山水，大胆倾泼墨色与矿物色，深青绿彩池间以金赭，细笔勾勒天台植物自彩墨中浮现，雄浑夺人。
- Negative: 见第 (6) 节。
- 检验点：彩池是否泼得大胆而不是小心翼翼；勾勒是否自彩中浮现；画面是否浓艳夺人而不是淡雅小品。
