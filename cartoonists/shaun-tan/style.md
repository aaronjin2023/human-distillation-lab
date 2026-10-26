# Shaun Tan — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shaun Tan, wordless graphic novel, pencil and paint, muted ochre and sepia, strange creatures in ordinary suburbs, meticulous detail, quiet migrant fable page`
- ZH: 肖恩·谭风格，无字图像小说，铅笔与颜料，低沉赭石与棕褐，寻常郊区的奇异生物，精细细节，安静的移民寓言页。

## (2) 线条、网点/色彩

- 线条：铅笔与墨水细线，排线细密如蚀刻；线条求精细，不求速度。`verbatim`
- 网点/色彩：赭石、棕褐、灰蓝为主，低沉怀旧；色彩如旧照片。
- 质感：铅笔、墨水、彩铅、拼贴并用；纸面有旧照片的颗粒感。

## (3) 分镜

- 格数与格形：格数多，方格如旧相册；整页大格展现异乡城市全景。
- 节奏：节奏缓慢安静，无字页靠画面呼吸；一页可只讲一个眼神。
- 视线引导：英式左→右阅读；视线被异乡城市的全景牵引，先看风景再看人物。

## (4) 角色造型

- 造型：移民男子：提箱、礼帽、异乡人；奇异生物：会走路的壶、长腿的鱼；郊区孩子：与怪物做朋友的普通人。
- 角色类型：移民、郊区孩子、奇异生物、异乡官员；主角渺小，世界巨大。
- 动作：动作缓慢安静：提箱、张望、等待；动态靠画面不靠速度线。

## (5) 对话框与拟声词

- 对话框：无字：《The Arrival》全无文字；《Tales from Outer Suburbia》短文配图。
- 拟声词：拟声词全无；静默本身就是语言。
- 文字量：《The Arrival》零文字；短篇集每页短文一段，画面为主。

## (6) 该画什么 / 不该画什么

- 该画：异乡城市与巨型雕像、移民的行李箱、奇异生物（会走路的壶、长腿的鱼）、郊区后院、《The Lost Thing》的红色怪物、《The Red Tree》的红叶、旧相册式分格、语言不通的符号。`verbatim`
- 不该画：不画明亮欢快色彩、不画干净清晰线、不画滑稽笑料、不画拥挤对话框、不画写实渲染。
- Negative prompt: `No bright cheerful colour, no clean ligne claire, no slapstick gags, no crowded dialogue, no photorealistic rendering, no flat vector illustration`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Shaun Tan, a small Yorkshire terrier on a subway seat, wordless graphic novel page, pencil and paint, muted ochre and sepia, a strange creature watching from the luggage rack, no words at all`
- 中文对照：肖恩·谭风格：一只小约克夏犬坐在地铁座位上，无字图像小说页，铅笔与颜料，低沉赭石与棕褐，行李架上一只奇异生物在张望，全无文字。
- Negative: `No bright cheerful colour, no clean ligne claire, no crowded dialogue`
- 检验点：是否全无文字；色彩是否低沉怀旧；奇异生物是否安静在场。
