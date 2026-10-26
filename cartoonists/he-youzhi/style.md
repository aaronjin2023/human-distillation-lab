# He Youzhi — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of He Youzhi, lianhuanhua of rural China, lively peasants, fine ink line, everyday life in the mountains`
- ZH: 贺友直风格：乡土连环画，活泼农民，细腻墨线，山乡日常生活。

## (2) 线条、网点/色彩

- 线条：细腻的钢笔与毛笔线，线条流畅、带速写感；人物动态生动，线条不板滞。`impression`
- 色彩：黑白为主，偶施淡彩；明暗靠线条疏密，画面清朗。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：连环画分幅，每幅一景、图文并置；幅数多、节奏舒缓；视线随人物在山乡间移动。`impression`
- 节奏：逐幅定构图与人物位置（分幅草图（每幅一小稿））；分镜示例：逐幅定构图，犬为赶集人。`impression`

## (4) 角色造型

- 角色造型：农民最见功力——体态、衣着、神态皆有乡土味；妇女、老农、干部各有标志；动作生活化。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：文字在幅下，以旁白与对白交替；对白口语化、带乡音；无拟声词大字。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：山乡巨变：农村合作化与乡土变迁、农民众生相：老农、妇女、干部、小二黑结婚：农村青年婚恋、山乡风光：田野、山路、农舍、日常生活：吃饭、赶集、开会、白光等鲁迅小说改编。`verbatim`
- 不该画：No urban glamour、No photorealistic rendering、No exaggerated speed lines、No crowded dialogue balloons。`impression`
- Negative prompt: `No urban glamour, No photorealistic rendering, No exaggerated speed lines, No crowded dialogue balloons`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of He Youzhi, a small Yorkshire terrier sitting on a subway seat, lianhuanhua of rural China, lively peasants, fine ink line, everyday life`
- 中文对照：贺友直风格：一只小约克夏犬坐在地铁座位上，乡土连环画，活泼农民，细腻墨线，日常生活。
- Negative: `No urban glamour, no photorealistic rendering, no exaggerated speed lines, no crowded dialogue balloons`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
