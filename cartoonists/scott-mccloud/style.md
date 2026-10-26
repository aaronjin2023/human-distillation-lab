# Scott McCloud — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Scott McCloud, clear explanatory diagrams, cartoon avatar self, bold clean line, comics theory, graphic novel page`
- ZH: 麦克劳德风格，清晰解说图解，卡通化身，粗黑干净线，漫画理论，图像小说页。

## (2) 线条、网点/色彩

- 线条：粗黑干净的线，卡通化身简洁；图解箭头与标注。`verbatim`
- 网点/色彩：黑白为主，间有蓝（《理解漫画》的蓝调）；色彩功能性。
- 质感：粗黑墨线 + 功能色块；纸面干净，图解精确。

## (3) 分镜

- 格数与格形：格数多，图解式分镜；箭头引导视线；节奏如讲课。
- 节奏：节奏如讲课，图解即节奏；一页可讲一个理论。
- 视线引导：美式阅读顺序左→右；视线被箭头牵引，先看图解再看化身。

## (4) 角色造型

- 造型：麦克劳德卡通化身（圆脸、眼镜）、佐特与珍妮；理论图解中的小人。
- 角色类型：卡通化身、佐特、理论小人；主角讲解，配角演示。
- 动作：动作功能性，指向、演示、跳接；速度线少。

## (5) 对话框与拟声词

- 对话框：对话框多，讲解口吻；旁白理论化。
- 拟声词：拟声词功能性；理论演示以画面代替。
- 文字量：每页文字密度高，讲解口吻，旁白理论化。

## (6) 该画什么 / 不该画什么

- 该画：漫画理论图解、卡通化身讲解、格与格之间的“沟”（gutter）、时间与空间、佐特的科幻冒险、漫画史、数字漫画的无限画布。`verbatim`
- 不该画：不画松散速写线、不画灰调写实、不画冷嘲讽刺、不画密集排线、不画写实渲染。
- Negative prompt: `No loose sketchy line, no muted naturalism, no cynical satire, no dense hatching, no photorealistic detail`

## (7) 测试提示词示例（现代题材：在地铁里向乘客讲解漫画的年轻人）

- Prompt: `In the style of Scott McCloud, a young person explaining comics to passengers on a subway, clear explanatory diagrams, cartoon avatar, bold clean line`
- 中文对照：麦克劳德风格：年轻人在地铁里向乘客讲解漫画，清晰解说图解，卡通化身，粗黑干净线。
- Negative: `No loose sketchy line, no muted naturalism, no cynical satire`
- 检验点：图解是否清晰；箭头是否引导视线；讲解口吻是否成立。
