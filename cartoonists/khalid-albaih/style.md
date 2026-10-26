# Khalid Albaih — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Khalid Albaih, Khartoon, minimal single-panel satire, bold simple shapes, Arabic text, Sudan and the world`
- ZH: 阿尔拜赫风格：喀土穆漫画，极简单幅讽刺，大胆简形，阿拉伯文字，苏丹与世界。

## (2) 线条、网点/色彩

- 线条：极简的数码线，轮廓干净；人物造型简化为符号，大胆简形。`impression`
- 色彩：平涂为主，一色点题是标志；色彩明快，对比强。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：单幅为主，一幅一点题；社交媒体竖图；构图主体居中，文字点题。`impression`
- 节奏：单幅构图：靶子居中、陪衬退后（单幅构图草图）；分镜示例：单幅竖图构图，犬居中。`impression`

## (4) 角色造型

- 角色造型：政客简化为符号——大鼻子、墨镜；普通人小而简练；表情一笔点出。`impression`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：少用对话框；多在画中配一句阿拉伯语或英语点题；拟声词无。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：喀土穆漫画：苏丹时局、苏丹：喀土穆、尼罗河、苏丹人、阿拉伯世界：各国政客、极简符号：政客简化为符号、一幅一点题：社交媒体单幅、世界议题：监控、战争、难民。`verbatim`
- 不该画：No detailed rendering、No photorealistic detail、No ornate decoration、No crowded panels。`impression`
- Negative prompt: `No detailed rendering, No photorealistic detail, No ornate decoration, No crowded panels`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Khalid Albaih, a small Yorkshire terrier sitting on a subway seat, Khartoon style, minimal single-panel satire, bold simple shapes, Arabic text`
- 中文对照：阿尔拜赫风格：一只小约克夏犬坐在地铁座位上，喀土穆漫画式极简单幅讽刺，大胆简形，阿拉伯文字。
- Negative: `No detailed rendering, no photorealistic detail, no ornate decoration, no crowded panels`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
