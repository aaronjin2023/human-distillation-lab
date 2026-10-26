# Zhang Guangyu — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhang Guangyu, decorative modernist manhua, bold flat colour, folk motifs mixed with Egyptian and Mexican art, satirical Journey to the West`
- ZH: 张光宇风格：装饰性现代主义漫画，大胆平涂色彩，民间纹样杂糅埃及与墨西哥艺术，讽刺版西游。

## (2) 线条、网点/色彩

- 线条：装饰性轮廓线，粗细均匀、带民间年画味；造型夸张变形，线条服务于图案感。`impression`
- 色彩：大胆平涂，朱红、明黄、石青、石绿并置；色彩浓烈而有装饰秩序，不写实。`verbatim`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：《西游漫记》为整幅彩色连环画式分幅，每幅一景、图文并置；节奏舒缓如壁画，视线随取经四众横向移动。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：孙悟空、猪八戒、唐僧、沙僧取西游旧形而加现代讽刺变形；妖魔鬼怪杂糅异域纹样；人物造型图案化。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：文字多在画面下方或旁侧，以说明与讽刺句为主；少用对话框，文字即画外音。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：西游取经四众的讽刺变形、纸钞王国、黑市等寓言国度、埃及、墨西哥、印度纹样的杂糅、民间年画与装饰图案、妖魔鬼怪的异域造型、时局讽刺：黑气、黑市场、闲资本幽灵。`verbatim`
- 不该画：No realistic shading、No thin sketchy line、No empty blank space、No photorealistic rendering。`impression`
- Negative prompt: `No realistic shading, No thin sketchy line, No empty blank space, No photorealistic rendering`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Zhang Guangyu, a small Yorkshire terrier sitting on a subway seat, decorative modernist manhua, bold flat colour, folk motifs, satirical`
- 中文对照：张光宇风格：一只小约克夏犬坐在地铁座位上，装饰性现代主义漫画，大胆平涂色彩，民间纹样，讽刺意味。
- Negative: `No realistic shading, no thin sketchy line, no empty blank space, no photorealistic rendering`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
