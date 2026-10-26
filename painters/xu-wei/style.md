# Xu Wei — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xu Wei, bold freehand xieyi ink painting on paper, splashed and broken ink, fast cursive-like brushwork, wet and dry ink in one breath, grapes and peonies in pure ink, large empty space, wild yet controlled, seeking spirit not likeness`
- ZH: 徐渭风格，纸上大写意水墨，泼墨破墨，笔走如草书，干湿浓淡一气呵成，纯墨葡萄牡丹，大量留白，狂放而有节制，不求形似但求神韵。

## (2) 色板方向

- 主色（5 色，颜料名）：
- 墨色（浓—淡—干—湿分层）
- 淡赭石（极少）
- 淡花青（极少）
- 纸白（留白即气）
- 淡朱砂（极少，仅点睛）
- 主色 / 辅色：主色是纯墨；辅色几乎不用，牡丹亦只用墨——“无色而色自足”。`verbatim` / `artifact`（《墨牡丹》只用墨而显牡丹华贵）
- 禁色：工笔细描；重彩大面积平涂；满幅构图；板滞院体。
- 冷暖：冷调为主，纯墨偏冷；暖只在淡赭微染处，整体清、冷、烈。
- 明暗 / 饱和：靠墨的浓淡干湿与泼墨的偶然性，不靠明暗渐变；饱和度克制，亮在留白与水渍处。

## (3) 笔触与线条

- 笔触：笔法如草书：行笔如飞、泼墨、破墨、枯笔并用；干笔、湿笔、破笔交替，一气呵成。`verbatim` / `artifact`
- 线条：线条如草书，纵横恣肆；轮廓不封闭，靠笔意收住形；线条粗细干湿变化极大。
- 质感：纸上泼墨的水渍 + 枯笔飞白；墨色浓淡干湿一次成形，无堆积。
- 关键技法：泼墨破墨——以水饱墨点染葡萄，干墨勾藤，大片泼墨写叶；“不求形似”——徐渭自倡“不求形似”，以笔墨写胸中块垒。`artifact`（画史通说；徐渭语）

## (4) 构图习惯

- 画幅：竖幅大轴为主；《墨葡萄图》纵 165.7 厘米，气势夺人。
- 视点：平视 / 轻微俯视；无焦点透视，散点构成。
- 布局：藤蔓自上垂下，葡萄成串倒挂，主体偏一角，余下大面积留白；视线随藤蔓上下走。
- 裁切：主体可顶边；藤蔓不见首尾；不画满幅细节。

## (5) 光影与透视

- 光源：无固定光源；亮在留白与水渍处。
- 阴影：无写实阴影；墨的浓淡即体积，淡即远、浓即近。
- 透视：无焦点透视；空间靠留白 + 墨色浓淡推远近。

## (6) 该画什么 / 不该画什么

- 该画：葡萄、牡丹、墨竹、芭蕉、杂花；大写意花鸟一路。`verbatim`
- 不该画：工笔细描；重彩满幅；院体楼阁；疏朗一河两岸。
- Negative prompt: `meticulous gongbi fine lines, heavy colour filling the whole paper, stiff academic style, sparse one-river-two-banks composition, photorealistic detail, oil paint texture`

## (7) 测试提示词示例（现代题材：街头夜市烧烤摊）

- Prompt: `In the style of Xu Wei, a street night-market barbecue stall in a modern city, bold freehand xieyi ink painting on paper, splashed and broken ink, fast cursive-like brushwork, wet and dry ink in one breath, smoke and skewers in pure ink, large empty space, wild yet controlled`
- 中文对照：徐渭风格，现代城市街头夜市烧烤摊，大写意水墨，泼墨破墨，笔走如草书，干湿浓淡一气呵成，烟火与肉串皆纯墨，大量留白，狂放而有节制。
- Negative: 见第 (6) 节。
- 检验点：烧烤摊是否几笔就立住而不是工笔描画；泼墨是否一气呵成；背景是否留白而不是画满夜市。
