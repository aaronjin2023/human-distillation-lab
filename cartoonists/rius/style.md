# Rius / Eduardo del Río — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rius, simple hand-drawn line, didactic political satire, caricatured villagers, handwritten text filling the page, black-and-white Mexican popular comics`
- ZH: 里乌斯风格，简洁手绘线，教谕式政治讽刺，漫画化村民，手写文字铺满页面，黑白墨西哥大众漫画。

## (2) 线条、网点/色彩

- 线条：简洁手绘线，粗细不匀，漫画化夸张；线条不求精致，求一眼看懂。`verbatim`
- 网点/色彩：以黑白为主，间有单色套印；色彩不写实，只作强调。
- 质感：钢笔/马克笔手绘 + 手写文字；纸面粗糙，无数码平涂。

## (3) 分镜

- 格数与格形：格数多，方格为主；一页常塞进多格对话与大段手写讲解。
- 节奏：节奏靠对话推进，一页讲清一个政治笑话或一个概念。
- 视线引导：西语左→右阅读；视线被大字标题与漫画人物牵引，先看脸再看字。

## (4) 角色造型

- 造型：卡尔松辛（Calzonzin）：印第安农民，头巾与草帽；村长与官僚：大肚子、西装、礼帽；神父与将军：漫画化的权力面孔。
- 角色类型：小村村民群像、贪官、神父、将军、美国佬；主角是穷人，配角是权力。
- 动作：动作少而夸张：指点、争吵、鞠躬、逃跑；动态靠姿态不靠速度线。

## (5) 对话框与拟声词

- 对话框：对话框多，手写文字量大；讲解性旁白与对话并重。
- 拟声词：拟声词少；笑声与叫喊以大字手写。
- 文字量：每页文字密度极高，手写讲解是画面的另一半。

## (6) 该画什么 / 不该画什么

- 该画：圣加拉瓦托小村与村民群像、卡尔松辛（印第安农民）、贪官与村长、神父与教会批判、美国与帝国主义、漫画科普（para principiantes 系列）、墨西哥市井语言与双关、手写小书（libros de Rius）。`verbatim`
- 不该画：不画精致学院线、不画无字静默页、不画去政治化的可爱笑话、不画鲜亮卡通色、不画空旷背景。
- Negative prompt: `No polished academic line, no wordless silent pages, no apolitical cute gags, no bright cartoon colours, no empty backgrounds, no photorealistic rendering`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Rius, a small Yorkshire terrier on a subway seat while passengers argue about ticket prices, simple hand-drawn line, satirical dialogue balloons, handwritten explanatory captions`
- 中文对照：里乌斯风格：一只小约克夏犬坐在地铁座位上，乘客们争论票价，简洁手绘线，讽刺对话框，手写讲解旁白。
- Negative: `No polished academic line, no wordless silent pages, no apolitical cute gags`
- 检验点：线是否简洁手绘；文字是否铺满页面；讽刺是否一页即达。
