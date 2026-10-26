# Art Spiegelman — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Art Spiegelman, stark black-and-white, mice and cats metaphor, dense panel grids, Holocaust memoir, graphic novel page`
- ZH: 斯皮格曼风格，黑白分明，老鼠与猫的隐喻，密集格网，大屠杀回忆录，图像小说页。

## (2) 线条、网点/色彩

- 线条：简洁有力的黑白线，黑块分明；动物造型极简。`verbatim`
- 网点/色彩：纯黑白；间有红（《影子之塔》的红塔）。
- 质感：黑白墨线 + 黑块；纸面干净，对比强烈。

## (3) 分镜

- 格数与格形：格网密集，方格为主；节奏沉重，时间跳接。
- 节奏：节奏沉重，格网密集；过去与现在并置，时间跳接。
- 视线引导：美式阅读顺序左→右；视线在格网间跳动，过去与现在同页。

## (4) 角色造型

- 造型：老鼠犹太人、猫纳粹、猪波兰人；弗拉德克的皱纹与号码；阿特自画像戴鼠面具。
- 角色类型：老鼠、猫、猪、狗；动物即民族，面具即身份。
- 动作：动作克制沉重，行走、躲藏、讲述；速度线全无。

## (5) 对话框与拟声词

- 对话框：对话框多，口述史口吻；旁白父子对话。
- 拟声词：拟声词少；枪声与爆炸以黑块代替。
- 文字量：每页文字密度高，口述史口吻，父子对话。

## (6) 该画什么 / 不该画什么

- 该画：老鼠与猫的隐喻、奥斯维辛、父子口述、幸存者的内疚、面具与身份、纽约与雷哥公园、时间跳接（过去与现在并置）。`verbatim`
- 不该画：不画彩色、不画写实人脸、不画滑稽幽默、不画空旷背景、不画英雄光环。
- Negative prompt: `No colour, no realistic human faces, no slapstick humour, no empty backgrounds, no heroic glamour`

## (7) 测试提示词示例（现代题材：地铁里读旧照片的老人）

- Prompt: `In the style of Art Spiegelman, an old man looking at old photographs on a subway, stark black-and-white, dense panel grids, past and present side by side, quiet memoir tone`
- 中文对照：斯皮格曼风格：老人在地铁里看旧照片，黑白分明，密集格网，过去与现在并置，安静回忆录口吻。
- Negative: `No colour, no realistic human faces, no slapstick humour`
- 检验点：黑白对比是否强烈；格网是否密集；过去与现在是否并置。
