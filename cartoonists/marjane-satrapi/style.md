# Marjane Satrapi — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Marjane Satrapi, stark black-and-white, bold black shapes, naive expressive line, autobiographical graphic novel page, Iranian patterns`
- ZH: 莎塔碧风格，黑白分明，大块黑形，天真表现线，自传图像小说页，伊朗纹样。

## (2) 线条、网点/色彩

- 线条：粗黑轮廓，黑白对比强烈；线条朴拙有力。`verbatim`
- 网点/色彩：纯黑白，间有伊朗纹样装饰；无灰调。
- 质感：墨水黑块 + 白底；纸面干净，对比强烈。

## (3) 分镜

- 格数与格形：格数中等，方格为主；黑白对比造节奏；童年视角。
- 节奏：节奏平稳，童年视角拉长时间；黑白对比造呼吸。
- 视线引导：法式阅读顺序左→右；视线被黑块牵引，先看人脸再看纹样。

## (4) 角色造型

- 造型：小玛嘉的短发与大眼睛；戴面纱的女性群像；祖母的皱纹与微笑。
- 角色类型：童年玛嘉、祖母、戴面纱的女性、革命卫兵；主角天真，配角鲜明。
- 动作：动作朴拙直接，奔跑、抗议、拥抱；速度线少。

## (5) 对话框与拟声词

- 对话框：对话框简短直接；旁白第一人称。
- 拟声词：拟声词少；爆炸与枪声以黑块代替。
- 文字量：每页文字密度中等，旁白第一人称，对话简短。

## (6) 该画什么 / 不该画什么

- 该画：德黑兰童年、面纱与革命、祖母与家庭、流亡巴黎、东西文化冲突、伊朗纹样与地毯、茉莉与花园、战争与空袭。`verbatim`
- 不该画：不画灰调渐变、不画写实解剖、不画装饰细节、不画柔和粉彩、不画拥挤格子。
- Negative prompt: `No grey shading, no realistic anatomy, no decorative detail, no muted pastel colour, no crowded panels`

## (7) 测试提示词示例（现代题材：在地铁里给陌生人让座的女孩）

- Prompt: `In the style of Marjane Satrapi, a girl giving up her subway seat to a stranger, stark black-and-white, bold black shapes, naive expressive line`
- 中文对照：莎塔碧风格：一个女孩在地铁里给陌生人让座，黑白分明，大块黑形，天真表现线。
- Negative: `No grey shading, no realistic anatomy, no muted pastel colour`
- 检验点：黑白对比是否强烈；线是否朴拙有力；童年视角是否还在。
