# Sesshū Tōyō — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `Muromachi Zen ink wash landscape, sharp angular brushstrokes, splashed ink (hatsuboku), ink gradations from wet wash to dry strokes, vast empty mist, small human figures in a monumental landscape`
- ZH: 室町禅宗水墨山水，锐利的折角皴笔，泼墨法，墨色由湿润晕染到枯笔飞白层层分级，空旷雾气留白，宏大山水中点缀渺小人物。

## (2) 色板方向

- 主色（4 色，颜料名）：墨色（浓—淡—干—湿分层）、淡赭、淡花青、淡石绿。`verbatim` / `artifact`
- 以墨为主，淡彩只作远山的微染；《秋冬山水图》几乎纯墨，秋冬两幅一暖一寒全靠墨色冷暖。`verbatim`
- 辅色：淡赭点染秋树、淡青染远山。
- 禁色：大面积重彩平涂；油画式明暗渐变；鲜艳高饱和色块。
- 冷暖：整体偏冷，秋幅略暖、冬幅极寒；亮在留白与雾气处。
- 明暗 / 饱和：靠墨的浓淡干湿分远近，不靠明暗渐变；饱和度极低，亮在空处。

## (3) 笔触与线条

- 笔触：锐利、折角、有棱角的皴笔，近景岩石用重而短的斧劈式皴线，远山只一笔淡线勾出轮廓；泼墨（hatsuboku）以湿墨泼洒成雾与山形。`verbatim` / `artifact`（以夏圭为师法对象，见维基百科“Sesshū Tōyō”）
- 线条：中锋与侧锋并用，轮廓线如闪电般一笔贯下，山脊一笔而就、顶端没入雾中；线有断有续，断处即是雾。`verbatim`（《秋冬山水图·冬景》）
- 质感：纸上水墨晕染 + 枯笔飞白；墨色层层叠加而非一次平涂。

## (4) 构图习惯

- 画幅：竖幅挂轴为主，也有逾 15 米的《四季山水图》长卷（毛利美术馆藏）。`artifact`
- 视点：多视点“渐进视点”（progressive vision），近、中、远各取最佳角度拼合，非单一焦点透视。`artifact`
- 布局：对角线构图，前景重岩斜入、远景高置；大面积留白即雾、即水、即空，实处只占画面小半。
- 裁切：山形常被雾截断，顶端出画；人物极小，置于山脚或舟中，视线随之入深。

## (5) 光影与透视

- 光源：无固定光源；亮在雾与留白处，不在高光点。
- 阴影：无写实阴影；墨的浓淡即体积与远近，淡即远、浓即近。
- 透视：无焦点透视；以墨色浓淡与位置高低推远近（空气透视的水墨版），近大远小但比例随视点切换而变。

## (6) 该画什么 / 不该画什么

- 该画：山水、松石、楼阁、舟楫、禅宗人物（如慧可断臂）、花鸟小品。`verbatim`
- 不该画：满幅重彩；工笔细描；焦点透视的写实空间；拥挤的细节堆砌。
- Negative prompt: `heavy opaque colour, meticulous gongbi fine lines, single-point perspective realism, crowded details, photorealistic shading`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Sesshū Tōyō, a small Yorkshire terrier sitting on a subway seat, Muromachi Zen ink wash, sharp angular brushstrokes, splashed ink, vast empty mist, the dog tiny in a monumental empty space, ink gradations on paper`
- 中文对照：雪舟风格，一只小约克夏犬坐在地铁座位上，室町禅宗水墨，锐利折角皴笔，泼墨，空旷雾气留白，狗渺小如山水中的人物，纸上墨色分级。
- Negative: 见第 (6) 节。
- 检验点：狗是否几笔就立住、是否被空旷留白衬得渺小；墨色是否有浓淡干湿的层次而不是一团灰。
