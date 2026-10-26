# Chen Anni — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chen Anni, webcomic about siblings, simple digital line, everyday family humour, warm and relatable`
- ZH: 陈安妮风格：网络漫画，兄妹日常，简笔数码线，家庭幽默，温暖而有共鸣。

## (2) 线条、网点/色彩

- 线条：简笔数码线，轮廓干净、略带手绘感；人物大头小身，表情夸张。`impression`
- 色彩：数码平涂，色彩明快淡雅；色彩服务于日常氛围。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：竖屏长条切格，一屏一梗；格数少、留白多；下滑节奏轻快，视线随兄妹走。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：兄妹大头小身，哥哥时分、妹妹时秒各有标志；父母简省；表情夸张而可爱。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：对白短、口语化、网络味；对话框圆润；拟声词小而活泼。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：快把我哥带走：兄妹打闹日常、安妮和王小明：恋爱与日常、二胎：二胎家庭、兄妹：打闹与温情并行、家庭日常：吃饭、作业、手机、网络共鸣：当代年轻人的生活。`verbatim`
- 不该画：No dark satire、No photorealistic rendering、No crowded panels、No long explanatory text。`impression`
- Negative prompt: `No dark satire, No photorealistic rendering, No crowded panels, No long explanatory text`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Chen Anni, a small Yorkshire terrier sitting on a subway seat, webcomic about siblings, simple digital line, everyday family humour, warm`
- 中文对照：陈安妮风格：一只小约克夏犬坐在地铁座位上，网络漫画，兄妹日常，简笔数码线，家庭幽默，温暖。
- Negative: `No dark satire, no photorealistic rendering, no crowded panels, no long explanatory text`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
