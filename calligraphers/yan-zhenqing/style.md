# Yan Zhenqing — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yan Zhenqing: Tang regular and running script, broad and thick-boned, centered brush, hidden tip, muscle over charm`
- ZH: 颜真卿风格：唐楷宽博厚重，中锋圆笔、藏头护尾，宁舍秀媚而保筋骨。

## (2) 笔法

- 中锋圆笔，藏头护尾，屋漏痕；提按厚重，笔画如锥画沙、印印泥；行书则笔力沉雄，涂改即兴。`verbatim`
- 禁笔：他几乎不用的笔法——纤弱的秀媚、轻滑的浮笔。

## (3) 结字与章法

- 结字宽博厚重，外拓而重心稳；楷书笔画横轻竖重，行书欹侧而筋骨不失。`verbatim`
- 幅式：卷 / 尺牍 / 册页，横卷为主，行列疏朗。

## (4) 墨色与节奏

- 墨色浓厚，枯润相间；《祭侄文稿》一幅之内墨色多次转换，节奏由悲痛而疾速。`verbatim`

## (5) 书体与取法

- 书体：楷书、行书。唐楷书代表，与柳公权并称“颜柳”；取法二王与北碑而变之，后世楷法宗颜者众。`impression`
- 演变：早期《多宝塔碑》尚秀润，晚年《祭侄文稿》沉雄悲壮——此说据作品年代与风格对比，见于学界通说。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 宽博厚重的结字
- 中锋圆笔、藏头护尾
- 横轻竖重的笔画
- 浓厚枯润相间的墨色
- 涂改即兴的行书草稿气息
- 不该写：
- 纤弱的秀媚
- 轻滑的浮笔
- 瘦劲清秀
- 端正划一
- 刻意装饰
- Negative prompt: `No slender delicate charm, no light slippery strokes, no thin elegant lines, no uniform character size, no deliberate ornament`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Yan Zhenqing, Tang running script writing a short mourning note about modern Tokyo subway stations, broad thick-boned strokes, centered brush, heavy ink with dry-brush breaks, honest corrections left visible`
- 中文对照：颜真卿风格：以行书写一则关于现代东京地铁站的悼念短札，笔画宽博厚重，中锋圆笔，墨色浓厚，涂改留痕。
- Negative: `No slender delicate charm, no light slippery strokes, no thin elegant lines, no uniform character size, no deliberate ornament`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
