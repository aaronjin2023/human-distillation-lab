# Artemisia Gentileschi — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Artemisia Gentileschi, Italian Baroque oil painting, Caravaggesque tenebrism, powerful heroines, violent light against darkness, physical struggle, female protagonists, oil on canvas`
- ZH: 阿特米西娅风格，意大利巴洛克油画，卡拉瓦乔式明暗对照法，强有力的女主人公，强光劈开黑暗，身体的搏斗，女性主角，布面油画。

## (2) 色板方向

- 主色（7 色，颜料名）：暗褐、朱红、铅白、土黄、群青、墨绿、赭石。`verbatim`
- 辅色：金黄（衣袍与光）、灰黑（暗部）。
- 禁色：柔弱的女性形象；明朗的均匀光；优雅的理想人体；装饰性金底。
- 冷暖：暗部冷黑、亮部暖黄，光是暖的、暗是冷的，冷暖对撞极烈。
- 明暗 / 饱和：极高对比，亮部极亮、暗部极暗，中间调极短；饱和度在亮部高、在暗部几近于无。

## (3) 笔触与线条

- 笔触：直接写生，笔触肯定、厚重；亮部厚涂、暗部薄涂。`artifact`
- 线条：无硬轮廓线——形体由光切出，亮与暗的交界即轮廓。`verbatim`
- 质感：布面油画，皮肤、织物、金属的质感在强光下极致真实，暗部则沉入黑洞；血与布的质感对照是其特点。

## (4) 构图习惯

- 画幅：大幅叙事皆有；《朱迪思斩首霍洛弗尼斯》为横幅，人物横向搏斗。`verbatim`
- 视点：平视略近；《朱迪思》中朱迪思与女仆按住霍洛弗尼斯，刀在中央，观者如在现场。
- 布局：对角线搏斗构图——三人身体交错，刀与血在中央，视线被搏斗吸住；《苏珊娜与长老》苏珊娜居中、两长老分列左右，身体蜷缩。`verbatim`
- 裁切：人物常被画框边缘截断，营造近景感与紧张感；画面如舞台剧的定格。

## (5) 光影与透视

- 光源：单一、强烈的光源，光从画面外斜射，是画面的主角。`verbatim`
- 阴影：暗部极暗、近乎纯黑，体积靠亮部的厚涂，不靠中间调。
- 透视：浅空间——人物贴近画面，背景沉入黑暗，空间压缩而非深远；透视克制，戏剧靠光影与搏斗。

## (6) 该画什么 / 不该画什么

- 该画：朱迪思、苏珊娜、女性圣徒；身体的搏斗与反抗；强光下的皮肤与织物。
- 不该画：柔弱的女性形象；明朗的均匀光；优雅的理想人体；装饰性金底。
- Negative prompt: `passive delicate heroines, bright even daylight, idealised graceful figures, uniform diffused light, gold leaf background, smooth academic blending`

## (7) 测试提示词示例（现代题材：厨房里切菜的女子）

- Prompt: `In the style of Artemisia Gentileschi, a woman chopping vegetables in a kitchen at night, Italian Baroque oil painting, Caravaggesque tenebrism, a powerful heroine, violent light against darkness, physical strength, female protagonist, oil on canvas`
- 中文对照：阿特米西娅风格，深夜厨房里切菜的女子，意大利巴洛克油画，卡拉瓦乔式明暗对照法，强有力的女主人公，强光劈开黑暗，身体的力量，女性主角，布面油画。
- Negative: 见第 (6) 节。
- 检验点：女子是否强有力而不是柔弱摆拍；光是否劈开黑暗；动作是否有身体的力量感。
