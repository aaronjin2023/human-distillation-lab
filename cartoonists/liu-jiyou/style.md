# Liu Jiyou — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Liu Jiyou, heroic lianhuanhua, dynamic figures, fine brush line, classical tales in vivid action`
- ZH: 刘继卣风格：英雄连环画，动态人物，精细笔线，古典故事的生动动作。

## (2) 线条、网点/色彩

- 线条：精细的毛笔线，兼工带写；人物动态线条流畅有力，动物毛发一笔可辨。`impression`
- 色彩：工笔重彩与白描并行；《大闹天宫》色彩浓烈，《武松打虎》墨色为主。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：连环画分幅，每幅一景；打斗场面幅面大、动态强；视线随英雄动作移动。`impression`
- 节奏：逐幅定构图与人物位置（分幅草图（每幅一小稿））；分镜示例：逐幅定构图，犬为打虎英雄。`impression`

## (4) 角色造型

- 角色造型：孙悟空、武松等英雄人物动态夸张、神态凛然；虎、猴等动物造型生动逼真；人物体型健壮。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：文字在幅下，旁白与对白交替；对白简短有力；无拟声词大字。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：大闹天宫：孙悟空大闹天宫、武松打虎：景阳冈打虎、古典英雄：水浒、三国人物、动物：虎、猴、马的生动造型、民间故事与神话、工笔重彩与白描并行。`verbatim`
- 不该画：No flat cartoon simplification、No photorealistic rendering、No crowded small panels、No modern urban slang。`impression`
- Negative prompt: `No flat cartoon simplification, No photorealistic rendering, No crowded small panels, No modern urban slang`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Liu Jiyou, a small Yorkshire terrier sitting on a subway seat, heroic lianhuanhua, dynamic figures, fine brush line, classical action`
- 中文对照：刘继卣风格：一只小约克夏犬坐在地铁座位上，英雄连环画，动态人物，精细笔线，古典动作。
- Negative: `No flat cartoon simplification, no photorealistic rendering, no crowded small panels, no modern urban slang`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
