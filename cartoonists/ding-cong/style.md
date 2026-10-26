# Ding Cong — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ding Cong, sharp satirical illustration, thin precise line, Ah Q and little figures, humour with a sting`
- ZH: 丁聪风格：尖锐讽刺插图，精细线条，阿Q与小人物，幽默带刺。

## (2) 线条、网点/色彩

- 线条：精细的钢笔线，线条流畅、略带速写感；人物造型简练，表情一笔点出。`impression`
- 色彩：黑白为主，偶施淡彩；明暗靠线条疏密。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：单幅与插图并行；单幅一幅一点题；插图随文走，视线随人物走。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：阿Q最见功力——瘦小、滑稽而可悲；小人物类型化，体型对照生讽刺。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：少用对话框；多在画下配一句点题文字；插图无对白，随文叙事。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：阿Q：鲁迅阿Q的插图造型、小人物：市井小人物的讽刺、时事讽刺：紧贴时局的单幅、知识分子与官僚、民间生活速写、自画像与自嘲。`verbatim`
- 不该画：No gentle poetic blank space、No photorealistic detail、No ornate decoration、No wordless ambiguity。`impression`
- Negative prompt: `No gentle poetic blank space, No photorealistic detail, No ornate decoration, No wordless ambiguity`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Ding Cong, a small Yorkshire terrier sitting on a subway seat, sharp satirical illustration, thin precise line, humour with a sting`
- 中文对照：丁聪风格：一只小约克夏犬坐在地铁座位上，尖锐讽刺插图，精细线条，幽默带刺。
- Negative: `No gentle poetic blank space, no photorealistic detail, no ornate decoration, no wordless ambiguity`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
