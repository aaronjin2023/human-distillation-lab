# Albert Uderzo — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Albert Uderzo comics style, lively clear line, expressive cartoon faces, dynamic action, flat colour, Asterix humour, colour comics`
- ZH: 阿尔贝·乌德佐风格，活泼明线，表情丰富的卡通面孔，动态动作，平涂色彩，阿斯泰利克斯式幽默，彩色漫画

## (2) 线条、网点/色彩

- 线条：活泼清晰的线，人物鼻子大、表情夸张，动作线流畅。`verbatim`
- 网点/色彩：平涂彩色，主色红、蓝、黄，辅色柔和。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数多，方格整齐，左至右阅读，动作分解细，笑点格放大。`verbatim`
- 节奏：格间时间按作品节奏走，详见 process.md。`impression`
- 视线引导：欧美左→右阅读，视线平稳走。`impression`

## (4) 角色造型

- 阿斯泰利克斯式小个子、奥贝利克斯式胖大力士，造型圆润。`verbatim`
- 角色类型：高卢村庄的日常与宴会、罗马军团的追逐、奥贝利克斯的巨石与野猪。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框椭圆，台词机智；拟声词彩色大字，常出格。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：高卢村庄的日常与宴会、罗马军团的追逐、奥贝利克斯的巨石与野猪、魔法药水的变身、旅行的异国风情、宴会的收尾。`verbatim`
- 不该画：No sketchy rough line、no dark gritty shading、no photorealistic rendering、no sparse slow panels。`impression`
- Negative prompt: `No sketchy rough line, no dark gritty shading, no photorealistic rendering, no sparse slow panels`

## (7) 测试提示词示例（现代题材：一只小约克夏犬扮高卢人扛巨石于现代地铁站台）

- Prompt: `In the style of Albert Uderzo, a small Yorkshire terrier Gaul carrying a giant menhir on a modern subway platform, humour comics page, comics page`
- 中文对照：阿尔贝·乌德佐风格，一只小约克夏犬扮高卢人扛巨石于现代地铁站台，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
