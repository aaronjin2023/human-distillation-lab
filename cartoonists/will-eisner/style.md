# Will Eisner — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Will Eisner, cinematic splash pages, rain and city noir, expressive ink, sequential art, graphic novel page`
- ZH: 艾斯纳风格，电影感满页，雨与城市黑夜，表现力墨水，连环画艺术，图像小说页。

## (2) 线条、网点/色彩

- 线条：表现力强的墨水线，雨线与阴影密；人物表情戏剧化。`verbatim`
- 网点/色彩：黑白为主，间有灰调；雨夜蓝黑。
- 质感：墨水 + 雨线 + 阴影；纸面粗粝，雨感强。

## (3) 分镜

- 格数与格形：满页大格（splash page）开创者；格形自由；电影式运镜。
- 节奏：节奏如电影，满页开场，格形自由；雨声即节奏。
- 视线引导：美式阅读顺序左→右；视线被满页大格牵引，先看全景再看人物。

## (4) 角色造型

- 造型：闪灵的面具与风衣；纽约小人物（《与上帝的契约》）；城市本身就是角色。
- 角色类型：蒙面义警、纽约小人物、公寓楼居民；主角戏剧，配角真实。
- 动作：动作戏剧化，追逐、打斗、雨中奔跑；速度线密。

## (5) 对话框与拟声词

- 对话框：对话框融入画面，字体手写；拟声词大（雨声、脚步）。
- 拟声词：拟声词大：雨声、脚步、火车。
- 文字量：每页文字密度中等，旁白文学化，对话戏剧化。

## (6) 该画什么 / 不该画什么

- 该画：雨夜城市、闪灵与罪犯、纽约公寓楼（《与上帝的契约》）、小人物的尊严、火车站与街角、阴影与路灯、契约与信仰。`verbatim`
- 不该画：不画干净极简线、不画明亮欢快色、不画整齐小格、不画滑稽笑料、不画空旷背景。
- Negative prompt: `No clean minimal line, no bright cheerful colour, no small uniform panels, no slapstick gags, no empty backgrounds`

## (7) 测试提示词示例（现代题材：雨夜便利店门口躲雨的人）

- Prompt: `In the style of Will Eisner, people sheltering from rain outside a convenience store at night, cinematic splash page, rain and city noir, expressive ink`
- 中文对照：艾斯纳风格：人们雨夜在便利店门口躲雨，电影感满页，雨与城市黑夜，表现力墨水。
- Negative: `No clean minimal line, no bright cheerful colour, no small uniform panels`
- 检验点：满页大格是否如电影开场；雨线是否密；城市是否本身就是角色。
