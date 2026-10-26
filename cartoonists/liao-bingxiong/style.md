# Liao Bingxiong — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Liao Bingxiong, Cantonese satire, cats as the nation, folk rhyme and woodcut line, self-mocking humour`
- ZH: 廖冰兄风格：粤味讽刺，猫国喻世，民间歌谣与木刻线，自嘲幽默。

## (2) 线条、网点/色彩

- 线条：木刻味的粗黑线与民间画线并用；猫造型简练夸张，线条有力、带民间拙趣。`impression`
- 色彩：黑白为主，偶施淡彩；黑块对比强，民间色彩点染。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：单幅与连环并行；《猫国春秋》为连环，格数中等；单幅则一幅一点题，标题多为打油词话。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：猫拟人化为国民众生相；猫王、猫官、猫民各有标志；人物造型带粤人神态。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：打油词话配画，粤语歌谣入题；对话框少，文字多在画下；拟声词小。`artifact`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：猫国春秋：猫拟人喻世、粤语歌谣与打油词话、自嘲：画家自画像式的自嘲、时局讽刺：各时代当权者、民间木刻与年画味、儿童与市井小人物。`verbatim`
- 不该画：No gentle poetic blank space、No photorealistic detail、No ornate gongbi lines、No wordless ambiguity。`impression`
- Negative prompt: `No gentle poetic blank space, No photorealistic detail, No ornate gongbi lines, No wordless ambiguity`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Liao Bingxiong, a small Yorkshire terrier sitting on a subway seat, Cantonese satire, cats as the nation, folk rhyme, woodcut line`
- 中文对照：廖冰兄风格：一只小约克夏犬坐在地铁座位上，粤味讽刺，猫国喻世，民间歌谣，木刻线。
- Negative: `No gentle poetic blank space, no photorealistic detail, no ornate gongbi lines, no wordless ambiguity`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
