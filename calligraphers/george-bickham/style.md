# George Bickham — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of George Bickham, English round hand, flowing copperplate letters, elegant flourished capitals, black ink on paper, 18th-century writing manual page`
- ZH: 乔治·比克汉姆风格：鹅毛笔圆体：笔画圆润流畅，粗细对比明显，字母连写，起收笔尖锐而有弹性；圆体行款流畅，字母大小参差，装饰性花体首字母，行气连绵。

## (2) 笔法

- 用笔：鹅毛笔圆体：笔画圆润流畅，粗细对比明显，字母连写，起收笔尖锐而有弹性。`artifact`
- 禁笔：不用圆润流畅、不用生硬断笔以外的笔法不在此列；具体禁笔见第 (6) 节 Negative prompt。

## (3) 结字与章法

- 结字：圆体行款流畅，字母大小参差，装饰性花体首字母，行气连绵。`artifact`
- 章法：圆体行款流畅，字母大小参差，装饰性花体首字母，行气连绵。
- 落款与印章：落款小字，位置与大小依本传统通例，不喧宾夺主。

## (4) 墨色与节奏

- 墨色：黑墨为主，刻本黑白对比清晰。`artifact`
- 节奏：行笔快慢与提按起伏以代表作为准，一幅之内墨色变化的节奏不另编。

## (5) 书体与取法

- 书体：主导：圆体（round hand）；《通用书写大师》为英国圆体范式。`artifact`
- 取法与演变：18世纪英国：圆体字帖范式，影响商业书写与铜版雕刻。`impression`

## (6) 该写什么 / 不该写什么

- 该写：圆体字母形制, 《通用书写大师》的示范页, 装饰性花体首字母；主导：圆体（round hand）；《通用书写大师》为英国圆体范式；鹅毛笔圆体：笔画圆润流畅，粗细对比明显，字母连写，起收笔尖锐而有弹性；黑墨为主，刻本黑白对比清晰。
- 不该写：Gothic blackletter, no upright roman capitals, no irregular handwriting, no printed roman typeface, no plain unadorned layout。
- Negative prompt: `No Gothic blackletter, no upright roman capitals, no irregular handwriting, no printed roman typeface, no plain unadorned layout`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of George Bickham, English round hand, flowing copperplate letters, elegant flourished capitals, black ink on paper, 18th-century writing manual page`
- 中文对照：比克汉姆风格：英国圆体，花体字母圆润流畅，装饰性首字母，黑墨纸面。
- Negative: `No Gothic blackletter, no upright roman capitals, no irregular handwriting, no printed roman typeface, no plain unadorned layout`
- 检验点：笔法、结字、章法、墨色是否与第 (2)–(5) 节一致；传本情况是否被误写为真迹。
