# Wang Shuhui — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Shuhui, gongbi lianhuanhua, elegant ladies, fine orchid-leaf line, heavy colour, classical romance`
- ZH: 王叔晖风格：工笔连环画，仕女优雅，兰叶描细线，重彩，古典爱情。

## (2) 线条、网点/色彩

- 线条：工笔兰叶描，线条细腻流畅、如吴带当风；仕女衣纹一笔见功力。`impression`
- 色彩：工笔重彩，石青、石绿、朱红并置而雅致；色彩服务于仕女风韵，不俗艳。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：连环画分幅，每幅一景；节奏舒缓如戏曲；视线随仕女移动，画面如舞台。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：仕女最见功力——面容清秀、体态婀娜、衣纹飘逸；书生俊朗；人物造型戏曲化。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：文字在幅下，旁白与对白交替；对白文雅、带古典味；无拟声词。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：西厢记：莺莺与张生、孔雀东南飞：刘兰芝、梁祝：梁山伯与祝英台、仕女：古典才女与闺秀、古典爱情与礼教冲突、戏曲化场景：园林、闺房、书斋。`verbatim`
- 不该画：No rough sketchy line、No photorealistic rendering、No modern urban scenes、No exaggerated action lines。`impression`
- Negative prompt: `No rough sketchy line, No photorealistic rendering, No modern urban scenes, No exaggerated action lines`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Wang Shuhui, a small Yorkshire terrier sitting on a subway seat, gongbi lianhuanhua, elegant ladies, fine orchid-leaf line, heavy colour`
- 中文对照：王叔晖风格：一只小约克夏犬坐在地铁座位上，工笔连环画，仕女优雅，兰叶描细线，重彩。
- Negative: `No rough sketchy line, no photorealistic rendering, no modern urban scenes, no exaggerated action lines`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
