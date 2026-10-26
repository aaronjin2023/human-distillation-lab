# Ye Qianyu — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ye Qianyu, lively Shanghai manhua, quick ink line, Mr. Wang the little man, crowded city life, humorous and sharp`
- ZH: 叶浅予风格：活泼的上海漫画，快捷墨线，王先生式小人物，拥挤都市生活，幽默而尖锐。

## (2) 线条、网点/色彩

- 线条：快捷的钢笔与毛笔线，线条流畅、略带速写感；人物轮廓简练，表情一笔点出。`impression`
- 色彩：黑白为主，偶施淡彩；明暗对比中等，靠线条疏密造体积，不靠网点。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：连环小格为主，每格一景；格数中等，节奏轻快；阅读顺序自左而右、由上而下，视线随王先生走。`impression`
- 节奏：切分格子、定视线与节奏（分镜稿（name）、格线）；分镜示例：切 4 格——车厢、犬、乘客、犬与乘客对视。`impression`

## (4) 角色造型

- 角色造型：王先生——小个子、戴礼帽、滑稽而精明；市民众生相：阔太、流氓、舞女，各有标志性打扮；表情夸张而不过火。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：对话框圆润、文字简短口语；拟声词小而少，不出格；旁白短句点题。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：王先生：上海小市民的滑稽遭遇、上海都市生活：舞厅、弄堂、马路、百货公司、市民众生相：阔太、流氓、舞女、小贩、时事讽刺：时局与世相的速写、旅行速写：各地风土人物、小陈等连环人物小传。`verbatim`
- 不该画：No heavy gongbi fine lines、No empty poetic blank space、No photorealistic rendering、No wordless silent panels。`impression`
- Negative prompt: `No heavy gongbi fine lines, No empty poetic blank space, No photorealistic rendering, No wordless silent panels`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Ye Qianyu, a small Yorkshire terrier sitting on a subway seat, lively Shanghai manhua, quick ink line, crowded city life, humorous and sharp`
- 中文对照：叶浅予风格：一只小约克夏犬坐在地铁座位上，上海漫画，快捷墨线，拥挤都市生活，幽默而尖锐。
- Negative: `No heavy gongbi lines, no empty poetic blank space, no photorealistic rendering, no wordless silent panels`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
