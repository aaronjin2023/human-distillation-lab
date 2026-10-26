# Dong Qichang — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dong Qichang, Southern School literati ink landscape on paper, pale ink with calligraphic brushwork, deliberately distorted space, imitating ancient masters yet transforming them, sparse composition, quiet and scholarly, much expressed with little detail`
- ZH: 董其昌风格，纸上南宗文人水墨，淡墨书法性用笔，空间有意扭曲，仿古而化古，构图疏朗，淡雅沉静，言少意多。

## (2) 色板方向

- 主色（6 色，颜料名）：
- 墨色（淡—浓分层，以淡为主）
- 淡赭石
- 淡花青
- 淡石绿
- 纸白（留白即云雾）
- 淡朱砂（极少）
- 主色 / 辅色：主色是淡墨 + 纸白；辅色淡赭、淡花青微染，色比沈周更淡、更疏。`verbatim`
- 禁色：北宗式的精细浓艳；重彩大面积平涂；满幅密体；写实空间。
- 冷暖：冷调为主，淡墨偏冷；暖只在淡赭微染处，整体清、淡、疏。
- 明暗 / 饱和：靠墨的淡浓与书法性用笔，不靠明暗渐变；饱和度极低，亮在留白处。

## (3) 笔触与线条

- 笔触：笔法书法性极强：以书入画，笔触如行草；淡墨为主，浓墨只作点睛。`verbatim` / `artifact`
- 线条：线条如行草书，纵横有致；轮廓不求精细，靠书法的势收住形；线条少而精。
- 质感：纸上淡墨轻染 + 枯笔擦出的淡雅感；墨色薄而透，无堆积。
- 关键技法：仿古化古——临倪瓒、米芾、黄公望等古人，仿其意而不泥其形；南北宗论——南宗重笔墨意趣、北宗重形色工细，画论只写对画面的影响（见 technique.md）。`artifact`（画史通说）

## (4) 构图习惯

- 画幅：竖幅 / 手卷 / 册页皆有；《仿古山水册》为册页，一页一古人。
- 视点：平视 / 轻微俯视；无焦点透视，散点构成，空间有意扭曲。
- 布局：山水疏朗，主体偏一角，留白适中；空间扭曲，山形不求写实，视线从容地走。
- 裁切：主体不顶边；山势舒缓，不画高耸主峰；不画满幅。

## (5) 光影与透视

- 光源：无固定光源；亮在留白云雾与纸白。
- 阴影：无写实阴影；墨的淡浓即远近，淡即远、浓即近。
- 透视：无焦点透视；空间有意扭曲——董其昌自言“以境之奇怪论，则画不如山水；以笔墨之精妙论，则山水决不如画”，空间服从笔墨。`artifact`（董其昌《画禅室随笔》引述，见 conflicts.md）

## (6) 该画什么 / 不该画什么

- 该画：疏朗山水、仿古山水、淡墨小景；南宗一路的淡雅山水。`verbatim`
- 不该画：北宗式精细浓艳；重彩满幅；密体满幅；写实空间。
- Negative prompt: `Northern School meticulous detail and bright colour, heavy colour filling the whole paper, dense full composition, realistic perspective space, photorealistic detail, oil paint texture`

## (7) 测试提示词示例（现代题材：高铁站台）

- Prompt: `In the style of Dong Qichang, a high-speed rail platform in a modern city, Southern School literati ink landscape on paper, pale ink with calligraphic brushwork, deliberately distorted space, the platform as a sparse ancient landscape, imitating old masters yet transforming them, quiet and scholarly`
- 中文对照：董其昌风格，现代城市高铁站台，南宗文人水墨，淡墨书法性用笔，空间有意扭曲，站台如疏朗古人山水，仿古而化古，淡雅沉静。
- Negative: 见第 (6) 节。
- 检验点：站台是否画得疏朗淡雅而不是写实透视；空间扭曲是否服从笔墨；仿古意味是否成立。
