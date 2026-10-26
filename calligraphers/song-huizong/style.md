# 宋徽宗 — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Emperor Huizong: slender-gold script, thin hard strokes like iron wire and silver hooks, sharp turns, elegant and precise, every character upright and jewel-like`
- ZH: 宋徽宗风格：瘦金体铁划银钩，笔画瘦硬挺拔，转折锐利，结字端正秀润，如珠玉在列。

## (2) 笔法

- 用笔瘦硬挺拔，中锋行笔，提按极小，笔画如铁线；转折多方折，收笔多作钩挑，如“铁划银钩”（后人评语）。`impression` 起笔藏锋微露，行笔匀速，收笔锐利。`impression` 禁笔：不用丰腴扁笔，不用侧锋刷字，不用枯笔飞白。`impression`

## (3) 结字与章法

- 结字端正秀润，字形瘦长，重心居中，笔画疏朗而精到；字与字大小均匀，行距整齐。`verbatim` 章法行列分明，行气端直，留白均匀，落款“天下一人”押字，花押与钤印讲究。`artifact` 幅式多为卷、册，字数规整。`artifact`

## (4) 墨色与节奏

- 墨色浓而匀，一幅之内浓淡变化极小，少枯笔；笔画墨色均匀，如金石刻划。`verbatim` 节奏匀速平稳，少顿挫，一字一顿，笔笔精到。`impression` 纸多用熟纸与绢，墨色附着清晰。`impression`

## (5) 书体与取法

- 书体以瘦金体楷书为主，兼擅行书；取法薛稷、褚遂良，自创瘦金一路。`artifact` 演变：早年瘦硬已成，中年更趋精到，晚年瘦金更瘦更硬。`impression`

## (6) 该写什么 / 不该写什么

- 该写：瘦硬挺拔的铁线笔画、方折锐利的转折、瘦长端正的结字、均匀浓黑的墨色、行列分明的章法。
- 不该写：丰腴扁笔、侧锋刷字、枯笔飞白、欹侧险绝的结字、大小悬殊的参差。
- Negative prompt: `No plump flat brush, no side-brush flourish, no dry flying-white strokes, no tilted dangerous characters, no extreme size contrast, no printed typeface`

## (7) 测试提示词示例（现代题材：地铁站名瘦金体）

- Prompt: `In the style of Emperor Huizong, slender-gold script calligraphy writing modern subway station names, thin hard iron-wire strokes, sharp square turns, upright jewel-like characters, even ink, neat columns`
- 中文对照：宋徽宗风格：瘦金体写地铁站名，铁划银钩，转折锐利，字瘦长端正，墨匀而浓，行列分明。
- Negative: `No plump flat brush, no side-brush flourish, no dry flying-white strokes, no tilted dangerous characters, no extreme size contrast, no printed typeface`
- 检验点：笔法、结字、章法、墨色是否符合本条风格；是否出现第 6 节禁区里的写法。
