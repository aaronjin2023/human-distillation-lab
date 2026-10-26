# Kim Soo-jung — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kim Soo-jung, Dooly the little dinosaur, round cute figures, simple line, family humour under censorship`
- ZH: 金洙政风格：小恐龙多利，圆润可爱造型，简笔线条，家庭幽默。

## (2) 线条、网点/色彩

- 线条：简笔圆润线，轮廓干净；多利绿身、白肚、头顶两撮毛，一笔可认。`verbatim`
- 色彩：彩色平涂，绿、白、明黄并置；色彩明快，不抢线条。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：多格连环，每格一景；节奏轻快，笑点在末格；阅读自左而右，视线随多利走。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：多利——小恐龙、绿身白肚；高吉童大叔、道奇、杜内等配角各有标志；表情夸张可爱。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：对白短、口语化；对话框圆润；拟声词小而活泼。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：小恐龙多利：冰封一亿年的小恐龙、高吉童一家：首尔普通家庭、多利与朋友们：道奇、杜内、希东、家庭日常：饭桌、吵架、和好、多利大冒险：时空旅行、动物代儿童：审查下的动物主角。`verbatim`
- 不该画：No dark satire、No photorealistic rendering、No crowded panels、No long explanatory text。`impression`
- Negative prompt: `No dark satire, No photorealistic rendering, No crowded panels, No long explanatory text`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Kim Soo-jung, a small Yorkshire terrier sitting on a subway seat, Dooly the little dinosaur style, round cute figures, simple line, family humour`
- 中文对照：金洙政风格：一只小约克夏犬坐在地铁座位上，小恐龙多利式圆润可爱造型，简笔线条，家庭幽默。
- Negative: `No dark satire, no photorealistic rendering, no crowded panels, no long explanatory text`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
