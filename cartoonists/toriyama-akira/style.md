# Akira Toriyama — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Akira Toriyama manga style, round cute line, dynamic battle, speed lines, expressive faces, detailed machines, black-and-white manga`
- ZH: 鸟山明风格，圆润线条，动态战斗，速度线，表情丰富，机械精细，黑白漫画

## (2) 线条、网点/色彩

- 线条：圆润干净的线，人物肌肉用简洁曲线，机械用硬线精细。`verbatim`
- 网点/色彩：黑白为主，网点表现阴影；彩色时橙、蓝主调。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数多，战斗分解极细，速度线密，跨页作必杀。`verbatim`
- 节奏：格间时间按作品节奏走，详见 process.md。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 悟空式少年、阿拉蕾式机器人少女，发型尖锐，肌肉简洁。`verbatim`
- 角色类型：龙珠的收集与战斗、阿拉蕾的企鹅村日常、沙漠的冒险与机械。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框圆，台词短；拟声词超大出格，与冲击波同框。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：龙珠的收集与战斗、阿拉蕾的企鹅村日常、沙漠的冒险与机械、气功波与变身、师徒与对手、机械与载具的细节。`verbatim`
- 不该画：No realistic fine line、no sparse slow panels、no dark gritty tone、no photorealistic rendering。`impression`
- Negative prompt: `No realistic fine line, no sparse slow panels, no dark gritty tone, no photorealistic rendering`

## (7) 测试提示词示例（现代题材：一只小约克夏犬在地铁站台蓄力发光）

- Prompt: `In the style of Akira Toriyama, a small Yorkshire terrier powering up with aura on a subway platform, battle manga page`
- 中文对照：鸟山明风格，一只小约克夏犬在地铁站台蓄力发光，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
