# Qi Baishi — 图像风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。色板只写颜料名，不编 HEX。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Qi Baishi, freehand xieyi ink and light colour on paper, bold wet ink strokes, minimal background, large empty space, playful, between likeness and unlikeness`
- ZH: 齐白石风格，写意水墨淡彩，纸上大胆湿墨笔触，背景极简，大量留白，活泼诙谐，似与不似之间。

## (2) 色板方向

- 主色（7 色，颜料名）：墨色（浓—淡—干—湿分层）、朱砂红、西洋红 / 洋红、藤黄、石绿、石青、花青。`verbatim` / `artifact`（西洋红见《荔枝蜻蜓》；洋红、石青、石绿见鉴定文献）
- 分两路（v0.2 修正）：虾 / 水族一路以墨为主，红只点睛（虾眼、蟹钳）；花卉一路是“红花墨叶”，西洋红 / 洋红的花可以占大幅，配浓墨叶，纯红与深墨并用、强烈对比。`artifact`
- 辅色：淡赭、花青淡染。
- 禁色：油画式厚重堆积；灰暗死墨；满幅重彩平涂。
- 冷暖：墨分五色为主，暖色成片时仍以墨叶压住；整体清、亮、透，不沉。
- 明暗 / 饱和：靠墨的浓淡干湿，不靠明暗渐变；饱和度克制，亮在留白。

## (3) 笔触与线条

- 笔触：中锋为主，大胆、湿润、一气呵成；虾身淡墨、虾须浓墨、虾眼焦墨，一笔是一笔，不反复描。`verbatim` / `artifact`（破墨法：淡墨未干加浓墨，虾身显透明）
- 线条：书法性线条，钉头鼠尾、枯笔飞白并存；轮廓不封闭，靠笔意收住形。
- 质感：纸上水墨晕染 + 枯笔飞白；无油彩堆积，无工笔细线。
- 关键技法：破墨——先淡墨画虾头，趁未干用浓墨勾触须与眼，虾身因而透明如在水中。`artifact`（清华大学美术馆展览讲解）

## (4) 构图习惯

- 画幅：竖幅 / 方幅小品为主；主体偏一角，余下大面积留白。
- 视点：平视 / 轻微俯视；无焦点透视，散点 / 平面构成。
- 布局：一角式 + 大留白；虾群游向留白处，视线随须的方向走；题款、印章是构图的一部分，位置计入画面平衡。
- 裁切：主体不顶边，留白就是画面；不画满幅。

## (5) 光影与透视

- 光源：无固定光源；亮在留白与淡墨的“空”处，不在高光点。
- 阴影：无写实阴影；墨的浓淡即体积，淡即远、浓即近。
- 透视：无焦点透视；空间靠留白 + 墨色浓淡推远近，水是“不画的水”——背景无水纹，观者从墨色浓淡与须的方向感知水。`verbatim`

## (6) 该画什么 / 不该画什么

- 该画：虾、蟹、鱼、蛙、蝉、草虫、花果、蔬果等日常小物；小中见大，活泼诙谐。`verbatim`
- 不该画：全幅工笔；满幅重彩平涂；拥挤背景；写实毛发 / 鳞片细节；油画质感。
- 例外（v0.2 修正）：草虫可以工笔——《可惜无声·花鸟工虫册》是写意花卉 + 工笔草虫的经典组合；禁的是“整幅都工笔”，不是“虫工笔”。v1 模板示例里的 `detailed gongbi fine lines` 在此收窄为全幅工笔。
- Negative prompt: `meticulous gongbi rendering of the whole picture, heavy oil paint, crowded background, photorealistic fur detail, dark heavy ink wash filling the whole paper`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Qi Baishi, a small Yorkshire terrier sitting on a subway seat, freehand xieyi ink and light colour on paper, bold wet ink strokes, minimal background, large empty space, playful, between likeness and unlikeness`
- 中文对照：齐白石风格，一只小约克夏犬坐在地铁座位上，写意水墨淡彩，纸上大胆湿墨笔触，背景极简，大量留白，活泼诙谐，似与不似之间。
- Negative: 见第 (6) 节。
- 检验点：狗是否“几笔就立住”而不是工笔描毛；背景是否留白而不是画满车厢；红 / 淡彩是否只点睛而不是铺满。
