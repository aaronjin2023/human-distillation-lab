# Guy Delisle — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Guy Delisle, travelogue comics, simple clean line, an outsider in Shenzhen Pyongyang Jerusalem, quiet observation`
- ZH: 居伊·德利尔风格：旅行纪实漫画，简洁干净线条，异乡人在深圳、平壤、耶路撒冷，安静观察。

## (2) 线条、网点/色彩

- 线条：简洁干净的线条，轮廓流畅；人物造型简练，表情含蓄。`impression`
- 色彩：淡彩为主（《平壤》为黑白），色彩淡雅，氛围重于情节。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：多格连环，格数中等；节奏舒缓，留白多；阅读自左而右，视线随异乡人走。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：作者本人——戴眼镜、简练造型；异乡人物造型写实而简练；表情含蓄。`impression`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：旁白多、观察味；对白简短生活化；拟声词小。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：深圳：中国改革开放的都市、平壤：朝鲜的异乡生活、耶路撒冷：圣城的日常、异乡人：戴眼镜的作者、城市观察：街道、饭馆、检查站、安静的幽默。`verbatim`
- 不该画：No dense crosshatching、No bright saturated colour、No exaggerated action lines、No crowded small panels。`impression`
- Negative prompt: `No dense crosshatching, No bright saturated colour, No exaggerated action lines, No crowded small panels`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Guy Delisle, a small Yorkshire terrier sitting on a subway seat, travelogue comics, simple clean line, an outsider in a foreign city, quiet observation`
- 中文对照：居伊·德利尔风格：一只小约克夏犬坐在地铁座位上，旅行纪实漫画，简洁干净线条，异乡人，安静观察。
- Negative: `No dense crosshatching, no bright saturated colour, no exaggerated action lines, no crowded small panels`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
