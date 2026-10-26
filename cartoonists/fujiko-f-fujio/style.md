# Fujiko F. Fujio — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Fujiko F. Fujio manga style, round cute characters, gentle clean line, simple panels, warm everyday wonder, black-and-white manga with soft screentone`
- ZH: 藤子·F·不二雄风格，圆润可爱角色，温柔干净线条，简单分镜，日常奇遇，黑白漫画配柔和网点

## (2) 线条、网点/色彩

- 线条：圆润均匀的细线，轮廓柔和，无锋利折角。`verbatim`
- 网点/色彩：黑白为主，淡网点；彩色时蓝、白、红平涂，明亮干净。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数中等，方格整齐，节奏平稳，跨页少，大格留给道具登场。`verbatim`
- 节奏：格间时间按作品节奏走，详见 process.md。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 圆脸大眼，哆啦A梦式圆身，儿童与动物造型简洁，表情温和。`verbatim`
- 角色类型：未来道具从口袋取出的一刻、大雄式普通少年与哆啦A梦的搭档、日常场景突然出现科幻道具。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框圆而大，字体清晰；拟声词小而圆，不抢画面。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：未来道具从口袋取出的一刻、大雄式普通少年与哆啦A梦的搭档、日常场景突然出现科幻道具、家庭、学校、空地的日常、温柔的失败与再试一次、奇天烈式发明与机关。`verbatim`
- 不该画：No dark gritty gekiga line、no crowded tiny panels、no photorealistic rendering、no cynical bleak ending。`impression`
- Negative prompt: `No dark gritty gekiga line, no crowded tiny panels, no photorealistic rendering, no cynical bleak ending`

## (7) 测试提示词示例（现代题材：一只小约克夏犬在地铁座位上遇见一只机器猫）

- Prompt: `In the style of Fujiko F. Fujio, a small Yorkshire terrier meeting a robot cat on a subway seat, gentle manga page`
- 中文对照：藤子·F·不二雄风格，一只小约克夏犬在地铁座位上遇见一只机器猫，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
