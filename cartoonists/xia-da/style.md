# Xia Da — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xia Da, elegant Chinese-style shojo manga, fine line, beautiful costumes, Tang dynasty atmosphere, lyrical and quiet`
- ZH: 夏达风格：优雅古风少女漫画，细腻线条，华美服饰，大唐气氛，抒情安静。

## (2) 线条、网点/色彩

- 线条：细腻的数码线，轮廓流畅、带工笔味；服饰纹样精细，线条不板滞。`impression`
- 色彩：淡彩为主，色调雅致；明暗柔和，靠淡彩层次造氛围。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：大格抒情与小格叙事交错；节奏舒缓，留白多；阅读自右而左，视线随女主角走。`impression`
- 节奏：切格：大格抒情、小格叙事（分镜稿（name））；分镜示例：大格抒情——犬立车厢，小格叙事。`impression`

## (4) 角色造型

- 角色造型：女主角面容清秀、长发飘逸；唐代服饰华美而考据；配角造型各有标志；表情细腻。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：对话框圆润、文字文雅；拟声词小而少；旁白抒情、文字量中等。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：长歌行：李长歌的大唐江湖、子不语：志怪与日常、步天歌：星象与命运、唐代服饰与建筑、少女心境：成长与抉择、古风抒情：花、月、长安。`verbatim`
- 不该画：No rough sketchy line、No photorealistic rendering、No exaggerated speed lines、No crowded small panels。`impression`
- Negative prompt: `No rough sketchy line, No photorealistic rendering, No exaggerated speed lines, No crowded small panels`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Xia Da, a small Yorkshire terrier sitting on a subway seat, elegant Chinese-style shojo manga, fine line, Tang dynasty atmosphere, lyrical`
- 中文对照：夏达风格：一只小约克夏犬坐在地铁座位上，古风少女漫画，细腻线条，大唐气氛，抒情安静。
- Negative: `No rough sketchy line, no photorealistic rendering, no exaggerated speed lines, no crowded small panels`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
