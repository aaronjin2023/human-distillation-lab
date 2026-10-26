# Alberto Breccia — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alberto Breccia, expressionist graphic novel, rough ink and collage, heavy black, nightmarish Buenos Aires`
- ZH: 布雷恰风格：表现主义图像小说，粗粝墨色与拼贴，浓重黑块，梦魇般的布宜诺斯艾利斯。

## (2) 线条、网点/色彩

- 线条：粗粝的表现性线条，墨色浓重、带拼贴与刮擦；人物造型扭曲有力，线条不求光滑。`impression`
- 色彩：黑白为主，黑块面积大；偶施淡彩；明暗对比极强，气氛阴郁。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：不规则格、大格压迫；节奏沉重，留白少；阅读自左而右，视线随黑块走。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：莫特·辛德等人物面容扭曲、体型瘦长；怪物与市民皆带梦魇感；表情阴郁。`impression`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：对白少、沉重；旁白多、文学味；对话框不规则；拟声词少。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：莫特·辛德：死去又归来的男人、佩拉姆斯：布宜诺斯艾利斯的梦魇、洛夫克拉夫特：恐怖改编、黑块与拼贴：粗粝的质感、阿根廷都市：夜晚的街道、死亡与归来。`verbatim`
- 不该画：No clean smooth line、No bright cheerful colour、No cute round figures、No crowded dialogue balloons。`impression`
- Negative prompt: `No clean smooth line, No bright cheerful colour, No cute round figures, No crowded dialogue balloons`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Alberto Breccia, a small Yorkshire terrier sitting on a subway seat, expressionist graphic novel, rough ink and collage, heavy black, nightmarish city`
- 中文对照：布雷恰风格：一只小约克夏犬坐在地铁座位上，表现主义图像小说，粗粝墨色与拼贴，浓重黑块，梦魇都市。
- Negative: `No clean smooth line, no bright cheerful colour, no cute round figures, no crowded dialogue balloons`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
