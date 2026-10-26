# Lu Shaofei — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lu Shaofei, early Shanghai manhua, bold expressive line, caricature of city life, founder of the Manhua Society`
- ZH: 鲁少飞风格：早期上海漫画，大胆表现线条，都市生活漫画，漫画会创始人。

## (2) 线条、网点/色彩

- 线条：大胆的表现性线条，粗细对比强；漫画造型夸张，线条有力。`impression`
- 色彩：黑白为主；明暗对比强，靠黑块造体积。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：单幅与连环并行；单幅一幅一点题；连环格数中等，节奏轻快。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：都市人物漫画化——阔太、舞女、流氓，造型夸张而可认；表情一笔点出。`impression`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：对白短、口语化；画下点题文字常见；拟声词小。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：上海都市生活：舞厅、弄堂、马路、漫画会：早期漫画家的集体、都市人物漫画：阔太、舞女、流氓、时事讽刺：时局速写、旅行与风土速写、单幅点题与连环小品。`verbatim`
- 不该画：No gongbi fine lines、No empty poetic blank space、No photorealistic rendering、No wordless silent panels。`impression`
- Negative prompt: `No gongbi fine lines, No empty poetic blank space, No photorealistic rendering, No wordless silent panels`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Lu Shaofei, a small Yorkshire terrier sitting on a subway seat, early Shanghai manhua, bold expressive line, caricature of city life`
- 中文对照：鲁少飞风格：一只小约克夏犬坐在地铁座位上，早期上海漫画，大胆表现线条，都市生活漫画。
- Negative: `No gongbi fine lines, no empty poetic blank space, no photorealistic rendering, no wordless silent panels`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
