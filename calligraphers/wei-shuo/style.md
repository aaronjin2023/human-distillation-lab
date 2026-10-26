# Wei Shuo — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wei Shuo: early Jin regular and running script, delicate yet firm, the brush-array teaching behind Wang Xizhi`
- ZH: 卫夫人风格：东晋楷行，秀润而有筋骨，为王羲之所师之法。

## (2) 笔法

- 楷行之间的用笔：中锋为主，提按轻灵；传说其笔法授王羲之，见《笔阵图》著录。`artifact`（托名书论，非真迹证据）
- 禁笔：他几乎不用的笔法——唐楷的方折峻利、狂草的连绵放纵。

## (3) 结字与章法

- 结字端正而秀润，笔画疏朗；行书欹侧含蓄，未见后世放纵。`impression`
- 幅式：卷 / 尺牍 / 册页，横卷为主，行列疏朗。

## (4) 墨色与节奏

- 无真迹可考；墨色与节奏按东晋楷行通例反推：墨色清润，节奏从容。`impression`

## (5) 书体与取法

- 书体：楷书、行书。传说为王羲之之师，《笔阵图》托名于她；其书论影响后世笔法论述。`artifact`
- 演变：无作品序列；蒸馏以书论影响为主，不编造分期。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 东晋楷行的端正秀润
- 中锋为主、提按轻灵的用笔
- 疏朗的结字与从容的节奏
- 清润的墨色
- 《笔阵图》笔法论述中的七势
- 不该写：
- 唐楷的方折峻利
- 狂草的连绵放纵
- 浓墨滞重的笔意
- 欹侧险绝的取势
- 华丽装饰
- Negative prompt: `No sharp Tang square turns, no wild-cursive tangling, no heavy stagnant ink, no daring slanted compositions, no ornate decoration`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Wei Shuo, early Jin regular and running script writing modern Tokyo subway station names, delicate yet firm strokes, clear unhurried rhythm, light moist ink, elegant restraint`
- 中文对照：卫夫人风格：以东晋楷行写现代东京地铁站名，笔画秀润有筋骨，节奏从容，墨色清润。
- Negative: `No sharp Tang square turns, no wild-cursive tangling, no heavy stagnant ink, no daring slanted compositions, no ornate decoration`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
