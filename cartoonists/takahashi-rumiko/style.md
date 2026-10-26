# Rumiko Takahashi — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Rumiko Takahashi manga style, round cute characters, lively comedy, dynamic action, expressive faces, black-and-white manga with screentone`
- ZH: 高桥留美子风格，圆润可爱角色，活泼喜剧，动态动作，表情丰富，黑白漫画配网点

## (2) 线条、网点/色彩

- 线条：圆润干净的线，人物造型圆润，表情夸张多变。`verbatim`
- 网点/色彩：黑白为主，网点表现发色与服装；彩色时红、蓝跳色。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数多，动作分解细，笑点格放大，节奏快。`verbatim`
- 节奏：格间时间按作品节奏走，详见 process.md。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 拉姆式外星少女、乱马式变身少年、犬夜叉式半妖，服装华丽。`verbatim`
- 角色类型：外星少女的追逐、变身与性别错位、半妖的冒险与羁绊。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框多，台词快；拟声词大字出格。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：外星少女的追逐、变身与性别错位、半妖的冒险与羁绊、日常喜剧的误会、夸张的表情与追逐、浪漫喜剧的收尾。`verbatim`
- 不该画：No realistic fine line、no sparse slow panels、no dark gritty tone、no photorealistic rendering。`impression`
- Negative prompt: `No realistic fine line, no sparse slow panels, no dark gritty tone, no photorealistic rendering`

## (7) 测试提示词示例（现代题材：一只小约克夏犬在深夜便利店追逐失控机器人）

- Prompt: `In the style of Rumiko Takahashi, a small Yorkshire terrier chasing a runaway robot in a night convenience store, comedy manga page`
- 中文对照：高桥留美子风格，一只小约克夏犬在深夜便利店追逐失控机器人，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
