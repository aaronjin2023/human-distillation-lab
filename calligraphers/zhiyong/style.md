# Zhiyong — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhiyong: Sui regular and cursive script, true and cursive side by side, neat and disciplined, the monk who wrote the Thousand Character Classic eight hundred times`
- ZH: 智永风格：隋代真草并行，工整有法，《真草千字文》为楷草对照之祖。

## (2) 笔法

- 楷书中锋端正，提按分明；草书圆转连绵而有法度，真草同一人而体分明。`impression`（摹本与隋代书风通说）
- 禁笔：他几乎不用的笔法——狂草的放纵连绵、唐楷的方折峻利。

## (3) 结字与章法

- 楷书结字端正，草书结字欹侧而有度；真草对照，同一字两种体式，章法行列整齐。`impression`
- 幅式：卷 / 尺牍 / 册页，横卷为主，行列疏朗。

## (4) 墨色与节奏

- 摹本墨色不可据为原墨；节奏楷缓草疾，真草对照见节奏对比。`artifact`

## (5) 书体与取法

- 书体：楷书、草书。传为王羲之七世孙；《真草千字文》为后世学书范本，唐初楷法溯源于此。`impression`
- 演变：真迹已佚，无分期；多个摹本系统风格略异，见 conflicts。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 真草并行的对照体式
- 楷书端正、草书有度的结字
- 中锋端正的楷书用笔
- 圆转而有法度的草书
- 整齐的行列章法
- 不该写：
- 狂草的放纵连绵
- 唐楷的方折峻利
- 险绝欹侧
- 浓墨滞重
- 刻意装饰
- Negative prompt: `No unrestrained wild cursive, no sharp Tang square turns, no daring slanted compositions, no heavy stagnant ink, no deliberate ornament`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Zhiyong, Sui regular and cursive script writing modern Tokyo subway station names, first in neat regular script then in disciplined cursive, side by side, ink on paper`
- 中文对照：智永风格：以隋代真草写现代东京地铁站名，先楷后草对照并行，楷端正、草有度。
- Negative: `No unrestrained wild cursive, no sharp Tang square turns, no daring slanted compositions, no heavy stagnant ink, no deliberate ornament`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
