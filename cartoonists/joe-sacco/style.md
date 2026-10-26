# Joe Sacco — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joe Sacco, comics journalism, dense crosshatching, crowded panels, eyewitness testimony from Palestine and Bosnia`
- ZH: 乔·萨科风格：新闻漫画，密集排线，拥挤分格，巴勒斯坦与波斯尼亚的目击证言。

## (2) 线条、网点/色彩

- 线条：密集的排线与交叉排线，线条细密有力；人物造型写实，面容细节多。`impression`
- 色彩：黑白为主；明暗靠排线密度，画面沉重。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：多格连环，格数多、拥挤；节奏沉重，旁白多；阅读自左而右，视线随证言走。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：巴勒斯坦人与波斯尼亚人造型写实；记者本人常入画，戴眼镜；表情沉重。`impression`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：旁白多、纪实味；对白为采访实录，简短；拟声词少。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：巴勒斯坦：加沙与约旦河西岸、安全区戈拉日代：波斯尼亚战争、加沙笔记：加沙地带、新闻漫画：采访实录入画、拥挤分格：密集排线、记者入画：戴眼镜的记者。`verbatim`
- 不该画：No clean empty panels、No bright cheerful colour、No cute cartoon simplification、No fictional superhero action。`impression`
- Negative prompt: `No clean empty panels, No bright cheerful colour, No cute cartoon simplification, No fictional superhero action`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Joe Sacco, a small Yorkshire terrier sitting on a subway seat, comics journalism, dense crosshatching, crowded panels, eyewitness testimony`
- 中文对照：乔·萨科风格：一只小约克夏犬坐在地铁座位上，新闻漫画，密集排线，拥挤分格，目击证言。
- Negative: `No clean empty panels, no bright cheerful colour, no cute cartoon simplification, no fictional superhero action`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
