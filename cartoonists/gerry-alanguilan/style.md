# Gerry Alanguilan — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gerry Alanguilan, Elmer the talking chicken, clean ink line, Filipino graphic novel, racism and family`
- ZH: 阿拉吉兰风格：《埃尔默》会说话的鸡，干净墨线，菲律宾图像小说，种族与家庭。

## (2) 线条、网点/色彩

- 线条：干净的钢笔墨线，轮廓清晰；埃尔默鸡造型写实而拟人，线条不板滞。`impression`
- 色彩：黑白为主；明暗靠线条疏密，气氛沉静。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：多格连环，格数中等；节奏舒缓，留白多；阅读自左而右，视线随埃尔默走。`impression`
- 节奏：切格：纪实节奏慢、留白多（分镜稿（name））；分镜示例：多格连环，节奏舒缓。`impression`

## (4) 角色造型

- 角色造型：埃尔默——会说话的鸡，造型写实拟人；菲律宾家庭人物写实；表情细腻。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：对白简短、生活化；旁白少；拟声词小。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：埃尔默：会说话的鸡、浪费：青年与虚无、蒂默格林：菲律宾日常、种族与偏见：鸡喻人、菲律宾家庭：父子、兄弟、超英描线：美式漫画的描线功力。`verbatim`
- 不该画：No exaggerated cartoon violence、No photorealistic rendering、No crowded small panels、No cynical humour。`impression`
- Negative prompt: `No exaggerated cartoon violence, No photorealistic rendering, No crowded small panels, No cynical humour`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Gerry Alanguilan, a small Yorkshire terrier sitting on a subway seat, Elmer the talking chicken style, clean ink line, Filipino graphic novel`
- 中文对照：阿拉吉兰风格：一只小约克夏犬坐在地铁座位上，《埃尔默》式干净墨线，菲律宾图像小说。
- Negative: `No exaggerated cartoon violence, no photorealistic rendering, no crowded small panels, no cynical humour`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
