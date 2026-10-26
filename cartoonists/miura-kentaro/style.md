# Kentaro Miura — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Kentaro Miura manga style, dark fantasy, hyper-detailed line, massive swords, grotesque demons, black-and-white manga with dense hatching`
- ZH: 三浦建太郎风格，黑暗奇幻，超精细线条，巨剑，怪异恶魔，黑白漫画配密排线

## (2) 线条、网点/色彩

- 线条：极细密的线，铠甲与恶魔如雕刻，人物肌肉精细。`verbatim`
- 网点/色彩：黑白为主，黑块与排线极密，明暗强烈。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数多，战斗分解细，跨页作巨剑与恶魔，节奏沉重。`verbatim`
- 节奏：格间时间按作品节奏走，详见 process.md。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 格斯式独臂剑士、巨剑，恶魔形态怪异，铠甲细节极密。`verbatim`
- 角色类型：格斯的复仇与挣扎、巨剑与铠甲、恶魔与使徒。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框密，台词沉重；拟声词大字，斩击音效粗黑。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：格斯的复仇与挣扎、巨剑与铠甲、恶魔与使徒、中世纪战场、同伴的牺牲、黑暗中的微光。`verbatim`
- 不该画：No cute round line、no bright cheerful colour、no sparse empty panels、no simple cartoon demon。`impression`
- Negative prompt: `No cute round line, no bright cheerful colour, no sparse empty panels, no simple cartoon demon`

## (7) 测试提示词示例（现代题材：一只小约克夏犬骑士持巨剑站在深夜废墟战场）

- Prompt: `In the style of Kentaro Miura, a small Yorkshire terrier knight with a giant sword on a ruined battlefield at night, dark fantasy manga page`
- 中文对照：三浦建太郎风格，一只小约克夏犬骑士持巨剑站在深夜废墟战场，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
