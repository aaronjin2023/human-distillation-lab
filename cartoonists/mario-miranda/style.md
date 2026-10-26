# Mario Miranda — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mario Miranda, Goan caricature, crowded lively scenes, quick ink line, gentle satire of Indian life`
- ZH: 米兰达风格：果阿漫画，拥挤生动的场景，快捷墨线，印度生活的温和讽刺。

## (2) 线条、网点/色彩

- 线条：快捷的墨水漫画线，轮廓流畅；人物造型夸张而亲切，场景拥挤生动。`impression`
- 色彩：黑白与彩色并行；彩色版平涂明快。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：单幅拥挤场景与连环并行；一幅一景，人多而不乱；阅读自左而右，视线随人群走。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：果阿人物造型夸张——大鼻子、小个子；印度众生相各有标志；表情生动。`impression`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：对白短、口语化；画下点题文字常见；拟声词小。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：米兰达的果阿：果阿风光与人物、印度漫画集：印度众生相、拥挤场景：街头、集市、教堂、果阿：葡萄牙味的印度、印度日常：火车、婚礼、节日、温和讽刺。`verbatim`
- 不该画：No dark satire、No photorealistic rendering、No empty blank space、No cynical humour。`impression`
- Negative prompt: `No dark satire, No photorealistic rendering, No empty blank space, No cynical humour`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Mario Miranda, a small Yorkshire terrier sitting on a subway seat, Goan caricature, crowded lively scenes, quick ink line, gentle satire`
- 中文对照：米兰达风格：一只小约克夏犬坐在地铁座位上，果阿漫画，拥挤生动的场景，快捷墨线，温和讽刺。
- Negative: `No dark satire, no photorealistic rendering, no empty blank space, no cynical humour`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
