# Lee Hyun-se — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lee Hyun-se, Korean manhwa, dynamic sports and action, bold ink line, hot-blooded youth`
- ZH: 李贤世风格：韩国漫话，动态运动与动作，大胆墨线，热血青春。

## (2) 线条、网点/色彩

- 线条：大胆的墨线，轮廓有力；运动动态线条流畅，速度线密。`impression`
- 色彩：黑白为主，偶施淡彩；明暗对比强，气氛热血。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：多格连环，打斗与运动分解细；节奏快，跨页落点在决胜；阅读自左而右，视线随主角走。`impression`
- 节奏：切格：抒情大格与叙事小格交错（分镜稿（name））；分镜示例：多格连环，动作分解细。`impression`

## (4) 角色造型

- 角色造型：青年运动员体型健壮、表情坚毅；外星人与怪物造型夸张；动作动态大。`impression`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：对白简短有力；拟声词大字出格；旁白少。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：恐怖的外人球团：棒球与外星人、南瓜脸：校园与成长、韩国漫画史：漫画史的漫画版、运动：棒球、动作、热血青春：青年主角、外星人与怪物。`verbatim`
- 不该画：No gentle poetic blank space、No photorealistic rendering、No crowded dialogue balloons、No slow lyrical pacing。`impression`
- Negative prompt: `No gentle poetic blank space, No photorealistic rendering, No crowded dialogue balloons, No slow lyrical pacing`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Lee Hyun-se, a small Yorkshire terrier sitting on a subway seat, Korean manhwa, dynamic sports, bold ink line, hot-blooded youth`
- 中文对照：李贤世风格：一只小约克夏犬坐在地铁座位上，韩国漫话，动态运动，大胆墨线，热血青春。
- Negative: `No gentle poetic blank space, no photorealistic rendering, no crowded dialogue balloons, no slow lyrical pacing`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
