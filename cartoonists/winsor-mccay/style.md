# Winsor McCay — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Winsor McCay, Art Nouveau line, architectural precision, full-page dream landscapes, luminous colour lithography, newspaper comic page`
- ZH: 麦凯风格，新艺术线条，建筑般精确，整版梦境风景，明亮石版彩色，报纸连环画页。

## (2) 线条、网点/色彩

- 线条：精确优雅的线，建筑透视准确；装饰性新艺术曲线。`verbatim`
- 网点/色彩：石版彩色明亮，粉蓝、粉红、金黄；色彩经印刷精细调配。
- 质感：石版彩色 + 精确墨线；纸面光滑，色彩明亮。

## (3) 分镜

- 格数与格形：整版大格，格形随梦境变形；格数少而大。
- 节奏：节奏如梦，大格与变形拉长时间；每页末格必醒。
- 视线引导：美式阅读顺序左→右；视线被整版风景牵引，先看全景再看小尼莫。

## (4) 角色造型

- 造型：小尼莫的睡衣与金发；弗利普的绿帽；小萨米的喷嚏；梦境中的巨人、宫殿、会走路的床。
- 角色类型：做梦的孩子、绿帽捣蛋鬼、喷嚏男孩、梦境巨人；主角渺小，梦境巨大。
- 动作：动作如梦，飞行、坠落、变形；速度线少，变形本身就是动作。

## (5) 对话框与拟声词

- 对话框：对话框小，文字粗糙（学界共识：对话框是其弱项）；旁白少。
- 拟声词：拟声词少；梦境声响以画面代替。
- 文字量：每页文字密度低，画面为主，对话粗糙。

## (6) 该画什么 / 不该画什么

- 该画：梦境宫殿与巨人、会走路的床、翻滚的城市、稀有牛排的噩梦、小萨米的喷嚏、建筑透视的奇观、醒来收束。`verbatim`
- 不该画：不画微小拥挤格、不画潦草速写线、不画灰调色彩、不画现代俚语对话、不画写实渲染。
- Negative prompt: `No small crowded panels, no rough sketchy line, no muted palette, no modern slang dialogue, no photographic realism`

## (7) 测试提示词示例（现代题材：地铁里打瞌睡的上班族做梦）

- Prompt: `In the style of Winsor McCay, an office worker dozing on a subway and dreaming, Art Nouveau line, full-page dream landscape, luminous colour, the dream ends with waking`
- 中文对照：麦凯风格：上班族在地铁里打瞌睡做梦，新艺术线条，整版梦境风景，明亮色彩，梦以醒来收束。
- Negative: `No small crowded panels, no rough sketchy line, no muted palette`
- 检验点：整版风景是否如梦；建筑透视是否精确；末格是否醒来收束。
