# Hua Junwu — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hua Junwu, sharp political satire, bold ink line, animal metaphors, one panel one punchline`
- ZH: 华君武风格：尖锐政治讽刺，大胆墨线，动物隐喻，一幅一点题。

## (2) 线条、网点/色彩

- 线条：大胆的毛笔与钢笔线，粗细对比强；动物造型夸张，线条有力、不拖泥带水。`impression`
- 色彩：黑白为主，偶施淡彩；黑块面积大，明暗对比强。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：单幅为主，一幅一点题；偶有两三幅连作；构图主体居中，陪衬退后，标题文字点题。`impression`
- 节奏：单幅构图：靶子居中、陪衬退后（单幅构图草图）；分镜示例：单幅构图，犬居中，乘客退后。`impression`

## (4) 角色造型

- 角色造型：动物隐喻最见功力——猪、狼、狐狸拟人化；官僚与小人物类型化，体型对照强烈。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：少用对话框；多在画下配一句点题文字，标题即笑点；无拟声词大字。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：动物隐喻：猪、狼、狐狸拟人讽刺、官僚主义与形式主义、死猪不怕开水烫等经典单幅、社会风气与人情世故、时事讽刺：紧贴时局、民间谚语入画。`verbatim`
- 不该画：No gentle poetic blank space、No photorealistic detail、No wordless ambiguity、No ornate decoration。`impression`
- Negative prompt: `No gentle poetic blank space, No photorealistic detail, No wordless ambiguity, No ornate decoration`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Hua Junwu, a small Yorkshire terrier sitting on a subway seat, sharp political satire, bold ink line, animal metaphor, one panel one punchline`
- 中文对照：华君武风格：一只小约克夏犬坐在地铁座位上，尖锐讽刺，大胆墨线，动物隐喻，一幅一点题。
- Negative: `No gentle poetic blank space, no photorealistic detail, no wordless ambiguity, no ornate decoration`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
