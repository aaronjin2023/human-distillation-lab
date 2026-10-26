# Chen Uen — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chen Uen, martial arts manga, ink wash and fine line, heroic swordsmen, dramatic historical scenes`
- ZH: 郑问风格：武侠历史漫画，水墨与细线，英雄剑客，戏剧性历史场面。

## (2) 线条、网点/色彩

- 线条：水墨与细线并用，剑客衣纹飘逸、动态有力；线条时而工笔时而泼墨。`impression`
- 色彩：水墨为主，偶施重彩；明暗对比强，气氛肃穆。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：大格与跨页多，打斗分解细；节奏先慢后急，跨页落点在决战；阅读自右而左，视线随剑光走。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：剑客体型修长、面容冷峻；历史人物造型考据而夸张；动作动态大、衣袂飘飞。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：对白简短有力，带古风；拟声词大字出格，与剑光融合；旁白少。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：阿鼻剑：剑客与地狱意象、东周英雄传：春秋战国英雄、大霹雳：霹雳布袋戏式人物、剑客：修长冷峻的剑客、历史场面：战争与朝堂、水墨武侠：泼墨与细线并行。`verbatim`
- 不该画：No cute round figures、No photorealistic rendering、No crowded small panels、No modern slang dialogue。`impression`
- Negative prompt: `No cute round figures, No photorealistic rendering, No crowded small panels, No modern slang dialogue`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Chen Uen, a small Yorkshire terrier sitting on a subway seat, martial arts manga, ink wash and fine line, heroic swordsmen, dramatic scenes`
- 中文对照：郑问风格：一只小约克夏犬坐在地铁座位上，武侠漫画，水墨与细线，英雄剑客，戏剧性场面。
- Negative: `No cute round figures, no photorealistic rendering, no crowded small panels, no modern slang dialogue`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
