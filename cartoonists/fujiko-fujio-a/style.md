# Fujiko Fujio A — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Fujiko Fujio A manga style, round cute line with black humour twist, simple panels, sly smile, everyday life turning uncanny, black-and-white manga`
- ZH: 藤子不二雄Ⓐ风格，圆润线条配黑色幽默，简单分镜，狡黠微笑，日常转向诡异，黑白漫画

## (2) 线条、网点/色彩

- 线条：圆润细线，人物笑容线条弯曲，阴影处突然加粗黑块。`verbatim`
- 网点/色彩：黑白为主，黑块对比强；彩色时色调偏暗，红、黑点缀。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数中等，方格整齐，结尾一格常为反转或冷笑特写。`verbatim`
- 节奏：格间时间按作品节奏走，详见 process.md。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 圆脸角色配细长眼睛，推销员式西装男反复出现，怪物造型圆润不吓人。`verbatim`
- 角色类型：笑面推销员的登场与交易、忍者哈特利的恶作剧与失败、怪物君与人类社会的错位。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框圆，结尾格对话框常只留一句短语；拟声词小而冷。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：笑面推销员的登场与交易、忍者哈特利的恶作剧与失败、怪物君与人类社会的错位、欲望得到满足后的代价、日常小人物的贪念、冷笑收尾。`verbatim`
- 不该画：No warm sentimental ending、no photorealistic rendering、no crowded tiny panels、no heroic action spectacle。`impression`
- Negative prompt: `No warm sentimental ending, no photorealistic rendering, no crowded tiny panels, no heroic action spectacle`

## (7) 测试提示词示例（现代题材：一个笑面推销员在地铁上向疲惫的上班族推销奇怪小道具）

- Prompt: `In the style of Fujiko Fujio A, a smiling salesman offering a strange gadget to a tired commuter on a subway, black humour manga page`
- 中文对照：藤子不二雄Ⓐ风格，一个笑面推销员在地铁上向疲惫的上班族推销奇怪小道具，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
