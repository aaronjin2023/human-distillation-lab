# Mitsuteru Yokoyama — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Mitsuteru Yokoyama manga style, bold clear line, giant robot, historical epic, dense battle panels, black-and-white manga`
- ZH: 横山光辉风格， bold 清晰线条，巨大机器人，历史史诗，密集战斗格，黑白漫画

## (2) 线条、网点/色彩

- 线条：粗细均匀的清晰轮廓线，机器人用直尺感硬线，人物用圆线。`verbatim`
- 网点/色彩：黑白为主，网点表现金属与铠甲；彩色时红、蓝、金平涂。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数多，战斗场面格子碎，跨页作机器人全貌与战场。`verbatim`
- 节奏：格间时间按作品节奏走，详见 process.md。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 铁人 28 号式巨大机器人，少年操纵者，三国武将铠甲造型。`verbatim`
- 角色类型：巨大机器人与少年操纵者、三国武将与战场、水户黄门式巡游与惩恶。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框密，旁白多；拟声词大字，机器人音效粗黑。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：巨大机器人与少年操纵者、三国武将与战场、水户黄门式巡游与惩恶、古代中国与日本历史、机械与铠甲的细节、群雄对决。`verbatim`
- 不该画：No sketchy rough line、no sparse slow panels、no photorealistic rendering、no modern minimalist style。`impression`
- Negative prompt: `No sketchy rough line, no sparse slow panels, no photorealistic rendering, no modern minimalist style`

## (7) 测试提示词示例（现代题材：一个巨大机器人与一只小约克夏犬在现代地铁站并肩等车）

- Prompt: `In the style of Mitsuteru Yokoyama, a giant robot waiting beside a small Yorkshire terrier at a modern subway station, manga page`
- 中文对照：横山光辉风格，一个巨大机器人与一只小约克夏犬在现代地铁站并肩等车，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
