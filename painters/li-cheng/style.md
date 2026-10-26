# Li Cheng — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Cheng, Five Dynasties ink landscape, pale ink like gold, crab-claw trees, cold forests and flat wilderness, misty level distance, elegant and desolate`
- ZH: 李成风格，五代水墨山水，惜墨如金，蟹爪树，寒林平野，烟岚平远，清润而萧疏。

## (2) 色板方向

- 主色（颜料名）：墨色、淡赭、花青、淡石绿。`verbatim` / `artifact`
- 辅色：淡赭染寒林、淡花青染远峦，墨色为主、色极淡，惜墨如金。
- 禁色：青绿重彩；浓墨重皴；满幅高山。
- 冷暖：墨分浓淡为主，暖色只作点染；整体清、亮、透，不沉。
- 明暗 / 饱和：靠墨的浓淡干湿，不靠明暗渐变；饱和度克制，亮在留白。

## (3) 笔触与线条

- 笔触：“惜墨如金”：用墨极省，淡墨为主，层层淡染见远近；树枝如蟹爪，屈曲有节，枯枝向空。`artifact`（画史通说；《晴峦萧寺图》画面可见）
- 线条：书法性线条，中锋为主；轮廓不封闭，靠笔意收住形。
- 质感：绢 / 纸上水墨晕染 + 枯笔飞白；无油彩堆积，无工笔细线。

## (4) 构图习惯

- 画幅：平远为主：近景寒林、平野，中景萧寺，远景淡峦，三段以烟雾隔开；画面疏朗，留白即烟岚。`verbatim`
- 视点：平视 / 轻微俯视；无焦点透视，散点 / 平面构成。
- 布局：题款、印章是构图的一部分，位置计入画面平衡。
- 裁切：平远三段，近景寒林、中景萧寺、远景淡峦，三段以烟雾隔开；留白即烟岚，不画满幅。

## (5) 光影与透视

- 光源：无固定光源；亮在烟雾留白，暗在淡墨层染；空间靠墨色由淡到更淡推远，不用焦点透视。`verbatim`
- 阴影：无写实阴影；墨的浓淡即体积，淡即远、浓即近。
- 透视：无焦点透视；空间靠留白 + 墨色浓淡推远近。

## (6) 该画什么 / 不该画什么

- 该画：寒林、平野、萧寺、远岫、蟹爪枯枝、烟岚平远、淡墨山水。`verbatim`
- 不该画：繁密皴擦、重彩青绿、满幅高山、焦点透视、浓墨重染、工笔细节。
- Negative prompt: `dense texture strokes, heavy blue-green colour, crowded monumental mountains, linear perspective, heavy dark ink, meticulous gongbi detail`

## (7) 测试提示词示例（现代题材：共享单车停放点）

- Prompt: `In the style of Li Cheng, a shared-bike parking area in a modern city, pale ink like gold, crab-claw bare trees, cold flat wilderness, misty level distance, elegant and desolate, a small temple in the middle distance`
- 中文对照：李成风格，现代城市一处共享单车停放点，惜墨如金，蟹爪枯枝，寒林平野，烟岚平远，清润萧疏，中景一座小寺。
- Negative: 见第 (6) 节。
- 检验点：蟹爪枯枝的线与平远三段构图二者至少其一成立；画面是否清润萧疏、寒林平野，而不是只换了题材。
