# Feng Zikai — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Feng Zikai, gentle ink sketch manga, childlike figures, large empty space, a short poetic caption, warm and quiet`
- ZH: 丰子恺风格：温润水墨速写漫画，稚拙人物，大量留白，一句短诗点题，温暖安静。

## (2) 线条、网点/色彩

- 线条：毛笔淡墨中锋，线条简练、圆润、略带颤笔，似儿童涂鸦而有书法根底；不求精细，求神态。`verbatim`
- 色彩：以淡墨为主，偶施淡彩（淡赭、淡青）；黑白与淡彩并行，明暗对比弱，整体清淡、温润。`verbatim`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：多为单幅，偶有两三幅连作；无格框或极淡格线；画面主体偏一角，留白即画面的一半；阅读自上而下、一幅一境。`verbatim`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：儿童最见功力——圆头、短身、大眼、神态天真；成人画得简省，多为侧影与背影；动作小而含蓄，静中见动。`impression`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：极少对话框；多在画外配一句短诗或散文小句，题字是画面的一部分；无拟声词大字，文字安静、不抢画。`verbatim`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：儿童嬉戏与日常小景（放风筝、捉迷藏、阿宝赤膊）、母子与亲情小景、护生题材：小动物、放生、众生平等、战时流离与民间疾苦、旧式文人生活：读书、弹琴、赏月、一幅一境的诗意留白。`verbatim`
- 不该画：No sharp satirical exaggeration、No crowded panels、No loud sound effects、No photorealistic detail。`impression`
- Negative prompt: `No sharp satirical exaggeration, No crowded panels, No loud sound effects, No photorealistic detail`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Feng Zikai, a small Yorkshire terrier sitting on a subway seat, gentle ink sketch, childlike figure, large empty space, one short poetic caption, warm and quiet`
- 中文对照：丰子恺风格：一只小约克夏犬坐在地铁座位上，水墨速写，稚拙造型，大量留白，一句短诗点题，温暖安静。
- Negative: `No sharp satire, no crowded panels, no loud sound effects, no photorealistic detail`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
